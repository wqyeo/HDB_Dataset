from model.data import Data
from model.charts.visual_chart import VisualChart

class LineChart(VisualChart):
    def __init__(self, title, x_data: Data, y_data: Data):
        self.x_data = x_data
        self.y_data = y_data
        super().__init__(title)