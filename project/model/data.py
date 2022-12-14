from inspect import _void
from numpy import *
from model.data_category import DataCategory
from model.point import Point
from multiprocessing.dummy import Array
import re

class Data:
    def __init__(self, name: str, data_category: DataCategory, display_name: str):
        self.name = name
        self.data_category = data_category
        self.points = []
        self.display_name = display_name

    # TODO: Find better way to do this stuff
    def get_data_value(self) -> Array:
        res = []
        for p in self.points:
            res.append(p.value)
        return res

    def set_data_from_raw(self, raw_data: Array) -> _void:
        # Remaining Lease in Years
        if self.data_category == DataCategory.DATE_REMAINING:
            for ele in raw_data:
                self.points.append(self._get_point_from_date_remaining_str(ele))

        # For counting how many houses are in a town
        elif self.data_category == DataCategory.TOWN:
            for ele in raw_data:
                # Pattern match to remove block number from house
                # We only need to know the town it is in
                town = re.sub(r'[0-9]', '', ele)
                self._increment_value_to_category(town)

        # For counting how many times a cateory occured
        elif self.data_category == DataCategory.COUNTABLES:
            for ele in raw_data:
                self._increment_value_to_category(ele)

        # Others (raw Numerical data)
        else:
            for i in range(len(raw_data)):
                self.points.append(Point(int(raw_data[i]), str(raw_data[i])))

        # Sort data
        self.points = sorted(self.points)

    def _find_point_by_label(self, label: str) -> Point:
        for p in self.points:
            if p.label == label:
                return p
        return None

    def _increment_value_to_category(self, category_label:str, increment_value: int = 1) -> _void:
        p = self._find_point_by_label(category_label)
        if p == None:
            p = Point(increment_value, category_label)
            self.points.append(p)
        else:
            p.value += increment_value

    def _get_point_from_date_remaining_str(self, input: str) -> Point:
        # Get year/month as string
        years_str = re.sub(r'[^0-9]', '', input.split("year")[0])
        months_str = re.sub(r'[^0-9]', '', input.split("year")[1])

        # Apply year/month if exists, otherwise default to 0
        years = 0
        months = 0
        if years_str.strip():
            years = int(years_str)
        if months_str.strip():
            months = int(months_str)

        value = float(years) + (months / 12.0)
        label = str(years) + "Y " + str(months) + "M"
        return Point(value, label)

    def cutoff_category(self, cutoff_point: int) -> _void:
        """
        If data category is COUNTABLES or TOWN, it will cutoff
        any value below the given into a category called 'others'
        """
        if not (self.data_category == DataCategory.COUNTABLES or self.data_category == DataCategory.TOWN):
            print("Cannot cutoff data values, wrong data category")
            return

        refcopy = self.points.copy()

        for p in refcopy:
            if p.value < cutoff_point:
                self.points.remove(p)
                self._increment_value_to_category("Others", p.value)