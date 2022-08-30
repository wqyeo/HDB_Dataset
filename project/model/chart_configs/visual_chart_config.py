from model.chart_configs.grid_config import GridConfig
from model.chart_configs.plot_config import PlotConfig
from model.chart_configs.figure_size import FigureSize

class VisualChartConfig:
    def __init__(self, grid_config: GridConfig = None, plot_config: PlotConfig = None, figure_size: FigureSize = None):
        self.grid_config = grid_config
        self.plot_config = plot_config
        self.figure_size = figure_size