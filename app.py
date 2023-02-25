import dash
from dash import Dash 
from frontend.front_app import app_layout

app = dash.Dash(__name__)

app.layout=app_layout

if __name__ == '__main__':
    app.run_server(debug=True, port=7042)