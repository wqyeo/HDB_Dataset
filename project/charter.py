from ast import Str
from inspect import _void
from multiprocessing.dummy import Array
import matplotlib.pyplot as plt
import numpy as np

from model.data import Data
from model.visual_chart import VisualChart

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

    visual_chart.x_data.set_data_by_category(_get_column_data_from_excel(excel_content, visual_chart.x_data.name), visual_chart.x_data.data_category)
    visual_chart.y_data.set_data_by_category(_get_column_data_from_excel(excel_content, visual_chart.y_data.name), visual_chart.y_data.data_category)

    ax = plt.axes()
    plt.plot(visual_chart.x_data.get_data_value(), visual_chart.y_data.get_data_value())

    # TODO: Set proper tick labels (?)
    xticks = visual_chart.x_data.get_data_ticks()
    yticks = visual_chart.x_data.get_data_ticks()

    plt.title(visual_chart.title)

    plt.xlabel(visual_chart.x_data.display_name)
    plt.ylabel(visual_chart.y_data.display_name)

    plt.savefig(output_path)

def test(output_path: str) -> _void:
    
    x = np.random.randint(low=9000, high=10000, size=50)
    y = np.random.randint(low=0, high=100000, size=1000000)
    plt.plot(x)

    plt.savefig(output_path)