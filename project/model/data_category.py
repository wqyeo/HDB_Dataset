from curses import def_prog_mode
from enum import Enum

class DataCategory(Enum):
    NUMBERS = 1,
    COUNTABLES = 2, # Can be seperated into different categories and counted
    DATE_REMAINING = 3,
    TOWN = 4