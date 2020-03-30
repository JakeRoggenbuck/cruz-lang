class Parse():

    def read(self, fileName):
        with open(fileName) as f:
            content = f.readlines()
            return content
