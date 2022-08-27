from inspect import _void
from model.data_category import DataCategory
from multiprocessing.dummy import Array
import re

class Data:
    def __init__(self, name: str, data_category: DataCategory):
        self.name = name
        self.data_category = data_category
        self.data = []
        self.major_label = []

    def set_data_by_category(self, raw_data: Array, data_category: DataCategory) -> _void:
        if data_category == DataCategory.DATE_REMAINING:
            for i in range(len(raw_data)):
                years = int(re.sub(r'[^0-9]', '', raw_data[i].split("year")[0]))
                months = int(re.sub(r'[^0-9]', '', raw_data[i].split("year")[1]))
                self.data.append((years * 12) + months)
                self.major_label.append(str(years) + "Y " + str(months) + "M")
        else:
            for i in range(len(raw_data)):
                self.data.append(int(raw_data[i]))
                self.major_label.append(str(raw_data[i]))

