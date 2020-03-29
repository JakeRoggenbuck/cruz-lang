class ReadFile():
    pass

    def read(self, fileName):
        with open(fileName) as f:
            return f.name

