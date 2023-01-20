import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

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
            inline=True,
            id="check_potential",
            value=["Etablierung", "Nachhaltigkeit"],
        ),
    ], style={
        'width': '50%',
        'display': 'inline-block'
    },
    className="mb-4",
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

chart1 = dbc.Card([fig], body=True)


app.layout = dbc.Container(
    [
        header,
        dbc.Row
        (
            [
                dbc.Col([checklist],
                        #width=6,
                        xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
                dbc.Col([chart1],
                        #width=6,
                        xs=10, sm=8, md=5, lg=6, xl=5,
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


@app.callback(
    # keeping the square brackets around the output (inherited from a project with multiple outputs) caused severe problems
    # remember to place / remove the square brackets depending on wether its one or several ouputs...
    Output(component_id='radar-graph', component_property='figure'),
    Input(component_id='check_potential', component_property='value')
    )

def update_graph(selected_potential):
    dff = df[df['Potenzial'].isin(selected_potential)]
    dff = dff.set_index('Potenzial')

    dff.astype({"spreadsheet": 'float64',
                "language": 'float64',
                "bi": 'float64'
                })

    dff = dff.reset_index()
    dffm = pd.melt(dff, id_vars='Potenzial', value_vars=['spreadsheet', 'language', 'bi'])
    
    dffg = dffm.groupby(['variable']).agg({'value':'sum'}).reset_index()

    fig = px.line_polar(dffg, r='value', theta='variable', line_close=True)

    return fig

# run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),