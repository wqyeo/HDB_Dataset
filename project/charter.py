from ast import Str
from inspect import _void
from multiprocessing.dummy import Array
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

from model.data import Data
from model.charts.visual_chart import VisualChart
from model.charts.bar_chart import BarChart
from model.charts.line_chart import LineChart

def _read_file_content(file_path: str):
    f = open(file_path)
    content = f.readlines()
    f.close()
    return content

def _get_column_data_from_excel(excel_content: Array, header_name: str) -> Array:
    excel_headers = (excel_content[0].replace("\n", "").split(","))

    header_index = 0
    for header in excel_headers:
        if header.lower() == header_name.lower():
            break
        header_index += 1

    if header_index == None:
        raise Exception("The corresponding header name was not found in the excel path")
    
    column_data = []
    skip_first = False
    for row in excel_content:
        if not skip_first:
            skip_first = True
        else:
            curr_row_data = (row.replace("\n", "").split(","))[header_index]
            column_data.append(curr_row_data)
    return column_data

def visual_chart(excel_file_path: str, visual_chart: VisualChart,  output_path: str) -> _void:
    excel_content = _read_file_content(excel_file_path)

    if isinstance(visual_chart, LineChart):
        print_line_chart(excel_content, visual_chart, output_path)
    elif isinstance(visual_chart, BarChart):
        print_bar_chart(excel_content, visual_chart, output_path)
    else:
        raise ValueError("visual_chart: Unknown type of Chart")
    plt.clf()

def print_bar_chart(excel_content: str, bar_chart: BarChart, output_path: str) -> _void:
    raw_data = _get_column_data_from_excel(excel_content, bar_chart.data.name)
    bar_chart.data.set_data_from_raw(raw_data)

    # Get both axis first (Towns)

    # Y axis = Value
    # X axis = Labels
    y_points = []
    x_points = []

    for p in bar_chart.data.points:
        x_points.append(p.label)
        y_points.append(p.value)

    # TODO: Accept a settings input
    #plt.rc('font', size=15)
    plt.figure(figsize=(50, 5))
    plt.bar(x_points, y_points, align='center', width=0.4)
    plt.grid(axis = 'y', linestyle = '--', linewidth = 0.5)

    plt.title(bar_chart.title)
    plt.xlabel(bar_chart.x_name)
    plt.ylabel(bar_chart.y_name)

    plt.savefig(output_path)

def print_line_chart(excel_content: str, line_chart: LineChart, output_path: str) -> _void:
    x_raw_data = _get_column_data_from_excel(excel_content, line_chart.x_data.name)
    line_chart.x_data.set_data_from_raw(x_raw_data)

    y_raw_data = _get_column_data_from_excel(excel_content, line_chart.y_data.name)
    line_chart.y_data.set_data_from_raw(y_raw_data)

    plt.plot(line_chart.x_data.get_data_value(), line_chart.y_data.get_data_value())

    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.title(line_chart.title)
    plt.xlabel(line_chart.x_data.display_name)
    plt.ylabel(line_chart.y_data.display_name)

    plt.savefig(output_path)

def test(output_path: str) -> _void:
    """
    For Testing
    """
    
    data = [23, 45, 56, 78, 213]
    plt.bar(["A","B","c","D","E"], data)
    plt.savefig(output_path)