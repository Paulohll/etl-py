import dash
from dash import dcc,html
import lib.db_utils as utils


data = utils.read_dw_sql("SELECT * FROM warehouse_students")

def generate_table(dataframe, max_rows=50):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col],style={'padding-inline': '20px'}) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ]),
    ], style={'marginLeft': 'auto', 'marginRight': 'auto'})



app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(children="Students Warehouse",
        style={
            'textAlign': 'center',
            'color': '#7FDBFF'
        }),
        generate_table(data),
        
    ]
)
if __name__ == "__main__":
    app.run_server(debug=True)