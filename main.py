import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np

# read data

df = pd.read_csv("data.csv", encoding='utf-8-sig', sep=';')

# init app

external_stylesheets = [dbc.themes.SPACELAB]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           )

server = app.server

# create html components

header = html.H4("Softwaresondierung",
                 className="bg-primary text-white p-3 mb-2 text-center")

# checkliste
check_potential = html.Div(
    [
        dbc.Label("Wählen Sie die für Sie wichtigen Potentiale aus:"),
        dcc.Checklist(
            df['Potenzial'].unique(),
            id="check_potential",
            value=["Etablierung", "Nachhaltigkeit"],
            labelStyle = dict(display='block'), # places each checkbox in a single line
            inputStyle={"margin-right": "10px"} # creates space between checkbox and label
        ),
    ], style={
        'width': '50%',
        'display': 'inline-block'
    },
    className="mb-4",
)

# slider
slider_etablierung = html.Div(
    [
    dcc.Slider(
        min=0, 
        max=2, 
        step=0.2, 
        value=1, 
        id='slider_etablierung')
    ], style={
        'width': '50%',
        'display': 'inline-block'
    },
)

# diagramm
fig = html.Div(
    [dcc.Graph
        (
        id='radar-graph',
        config={'displayModeBar': True},
        #style={'width': '80vh', 'height': '40vh', 'display': 'inline-block'},
        style={'height': '60vh'},
    ),
    ],
)
# create layout


checklist = dbc.Card([check_potential], body=True)

slider = dbc.Card([slider_etablierung], body=True)

chart1 = dbc.Card([fig], body=True)


app.layout = dbc.Container(
    [
        header,
        dbc.Row
        (
            [
                dbc.Col([checklist],
                        width=3,
                        #xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
                dbc.Col([slider],
                        width=3,
                        #xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
                dbc.Col([chart1],
                        width=6,
                        #xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
            ],
            className="vh-50, g-6"
        ),
    ],
    fluid=True,
    className="dbc",
    style={"height": "100vh"}
)


# callback function
# TODO implement sliders for weihging the potentials. Idea: store value of slider input in variable, then mutiply the corresponding line in dffm with it (before aggregating)

@app.callback(
    # keeping the square brackets around the output (inherited from a project with multiple outputs) caused severe problems, because it expected a list of outputs
    # remember to place / remove the square brackets around the output components depending on wether its one or several ouputs...
    Output(component_id='radar-graph', component_property='figure'),
    [
        Input(component_id='check_potential', component_property='value'),
        Input(component_id='slider_etablierung', component_property='value'), #remove this line for working version
    ]
    )

def update_graph(selected_potential, weight_etablierung):
    dff = df[df['Potenzial'].isin(selected_potential)]
    dff = dff.set_index('Potenzial')

    dff.astype({"spreadsheet": 'float64',
                "language": 'float64',
                "bi": 'float64'
                })

    dff = dff.reset_index()
    dffm = pd.melt(dff, id_vars='Potenzial', value_vars=['spreadsheet', 'language', 'bi'])

    dffm["value"] = np.where(dffm["Potenzial"]=="Etablierung", dffm["value"]*weight_etablierung, dffm['value'])

    #data["10th"] = np.where(data["10th"]<10, data["10th"]*10, data["10th"])
    
    dffg = dffm.groupby(['variable']).agg({'value':'sum'}).reset_index()

    fig = px.line_polar(dffg, r='value', theta='variable', line_close=True)

    return fig

# run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),