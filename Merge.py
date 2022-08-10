class Header:
    def __init__(self, name, index):
        self.name = name
        self.index = index

# NOTE: The Jan's xlsx file is converted to a text-csv file first.
jan_file_loc = ("Dataset/HDB Dataset - Jan.csv")
feb_file_loc = ("Dataset/HDB Dataset - Feb.csv")

merged_csv_excel = []
headers = []

# FOR DEBUG
def _print_headers():
    for header in headers:
        print(header.name + " @ " + str(header.index))

def _save_merged_csv_excel():
    f = open('Dataset/HDB_MERGED_Dataset.csv', 'a')
    for row in merged_csv_excel:
        f.write(','.join(row))
    f.close


# MAIN
with open(jan_file_loc) as f:
    row = 0

    lines = f.readlines()
    curr_headers = (lines[0].replace("\n", "").split(","))
    csv_header = []
    # This first sheet is used as base-line to determine the headers
    for i in range(len(curr_headers)):
        headers.append(Header(curr_headers[i].lower(), i))
        csv_header.append(curr_headers[i].lower())
    merged_csv_excel.append(csv_header)
    
    _save_merged_csv_excel()