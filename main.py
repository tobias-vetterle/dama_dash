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

# region create html components

header = html.H4("Softwaresondierung",
                 className="bg-primary text-white p-3 mb-2 text-center")

 
collapse_etablierung = html.Div(
    [
        dbc.Button(
            "Etablierung",
            id="collapse_etablierung_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Etablierung und Verfügbarkeit in der kommunalen Verwaltung"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_etablierung",
                is_open=False,
            ),
    ]
)

collapse_benutzerfreundlichkeit = html.Div(
    [
        dbc.Button(
            "Benutzerfreundlichkeit",
            id="collapse_benutzerfreundlichkeit_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_benutzerfreundlichkeit",
                is_open=False,
            ),
    ]
)

collapse_anschaffungskosten = html.Div(
    [
        dbc.Button(
            "Anschaffungskosten",
            id="collapse_anschaffungskosten_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_anschaffungskosten",
                is_open=False,
            ),
    ]
)

collapse_integration = html.Div(
    [
        dbc.Button(
            "Integration",
            id="collapse_integration_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_integration",
                is_open=False,
            ),
    ]
)

collapse_zusammenarbeit = html.Div(
    [
        dbc.Button(
            "Zusammenarbeit",
            id="collapse_zusammenarbeit_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_zusammenarbeit",
                is_open=False,
            ),
    ]
)

collapse_datenmengen = html.Div(
    [
        dbc.Button(
            "Datenmengen",
            id="collapse_datenmengen_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_datenmengen",
                is_open=False,
            ),
    ]
)

collapse_datenqualitaet = html.Div(
    [
        dbc.Button(
            "Datenqualität",
            id="collapse_datenqualitaet_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_datenqualitaet",
                is_open=False,
            ),
    ]
)

collapse_datenanalyse = html.Div(
    [
        dbc.Button(
            "Datenanalyse",
            id="collapse_datenanalyse_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_datenanalyse",
                is_open=False,
            ),
    ]
)

collapse_rechtemanagement = html.Div(
    [
        dbc.Button(
            "Rechtemanagement",
            id="collapse_rechtemanagement_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_rechtemanagement",
                is_open=False,
            ),
    ]
)

collapse_nachhaltigkeit = html.Div(
    [
        dbc.Button(
            "Nachhaltigkeit",
            id="collapse_nachhaltigkeit_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_nachhaltigkeit",
                is_open=False,
            ),
    ]
)

collapse_dashboards = html.Div(
    [
        dbc.Button(
            "Dashboards",
            id="collapse_dashboards_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_dashboards",
                is_open=False,
            ),
    ]
)

collapse_schnittstellen = html.Div(
    [
        dbc.Button(
            "Schnittstellen",
            id="collapse_schnittstellen_button",
            className="mb-3",
            color="primary",
            outline=True,
            size="sm",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                        "Benutzerfreundlichkeit und Einarbeitungsaufwand der Software"
                    ),
                    style={"width": "400px", "margin-bottom": "10px"},
                ),
                id="collapse_schnittstellen",
                is_open=False,
            ),
    ]
)
# checklist

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
    dbc.Label("Die Anforderungen an eine Datenmanagement-Lösung variieren von Fall zu Fall. Wählen Sie aus der Liste aus, welche Anforderungen die von Ihnen gesuchte Software-Lösung für das kommunale Datenmanagement erfüllen soll: ",
        style={"margin-bottom": "13px"}
        ),
    ], style={
        'width': '100%',
        'display': 'inline-block'
    },
    className="mb-4",
)

# header for the sliders
header_sliders = html.Div(
    [
    dbc.Label("Für ein genaueres Ergebnis können Sie die ausgewählten Anforderungen mit den Schiebereglern gewichten. Fragen Sie sich: 'Wie wichtig ist mir diese Anforderung im Vergleich zu den anderen ausgewählten Anforderungen?'",
        style={"margin-bottom": "13px"}
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
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_etablierung')
    ],
    style= {'visibility': 'visible'}
)

container_slider_benutzerfreundlichkeit = html.Div(id="container_slider_benutzerfreundlichkeit", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_benutzerfreundlichkeit'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_anschaffungskosten = html.Div(id="container_slider_anschaffungskosten", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_anschaffungskosten'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_integration = html.Div(id="container_slider_integration", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_integration'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_zusammenarbeit = html.Div(id="container_slider_zusammenarbeit", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_zusammenarbeit'),
    ],
    style= {'visibility': 'visible'}
)
container_slider_datenmengen = html.Div(id="container_slider_datenmengen", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_datenmengen'),
    ],
    style= {'visibility': 'visible'}
)
container_slider_datenqualitaet = html.Div(id="container_slider_datenqualitaet", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_datenqualitaet'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_datenanalyse = html.Div(id="container_slider_datenanalyse", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_datenanalyse'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_rechtemanagement = html.Div(id="container_slider_rechtemanagement", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_rechtemanagement'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_nachhaltigkeit = html.Div(id="container_slider_nachhaltigkeit", 
    children=[
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_nachhaltigkeit'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_dashboards = html.Div(id="container_slider_dashboards", 
    children=[
        dbc.Label("Dashboards", className="small"),
        dcc.Slider(min=min_var, max=max_var, step=step_var, value=value_var, marks=marks_dict, id='slider_dashboards'),
    ],
    style= {'visibility': 'visible'}
)

container_slider_schnittstellen = html.Div(id="container_slider_schnittstellen", 
    children=[
        dbc.Label("Schnittstellen", className="small"),
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

# diagramm
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

# region create layout

# TODO place the headers above checklist and sliders in dedicated row OR card OR cardgroup, so they always have the same height and therefore checklist and sliders stay aligned


checklist = dbc.Card([
    header_checklist,
    check_potential], 
    className="border-0"
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
    container_slider_schnittstellen], className="border-0")

chart1 = dbc.Card([fig], body=True, className="border-0")

app.layout = dbc.Container(
    [
        header,
        dbc.Row
        ([
            dbc.Col([collapse_etablierung], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_benutzerfreundlichkeit], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_anschaffungskosten], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_integration], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_zusammenarbeit], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_datenmengen], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_datenqualitaet], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_datenanalyse], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_rechtemanagement], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_nachhaltigkeit], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_dashboards], xs=6, sm=3, md=2, lg=2, xl=2,),
            dbc.Col([collapse_schnittstellen], xs=6, sm=3, md=2, lg=2, xl=2,),
          ],
          justify="center"
        ),
        # dbc.Row
        # (
        #     [
        #         dbc.Col([header_checklist],
        #                 xs=10, sm=8, md=5, lg=3, xl=3,
        #         ),
        #         dbc.Col([header_sliders],
        #                 xs=10, sm=8, md=5, lg=3, xl=3,
        #         )
        #     ],
        #     justify="center"
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
                        xs=10, sm=8, md=5, lg=12, xl=5,
                        style={"height": "80%"}
                        ),
                dbc.Col([sliders],
                        #width=3,
                        xs=10, sm=8, md=5, lg=3, xl=3,
                        style={"height": "80%"}
                        ),

            ],
            className="vh-50, g-6",
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
@app.callback(
    Output("collapse_etablierung", "is_open"),
    [Input("collapse_etablierung_button", "n_clicks")],
    [State("collapse_etablierung", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_benutzerfreundlichkeit", "is_open"),
    [Input("collapse_benutzerfreundlichkeit_button", "n_clicks")],
    [State("collapse_benutzerfreundlichkeit", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_anschaffungskosten", "is_open"),
    [Input("collapse_anschaffungskosten_button", "n_clicks")],
    [State("collapse_anschaffungskosten", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_integration", "is_open"),
    [Input("collapse_integration_button", "n_clicks")],
    [State("collapse_integration", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_zusammenarbeit", "is_open"),
    [Input("collapse_zusammenarbeit_button", "n_clicks")],
    [State("collapse_zusammenarbeit", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_datenmengen", "is_open"),
    [Input("collapse_datenmengen_button", "n_clicks")],
    [State("collapse_datenmengen", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_datenqualitaet", "is_open"),
    [Input("collapse_datenqualitaet_button", "n_clicks")],
    [State("collapse_datenqualitaet", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_datenanalyse", "is_open"),
    [Input("collapse_datenanalyse_button", "n_clicks")],
    [State("collapse_datenanalyse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_rechtemanagement", "is_open"),
    [Input("collapse_rechtemanagement_button", "n_clicks")],
    [State("collapse_rechtemanagement", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_nachhaltigkeit", "is_open"),
    [Input("collapse_nachhaltigkeit_button", "n_clicks")],
    [State("collapse_nachhaltigkeit", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_dashboards", "is_open"),
    [Input("collapse_dashboards_button", "n_clicks")],
    [State("collapse_dashboards", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_schnittstellen", "is_open"),
    [Input("collapse_schnittstellen_button", "n_clicks")],
    [State("collapse_schnittstellen", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
# endregion

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

# run server
if __name__ == '__main__':
    app.run_server(debug=True,
                   # mode='external',
                   # port=3003)
                   ),