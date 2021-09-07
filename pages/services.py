import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from components import header
from app import app

services = ['Frikort', 'Legemidler', 'Verktoy', 'Bytte-fastlege', 
            'Pasientreiser', 'Prøvesvar', 'Meldinger', 'Pasientjournal', 
            'Timeavtaler', 'Fastlegetjenester', 'Henvisninger', 
            'Kjernejournal', 'Helsekontakter']


def get_data(service):
    if service not in services:
        return
    return pd.read_excel("data/Helsenorge-statistikk.xlsx", service)


data = pd.read_excel("data/Helsenorge-statistikk.xlsx", "Frikort")


layout = html.Div([
    header.get_navbar(),
    html.Div(className="container", children=[
        html.H1('Tjenester'),
        dcc.Dropdown(
            id='service-selector',
            options=[{'label': i, 'value': i} for i in services],
            value=services[0]
        ),
        dcc.Graph(
                id='visitors',
                className='my-2'
            ),
    ])

])


@app.callback(
    Output('visitors', 'figure'),
    Input('service-selector', 'value'))
def update_figure(selected_service):
    data = get_data(selected_service)

    figure = px.line(data,    
                     x='Month',
                     y='Visits')

    figure.update_layout(transition_duration=500)

    return figure
