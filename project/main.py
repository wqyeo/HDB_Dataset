from merger import merge_excels
from charter import visual_chart

# NOTE: The all excel files are converted to a text-csv file first.
EXCEL_FILE_LOCATIONS = [("project\Dataset\HDB Dataset - Jan.csv"), ("project\Dataset\HDB Dataset - Feb.csv")]
MERGED_FILE_PATH = ("project\Dataset\HDB_MERGED_Dataset.csv")

merge_excels(EXCEL_FILE_LOCATIONS, MERGED_FILE_PATH)

OUTPUT_VISUAL_CHART_PATH = ("project\VisualCharts\debug.png")

visual_chart(MERGED_FILE_PATH, "DEBUG", "resale_price", "month", "OUTPUT_VISUAL_CHART_PATH")