

class Renamer():
    names = []
    locations = []
    name_references = {}

    def __init__(self, oldName, newName):
        self.loadProjectLinks()
        self.loadNameReferences()
        self.replaceHTMLName(oldName, newName)
        self.saveProjectLinks()
        self.saveNameReferences()

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
            if(oldName in self.name_references.values()):
                self.names[self.names.index(oldName)] = newName
                for ref in self.name_references:
                    if(self.name_references[ref] == oldName):
                        self.name_references[ref] = newName
            elif(oldName in self.name_references):
                self.names[self.names.index(oldName)] = newName
                self.name_references[oldName] = newName
            elif(oldName in self.names):
                self.name_references[oldName] = newName
            else:
                print("Please create at least 1 readme to html based on the associated url")
        except ValueError:
            print("Typo in Name!")

    def saveProjectLinks(self):
        text = ""
        for index_num in range(0, len(self.names)):
            text = text + self.names[index_num] + "/" + self.locations[index_num] + "\n"
        infile = open("Storage\ProjectLinks.csv", 'w')
        infile.write(text)
        infile.close()

    def loadNameReferences(self):
        infile = open("Storage\Reference Dictionary.dat")
        line = infile.readline().strip()
        while(len(line)>0):
            oldName, newName = line.split("/")
            self.name_references[oldName] = newName
            line = infile.readline().strip()

    def saveNameReferences(self):
        text = ""
        infile = open("Storage\Reference Dictionary.dat", 'w')
        for ref in self.name_references:
            text = text + ref + "/" + self.name_references[ref]
        infile.write(text)
        infile.close()
