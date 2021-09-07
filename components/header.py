import dash_core_components as dcc
import dash_html_components as html


def get_brand_link():
    return dcc.Link('Helsenorge statistikk', href='/', className="navbar-brand")


def get_menu():
    menu = html.Ul(children=[
        html.Li(children=[dcc.Link('Besøkende', href='/visitors', className="nav-link")], className="nav-item"),
        html.Li(children=[dcc.Link('Tjenester', href='/services', className="nav-link")], className="nav-item"),
    ], className="nav")
    return menu


def get_navbar():
    header = html.Nav(children=[
            html.Div(children=[get_brand_link(), get_menu()], className="container")
        ], className="navbar navbar-light bg-wrhite pt-1 pb-1")
    return header
