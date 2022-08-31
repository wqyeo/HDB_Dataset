from ast import Str
from inspect import _void
from multiprocessing.dummy import Array
from tkinter import Grid
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

from model.data import Data
from model.charts.visual_chart import VisualChart
from model.charts.bar_chart import BarChart
from model.charts.line_chart import LineChart

from model.chart_configs.visual_chart_config import VisualChartConfig
from model.chart_configs.grid_config import GridConfig
from model.chart_configs.bar_plot_config import BarPlotConfig
from model.chart_configs.plot_config import PlotConfig
from model.charts.pie_chart import PieChart

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

def visual_chart(excel_file_path: str, visual_chart: VisualChart,  output_path: str, visual_chart_config: VisualChartConfig = None) -> _void:
    plt.clf()
    plt.cla()
    plt.close()
    plt.rcParams["figure.figsize"]
    if not visual_chart_config == None:
        if not visual_chart_config.figure_size == None:
            plt.figure(figsize=(visual_chart_config.figure_size.x_size, visual_chart_config.figure_size.y_size))

    excel_content = _read_file_content(excel_file_path)
    if isinstance(visual_chart, LineChart):
        print_line_chart(excel_content, visual_chart, output_path, visual_chart_config)
    elif isinstance(visual_chart, BarChart):
        print_bar_chart(excel_content, visual_chart, output_path, visual_chart_config)
    elif isinstance(visual_chart, PieChart):
        print_pie_chart(excel_content, visual_chart, output_path, visual_chart_config)
    else:
        raise ValueError("visual_chart: Unknown type of Chart")
    print("Printed a '" + visual_chart.title + "' chart to " + output_path)

def print_bar_chart(excel_content: str, bar_chart: BarChart, output_path: str, visual_chart_config: VisualChartConfig) -> _void:
    raw_data = _get_column_data_from_excel(excel_content, bar_chart.data.name)
    bar_chart.data.set_data_from_raw(raw_data)

    # Get both axis first
    # Y axis = Value
    # X axis = Labels
    y_points = []
    x_points = []
    for p in bar_chart.data.points:
        x_points.append(p.label)
        y_points.append(p.value)

    # TODO: Accept a settings input
    #plt.rc('font', size=15)
    if not visual_chart_config == None:
        if not visual_chart_config.figure_size == None:
            plt.figure(figsize=(visual_chart_config.figure_size.x_size, visual_chart_config.figure_size.y_size))

    bar_plot_config = BarPlotConfig()
    grid_config = GridConfig()
    if not visual_chart_config == None:
        if not visual_chart_config.plot_config == None:
            if isinstance(visual_chart_config.plot_config, BarPlotConfig):
                bar_plot_config = visual_chart_config.plot_config
        if not visual_chart_config.grid_config == None:
            grid_config = visual_chart_config.grid_config
                
    plt.bar(x_points, y_points, align= bar_plot_config.align, width= bar_plot_config.width) 
    plt.grid(axis = grid_config.get_target_axis(), linestyle = grid_config.linestyle, linewidth = grid_config.linewidth, which = grid_config.get_target_grid())

    plt.title(bar_chart.title)
    plt.xlabel(bar_chart.x_name)
    plt.ylabel(bar_chart.y_name)

    plt.savefig(output_path)

def print_line_chart(excel_content: str, line_chart: LineChart, output_path: str, visual_chart_config: VisualChartConfig) -> _void:
    x_raw_data = _get_column_data_from_excel(excel_content, line_chart.x_data.name)
    line_chart.x_data.set_data_from_raw(x_raw_data)

    y_raw_data = _get_column_data_from_excel(excel_content, line_chart.y_data.name)
    line_chart.y_data.set_data_from_raw(y_raw_data)

    grid_config = GridConfig()
    if not visual_chart_config == None:
        if not visual_chart_config.grid_config == None:
            grid_config = visual_chart_config.grid_config

    plt.plot(line_chart.x_data.get_data_value(), line_chart.y_data.get_data_value())
    plt.grid(axis = grid_config.get_target_axis(), linestyle = grid_config.linestyle, linewidth = grid_config.linewidth, which = grid_config.get_target_grid())
    plt.title(line_chart.title)
    plt.xlabel(line_chart.x_data.display_name)
    plt.ylabel(line_chart.y_data.display_name)

    plt.savefig(output_path)

def print_pie_chart(excel_content: str, pie_chart: PieChart, output_path: str, visual_chart_config: VisualChartConfig) -> _void:
    raw_data = _get_column_data_from_excel(excel_content, pie_chart.data.name)
    pie_chart.data.set_data_from_raw(raw_data)
    pie_chart.data.cutoff_category(pie_chart.others_cut_off)

    labels = []
    values = []
    for p in pie_chart.data.points:
        labels.append(p.label)
        values.append(p.value)

    plt.pie(np.array(values), labels = labels)
    plt.savefig(output_path)


def test(output_path: str) -> _void:
    """
    For Testing
    """
    
    data = [23, 45, 56, 78, 213]
    plt.bar(["A","B","c","D","E"], data)
    plt.savefig(output_path)