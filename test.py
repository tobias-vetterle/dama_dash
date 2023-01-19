import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# read data

df = pd.read_csv("data.csv", encoding='utf-8-sig', sep=';')
dff = df

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

fig.show()