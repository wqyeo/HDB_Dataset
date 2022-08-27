from model.data import Data
from model.chart_type import ChartType

class VisualChart:
    def __init__(self, title, x_data: Data, y_data: Data, chart_type: ChartType):
        self.title = title
        self.x_data = x_data
        self.y_data = y_data
        self.chart_type = chart_type
