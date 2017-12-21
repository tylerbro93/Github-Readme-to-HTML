

class Renamer():
    names = []
    locations = []

    def __init__(self, oldName, newName):
        self.loadProjectLinks()
        self.replaceHTMLName()
        self.saveProjectLinks()

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

    def saveProjectLinks(self):
        text = ""
        for index_num in range(0, len(self.names)):
            text = text + self.names[index_num] + "/" + self.locations[index_num] + "\n"
        infile = open("Storage\ProjectLinks.csv", 'w')
        infile.write(text)
        infile.close()

