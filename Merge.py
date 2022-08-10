# NOTE: The all excel files are converted to a text-csv file first.
file_locations = [("Dataset/HDB Dataset - Jan.csv"), ("Dataset/HDB Dataset - Feb.csv")]

merged_csv_excel = []

def _save_merged_csv_excel():
    # Empty the file first (in case it exists before)
    f = open('Dataset/HDB_MERGED_Dataset.csv', 'w')
    f.write('')
    f.close()
    # Write
    f = open('Dataset/HDB_MERGED_Dataset.csv', 'a')
    for row in merged_csv_excel:
        f.write(','.join(row) + "\n")
    f.close()

def _merge_csv_text(csv_text_lines):
    # We find the indexing order to sort the columns properly when merging
    # as different excel files might have different column positioning
    # (Ex: Excel-A has date on 1st column, while Excel-B has date on 4th column; We will have to properly arrange that)
    indexing_order = []
    curr_headers = (csv_text_lines[0].replace("\n", "").split(","))
    main_headers = merged_csv_excel[0]
    for i in range(len(curr_headers)):
        indexing_order.append(main_headers.index(curr_headers[i]))
    
    # Append the current excel items
    for i in range(i, len(csv_text_lines)):
        # Append row-by-row
        curr_row_line = csv_text_lines[i].replace("\n", "").split(",")
        curr_row_item = []
        for index in indexing_order:
            curr_row_item.append(curr_row_line[index])
        merged_csv_excel.append(curr_row_item)
        
def _main():
    # Set the main headers first based on the first excel file
    with open(file_locations[0]) as f:
        lines = f.readlines()
        curr_headers = (lines[0].replace("\n", "").split(","))
        csv_header = []
        # This first sheet is used as base-line to determine the headers and column positioning
        for i in range(len(curr_headers)):
            csv_header.append(curr_headers[i].lower())
        merged_csv_excel.append(csv_header)

    # Open each file and merge them
    for file in file_locations:
        with open(file) as f:
            _merge_csv_text(f.readlines())
        
_main()
_save_merged_csv_excel()