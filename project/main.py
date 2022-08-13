from merger import merge_excels

# NOTE: The all excel files are converted to a text-csv file first.
EXCEL_FILE_LOCATIONS = [("project\Dataset\HDB Dataset - Jan.csv"), ("project\Dataset\HDB Dataset - Feb.csv")]
MERGED_FILE_PATH = ("project\Dataset\HDB_MERGED_Dataset.csv")

merge_excels(EXCEL_FILE_LOCATIONS, MERGED_FILE_PATH)