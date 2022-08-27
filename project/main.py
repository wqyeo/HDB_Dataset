from merger import merge_excels
from charter import visual_chart

from model.data_category import DataCategory
from model.data import Data
from model.visual_chart import VisualChart
from model.chart_type import ChartType

# NOTE: The all excel files are converted to a text-csv file first.
EXCEL_FILE_LOCATIONS = [("project\Dataset\HDB Dataset - Jan.csv"), ("project\Dataset\HDB Dataset - Feb.csv")]
MERGED_FILE_PATH = ("project\Dataset\HDB_MERGED_Dataset.csv")

merge_excels(EXCEL_FILE_LOCATIONS, MERGED_FILE_PATH)

OUTPUT_VISUAL_CHART_PATH = ("project\VisualCharts\debug.png")

x_data = Data("resale_price", DataCategory.NUMBERS)
y_data = Data("remaining_lease", DataCategory.DATE_REMAINING)
debug_chart = VisualChart("Debug", x_data, y_data, ChartType.LINE_GRAPH)

visual_chart(MERGED_FILE_PATH, debug_chart, OUTPUT_VISUAL_CHART_PATH)