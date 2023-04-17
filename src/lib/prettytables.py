from src.lib.display import displayTable


class PrettyTable:
    def __init__(self, columns, padding=1, separator='default'):
        self.header = columns
        self.contents = []
        self.padding = padding
        self.columns = len(columns)
        self.rows = 0
        self.separator = separator

    def add_row(self, row):
        if len(row) != self.columns:
            raise ValueError("Length of rows need to be equal to the number of columns")

        self.contents.append(row)

    def __str__(self):
        return displayTable(self)
