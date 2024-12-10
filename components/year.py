from dash import dcc, html, Input, Output

def render(app,df):
    all_years = df["year"].unique()
    @app.callback(
        Output("year_dropdown", "value"),
        Input("select_all_years_button", "n_clicks")
        
    )
    def select_all_year( n):
        return all_years
    return html.Div([
        html.H6("Year"),
        dcc.Dropdown(
            id="year_dropdown",
            options=[{"label":y, "value":y} for y in all_years],
            multi=True
        ),
        html.Button(
            id="select_all_years_button",
            children = ["Select All"],
            n_clicks=0
        )
    ])