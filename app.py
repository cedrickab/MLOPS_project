import dash
from dash import Dash 
from dash import Output, Input, html, dcc, State
from dash.exceptions import PreventUpdate
import classnames

app = dash.Dash()


app.layout = html.Div(children=[html.H1("MLOPS",style={'color':'white',"text-align":"center","background-color":"#128DA8"}),

    html.Div(children=[                            
    dcc.Dropdown(id="Anime_Title",placeholder="Anime Title",options=classnames.options_producer),
    dcc.Dropdown(id="Anime_Genre(s)",placeholder="Anime Genre(s)",style={"margin-top":"1%"}),
    dcc.Dropdown(id="Anime_Description",placeholder="Anime Description",style={"margin-top":"1%"}),
    dcc.Dropdown(id="Anime_Type",placeholder="Anime Type",style={"margin-top":"1%"}),
    dcc.Dropdown(id="Anime_Producer",placeholder="Anime Producer",style={"margin-top":"1%"}),
    dcc.Dropdown(id="Anime_Studio",placeholder="Anime Studio",style={"margin-top":"1%"}),
    html.Button('Submit', id='btn', style={"margin-top":"5%","display":"inline"}),
    html.Div(id="result")

    ],
    style={"margin-top":"5%","margin-bottom":"15%","margin-left":"15%","margin-right":"15%"}
    )
],

)


if __name__=='__main__':
    app.run_server(debug=True, port=7042)
