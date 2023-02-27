
from dash import Output, Input, State, html
from dash.exceptions import PreventUpdate
import os
import sys

my_path_predict="../backend/data/model"
sys.path.insert(1, my_path_predict )

import predict

def register_callbacks(app):

        @app.callback(Output(component_id="result",component_property="children"),
                    [Input(component_id="btn",component_property='n_clicks')],
                    [State(component_id="Anime_Title",component_property="value"),
                    State(component_id="Anime_Genre",component_property="value"),
                    State(component_id="Anime_Description",component_property="value"),
                    State(component_id="Anime_Type",component_property="value"),
                    State(component_id="Anime_Producer",component_property="value"),
                    State(component_id="Anime_Studio",component_property="value")
            ])

        def display_result(btn,Anime_Title,Anime_Genre,Anime_Description,Anime_Type,Anime_Producer,Anime_Studio):
            print(btn)
            if btn== None:
                raise PreventUpdate
            else:
                data = {"Title":Anime_Title,
                        "Genre":[Anime_Genre],
                        "Synopsis":Anime_Description,
                        "Type":Anime_Type,
                        "Producer":[Anime_Producer],
                        "Studio":[Anime_Studio]
                        }
                print(data)
                p=predict.predict(data)
                # p="HERE IS P"
                return p