import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="My Kanban Board"),

    # Define columns
    dcc.Tabs(id="tabs", value="to-do", children=[
        dcc.Tab(label="To Do", value="to-do"),
        dcc.Tab(label="In Progress", value="in-progress"),
        dcc.Tab(label="Done", value="done"),
    ]),

    html.Div(id="tab-content"),

    # Input area for new tasks
    html.Div(children=[
        html.Label("New Task:"),
        dcc.Input(id="new-task-input", type="text", placeholder="Enter new task"),
        html.Button("Add Task", id="add-task-button"),
    ]),
])

@app.callback(
    dash.Output("tab-content", "children"),
    [dash.Input("tabs", "value"),
     dash.Input("add-task-button", "n_clicks")],
    [dash.State("new-task-input", "value"),
     dash.State("tab-content", "children")]
)
def update_content(tab, n_clicks, new_task, current_content):
    if n_clicks is None or n_clicks == 0:
        return current_content

    if tab == "to-do":
        if current_content is None:
            current_content = html.Ul()
        current_content.children.append(html.Li(new_task))
    elif tab == "in-progress":
        if current_content is None:
            current_content = html.Ul()
        current_content.children.append(html.Li(new_task))
    elif tab == "done":
        if current_content is None:
            current_content = html.Ul()
        current_content.children.append(html.Li(new_task))

    return current_content

if __name__ == "__main__":
    app.run_server(debug=False)