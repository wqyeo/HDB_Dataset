from curses import def_prog_mode
from enum import Enum

class DataCategory(Enum):
    OTHERS = 0,
    NUMBERS = 1,
    DATE = 2,
    DATE_REMAINING = 3