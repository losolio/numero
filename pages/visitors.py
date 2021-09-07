import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from components import colors, header

data = pd.read_excel("data/Helsenorge-statistikk.xlsx", "Helsenorge")

layout = html.Div([
    header.get_navbar(),
    html.Div(className="container", children=[
        html.H1('Besøkende på Helsenorge'),
        dcc.Graph(
            id='visits',
            figure={
                "data": [{
                        'name': 'Besøk',
                        'x': data['Month'],
                        'y': data['Visits']
                    },
                    {
                        'name': 'Besøk med innlogging',
                        'x': data['Month'],
                        'y': data['Besøk med innlogging']
                    }],
                'layout': {
                    'title': "Besøkende",
                    'plot_bgcolor': colors.colors['background-graph'],
                    'paper_bgcolor': colors.colors['light'],
                    'font': {
                        'color': colors.colors['text']
                    }
                }
            },
            className='my-2'
        ),
        dcc.Graph(
            id='visitors',
            figure={
                "data": [{
                        'name': 'Unike besøkende',
                        'x': data['Month'],
                        'y': data['Unique Visitors']
                    }],
                'layout': {
                    'title': "Unike besøkende",
                    'plot_bgcolor': colors.colors['background-graph'],
                    'paper_bgcolor': colors.colors['light'],
                    'font': {
                        'color': colors.colors['text']
                    }
                }
            },
            className='my-2'
        )
    ])
])
