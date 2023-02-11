# write an application in python, using the library "dash".

# the application should contain a bar plot and a dropdown element. 

# start the app server at the end of the code.

# use a random data set.

import dash
from dash import dcc
from dash import html
from dash import Dash
import pandas as pd
import plotly.graph_objs as go

# import random data set
df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [1, 2, 3, 4]})

# create the app
app = Dash(__name__)

server = app.server

# create bar plot
app.layout = html.Div([
    # create a dropdown element
    dcc.Dropdown(
        id='graph-dropdown',
        options=[
            {'label': 'Bar Plot', 'value': 'bar'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
        ],
        value='bar'
    ),
    dcc.Graph(id='graph')
])

# update the graph based on the dropdown selection
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('graph-dropdown', 'value')])

def update_graph(dropdown_value):
    if dropdown_value == 'bar':
        return {
            'data': [go.Bar(
                x=df['x'],
                y=df['y']
            )],
            'layout': go.Layout(
                title='Bar Plot'
            )
        }
    elif dropdown_value == 'scatter':
        return {
            'data': [go.Scatter(
                x=df['x'],
                y=df['y'],
                mode='markers'
            )],
            'layout': go.Layout(
                title='Scatter Plot'
            )
        }

# run the server
if __name__ == '__main__':
    app.run_server(port=3003)