from dash import Dash, html
import dash_bootstrap_components as dbc 
from components import (
        category,
        month,
        pie,
        year
    )
def create_layout(app,df):
    heading = html.H1("Gas sales")
    return dbc.Container([
        dbc.Row([heading]),
        dbc.Row([
            dbc.Col([
                html.Div(
            [
                year.render(app,df),
                month.render(app,df),
                category.render(app,df),
            ]
            )
            ], lg=6),
            dbc.Col([pie.render(app,df)], lg=6)
        ])
    ])