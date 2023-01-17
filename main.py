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
df.head()
# init app

external_stylesheets = [dbc.themes.SPACELAB]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           )

server = app.server

# potentiale = df['Potenzial'].unique()

# create html components

header = html.H4("Softwaresondierung",
                 className="bg-primary text-white p-3 mb-2 text-center")

## Checkboxen für jedes Potential

dcc.Checklist(
    id="check_etablierung",
    options=[
              {'label': 'Etablierung und Verfügbarkeit in der kommunalen Verwaltung', 'value': 'Etablierung und Verfügbarkeit in der kommunalen Verwaltung'},
            ],
)

dcc.Checklist(
    id="check_benutzerfreundlichkeit",
    options=[
              {'label': 'Benutzerfreundlichkeit und Einarbeitungsaufwand', 'value': 'Benutzerfreundlichkeit und Einarbeitungsaufwand'},
            ],
)

dcc.Checklist(
    id="check_anschaffungskosten",
    options=[
              {'label': 'Anschaffungskosten', 'value': 'Anschaffungskosten'},
            ],
)

dcc.Checklist(
    id="check_integration",
    options=[
              {'label': 'Möglichkeit der Zusammenführung und Integration von Datensätzen aus unterschiedlichen Quellen', 'value': 'Möglichkeit der Zusammenführung und Integration von Datensätzen aus unterschiedlichen Quellen'},
            ],
)

dcc.Checklist(
    id="check_zusammenarbeit",
    options=[
              {'label': 'Möglichkeit der effektiven Zusammenarbeit mehrerer Nutzer an derselben Datenbasis', 'value': 'Möglichkeit der effektiven Zusammenarbeit mehrerer Nutzer an derselben Datenbasis'},
            ],
)

dcc.Checklist(
    id="check_datenmengen",
    options=[
              {'label': 'Eignung zur effizienten Verarbeitung großer Datenmengen', 'value': 'Eignung zur effizienten Verarbeitung großer Datenmengen'},
            ],
)

dcc.Checklist(
    id="check_datenqualitaet",
    options=[
              {'label': 'Wirksame Funktionen und Mechanismen zum Schutz der Datenqualität (v. a. hinsichtlich Validität und Einheitlichkeit)', 'value': 'Wirksame Funktionen und Mechanismen zum Schutz der Datenqualität (v. a. hinsichtlich Validität und Einheitlichkeit)'},
            ],
)

dcc.Checklist(
    id="check_datenanalyse",
    options=[
              {'label': 'Leistungsfähige Funktionen zur Datenanalyse und -visualisierung', 'value': 'Leistungsfähige Funktionen zur Datenanalyse und -visualisierung'},
            ],
)

dcc.Checklist(
    id="check_rechtemanagement",
    options=[
              {'label': 'Leistungsfähiges Rechtemanagement, welches den Datenzugriff steuert und die Einhaltung von Datenschutzregeln ermöglicht', 'value': 'Leistungsfähiges Rechtemanagement, welches den Datenzugriff steuert und die Einhaltung von Datenschutzregeln ermöglicht'},
            ],
)

dcc.Checklist(
    id="check_nachhaltigkeit",
    options=[
              {'label': 'Nachhaltigkeit durch nachvollziehbare und nachnutzbare Bearbeitungs- und Dokumentationsformate', 'value': 'Nachhaltigkeit durch nachvollziehbare und nachnutzbare Bearbeitungs- und Dokumentationsformate'},
            ],
)

dcc.Checklist(
    id="check_dashboard",
    options=[
              {'label': 'Leistungsfähige Funktionen zur Erstellung von Berichten und Dashboards', 'value': 'Leistungsfähige Funktionen zur Erstellung von Berichten und Dashboards'},
            ],
)

dcc.Checklist(
    id="check_schnittstellen",
    options=[
              {'label': 'Nutzung von Schnittstellen für die Bereitstellung und Publikation von Daten sowie deren Beschaffung im Rahmen neuer Datenprojekte', 'value': 'Nutzung von Schnittstellen für die Bereitstellung und Publikation von Daten sowie deren Beschaffung im Rahmen neuer Datenprojekte'},
            ],
)

## SChieberegler für jedes Potential zur Gewichtung

# create layout

etablierung = dbc.Card([check_etablierung], body=True)

benutzerfreundlichkeit = dbc.Card([check_benutzerfreundlichkeit], body=True)

anschaffungskosten = dbc.Card([check_anschaffungskosten], body=True)

integration = dbc.Card([check_integration], body=True)

zusammenarbeit = dbc.Card([check_zusammenarbeit], body=True)

datenmengen = dbc.Card([check_datenmengen], body=True)

datenqualitaet = dbc.Card([check_datenqualitaet], body=True)

datenanalyse = dbc.Card([check_datenanalyse], body=True)

rechtemanagement = dbc.Card([check_rechtemanagement], body=True)

nachhaltigkeit = dbc.Card([check_nachhaltigkeit], body=True)

dashboard = dbc.Card([check_dashboard], body=True)

schnittstellen = dbc.Card([check_schnittstellen], body=True)


app.layout = dbc.Container(
    [
        header,
        dbc.Row
        (
            [
                dbc.Col([input_and_map],
                        #width=6,
                        xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
                dbc.Col([chart_dotplot],
                        #width=6,
                        xs=10, sm=8, md=5, lg=6, xl=5,
                        style={'overflowY': 'scroll', 'height': "1250px"} # https://community.plotly.com/t/add-scrolling-options-to-plots/9493
                        # TODO scrollbar und höhe anpassen
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

## Checkboxen und Schieberegler in linker Spalte

# callback function

#   Ziel:
#   Tabelle mit einer Zeile je Potential und einer Spalte je Tool, unten wird Summe gezogen, Ergebnis wird im Plot angezeigt
#   Ob Zeile mit in die Tabelle kommen oder nicht, wird per Checkbox vom Benutzer festgelegt
#   Bonus: Schieberegler unter jede Checkbox, mit der die Gewichtung beeinflusst werden kann

# run server
