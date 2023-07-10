#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymysql')


# In[2]:


get_ipython().system('pip install ipython-sql')


# In[3]:


get_ipython().system('pip install mysqlclient')


# In[4]:


import pymysql


# In[5]:


import pandas as pd


# In[6]:


db_name="hackveda_invitation"
db_host="hackveda.in"
db_username="hackveda_sahil_sinha"
db_password="p6MjB})Xn7b2"


# In[7]:



    conn=pymysql.connect(host=db_host,
                        port=int(3306),
                         user=db_username,
                         passwd=db_password,
                         db=db_name)


# In[8]:


df=pd.read_sql_query("select * from invitation group by(Email) order by(ID) desc ",conn)


# In[9]:


df_1=pd.read_sql_query("select distinct (Email) as Students, Course, Date from invitation where Course like '%interview_preperation%'  order by(ID) desc ",conn)
df_1


# In[10]:


df


# In[11]:


get_ipython().system('pip install pandasql')


# In[12]:


import pandasql as ps


# In[13]:



# Using pandas.DatetimeIndex() to extract month and year
df['year'] = pd.DatetimeIndex(df['Date']).year

print(df)


# In[14]:


q1 = """select year, count(distinct Name),Course from df group by Course,Email  """

print(ps.sqldf(q1, locals()))


# In[15]:


output =ps.sqldf("select year, count(distinct Email) as Students,Course from df group by (Course) order by (Students) desc limit 20")


# In[16]:


output


# In[17]:


pip install plotly_express==0.4


# In[18]:


get_ipython().system('pip install dash')
get_ipython().system('pip install dash-renderer')
get_ipython().system('pip install dash_html_components')
get_ipython().system('pip install dash_core_components')
get_ipython().system('pip install dash_bootstrap_components')


# In[19]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


# In[20]:


import re
from typing import Collection


# In[21]:


from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go


# In[22]:


get_ipython().system('pip install jupyter-dash -q')


# In[23]:


from jupyter_dash import JupyterDash


# In[24]:


import plotly.express as px

import base64


# In[25]:


fig_2 = px.bar(output, x = 'Course', y = 'Students')
fig_2.update_layout(bargap=0.2)
fig_2.update_layout(yaxis_range=[0,12000])
length=200
fig_2.update_layout(
    xaxis = {
     'tickmode': 'array',
     'tickvals': list(range(length)),
     'ticktext': output['Course'].str.slice(-30).tolist(),
    }
)
fig_2.show()


# In[26]:


output_1 =ps.sqldf("select year, count(distinct Email) as Students from df group by (year)")


# In[27]:


output_1


# In[28]:


fig_1 = px.bar(output_1, x = 'year', y = 'Students')
fig_1.update_layout(bargap=0.2)
fig_1.update_layout(yaxis_range=[200,15000])
fig_1.show()


# In[29]:


df['month'] = pd.DatetimeIndex(df['Date']).month
print(df)


# In[30]:


df["Date"] = pd.to_datetime(df["Date"],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)


# In[31]:


#df['Months']=df.Date.dt.strftime("%B")

df['month'] = pd.DatetimeIndex(df['Date']).month
print(df)


# In[32]:


#df['months']=df.Date.dt.month_name()

df['converted_col'] = pd.to_datetime(df.Date, format='%Y-%m-%d %H:%M:%S')
df


# In[33]:


df['months']=df.converted_col.dt.month_name()
df


# In[34]:


month = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


# In[35]:


#df.sort_values('month', key = lambda x : pd.Categorical(x, categories=months, ordered=True))

test_1 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2022 group by(months) ")


# In[36]:


test_1


# In[37]:


final_1=test_1.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_1


# In[38]:


test_2 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2021 group by(months)")
test_2


# In[39]:


final_2=test_2.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_2


# In[40]:


test_3 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2020 group by(months)")
test_3


# In[41]:


final_3=test_3.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_3


# In[42]:


test_4 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2019 group by(months)")
test_4


# In[43]:


final_4=test_4.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_4


# In[44]:


test_5 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2018 group by(months)")
test_5


# In[45]:


final_5=test_5.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_5


# In[46]:


test_6 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2017 group by(months)")
test_6


# In[47]:


final_6=test_6.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_6


# In[48]:


test_7 =ps.sqldf("select count(distinct Email) as Students,months from df  where year=2023 group by(months)")
test_7


# In[49]:


final_7=test_7.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
final_7


# In[50]:


inter_2022 =ps.sqldf("select count(distinct Email) as Students, months from df where Course like '%interview_preperation%' and year = '2022' group by months ")
inter_2022


# In[51]:


intprep_2022=inter_2022.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
intprep_2022


# In[52]:


inter_2023 =ps.sqldf("select count(distinct Email) as Students, months from df where Course like '%interview_preperation%' and year = '2023' group by months ")
inter_2023


# In[53]:



# Using pandas.DatetimeIndex() to extract month and year
df_1['year'] = pd.DatetimeIndex(df_1['Date']).year

print(df_1)


# In[54]:


df_1['month'] = pd.DatetimeIndex(df_1['Date']).month
print(df_1)


# In[55]:


df_1["Date"] = pd.to_datetime(df_1["Date"],errors='coerce').dt.strftime('%Y-%m-%d')
print(df_1)


# In[56]:


#df['Months']=df.Date.dt.strftime("%B")

df_1['month'] = pd.DatetimeIndex(df_1['Date']).month
print(df_1)


# In[57]:


#df['months']=df.Date.dt.month_name()

df_1['converted_col'] = pd.to_datetime(df_1.Date, format='%Y-%m-%d %H:%M:%S')
df_1


# In[58]:


df_1['Month']=df_1.converted_col.dt.month_name()
df_1['Date'] = pd.to_datetime(df_1['Date'])
df_1['month_year'] = df_1['Date'].dt.to_period('M')
df_1['Date'] = df_1['Date'].astype(str)
df_1['month_year'] = df_1['month_year'].astype(str)
df_1


# In[59]:


df = px.data.tips()
fig_2017 = px.bar(final_6, x="Students", y="months", orientation='h')
fig_2017.show()


# In[60]:


df = px.data.tips()
fig_2018 = px.bar(final_5, x="Students", y="months", orientation='h')
fig_2018.show()


# In[61]:


df = px.data.tips()
fig_2019 = px.bar(final_4, x="Students", y="months", orientation='h')
fig_2019.show()


# In[62]:


df = px.data.tips()
fig_2020 = px.bar(final_3, x="Students", y="months", orientation='h')
fig_2020.show()


# In[63]:


df = px.data.tips()
fig_2021 = px.bar(final_2, x="Students", y="months", orientation='h')
fig_2021.show()


# In[64]:


df = px.data.tips()
fig_2022 = px.bar(final_1, x="Students", y="months", orientation='h')
fig_2022.show()


# In[65]:


df = px.data.tips()
fig_2023 = px.bar(final_7, x="Students", y="months", orientation='h')
fig_2023.show()


# In[66]:


df = px.data.tips()
plot_2022 = px.bar(intprep_2022, x="Students", y="months", orientation='h')
plot_2022.show()


# In[67]:


intprep_2023=inter_2023.sort_values('months', key = lambda x : pd.Categorical(x, categories=month, ordered=True))
intprep_2023


# In[68]:


df = px.data.tips()
plot_2023 = px.bar(intprep_2023, x="Students", y="months", orientation='h')
plot_2023.show()


# In[69]:


get_ipython().system('pip install numpy')


# In[70]:


import numpy as np


# In[71]:


from dash.dependencies import Input, Output, State


# In[72]:


app = JupyterDash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server


# In[73]:


app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1('Hackveda '),
            html.H2('Statistics'),
        ], style={'textAlign': 'center'}),
    ]),

    html.Div([
      html.H4(children='Students Joined in Year',style={"margin-left": "26px", "margin-top": "20px"}),

    dcc.Graph(
        id='example-graph',
        figure=fig_1
    ),
    html.Div([
      html.H4(children='Number of Students in Course',style={"margin-left": "26px"}),
      dcc.Graph(id='graph2',figure=fig_2),
   ])
    ])
,



        dbc.Col([html.H4('Total Interns Monthly Breakdown'),], style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
        html.Label(['Year'],style={'font-weight': 'bold',"margin-left": "38px"}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': '2017', 'value': 'fig_2017'},
                {'label': '2018', 'value': 'fig_2018'},
                {'label': '2019', 'value': 'fig_2019'},
                {'label': '2020', 'value': 'fig_2020'},
                {'label': '2021', 'value': 'fig_2021'},
                {'label': '2022', 'value': 'fig_2022'},
                {'label': '2023', 'value': 'fig_2023'},
                    ],
            value='fig_2022',
            style={"width": "60%", "verticalAlign": "middle", "margin-left": "20px", "margin-top": "10px"}),

    (dcc.Graph(id='graph')),

         dbc.Col([html.H4('Students Enrolled In Interview Preparation'),
                  html.H5('Monthly Breakdown'),], style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
        html.Label(['Year'],style={'font-weight': 'bold',"margin-left": "38px"}),
        dcc.Dropdown(
            id='dropdown_1',
            options=[
                {'label': '2022', 'value': 'plot_2022'},
                {'label': '2023', 'value': 'plot_2023'},
        ],
        value='plot_2022',
        style={"width": "60%", "verticalAlign": "middle", "margin-left": "20px", "margin-top": "10px"}),
    (dcc.Graph(id='graph_1')),

    dbc.Row([
        dbc.Col([
            html.H4('Day Wise Joining In Interview Preparation')],
            style={"margin-top": "60px", 'textAlign': 'center', "font-size": "70"}),
    ]),
    dbc.Row([
        dbc.Col([
        html.Label(['Year'],style={'font-weight': 'bold',"margin-left": "3px","margin-top": "8px"}),
        dcc.Dropdown(
            id='dropdown_3',
            options=[{'label':x,'value':x} for x in df_1.sort_values('year')['year'].unique()],
            value=df_1['year'].iloc[0],
            ),
        ],style={"width": 5,"margin-left": "40px","margin-top": "20px"}),
        dbc.Col([
        html.Label(['Month'],style={'font-weight': 'bold',"margin-left": "3px","margin-top": "8px"}),
        dcc.Dropdown(
            id='dropdown_4',
            options=[{'label':x,'value':x} for x in df_1.sort_values('month_year')['month_year'].unique()],
            value=df_1['month_year'].iloc[0]),
        ],style={"width": 5,"margin-left": "55px","margin-top": "20px"}),
        dbc.Col([
        dbc.Button("SHOW", id="btn", color="dark", className="ms-2", size='sm'),
        ],style={"width": 1,"margin-top":"48px","margin-left":"35px"}),
    ]),
        dcc.Graph(id='graph_2'),
        dcc.Store(id='store-data', data=[], storage_type='memory')

])

@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def drop_chart(value):
    if value == 'fig_2017':
        fig_2017 = px.bar(final_6, x="Students", y="months", orientation='h')
        return fig_2017
    if value == 'fig_2018':
        fig_2018 = px.bar(final_5, x="Students", y="months", orientation='h')
        return fig_2018
    if value == 'fig_2019':
        fig_2019 = px.bar(final_4, x="Students", y="months", orientation='h')
        return fig_2019
    if value == 'fig_2020':
        fig_2020 = px.bar(final_3, x="Students", y="months", orientation='h')
        return fig_2020
    if value == 'fig_2021':
        fig_2021 = px.bar(final_2, x="Students", y="months", orientation='h')
        return fig_2021
    if value == 'fig_2022':
        fig_2022 = px.bar(final_1, x="Students", y="months", orientation='h')
        return fig_2022
    if value == 'fig_2023':
        fig_2023 = px.bar(final_7, x="Students", y="months", orientation='h')
        return fig_2023

@app.callback(
    Output('graph_1', 'figure'),
    [Input(component_id='dropdown_1', component_property='value')]
)
def drop_chart1(value_1):
    if value_1 == 'plot_2022':
        plot_2022 = px.bar(intprep_2022, x="Students", y="months", orientation='h')
        return plot_2022
    if value_1 == 'plot_2023':
        plot_2023 = px.bar(intprep_2023, x="Students", y="months", orientation='h')
        return plot_2023

@app.callback(Output('dropdown_4','options'),
             Input('dropdown_3','value'))
def update_options(dropdown_3):
    df_2 = df_1[df_1['year'] == dropdown_3]
    return [{'label':x,'value':x} for x in df_2.sort_values('month_year')['month_year'].unique()]

@app.callback(
    Output('store-data', 'data'),
    Input('btn','n_clicks'),
    [State(component_id='dropdown_3', component_property='value'),
     State(component_id='dropdown_4', component_property='value')])

def update_data(n_clicks,dropdown_3, dropdown_4):
    global dff
    dff = df_1.copy()
    if dropdown_3 != []:
        dff = dff[dff['year'] == dropdown_3]
    if dropdown_4 != []:
        dff = dff[dff['month_year'] == dropdown_4]
    else:
        dff = df_1.copy()
    return dff.to_dict(orient='records')


@app.callback(
    Output('graph_2', 'figure'),
    Input('store-data','data'))
def drop_chart2(n):
    dff_1 = dff.copy()
    dff_pivot = pd.pivot_table(dff_1,('Students'),index=['Date'],aggfunc='count').reset_index()
    plotd_2023_jan = px.bar(dff_pivot, x="Date", y="Students", orientation='v')
    plotd_2023_jan.update_layout(bargap=0.23,height=724,xaxis = {'type' : 'category'})

    return plotd_2023_jan


# In[74]:


if __name__ == '__main__':
        app.run_server(port=8037, mode="inline")

