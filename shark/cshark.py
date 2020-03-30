class Parse():
    pass

    def read(self, fileName):
        with open(fileName) as f:
            return f.readlines()[0].strip()
    
