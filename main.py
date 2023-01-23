# region import
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Dash
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

# region create html components

header = html.H4("Softwaresondierung",
                 className="bg-primary text-white p-3 mb-2 text-center")

# checkliste

check_potential = html.Div(
    [
        dbc.Label("Wählen Sie aus der Liste aus, welche Anforderungen die von Ihnen gesuchte Software-Lösung für das kommunale Datenmanagement erfüllen soll:", 
            style={"margin-bottom": "30px"}
            ),
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

# slider
sliders = html.Div(
    [
    dbc.Label("Für ein genaueres Ergebnis können Sie die ausgewählten Anforderungen mit den Schiebereglern gewichten. Fragen Sie sich: 'Wie wichtig ist mir diese Anforderung im Vergleich zu den anderen ausgewählten Anforderungen?'",
        style={"margin-bottom": "35px"}
        ),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks={0.2: "weniger wichtig", 1: "gleich wichtig", 1.8: "wichtiger"}, id='slider_etablierung'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_benutzerfreundlichkeit'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_anschaffungskosten'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_integration'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_zusammenarbeit'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_datenmengen'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_datenqualitaet'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_datenanalyse'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_rechtemanagement'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_nachhaltigkeit'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_dashboards'),
    dcc.Slider(min=0.2, max=1.8, step=0.8, value=1, marks=None, id='slider_schnittstellen')
    ], style={
        'width': '100%',
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

# endregion

# region create layout

checklist = dbc.Card([check_potential], className="border-0")

sliders = dbc.Card([sliders], className="border-0")

chart1 = dbc.Card([fig], body=True)

app.layout = dbc.Container(
    [
        header,
        dbc.Row
        (
            [
                dbc.Col([checklist],
                        width=2,
                        #xs=10, sm=8, md=5, lg=6, xl=5,
                        style={"height": "80%"}
                        ),
                dbc.Col([sliders],
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

# region second callback to have at least one checkbox checked
#  second callback function to set a minimum of 1 checked checkbox (otherwise error occurs)
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

#TODO implement third callback function which sets slider from min to mid position (or activates it, or makes a change to layout from grey to colour) when the according checkbox is activated
# only makes sense if checkbox is automatically checked when slider is set to mid...
    # if "benutzerfreundlichkeit" isin(selected_potential) ....
# run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),