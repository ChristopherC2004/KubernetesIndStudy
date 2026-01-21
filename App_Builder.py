import webbrowser
import codecs
import plotly.express as px
import pandas as pd

def open_file_in_browser(file_path):
    """Opens the specified file in the default web browser."""
    try:
        webbrowser.open(file_path)
    except Exception as e:
        print(f"An error occurred while trying to open the file: {e}")

def write_to_file(file_path, content):
    """Writes the given content to the specified file using UTF-8 encoding."""
    try:
        f = open(file_path, 'w')
        f.write(content)
        f.close()
    except Exception as e:
        print(f"An error occurred while trying to write to the file: {e}")

def plot_it(file_path, data, graph_type='scatter'):
    """Generates a sample plot using Plotly and displays it in the web browser."""
    #data = dict(
    #number=[39, 27.4, 20.6, 11, 2],
    #stage=["Website visit", "Downloads", "Potential customers", "Requested price", "Invoice sent"])
    x_val = data.keys()[0]
    y_val = data.keys()[1]

    if graph_type == 'area':
        fig = px.area(data, x = x_val, y = y_val)
    elif graph_type == 'funnel':
        fig = px.funnel(data, x = x_val, y = y_val)
    elif graph_type == 'bar':
        fig = px.bar(data, x = x_val, y = y_val)
    elif graph_type == 'line':
        fig = px.line(data, x = x_val, y = y_val)
    else:
        fig = px.scatter(data, x = x_val, y = y_val)
    
    write_to_file(file_path, fig.to_html(full_html=False, include_plotlyjs='cdn'))

