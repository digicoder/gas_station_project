from dash import dcc, html, Output,Input
import plotly.express as px

def render(app,df):
    @app.callback(
        Output("pie_chart", "children"),
        [
            Input("year_dropdown", "value"),
            Input("month_dropdown", "value"),
            Input("category_dropdown", "value")
        ]
    )
    def update_pie_chart(years, months, categories):
        filtered_df = df.query(
            "year in @years and month in @months and category in @categories"
        )
        if filtered_df.shape[0]==0:
            return html.Div(["No data selected"], id="pie_chart")
        fig = px.pie(filtered_df, values="amount",names="category", hole=0.4)
        return html.Div([dcc.Graph(figure=fig)], id="pie_chart")
    return html.Div(id="pie_chart")