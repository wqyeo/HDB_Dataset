from model.charts.visual_chart import VisualChart
from model.data import Data

class PieChart(VisualChart):
    def __init__(self, title, data: Data, others_cut_off: int = 3):
        """
        A Pie Chart

        Parameters
        ------------------------
        **others_cut_off**
        Anything below this value will be categorised into 'others' section instead.
        """
        self.data = data
        self.others_cut_off = others_cut_off
        super().__init__(title)
