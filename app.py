import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


data = pd.read_excel("data/Helsenorge-statistikk.xlsx", "Helsenorge")

app = dash.Dash(__name__)
server = app.server

colors = {
    'background': '#eeeeee',
    'background-graph': '#dddde6',
    'text': '111111'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Helsenorge statistikk'
    ),
    html.P(children='Hvor mange er innom?', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            "data": [{
                'x': data['Month'],
                'y': data['Visits']
            }],
            'layout': {
                'title': "Besøkende",
                'plot_bgcolor': colors['background-graph'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
