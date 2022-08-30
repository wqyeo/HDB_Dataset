from curses import def_prog_mode
from enum import Enum

class DataCategory(Enum):
    NUMBERS = 1,
    TOWN = 2,
    DATE_REMAINING = 3,