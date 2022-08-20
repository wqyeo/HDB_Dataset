from data_category import DataCategory

class Data:
    def __init__(self, name: str, data_category: DataCategory):
        self.name = name
        self.data_category = data_category
        self.data = []