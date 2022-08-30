from model.data import Data
from model.charts.visual_chart import VisualChart

class BarChart(VisualChart):
    def __init__(self, title, x_name: str, y_name: str, data: Data):
        self.data = data
        self.x_name = x_name
        self.y_name = y_name
        super().__init__(title)