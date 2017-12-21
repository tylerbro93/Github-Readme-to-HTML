

class Renamer():
    names = []
    locations = []

    def __init__(self, oldName, newName):
        self.loadProjectLinks()
        self.replaceHTMLName()

    def loadProjectLinks(self):
        infile = open("Storage\ProjectLinks.csv")
        line = infile.readline().strip()
        while (len(line) > 0):
            name, location = line.split("/")
            line = infile.readline().strip()
            self.names.append(name)
            self.locations.append(location)
        infile.close()

    def replaceHTMLName(self, oldName, newName):
        try:
            self.names[self.names.index(oldName)] = newName
        except ValueError:
            print("Typo in Name!")