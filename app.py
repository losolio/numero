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
                    'plot_bgcolor': colors['background-graph'],
                    'paper_bgcolor': colors['light'],
                    'font': {
                        'color': colors['text']
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
                    'plot_bgcolor': colors['background-graph'],
                    'paper_bgcolor': colors['light'],
                    'font': {
                        'color': colors['text']
                    }
                }
            },
            className='my-2'
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
