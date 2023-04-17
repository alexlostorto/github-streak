class PrettyTable:
    def __init__(self, columns, padding=2):
        self.header = columns
        self.contents = []
        self.padding = padding
        self.columns = len(columns)
        self.rows = 0

    def add_row(self, row):
        if len(row) != self.columns:
            raise ValueError("Length of rows need to be equal to the number of columns")

        self.contents.append(row)

    def __str__(self):
        def getMaxLengths():
            maxLengths = [len(x) + self.padding for x in self.header]

            for row in self.contents:
                for i in range(len(row)):
                    if len(row[i]) + self.padding * 2 > maxLengths[i]:
                        maxLengths[i] = len(row[i]) + self.padding * 2

            return maxLengths

        def createDivider(boxLengths):
            line = ''

            for length in boxLengths:
                line += '+' + '-' * length

            return line + '+'

        def createRow(boxLengths, row):
            def padString(text, length):
                while len(text) < length:
                    text += ' '

                    if len(text) == length:
                        return text
                    else:
                        text = ' ' + text
                return text

            line = ''

            for i in range(len(boxLengths)):
                line += '|' + padString(row[i], boxLengths[i])

            return line + '|'

        maxLengths = getMaxLengths()

        table = []
        table.append(createDivider(maxLengths))
        table.append(createRow(maxLengths, self.header))
        table.append(createDivider(maxLengths))

        for row in self.contents:
            table.append(createRow(maxLengths, row))

        table.append(createDivider(maxLengths))

        table = '\n'.join(table)

        return f"{table}"
