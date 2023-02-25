
from dash import dcc, html 
import sys
import os
import pandas as pd

my_path_opt = "C://Users//Arthy//Desktop//S9_efrei//MachineLearninginProduction//mlops_final_project//backend//pretreatment"


mypathopt= os.path.abspath("mlops_final_project//backend//pretreatment")
sys.path.insert(1, my_path_opt )
import treat_to_options
pathdf= os.path.abspath("mlops_final_project//data//raw_data//Anime_data.csv")
print("path df", pathdf)
df = pd.read_csv("C:\\Users\\Arthy\\Desktop\\S9_efrei\\MachineLearninginProduction\\mlops_final_project\\data\\raw_data\\Anime_data.csv",)


# app_layout = html.Div(children=[
#     html.H1("MLOPS"),
#     dcc.Input(id="Anime_Title", placeholder="Anime Title"),
#     dcc.Dropdown(id="Anime_Genre", options=genre_list, multi=True, placeholder="Anime Genre(s)"),
#     dcc.Input(id="Anime_Description", placeholder="Anime Description"),
#     dcc.Dropdown(id="Anime_Type", options=Types_list,placeholder="Anime Type"),
#     dcc.Dropdown(id="Anime_Producer", options=Producer_list + [{"label": "Other", "value": "Other"}], multi=True, placeholder="Anime Producer"),
#     dcc.Dropdown(id="Anime_Studio", options=Studio_list + [{"label": "Other", "value": "Other"}], multi=True, placeholder="Anime Studio"),
#     html.Div(id="other_producer_div", style={"display": "none"}, children=[
#         dcc.Input(id="Other_Producer", placeholder="Enter Other Producer")
#     ]),
#     html.Div(id="other_studio_div", style={"display": "none"}, children=[
#         dcc.Input(id="Other_Studio", placeholder="Enter Other Studio")
#     ]),
#     html.Button('Submit', id='btn'),
#     html.Div(id="result")
# ])