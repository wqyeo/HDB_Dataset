from model.chart_configs.target_axis import TargetAxis
from model.chart_configs.target_grid import TargetGrid

class GridConfig:
    def __init__(self, target_axis : TargetAxis = TargetAxis.BOTH, target_grid : TargetGrid = TargetGrid.MAJOR,linestyle :str = '--', linewidth : float = 0.5):
        self._target_axis = target_axis
        self._target_grid = target_grid
        self.linestyle = linestyle
        self.linewidth = linewidth

    def get_target_axis(self):
        return self._target_axis.name.lower()
    
    def get_target_grid(self):
        return self._target_grid.name.lower()