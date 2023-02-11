# region import
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Dash
from dash import State
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
# endregion

# region read data

df = pd.read_csv("data.csv", encoding='utf-8-sig', sep=';')

# endregion

# region init app

external_stylesheets = [dbc.themes.SPACELAB]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           )

server = app.server

#endregion

# region create html components: headers

header = html.H3("Durchblick im Datendschungel",
                 className="bg-primary mt-3 p-1 text-white text-center")

sub_header = html.H6("Eine Entscheidungshilfe zur Auswahl von Softwarelösungen für das kommunale (Bildungs)Datenmanagement",
                 className="bg-primary mb-2 p-1 pb-3 text-white text-center")
                 #className="bg-primary text-white p-3 mb-2 text-center")

# endregion
 
# region create html components: collapse bar 

# collapse_etablierung = html.Div(
#     [
#         dbc.Button(
#             "Etablierung",
#             id="collapse_etablierung_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Etablierung und Verfügbarkeit in der kommunalen Verwaltung"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_etablierung",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_benutzerfreundlichkeit = html.Div(
#     [
#         dbc.Button(
#             "Benutzerfreundlichkeit",
#             id="collapse_benutzerfreundlichkeit_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_benutzerfreundlichkeit",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_anschaffungskosten = html.Div(
#     [
#         dbc.Button(
#             "Anschaffungskosten",
#             id="collapse_anschaffungskosten_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_anschaffungskosten",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_integration = html.Div(
#     [
#         dbc.Button(
#             "Integration",
#             id="collapse_integration_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_integration",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_zusammenarbeit = html.Div(
#     [
#         dbc.Button(
#             "Zusammenarbeit",
#             id="collapse_zusammenarbeit_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_zusammenarbeit",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_datenmengen = html.Div(
#     [
#         dbc.Button(
#             "Datenmengen",
#             id="collapse_datenmengen_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_datenmengen",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_datenqualitaet = html.Div(
#     [
#         dbc.Button(
#             "Datenqualität",
#             id="collapse_datenqualitaet_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_datenqualitaet",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_datenanalyse = html.Div(
#     [
#         dbc.Button(
#             "Datenanalyse",
#             id="collapse_datenanalyse_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_datenanalyse",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_rechtemanagement = html.Div(
#     [
#         dbc.Button(
#             "Rechtemanagement",
#             id="collapse_rechtemanagement_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_rechtemanagement",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_nachhaltigkeit = html.Div(
#     [
#         dbc.Button(
#             "Nachhaltigkeit",
#             id="collapse_nachhaltigkeit_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_nachhaltigkeit",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_dashboards = html.Div(
#     [
#         dbc.Button(
#             "Dashboards",
#             id="collapse_dashboards_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_dashboards",
#                 is_open=False,
#             ),
#     ]
# )

# collapse_schnittstellen = html.Div(
#     [
#         dbc.Button(
#             "Schnittstellen",
#             id="collapse_schnittstellen_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_schnittstellen",
#                 is_open=False,
#             ),
#     ]
# )
# endregion

# region create html components: checklist

check_potential = html.Div(
    [
        #dbc.Label("Wählen Sie aus der Liste aus, welche Anforderungen die von Ihnen gesuchte Software-Lösung für das kommunale Datenmanagement erfüllen soll:", 
        #    style={"margin-bottom": "30px"}
        #    ),
        dcc.Checklist(
            df['Potenzial'].unique(),
            id="check_potential",
            value=["Benutzerfreundlichkeit"],
            #labelStyle = dict(display='block'), 
            labelStyle = {"display": "block", "margin-bottom": "15px"}, # places each checkbox in a single line, margin-bottom creates space between labels
            inputStyle={"margin-right": "10px"}, # creates space between checkbox and label
        ),
    ], style={
        'width': '100%',
        'display': 'inline-block'
    },
    className="mb-4",
)

# header for checklist
header_checklist = html.Div(
    [
    dbc.Label("Wählen Sie Ihre Anforderungen aus (mind. 1):",
        style={"margin-bottom": "13px", "margin-top": "13px", "font-weight": "bold"}
        ),
    ], style={
        'width': '100%',
        'display': 'inline-block'
    },
    className="mb-4",
)
# endregion

# region create html components: sliders

# header for the sliders
header_sliders = html.Div(
    [
    dbc.Label("Gewichten Sie Ihre Anforderungen (optional):",
        style={"margin-bottom": "13px", "margin-top": "13px", "font-weight": "bold"}
        ),
    ], style={
        'width': '100%',
        'display': 'inline-block'
    },
    className="mb-4",
)

# variables for quick adjustments to the statistical weight of the items (controlled by the sliders):

min_var= 1
max_var= 11
step_var= 5
value_var= 6
marks_dict = {1: "weniger wichtig", 6: "gleich wichtig", 11: "wichtiger"}

# slider elements to increase or decrease the importance of items. each slider is placed in a div-container so we can individually control their visibility:

container_slider_etablierung = html.Div(id="container_slider_etablierung", 
    children=[
        #dbc.Label("Etablierung", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_etablierung')
    ],
    style= {'visibility': 'visible'}
)

container_slider_benutzerfreundlichkeit = html.Div(id="container_slider_benutzerfreundlichkeit", 
    children=[
        #dbc.Label("Benutzerfreundlichkeit", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_benutzerfreundlichkeit'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_anschaffungskosten = html.Div(id="container_slider_anschaffungskosten", 
    children=[
        #dbc.Label("Anschaffungskosten", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_anschaffungskosten'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_integration = html.Div(id="container_slider_integration", 
    children=[
        #dbc.Label("Integration", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_integration'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_zusammenarbeit = html.Div(id="container_slider_zusammenarbeit", 
    children=[
        #dbc.Label("Zusammenarbeit", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_zusammenarbeit'),
    ],
    style= {'visibility': 'visible'}
)
container_slider_datenmengen = html.Div(id="container_slider_datenmengen", 
    children=[
        #dbc.Label("Datenmengen", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_datenmengen'),
    ],
    style= {'visibility': 'visible'}
)
container_slider_datenqualitaet = html.Div(id="container_slider_datenqualitaet", 
    children=[
        #dbc.Label("Datenqualität", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_datenqualitaet'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_datenanalyse = html.Div(id="container_slider_datenanalyse", 
    children=[
        #dbc.Label("Datenanalyse", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_datenanalyse'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_rechtemanagement = html.Div(id="container_slider_rechtemanagement", 
    children=[
        #dbc.Label("Rechtemanagement", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_rechtemanagement'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_nachhaltigkeit = html.Div(id="container_slider_nachhaltigkeit", 
    children=[
        #dbc.Label("Nachhaltigkeit", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_nachhaltigkeit'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_dashboards = html.Div(id="container_slider_dashboards", 
    children=[
        #dbc.Label("Dashboards", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_dashboards'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_schnittstellen = html.Div(id="container_slider_schnittstellen", 
    children=[
        #dbc.Label("Schnittstellen", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_schnittstellen')
    ],
    style= {'visibility': 'visible', 'display': 'flex'}
)

# for later, if sliders go under checkboxes and need a label:
# container_slider_etablierung = html.Div(id="container_slider_etablierung", 
#     children=[
#         dbc.Label("Etablierung", className="h6"),
#         dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_etablierung')
#     ],
#     style= {'visibility': 'visible'}
# )

# endregion

# region create html components: radar plot

fig = html.Div(
    [dcc.Graph
        (
        id='radar-graph',
        config={'displayModeBar': True},
        #style={'width': '80vh', 'height': '40vh', 'display': 'inline-block'},
        style={'height': '80vh'},
    ),
    ],
)

# endregion

# region create html components: intro text

# TODO integrate into text and tab bar in collar bar

intro_text = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Hinweise zur Bedienung", style={"font-weight": "bold"}),
            html.P("Die Anforderungen an eine Datenmanagement-Lösung variieren im Einzelfall je nach kommunalen Zielstellungen, Bedarfen und Voraussetungen. Wählen Sie aus der linken Liste aus, welche Anforderungen die von Ihnen gesuchte Software-Lösung für das kommunale Datenmanagement erfüllen soll. Das Diagramm in der Mitte gibt Ihnen eine Einschätzung, welche Art von Software-Lösung zu Ihren Anforderungen passt.", className="card-text"),
            html.P("Für ein genaueres Ergebnis können Sie die ausgewählten Anforderungen mit den Schiebereglern rechts gewichten. Fragen Sie sich: 'Wie wichtig ist mir diese Anforderung im Vergleich zu den anderen ausgewählten Anforderungen?'", className="card-text"),
            html.P("Klicken Sie auf die Tabs in der rechten Leiste, um Erläuterungen zu den unten auswählbaren Anforderungen an ein kommunales Datenmanagement zu erhalten.", className="card-text"),
        ],
        #style={"width": "400px", "margin-bottom": "10px"},
    ),
    className="mt-3",
)

# collapse_etablierung = html.Div(
#     [
#         dbc.Button(
#             "Etablierung",
#             id="collapse_etablierung_button",
#             className="mb-3",
#             color="primary",
#             outline=True,
#             size="sm",
#             n_clicks=0,
#         ),
#         dbc.Collapse(
#             dbc.Card(
#                 dbc.CardBody(
#                         "Etablierung und Verfügbarkeit in der kommunalen Verwaltung"
#                     ),
#                     style={"width": "400px", "margin-bottom": "10px"},
#                 ),
#                 id="collapse_etablierung",
#                 is_open=False,
#             ),
#     ]
# )


# endregion

# region create html components: tab bar

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Etablierung und Verfügbarkeit in der kommunalen Verwaltung: Tabellenkalkulationssoftware ist auf den meisten Arbeitsrechnern der Kommunalverwaltung vorinstalliert und entsprechend weit verbreitet. Kombinierte Datenbank/BI-Tools und statistische Programmiersprachen müssen meist zunächst ausgewählt, angeschafft und eingeführt werden.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Benutzerfreundlichkeit und Einarbeitungsaufwand: Tabellenkalkulationssoftware verfügt über eine relativ intuitive Benutzeroberfläche mit vielen vorgefertigten Optionen zur Datenanalyse und -visualisierung. Die Veränderung von Datensätzen erfolgt durch direkte Eingabe in Zellen. Kombinierte Datenbank-/BI-Tools sind in der Einarbeitung aufwändiger, wenngleich moderne Anwendungen mittlerweile großen Wert auf eine benutzerfreundliche Oberfläche legen. Statistische Programmiersprachen schließlich erfordern den höchsten Einarbeitungsaufwand, da hier meist mit Befehlszeilen statt einer klassischen Benutzeroberfläche gearbeitet wird.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab4_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Anschaffungskosten: Tabellenkalkulationssoftware ist in der Regel auf Arbeitsrechnern vorinstalliert, sodass die Frage nach Anschaffungskosten zumeist gar nicht aufkommt. Kombinierte Datenbank-/BI-Tools können vergleichsweise teuer in der Anschaffung sein. Statistische Programmiersprachen hingegen sind frei verfügbar; Kosten fallen hier maximal für die Lizenzierung einer Entwicklungsumgebung an, falls nicht auf freie Software zurückgegriffen wird.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab5_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Möglichkeit der Zusammenführung und Integration von Datensätzen aus unterschiedlichen Quellen. Tabellen sind innerhalb einer Kalkulationssoftware statisch und untereinander zumeist nicht verknüpft. Diese Verknüpfungen müssen manuell hergestellt werden, wobei Daten aus anderen Tabellen abgerufen werden. Es bleiben jedoch getrennt voneinander bestehende Dateien. Ändert sich ein Dateiname oder Speicherort, müssen die Verknüpfungen aktualisiert werden. Gleiches gilt für die Arbeit mit statistischen Programmiersprachen. Datenbanken hingegen sind standardmäßig relational, d.h. die in ihnen enthaltenen Daten sind im Rahmen eines Datenmodells miteinander verknüpft.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab6_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Möglichkeit der effektiven Zusammenarbeit mehrerer Nutzer an derselben Datenbasis. Die Bearbeitung von Tabellen per Kalkulationssoftware im Rahmen einer Cloudlösung ermöglicht ein Mindestmaß an Zusammenarbeitsmöglichkeiten. Gleiches gilt für die Arbeit mit statistischen Programmiersprachen. Kombinierte Datenbank-/BI-Tools sind dagegen für die Bearbeitung durch eine große Anzahl an Nutzern ausgelegt. Daten, die durch einen Nutzer eingegeben oder verändert werden, stehen sofort allen anderen Nutzern zur Verfügung, da sich alle auf dieselbe Datengrundlage beziehen.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab7_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Eignung zur effizienten Verarbeitung großer Datenmengen. Tabellen innerhalb einer Kalkulationssoftware laden jederzeit alle enthaltenen Daten und stellen sie für weitere Analyse- und Filteroperationen bereit. Das ist zunächst gut, um sich rasch einen Überblick zu verschaffen, kann aber den Arbeitsspeicher von Rechnern schnell an seine Grenzen bringen, sobald Tabellen einen gewissen Umfang erreichen. Statistische Programmiersprachen eignen sich in diesem Fall besser, da sie ab einer gewissen Datenmenge dieselben Rechenoperationen wesentlich schneller erledigen. Ähnliches gilt für kombinierte Datenbank-/BI-Tools, da diese die eigentlichen Daten im Hintergrund speichern und nur jene Ausschnitte laden, die zur Analyse und Betrachtung angefragt werden. Tabellenkalkulationssoftware ist daher für die Arbeit mit kleineren Datensätzen geeignet und ermöglicht deren schnelle Bearbeitung, während Datenbank-/BI-Systeme sowie statistische Programmiersprachen ihre Stärken bei der Verarbeitung großer bis sehr großer Datensätze entfalten.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab8_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Wirksame Funktionen und Mechanismen zum Schutz der Datenqualität (v. a. hinsichtlich Validität und Einheitlichkeit). Tabellen innerhalb einer Kalkulationssoftware haben standardmäßig keine Beschränkungen, welche Spalte mit welchem Datentyp gefüllt werden kann. Dies bringt viel Flexibilität, geht jedoch auf Kosten der Integrität, v. a. bei der Zusammenarbeit mit vielen Nutzern. Ähnliches gilt für die Arbeit mit statistischen Programmiersprachen. Kombinierte Datenbank-/BI-Tools sehen standardmäßig vor, dass z. B. für jede Spalte Datentypen definiert werden. Wird Text in eine Zahlenspalte eingegeben, erfolgt eine Fehlermeldung.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab9_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Leistungsfähige Funktionen zur Datenanalyse und -visualisierung. Tabellenkalkulationssoftware bietet eine Vielzahl an Analyseformeln sowie vorgefertigten Diagrammschablonen zur schnellen Datenanalyse und -visualisierung. Die diesbezüglichen Möglichkeiten von kombinierten Datenbank-/BI-Tools sind zumeist nicht viel weitreichender, wohingegen statistische Programmiersprachen durch die freie Verfügbarkeit einer Vielzahl an sog. „Bibliotheken“ zur Erweiterung des Funktionsumfangs schier unbegrenzte Möglichkeiten der Datenanalyse und -visualisierung bieten.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab10_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Leistungsfähiges Rechtemanagement, welches den Datenzugriff steuert und die Einhaltung von Datenschutzregeln ermöglicht. Kombinierte Datenbank-/BI-Tools machen es dem Anwender leicht, den Zugriff der Nutzer auf Datensätze zu kontrollieren und differenziert zu steuern. Softwareprodukte für Tabellenkalkulation haben hier weitaus weniger Möglichkeiten: Wenn z. B. ein Dashboard im Format der Tabellenkalkulationssoftware geteilt wird, hat der Nutzer uneingeschränkten Zugriff auf die dahinterliegenden Daten. Gleiches gilt für die Arbeit mit statistischen Programmiersprachen. Durch den Einsatz von Passwörtern lässt sich der Lese- und Schreibzugriff in gewissem Umfang kontrollieren, doch die Steuerungsmöglichkeiten bleiben deutlich hinter denen eines kombinierten Datenbank-/BI-Tools zurück.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab11_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Nachhaltigkeit durch nachvollziehbare und nachnutzbare Bearbeitungs- und Dokumentationsformate. Während die Möglichkeiten des syntaxbasierten Bearbeitens von Daten (also des Bearbeitens per Befehlssprache) inklusive der Speicherung und Automatisierung bestimmter Datenaufbereitungsschritte in Tabellenkalkulationsprogrammen eingeschränkt sind, ist dies in statistischen Programmiersprachen ein Standardverfahren und trägt somit zu einem personenunabhängigeren Datenmanagement bei.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab12_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Leistungsfähige Funktionen zur Erstellung von Berichten und Dashboards. Über die Verknüpfung einer „Berichts“-Tabelle mit mehreren Datentabellen lassen sich auch mit Tabellenkalkulationssoftware automatisch aktualisierte Berichte oder Dashboards erstellen. Jedoch übertragen sich hier die Nachteile der Aspekte „Analyse und Visualisierung“, „Datenschutz und Rechtemanagement“ sowie „Zusammenführung von Datensätzen“ auf die so zusammengebauten Dashboards. Kombinierte Datenbank-/BI-Tools hingegen haben zumeist eigens für die Erstellung von Berichten und Dashboards vorgesehene Funktionsbereiche, die ein stabiles und auf die dahinterliegende Datenbank bezogenes Berichtssystem ermöglichen. Statistische Programmiersprachen ermöglichen durch die Installation entsprechender Bibliotheken ebenfalls die Erstellung von interaktiven Dashboards, allerdings darf auch hier der Einarbeitungsaufwand nicht unterschätzt werden (vgl. „Benutzerfreundlichkeit und Einarbeitungsaufwand“).", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)

tab13_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("Nutzung von Schnittstellen für die Bereitstellung und Publikation von Daten sowie deren Beschaffung im Rahmen neuer Datenprojekte. Sowohl statistische Programmiersprachen als auch kombinierte Datenbank-/BI-Tools bieten gute Möglichkeiten der Schnittstellenprogrammierung, z. B. zum Bezug von Daten aus Fachinformationssystemen und Datenbanken. Bei Tabellenkalkulationsprogrammen sind diese Möglichkeiten eingeschränkter.", className="card-text"),
        ]
    ),
    className="mt-3 border-0",
)



# endregion

# region create layout


headers = dbc.Card([
    header,
    sub_header], 
    className="bg-primary border-0"
    )

tabs = dbc.Tabs(
    [
        dbc.Tab(tab2_content, label="Etablierung"),
        dbc.Tab(tab3_content, label="Benutzerfreundlichkeit"),
        dbc.Tab(tab4_content, label="Anschaffungskosten"),
        dbc.Tab(tab5_content, label="Integration"),
        dbc.Tab(tab6_content, label="Zusammenarbeit"),
        dbc.Tab(tab7_content, label="Datenmengen"),
        dbc.Tab(tab8_content, label="Datenqualität"),
        dbc.Tab(tab9_content, label="Datenanalyse"),
        dbc.Tab(tab10_content, label="Rechtemanagement"),
        dbc.Tab(tab11_content, label="Nachhaltigkeit"),
        dbc.Tab(tab12_content, label="Dashboards"),
        dbc.Tab(tab13_content, label="Schnittstellen"),
    ],
    style={"margin-bottom": "13px"},
    className="pt-3"
)

checklist = dbc.Card([
    header_checklist,
    check_potential], 
    className="border-0 pt-3"
    )

sliders = dbc.Card([
    header_sliders, 
    container_slider_etablierung, 
    container_slider_benutzerfreundlichkeit,
    container_slider_anschaffungskosten,
    container_slider_integration,
    container_slider_zusammenarbeit,
    container_slider_datenmengen,
    container_slider_datenqualitaet,
    container_slider_datenanalyse,
    container_slider_rechtemanagement,
    container_slider_nachhaltigkeit,
    container_slider_dashboards,
    container_slider_schnittstellen], 
    className="border-0 pt-3")

chart1 = dbc.Card([fig], body=True, className="border-0 pt-3")

app.layout = dbc.Container(
    [
        headers,

        dbc.Row(
            [
                dbc.Col(
                    [intro_text],
                    xs=10, sm=8, md=4, lg=4, xl=4,
                ),
                dbc.Col(
                    [tabs],
                    xs=10, sm=8, md=8, lg=8, xl=8
                )
            ],
            className="px-4",
        ),

        # dbc.Row
        # ([
        #     dbc.Col([collapse_etablierung], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_benutzerfreundlichkeit], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_anschaffungskosten], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_integration], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_zusammenarbeit], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_datenmengen], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_datenqualitaet], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_datenanalyse], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_rechtemanagement], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_nachhaltigkeit], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_dashboards], xs=6, sm=3, md=2, lg=2, xl=2,),
        #     dbc.Col([collapse_schnittstellen], xs=6, sm=3, md=2, lg=2, xl=2,),
        #   ],
        #   justify="center"
        # ),

        dbc.Row
        (
            [
                dbc.Col([checklist],
                        #width=2,
                        xs=10, sm=8, md=5, lg=3, xl=3,
                        style={"height": "80%"}
                        ),
                dbc.Col([chart1],
                        #width=6,
                        xs=10, sm=8, md=5, lg=12, xl=6,
                        style={"height": "80%"}
                        ),
                dbc.Col([sliders],
                        #width=3,
                        xs=10, sm=8, md=5, lg=3, xl=3,
                        style={"height": "80%"}
                        ),

            ],
            className="vh-50 g-6 px-4",
            justify="center"
        ),
    ],
    fluid=True,
    className="dbc",
    style={"height": "100vh"}
)

# endregion

# region callback function 1

@app.callback(
    # keeping the square brackets around the output (inherited from a project with multiple outputs) caused severe problems, because it expected a list of outputs
    # remember to place / remove the square brackets around the output components depending on wether its one or several ouputs...
    Output(component_id='radar-graph', component_property='figure'),
    [
        Input(component_id='check_potential', component_property='value'),
        Input(component_id='slider_etablierung', component_property='value'),
        Input(component_id='slider_benutzerfreundlichkeit', component_property='value'),
        Input(component_id='slider_anschaffungskosten', component_property='value'),
        Input(component_id='slider_integration', component_property='value'),
        Input(component_id='slider_zusammenarbeit', component_property='value'),
        Input(component_id='slider_datenmengen', component_property='value'),
        Input(component_id='slider_datenqualitaet', component_property='value'),
        Input(component_id='slider_datenanalyse', component_property='value'),
        Input(component_id='slider_rechtemanagement', component_property='value'),
        Input(component_id='slider_nachhaltigkeit', component_property='value'),
        Input(component_id='slider_dashboards', component_property='value'),
        Input(component_id='slider_schnittstellen', component_property='value'),
    ]
    )

def update_graph(selected_potential, weight_etablierung, weight_benutzerfreundlichkeit, weight_anschaffungskosten, weight_integration,
                weight_zusammenarbeit, weight_datenmengen, weight_datenqualitaet, weight_datenanalyse, 
                weight_rechtemanagement, weight_nachhaltigkeit, weight_dashboards, weight_schnittstellen):

    dff = df[df['Potenzial'].isin(selected_potential)]
    dff = dff.set_index('Potenzial')

    dff.astype({"Tabellenkalkulationssoftware": 'float64',
                "Statistische Programmiersprache": 'float64',
                "Kombinierte Datenbank/BI-Software": 'float64'
                })

    dff = dff.reset_index()
    dffm = pd.melt(dff, id_vars='Potenzial', value_vars=['Tabellenkalkulationssoftware', 'Statistische Programmiersprache', 'Kombinierte Datenbank/BI-Software'])

    # multiply values according to sliders
    dffm["value"] = np.where(dffm["Potenzial"]=="Etablierung", dffm["value"]*weight_etablierung, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Benutzerfreundlichkeit", dffm["value"]*weight_benutzerfreundlichkeit, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Anschaffungskosten", dffm["value"]*weight_anschaffungskosten, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Integration", dffm["value"]*weight_integration, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Zusammenarbeit", dffm["value"]*weight_zusammenarbeit, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Datenmengen", dffm["value"]*weight_datenmengen, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Datenqualität", dffm["value"]*weight_datenqualitaet, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Datenanalyse", dffm["value"]*weight_datenanalyse, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Rechtemanagement", dffm["value"]*weight_rechtemanagement, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Nachhaltigkeit", dffm["value"]*weight_nachhaltigkeit, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Dashboards", dffm["value"]*weight_dashboards, dffm['value'])
    dffm["value"] = np.where(dffm["Potenzial"]=="Schnittstellen", dffm["value"]*weight_schnittstellen, dffm['value'])

    
    dffg = dffm.groupby(['variable']).agg({'value':'sum'}).reset_index()

    fig = px.line_polar(dffg, r='value', theta='variable', 
        line_close=True, 
        title="Welches Software-Tool passt zu meinen Anforderungen?", 
        template="seaborn",
        hover_data=["value"]
        )
    
    #TODO implement text field which shows text according to whichever tool has max value (plus additional text when differenze between tools is <5% of max value)

    return fig

# endregion

# region callback function 2 to have at least one checkbox checked

# see here: https://stackoverflow.com/questions/70157734/how-to-limit-the-number-of-selected-checkboxes-in-checklist-in-dashplotly

@app.callback(
    Output("check_potential", "value"),
    Input("check_potential", "value"),
)
    
def update_checklist(value):
     if len(value) == 0:
        value = ["Benutzerfreundlichkeit"]
     return value
   
# endregion

# region one callback for each slider, to show/hide the slider when the corresponding checkbox is checked/not checked

@app.callback(
    Output(component_id='container_slider_etablierung', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_etabl(selected_boxes):
    if "Etablierung" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_benutzerfreundlichkeit', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_benutz(selected_boxes):
    if "Benutzerfreundlichkeit" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_anschaffungskosten', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_kosten(selected_boxes):
    if "Anschaffungskosten" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_integration', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_integ(selected_boxes):
    if "Integration" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}


@app.callback(
    Output(component_id='container_slider_zusammenarbeit', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_koop(selected_boxes):
    if "Zusammenarbeit" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_datenmengen', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_mengen(selected_boxes):
    if "Datenmengen" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_datenqualitaet', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_quali(selected_boxes):
    if "Datenqualität" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_datenanalyse', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_analyse(selected_boxes):
    if "Datenanalyse" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_rechtemanagement', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_rechte(selected_boxes):
    if "Rechtemanagement" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_nachhaltigkeit', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_nachhaltigkeit(selected_boxes):
    if "Nachhaltigkeit" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_dashboards', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_dash(selected_boxes):
    if "Dashboards" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}

@app.callback(
    Output(component_id='container_slider_schnittstellen', component_property='style'),
    Input(component_id='check_potential', component_property='value')
    )

def show_hide_sstellen(selected_boxes):
    if "Schnittstellen" in selected_boxes:
        return {'visibility': 'visible'}
    else:
        return {'visibility': 'hidden'}   
# endregion

# region callbacks for collapse buttons

# @app.callback(
#     Output("collapse_etablierung", "is_open"),
#     [Input("collapse_etablierung_button", "n_clicks")],
#     [State("collapse_etablierung", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_benutzerfreundlichkeit", "is_open"),
#     [Input("collapse_benutzerfreundlichkeit_button", "n_clicks")],
#     [State("collapse_benutzerfreundlichkeit", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_anschaffungskosten", "is_open"),
#     [Input("collapse_anschaffungskosten_button", "n_clicks")],
#     [State("collapse_anschaffungskosten", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_integration", "is_open"),
#     [Input("collapse_integration_button", "n_clicks")],
#     [State("collapse_integration", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_zusammenarbeit", "is_open"),
#     [Input("collapse_zusammenarbeit_button", "n_clicks")],
#     [State("collapse_zusammenarbeit", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_datenmengen", "is_open"),
#     [Input("collapse_datenmengen_button", "n_clicks")],
#     [State("collapse_datenmengen", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_datenqualitaet", "is_open"),
#     [Input("collapse_datenqualitaet_button", "n_clicks")],
#     [State("collapse_datenqualitaet", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_datenanalyse", "is_open"),
#     [Input("collapse_datenanalyse_button", "n_clicks")],
#     [State("collapse_datenanalyse", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_rechtemanagement", "is_open"),
#     [Input("collapse_rechtemanagement_button", "n_clicks")],
#     [State("collapse_rechtemanagement", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_nachhaltigkeit", "is_open"),
#     [Input("collapse_nachhaltigkeit_button", "n_clicks")],
#     [State("collapse_nachhaltigkeit", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_dashboards", "is_open"),
#     [Input("collapse_dashboards_button", "n_clicks")],
#     [State("collapse_dashboards", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("collapse_schnittstellen", "is_open"),
#     [Input("collapse_schnittstellen_button", "n_clicks")],
#     [State("collapse_schnittstellen", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# endregion

# region Todo

#TODO create callback for dynamic text field with nested if condition:
# https://www.w3schools.com/python/python_conditions.asp
#
# max_value = [place label of highest value tool here] 
#
# if max_value = "bi"
#   return text_bi
#       if "benutzerfreundlichkeit" in selected_potentials
#           return text_benutzerfreundlichkeit
# ...
# if max_value = "spreadsheet"
#   return text_spreadsheet
#       if "benutzerfreundlichkeit" in selected_potentials
#           return text_benutzerfreundlichkeit 
# endregion

# region run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),
# endregion