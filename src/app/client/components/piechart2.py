import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app


piechart2 = dcc.Graph(id='piechart2', figure={})