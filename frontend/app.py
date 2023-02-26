import dash
from dash import Dash 
import os
import sys
from dash import dcc, html 
import pandas as pd


path_call= "../backend/callbacks"
my_path_opt = "../backend/pretreatment"

sys.path.insert(1, path_call)
sys.path.insert(2, my_path_opt)

import callbacks
import treat_to_options


# pathdf= os.path.abspath("mlops_final_project//data//raw_data//Anime_data.csv")
# print("path df", pathdf)
df=pd.read_csv('../backend/data/raw_data/Anime_data.csv',encoding='utf-8')

print(df.head())

# l=treat_to_options.intro_options(df["Genre"])

# print(l)

app_layout = html.Div(children=[
    html.H1("MLOPS"),
    dcc.Input(id="Anime_Title", placeholder="Anime Title"),
    dcc.Dropdown(id="Anime_Genre", options=treat_to_options.intro_options(df["Genre"]), multi=True, placeholder="Anime Genre(s)"),
    dcc.Input(id="Anime_Description", placeholder="Anime Description"),
    dcc.Dropdown(id="Anime_Type", options=treat_to_options.intro_options(df["Type"]),placeholder="Anime Type"),
    dcc.Dropdown(id="Anime_Producer", options=treat_to_options.intro_options(df["Producer"]), multi=True, placeholder="Anime Producer"),
    dcc.Dropdown(id="Anime_Studio", options=treat_to_options.intro_options(df["Studio"]), multi=True, placeholder="Anime Studio"),
    html.Div(id="other_producer_div", style={"display": "none"}, children=[
        dcc.Input(id="Other_Producer", placeholder="Enter Other Producer")
    ]),
    html.Div(id="other_studio_div", style={"display": "none"}, children=[
        dcc.Input(id="Other_Studio", placeholder="Enter Other Studio")
    ]),
    html.Button('Submit', id='btn'),
    html.Div(id="result")
])


app = dash.Dash(__name__)
server = app.server

app.layout=app_layout

callbacks.register_callbacks(app)


if __name__ == '__main__':
    
    app.run_server(debug=True, port=4000)