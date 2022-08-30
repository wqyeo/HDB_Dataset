class Point:
    """
    Represents a point in the data
    """
    def __init__(self, value, label):
        self.value = value
        self.label = label

    # for sorted() func
    def __lt__(self, other):
        return self.value < other.value