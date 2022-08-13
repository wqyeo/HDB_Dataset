from inspect import _void
from multiprocessing.dummy import Array
from model.csv_excel import CSV_Excel

def _read_file_content(file_path: str) -> str:
    f = open(file_path)
    content = f.readlines()
    f.close()
    return content

def _set_excel_header(set_on: CSV_Excel, path_reference_file: str) -> _void:
    lines = _read_file_content(path_reference_file)
    curr_headers = (lines[0].replace("\n", "").split(","))
    csv_header = []
    for i in range(len(curr_headers)):
        csv_header.append(curr_headers[i].lower())
    set_on.append_row(csv_header)

def _merge_csv_text(merge_on: CSV_Excel, csv_text_lines: str) -> _void:
    """Merges a excel file into the current excel object.

    It will auto-conflict and sort out any headers that is misaligned
    on different columns.
    Ex: Excel-A has date on 1st column, while Excel-B has date on 4th column; 
    This function will automatically sort that out.

    Parameters
    ----------
    merge_on : CSV_Excel, 
        Excel object to merge on

    csv_text_lines : str,
        Path to the excel file to fetch and merge
    """
    # We find the indexing order to sort the columns properly when merging
    indexing_order = []
    curr_headers = (csv_text_lines[0].replace("\n", "").split(","))
    main_headers = merge_on.get_row(0)
    for i in range(len(curr_headers)):
        indexing_order.append(main_headers.index(curr_headers[i]))
    
    for i in range(i, len(csv_text_lines)):
        # Append row-by-row
        curr_row_line = csv_text_lines[i].replace("\n", "").split(",")
        curr_row_item = []
        for index in indexing_order:
            curr_row_item.append(curr_row_line[index])
        merge_on.append_row(curr_row_item)

def merge_excels(excel_file_paths: Array, saved_file_path: str) -> _void:
    """Merges all the given text-based CSV excel file into one based on the given headers.

    Parameters
    ----------
    excel_file_paths : Array(str), 
        Path to all the excel files to merge

    saved_file_path : str,
        Path to save the merged excel file
    """
    merged_csv_excel = CSV_Excel()
    _set_excel_header(merged_csv_excel, excel_file_paths[0])

    # Read each file and merge them
    for file in excel_file_paths:
        _merge_csv_text(merged_csv_excel, _read_file_content(file))

    merged_csv_excel.save_csv_excel(saved_file_path)