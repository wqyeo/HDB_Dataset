from inspect import _void
from model.data_category import DataCategory
from multiprocessing.dummy import Array
import re

class Data:
    def __init__(self, name: str, data_category: DataCategory, display_name: str):
        self.name = name
        self.data_category = data_category
        self.data = []
        self.display_name = display_name

    def set_data_by_category(self, raw_data: Array, data_category: DataCategory) -> _void:
        if data_category == DataCategory.DATE_REMAINING:
            for i in range(len(raw_data)):
                # Get year/month as string
                years_str = re.sub(r'[^0-9]', '', raw_data[i].split("year")[0])
                months_str = re.sub(r'[^0-9]', '', raw_data[i].split("year")[1])

                # Apply year/month if exists, otherwise default to 0
                years = 0
                months = 0
                if years_str.strip():
                    years = int(years_str)
                if months_str.strip():
                    months = int(months_str)

                value = float(years) + (months / 12.0)
                label = str(years) + "Y " + str(months) + "M"

                self.data.append(Point(value, label))
        else:
            for i in range(len(raw_data)):
                self.data.append(Point(int(raw_data[i]), str(raw_data[i])))

        # Sort data
        self.data = sorted(self.data)
    
    def get_data_ticks(self) -> Array:
        # TODO: Better way to return this result
        """
        Returns an array of 2 elements, first containing values, the second containing labels

        Result
        ----------
        An array of 2 elements
        1st element is an array tick **values**
        2nd element is an array of tick **labels**
        """
        tick_spacing = len(self.data) / 20
        t = tick_spacing

        res1 = []
        res2 = []
        for p in self.data:
            if t == tick_spacing or p == self.data[len(self.data) - 1]:
                t = 0
                res1.append(p.value)
                res2.append(p.label)
            else:
                t += 1
        return [res1, res2]

    # TODO: Find better way to do this stuff
    def get_data_value(self) -> Array:
        res = []
        for p in self.data:
            res.append(p.value)
        return res


class Point:
    def __init__(self, value, label):
        self.value = value
        self.label = label

    # for sorted() func
    def __lt__(self, other):
        return self.value < other.value

