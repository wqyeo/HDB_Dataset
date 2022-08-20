from inspect import _void
from multiprocessing.dummy import Array
import matplotlib.pyplot as plt

def _read_file_content(file_path: str) -> str:
    f = open(file_path)
    content = f.readlines()
    f.close()
    return content

def _get_column_data_from_excel(excel_content: Array, header_name: str) -> Array:
    excel_headers = (excel_content[0].replace("\n", "").split(","))
    header_index = next((header for header in excel_headers if header.lower() == header_name.lower()), None)

    if header_index == None:
        raise Exception("The corresponding header name was not found in the excel path")
    
    column_data = []
    for i in (1, len(excel_content)):
        curr_row_data = (excel_content[i].replace("\n", "").split(","))[header_index]
        column_data.append(curr_row_data)
    return column_data

def visual_chart(excel_file_path: str, plot_name: str, x_axis_name: str, y_axis_name: str, output_path: str) -> _void:
    excel_content = _read_file_content(excel_file_path)

    x = _get_column_data_from_excel(excel_content, x_axis_name)
    y = _get_column_data_from_excel(excel_content, y_axis_name)

    plt.plot(x, y)
    plt.title(plot_name)
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)

    plt.savefig(output_path)