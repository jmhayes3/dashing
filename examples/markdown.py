# Using Markdown in Dash.

from dash import Dash, html, dcc

app = Dash(__name__)

markdown_text = """
### Dash Markdown

Some text.
More text.
Thrice text.

Dash uses the [CommonMark](http://commonmark.org/) spec of Markdown.
"""

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == "__main__":
    app.run_server(debug=True)