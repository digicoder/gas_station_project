from dash import dcc, html, Input, Output

def render(app,df):
    all_categories = df["category"].unique()
    @app.callback(
    Output("category_dropdown", "value"),
        [
            Input("year_dropdown", "value"),
            Input("month_dropdown", "value"),
            Input("select_all_button", "n_clicks")
        ]
    )
    def select_all(years, months, n):
        filtered_df = df.query("year in @years and month in @months")
        return sorted(filtered_df["category"].unique())
    return html.Div([
        html.H6("Category"),
        dcc.Dropdown(
            id = "category_dropdown",
            options=[{"label":c, "value":c} for c in all_categories],
            multi=True
        ),
        html.Button(
            id="select_all_button",
            children= "Select All",
            n_clicks=0
        )
    ])