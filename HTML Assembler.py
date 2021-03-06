Github_Webscraper = __import__("Github Webscraper")


class HTMLDocument():
    header = ""
    footer = ""
    sideBar = ""
    article = ""
    sideTable = ""
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 1}
    url = ""
    projectName = ""
    htmlName = ""
    names = []
    locations = []
    htmlDoc = ""
    name_references = {}

    def __init__(self, url, commands=""):
        self.url = url
        self.loadNameReferences()
        self.readmeData = Github_Webscraper.GithubReadmeHTML(self.url)
        self.article = self.readmeData.article
        self.projectName = self.readmeData.projectName
        self.createFileName()
        self.parseCommands(commands)
        self.assembleHTML()

    def createFileName(self):
        self.htmlName = (self.projectName.replace(" ", "_").lower()) + ".html"

    def parseCommands(self, commands):
        commands.lower()
        if("-nosidebar" not in commands):
            self.loadSidebar()
            self.checkIfSidebarHasCurrentProject()
            self.buildSidebar()
        if("-noheader" not in commands):
            self.loadHeader()
        if("-nofooter" not in commands):
            self.loadFooter()

    def loadSidebar(self):
        self.names.clear()
        self.locations.clear()
        infile = open("Storage\ProjectLinks.csv")
        line = infile.readline().strip()
        while(len(line) > 0):
            name, location = line.split("/")
            line = infile.readline().strip()
            self.names.append(name)
            self.locations.append(location)
        infile.close()

    def checkIfSidebarHasCurrentProject(self):
        found = 0
        for location in self.locations:
            if(self.htmlName == location):
                found = 1
        if(found != 1):
            self.names.append(self.projectName)
            self.locations.append(self.htmlName)
            self.saveProjectLinks()

    def saveProjectLinks(self):
        text = ""
        for index_num in range(0, len(self.names)):
            try:
                text = text + self.name_references[self.names[index_num]] + "/" + self.locations[index_num] + "\n"
            except KeyError:
                text = text + self.names[index_num] + "/" + self.locations[index_num] + "\n"
                print(self.names)
        infile = open("Storage\ProjectLinks.csv", 'w')
        infile.write(text)
        infile.close()

    def buildSidebar(self):
        sidebarHTML = '<div class="sidebarProject">\n<ul>\n'
        for index_num in range(0, len(self.names)):
            try:
                values = {"name": self.name_references[self.names[index_num]], "location": self.locations[index_num]}
            except KeyError:
                values = {"name": self.names[index_num], "location": self.locations[index_num]}
            text = '<li>\n<a href="{location}">{name}</a>\n</li>\n'.format(**values)
            sidebarHTML = sidebarHTML + text
        sidebarHTML = sidebarHTML + "</ul>\n</div>\n"
        self.sideBar = sidebarHTML
        self.saveSidebarHTML()

    def saveSidebarHTML(self):
        infile = open("HTML Parts\sidebar.part", 'w')
        infile.write(self.sideBar)
        infile.close()

    def loadHeader(self):
        infile = open("HTML Parts\header.part")
        line = infile.readline()
        while(len(line)>0):
            self.header = self.header + line
            line = infile.readline()

    def loadFooter(self):
        infile = open("HTML Parts\\footer.part")
        line = infile.readline()
        while(len(line) > 0):
            self.footer = self.footer + line
            line = infile.readline()

    def loadNameReferences(self):
        infile = open("Storage\Reference Dictionary.dat")
        line = infile.readline().strip()
        while(len(line)>0):
            oldName, newName = line.split("/")
            self.name_references[oldName] = newName
            line = infile.readline().strip()

    def assembleHTML(self):
        self.htmlDoc = self.header + self.sideBar + self.article + self.sideTable + self.footer


# htmlDoc = HTMLDocument("https://github.com/tylerbro93/Multicast-Chat-System")
# htmlDoc = HTMLDocument("https://github.com/tylerbro93/COBOL-MERGE-AND-SORTED-WAREHOUSE-INVENTORY-SALES")

