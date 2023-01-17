import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import openpyxl

# read data
## Potentialtabelle in der Ausgangsversion
df = pd.read_csv("data.csv", encoding='utf-8-sig', sep=';')
# init app

external_stylesheets = [dbc.themes.SPACELAB]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           )

server = app.server

potentiale = df['Potenzial'].unique()

# create html components

header = html.H4("Softwaresondierung",
                 className="bg-primary text-white p-3 mb-2 text-center")

## Checkboxen für jedes Potential


check_potential = html.Div(
    [
        dbc.Label("Wählen Sie einen Landkreis aus (Texteingabe möglich):"),
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


## SChieberegler für jedes Potential zur Gewichtung

# create layout


checklist = dbc.Card([check_potential], body=True)


app.layout = dbc.Container(
    [
        header,
        dbc.Row
        (
            [
                dbc.Col([check_potential],
                        #width=6,
                        xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
            ],
            className="vh-50, g-6"
        ),
# to control space between rows, play around with "margin-top" and "g-x" (unclear how it works exactly)
    ],
    fluid=True,
    className="dbc",
    style={"height": "100vh"}
)


# callback function

#   Ziel:
#   Tabelle mit einer Zeile je Potential und einer Spalte je Tool, unten wird Summe gezogen, Ergebnis wird im Plot angezeigt
#   Ob Zeile mit in die Tabelle kommen oder nicht, wird per Checkbox vom Benutzer festgelegt
#   Bonus: Schieberegler unter jede Checkbox, mit der die Gewichtung beeinflusst werden kann

# run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),