""""Represents a text-based CSV sheet"""
from inspect import _void
from multiprocessing.dummy import Array


class CSVExcel:
    sheet = []

    def append_row(self, row_content: Array) -> _void:
        self.sheet.append(row_content)

    def get_row(self, row: int) -> Array:
        return self.sheet[row]

    def save_csv_excel(self, path: str) -> _void:
        # Empty the file first (in case it exists before)
        f = open(path, 'w')
        f.write('')
        f.close()
        # Write
        f = open(path, 'a')
        for row in self.sheet:
            f.write(','.join(row) + "\n")
        f.close()