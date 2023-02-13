import dash
from dash import Dash 
from dash import Output, Input, html, dcc, State
from dash.exceptions import PreventUpdate


app = dash.Dash()


app.layout = html.Div(children=[html.H1("MLOPS"),
    dcc.Input(id="Anime_Title",placeholder="Anime Title"),
    dcc.Input(id="Anime_Genre(s)",placeholder="Anime Genre(s)"),
    dcc.Input(id="Anime_Description",placeholder="Anime Description"),
    dcc.Input(id="Anime_Type",placeholder="Anime Type"),
    dcc.Input(id="Anime_Producer",placeholder="Anime Producer"),
    dcc.Input(id="Anime_Studio",placeholder="Anime Studio"),
    html.Button('Submit', id='btn'),
    html.Div(id="result")
    
])

@app.callback(Output(component_id="result",component_property="children"),
              [Input(component_id="btn",component_property='n_clicks')],
              [State(component_id="Anime_Title",component_property="value"),
               State(component_id="Anime_Genre(s)",component_property="value"),
               State(component_id="Anime_Description",component_property="value"),
               State(component_id="Anime_Type",component_property="value"),
               State(component_id="Anime_Producer",component_property="value"),
               State(component_id="Anime_Studio",component_property="value")
    ])
def display_result(btn,Anime_Title,Anime_Genre,Anime_Description,Anime_Type,Anime_Producer,Anime_Studio):
    l=[Anime_Title,Anime_Genre,Anime_Description,Anime_Type,Anime_Producer,Anime_Studio]

    l2= [type(Anime_Title),type(Anime_Genre),type(Anime_Description),type(Anime_Type),type(Anime_Producer),type(Anime_Studio)]
    
    if all(x!=None for x in l) or btn == None:
        raise PreventUpdate
    else:

        return html.Div(str(l+l2))


if __name__=='__main__':
    app.run_server(debug=True, port=7042)
