import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


data = pd.read_excel("data/Helsenorge-statistikk.xlsx", "Helsenorge")

app = dash.Dash(__name__, title='Helsenorge statistikk')
server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body class="bg-gray-100">
        <div class="container py-5">
        {%app_entry%}
        </div>
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

colors = {
    'background': '#eeeeee',
    'light': '#eeeeee',
    'background-graph': '#dddde6',
    'text': '111111'
}

app.layout = html.Div(
    children=[
        html.H1(
            children='Helsenorge statistikk'
        ),
        html.P(children='Hvor mange er innom?'),
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
                    'paper_bgcolor': colors['light'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
