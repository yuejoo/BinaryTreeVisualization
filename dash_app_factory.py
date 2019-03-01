import dash
import dash_cytoscape as cyto
import dash_core_components as dcc
import dash_html_components as html
import dash_helper
import flask_app_factory
import ast

colors = {
    'text': '#000000'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

flask_app = flask_app_factory.flask_app

dash_app = dash.Dash(__name__, server=flask_app, url_base_pathname='/', external_stylesheets=external_stylesheets)

dash_app.layout = html.Div(children=[
    html.H1(
        children='BinaryTree Visualization',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),
    
    dcc.Textarea(
        id='textInput',
        placeholder='Enter a value...',
        value='[1,2,null,3,4]',
        style={'width': '100%'}
    ),

    cyto.Cytoscape(
        id='cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '500px'},
        elements=[]
    )

])

@dash_app.callback(
    dash.dependencies.Output('cytoscape', 'elements'),
    [dash.dependencies.Input('textInput', 'value')])
def update_elements(textInput): 
    textInput = textInput.replace("null", "None")
    textInput = ast.literal_eval(textInput)
    return dash_helper.create_elements(textInput)
