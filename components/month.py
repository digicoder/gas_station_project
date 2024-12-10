from dash import dcc, html, Input, Output

def render(app,df):
    all_months = df["month"].unique()
    @app.callback(
        Output("month_dropdown", "value"),
        [
            Input("year_dropdown", "value"),
            Input("select_all_month_button", "n_clicks")
        ]
    )
    def select_all_month(year, n):
        filtered_df = df.query("year in @years")
        return sorted(filtered_df['month'].unique())
    return html.Div(
        [
        html.H6("Month"),
        dcc.Dropdown(
            id="month_dropdown",
            options=[{"label":m, "value":m} for m in all_months],
            multi=True,
            value="1"
        ),
        html.Button(
            id="select_all_month_button",
            children = ["Select All"],
            n_clicks=0
        )
    ]
    )