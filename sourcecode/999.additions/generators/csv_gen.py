class CSVFile(object):
    def __init__(self, path, sep=','):
        self.path = path
        self.sep = sep

    def __iter__(self):
        with open(self.path) as f:
            for l in f:
                yield l.split(self.sep)

csv_generator = CSVFile('sample.csv')

for row in csv_generator:
    print(row)
