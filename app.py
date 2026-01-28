import webbrowser
import codecs
import plotly.express as px
import pandas as pd
# from jinja2 import Template
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Get form values (always strings at first)
    x_vals = []
    x_vals.append(float(request.form["x1"]))
    x_vals.append(float(request.form["x2"]))
    x_vals.append(float(request.form["x3"]))
    y_vals = []
    y_vals.append(float(request.form["y1"]))
    y_vals.append(float(request.form["y2"]))
    y_vals.append(float(request.form["y3"]))

    pd_data = pd.DataFrame({
        "X": x_vals,
        "Y": y_vals
    })
    fig = px.scatter(pd_data, x = "X", y = "Y", title="Sample Scatter Plot")
    plot = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return render_template("result.html", plot=plot)


if __name__ == "__main__":
    app.run(debug=True)


### plotting function (not used in current Flask app)
# def plot_it(file_path, data, graph_type='scatter'):
#     """Generates a sample plot using Plotly and displays it in the web browser."""
#     #data = dict(
#     #number=[39, 27.4, 20.6, 11, 2],
#     #stage=["Website visit", "Downloads", "Potential customers", "Requested price", "Invoice sent"])
#     x_val = data.keys()[0]
#     y_val = data.keys()[1]

#     if graph_type == 'area':
#         fig = px.area(data, x = x_val, y = y_val)
#     elif graph_type == 'funnel':
#         fig = px.funnel(data, x = x_val, y = y_val)
#     elif graph_type == 'bar':
#         fig = px.bar(data, x = x_val, y = y_val)
#     elif graph_type == 'line':
#         fig = px.line(data, x = x_val, y = y_val)
#     else:
#         fig = px.scatter(data, x = x_val, y = y_val)
    
#     write_to_file(file_path, fig.to_html(full_html=False, include_plotlyjs='cdn'))