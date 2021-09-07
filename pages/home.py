import dash_html_components as html
from components import header

layout = html.Div([
    header.get_navbar(),
    html.Div(className="container", children=[
        html.H1('Helsenorge statistikk'),
        html.P('Litt tall om de som besøker Helsenorge.')
    ])
])
