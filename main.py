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
            id="check_potential",
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
    [
    Output(component_id='radar-graph', component_property='figure')
    ],
    Input(component_id='check_potential', component_property='value')
)

def update_graph(value):
    dff = df[df.Potenzial == value]

    dff.astype({"spreadsheet": 'float64',
                "language": 'float64',
                "bi": 'float64'
                })

    bi_val = dff['bi'].sum()

    spreadsheet_val = dff['spreadsheet'].sum()

    language_val = dff['language'].sum()

    df_radar = pd.DataFrame(dict(
        r=[bi_val, spreadsheet_val, language_val],
        theta=['BI', 'Tabellenkalkulation', 'Programmiersprache']))

    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)

    return fig

# run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),