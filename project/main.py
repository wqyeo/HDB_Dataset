from inspect import _void
from merger import merge_excels
from charter import visual_chart, test

from model.data_category import DataCategory
from model.data import Data
from model.charts.line_chart import LineChart
from model.charts.bar_chart import BarChart
from model.chart_configs.grid_config import GridConfig
from model.chart_configs.target_axis import TargetAxis
from model.chart_configs.visual_chart_config import VisualChartConfig
from model.chart_configs.figure_size import FigureSize
from model.charts.pie_chart import PieChart

def make_rsrl_chart() -> _void:
    """
    Line chart showing resale price over remaining lease
    """
    y_data = Data("resale_price", DataCategory.NUMBERS, "Resale Price")
    x_data = Data("remaining_lease", DataCategory.DATE_REMAINING, "Remaining Lease (Years)")
    rsrl_line_chart = LineChart("Resale Price over Remaining Lease (Years)", x_data, y_data)
    visual_chart(MERGED_FILE_PATH, rsrl_line_chart, "project\VisualCharts\\resale_price-remaining_lease.png")

def make_hitc_chart() -> _void:
    """
    Bar Chart showing how many houses are there in a specific town
    """
    grid_config = GridConfig(target_axis= TargetAxis.Y)
    figure_size = FigureSize(50, 6)

    data = Data("town", DataCategory.TOWN, "Town")
    hitc_bar_chart = BarChart("Houses in a Town", "Town", "Houses Count", data)
    visual_chart(MERGED_FILE_PATH, hitc_bar_chart, "project\VisualCharts\\houses_in_town_count.png", VisualChartConfig(grid_config=grid_config, figure_size=figure_size))

def make_fmc_chart()-> _void:
    """
    Pie Chart showing Flat Models and it's counts
    """
    data = Data("flat_model",DataCategory.COUNTABLES, "Flat Models")
    fmc_pie_chart = PieChart("Number of Flat Models", data, 6)
    visual_chart(MERGED_FILE_PATH, fmc_pie_chart, "project\VisualCharts\\flat_models_count.png")

# NOTE: The all excel files are converted to a text-csv file first before merging.
EXCEL_FILE_LOCATIONS = [("project\Dataset\HDB Dataset - Jan.csv"), ("project\Dataset\HDB Dataset - Feb.csv")]
MERGED_FILE_PATH = ("project\Dataset\HDB_MERGED_Dataset.csv")

merge_excels(EXCEL_FILE_LOCATIONS, MERGED_FILE_PATH)

make_rsrl_chart()
make_fmc_chart()
make_hitc_chart()
test("project\VisualCharts\\debug.png")