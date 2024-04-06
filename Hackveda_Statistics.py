import os
import pandas as pd
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dash.dependencies import Output, Input, State
import datetime
import numpy

# Load database credentials from environment variables
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
Session = sessionmaker(bind=engine)
session = Session()

# Load data from the database
df = pd.read_sql_query("SELECT * FROM invitation GROUP BY Email ORDER BY ID DESC", session.bind)
df_interview = pd.read_sql_query(
    "SELECT DISTINCT Email AS Students, Course, Date FROM invitation WHERE Course LIKE '%interview_preperation%' ORDER BY ID DESC",
    session.bind
)

# Data cleaning and preprocessing
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month_name()
df["month_year"] = df["Date"].dt.strftime('%B %Y')

df_interview["Date"] = pd.to_datetime(df_interview["Date"], errors="coerce")
df_interview["year"] = df_interview["Date"].dt.year
df_interview["month"] = df_interview["Date"].dt.month_name()
df_interview["month_year"] = df_interview["Date"].dt.strftime('%B %Y')
df_interview["day"] = df_interview["Date"].dt.date

# Define the order of months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server

# Define layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Hackveda'),
            html.H2('Statistics'),
        ], style={'textAlign': 'center'})
    ]),
    dbc.Row([
        dbc.Col([
            html.H4('Students Joined in Year'),],style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
            dcc.Graph(
                id='year-graph',
                figure=px.bar(df.groupby('year').size().reset_index(name='Students'), x='year', y='Students')
            )
        ]),

    dbc.Row([
        dbc.Col([
            html.H4('Total Interns Monthly Breakdown'),], style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
            html.Label(['Year'], style={'font-weight': 'bold', "margin-left": "38px"}),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in df['year'].unique()],
                value=df['year'].max(),
                style={"width": "60%", "verticalAlign": "middle", "margin-left": "20px", "margin-top": "10px"}
            ),
            dcc.Graph(id='month-graph')
        ]),

    dbc.Row([
        dbc.Col([
            html.H4('Students Enrolled In Interview Preparation'),
            html.H5('Monthly Breakdown'),], style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
            html.Label(['Year'], style={'font-weight': 'bold', "margin-left": "38px"}),
            dcc.Dropdown(
                id='interview-year-dropdown',
                options=[{'label': year, 'value': year} for year in df_interview['year'].unique()],
                value=df_interview['year'].max(),
                style={"width": "60%", "verticalAlign": "middle", "margin-left": "20px", "margin-top": "10px"}
            ),
            dcc.Graph(id='interview-month-graph')
        ]),
    
    dbc.Row([
        dbc.Col([
            html.H4('Day Wise Joining In Interview Preparation'),
        ], style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label(['Year'], style={'font-weight': 'bold', "margin-left": "3px", "margin-top": "8px"}),
            dcc.Dropdown(
                id='dropdown_3',
                options=[{'label': x, 'value': x} for x in df_interview.sort_values('year')['year'].unique()],
                value=df_interview['year'].iloc[0],
            ),
        ], style={"width": 5, "margin-left": "40px", "margin-top": "20px"}),
        dbc.Col([
            html.Label(['Month'], style={'font-weight': 'bold', "margin-left": "3px", "margin-top": "8px"}),
            dcc.Dropdown(
                id='dropdown_4',
                options=[{'label': x, 'value': x} for x in sorted(df_interview.sort_values('month_year')['month_year'].unique(), key=lambda x: months.index(x.split()[0]))],
                value=df_interview['month_year'].iloc[0],
            ),
        ], style={"width": 5, "margin-left": "55px", "margin-top": "20px"}),
        dbc.Col([
            dbc.Button("SHOW", id="btn", color="dark", className="ms-2", size='sm'),
        ], style={"width": 1, "margin-top": "48px", "margin-left": "35px"}),
    ]),
    dcc.Graph(id='graph_2'),
    dcc.Store(id='store-data', data=[], storage_type='memory')
])

# Callback functions
@app.callback(
    Output('month-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_month_graph(selected_year):
    filtered_df = df[df['year'] == selected_year]
    monthly_counts = filtered_df.groupby('month').size().reindex(months, fill_value=0)
    return px.bar(monthly_counts.reset_index(name='Students'), y='month', x='Students', orientation='h')

@app.callback(
    Output('interview-month-graph', 'figure'),
    Input('interview-year-dropdown', 'value')
)
def update_interview_month_graph(selected_year):
    filtered_df = df_interview[df_interview['year'] == selected_year]
    monthly_counts = filtered_df.groupby('month').size().reindex(months, fill_value=0).reset_index(name='Students')
    monthly_counts = monthly_counts[monthly_counts['Students'] > 0]
    return px.bar(monthly_counts, y='month', x='Students', orientation='h')

@app.callback(
    Output('dropdown_4', 'options'),
    Input('dropdown_3', 'value')
)
def update_options(dropdown_3):
    df_2 = df_interview[df_interview['year'] == dropdown_3]
    return [{'label': x, 'value': x} for x in sorted(df_2.sort_values('month_year')['month_year'].unique(), key=lambda x: months.index(x.split()[0]))]

@app.callback(
    Output('store-data', 'data'),
    Input('btn', 'n_clicks'),
    [State(component_id='dropdown_3', component_property='value'),
     State(component_id='dropdown_4', component_property='value')]
)
def update_data(n_clicks, dropdown_3, dropdown_4):
    global dff
    dff = df_interview.copy()
    if dropdown_3 is not None:
        dff = dff[dff['year'] == dropdown_3]
    if dropdown_4 is not None:
        dff = dff[dff['month_year'] == dropdown_4]
    return dff.to_dict(orient='records')

@app.callback(
    Output('graph_2', 'figure'),
    Input('store-data', 'data')
)
def drop_chart2(n):
    dff_1 = dff.copy()
    dff_pivot = pd.pivot_table(dff_1, ('Students'), index=['Date'], aggfunc='count').reset_index()
    dff_pivot['Date'] = dff_pivot['Date'].dt.date  # Extracting only the date component
    plotd_2023_jan = px.bar(dff_pivot, x="Date", y="Students", orientation='v')
    plotd_2023_jan.update_layout(bargap=0.23, height=724, xaxis={'type': 'category'})
    return plotd_2023_jan

# Run the Dash app
if __name__ == '__main__':
    app.run_server(port=8037)
