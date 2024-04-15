from dash import dcc, html
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from layouts import planLayout, codLayout, consLayout, pruLayout, lanLayout, dspLayout, opLayout, monLayout

app = dash.Dash(external_stylesheets=[dbc.themes.COSMO])
app.title = 'DevOps'
app.config.suppress_callback_exceptions = False 
meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]
# the style arguments for the sidebar. We use position:fixed and a responsive width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",  # Porcentaje del ancho de la ventana del navegador
   "padding": "1rem 1rem",
    "background-color": "#9c9c9c",
}


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "1rem",
   "padding": "1rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("Dashboard DevOps", className="lead"),
        html.Hr(),
        dbc.Nav(
            [dbc.NavItem(dbc.NavLink("Inicio",active="exact",href="/"))],
           vertical=True, 
           pills=True,
        ),
        html.Hr(),
        html.H2("Procesos", className="lead"),
        dbc.Nav(
            [
            dbc.NavItem(dbc.NavLink("Planeacion",active="exact",href="/plan")),
            dbc.NavItem(dbc.NavLink("Codificacion",active="exact",href="/cod")),
            dbc.NavItem(dbc.NavLink("Construccion",active="exact",href="/cons")),
            dbc.NavItem(dbc.NavLink("Pruebas",active="exact",href="/pru")),
            dbc.NavItem(dbc.NavLink("Lanzamiento",active="exact",href="/lan")),
            dbc.NavItem(dbc.NavLink("Despliegue",active="exact",href="/dsp")),
            dbc.NavItem(dbc.NavLink("Operacion",active="exact",href="/ope")),
            dbc.NavItem(dbc.NavLink("Monitoreo",active="exact",href="/mon")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
# Contenido principal
content = html.Div(id="page-content", style=CONTENT_STYLE)

# Diseño de la aplicación
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
# Callback para cambiar el contenido según la URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/':
         return html.Div(html.Img(src=app.get_asset_url('logo.png'))),html.Div([dcc.Markdown('''
          El objetivo de esta investigación es proporcionar una herramienta de control que permitirá a las empresas desarrolladoras de software visualizar de manera gráfica el estado de avance de sus proyectos DevOps. 
        Esto les permitirá dar seguimiento, mostrar su continuidad y progreso a lo largo del tiempo. Para lograr este objetivo, se desarrolló una herramienta de software basada en tecnologías de código abierto. Esta herramienta se basa en los 8 procesos más comunes del enfoque DevOps y se apoya en el estándar IEEE 2675 for DevOps.  
        ''')],className='home')
   
    if pathname =='/plan':
         return [

            html.Div(html.Img(src=app.get_asset_url('logo.png'))),
            html.Div(planLayout),html.H1("Dynamically rendered tab content"),
        ]
    if pathname == '/cod':
        return  dbc.Card("Proceso de codificacion - compilaciones de codigo exitosas", body=True),codLayout
    if pathname == '/cons':
        return html.Div(html.Img(src=app.get_asset_url('logo.png'))),consLayout
    if pathname == '/pru':
        return html.Div(pruLayout),html.P("Proceso de Pruebas")
    if pathname == '/lan':
        return html.Div(html.Img(src=app.get_asset_url('logo.png'))),html.Div(lanLayout)
    if pathname == '/dsp':
        return html.Div(dspLayout)
    if pathname == '/ope':
        return html.Div(html.Img(src=app.get_asset_url('logo.png'))),opLayout
    if pathname == '/mon':
        return  monLayout
    else:
        # If the user tries to reach a different page, return a 404 message
        return dbc.Alert(
        [
        html.H1("404: No encontrado", className="text-danger"),
        html.Hr(),
        html.P(f"La ruta {pathname} no fue reconocida..."),    
        html.A("Inicio", href="/", className="alert-link"),
        ]
        ),

# Call app server
if __name__ == '__main__':
    # set debug to false when deploying app
   app.run_server(debug=True)


    