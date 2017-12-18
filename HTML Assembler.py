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

    def __init__(self, url, commands=""):
        self.url = url
        self.readmeData = Github_Webscraper.GithubReadmeHTML(self.url)
        self.article = self.readmeData.article
        self.projectName = self.readmeData.projectName
        self.createFileName()
        self.parseCommands(commands)
        self.aassembleHTML()

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
        for name in self.names:
            if(self.projectName == name):
                found = 1
        if(found != 1):
            self.names.append(self.projectName)
            self.locations.append(self.htmlName)
            self.saveProjectLinks()

    def saveProjectLinks(self):
        text = ""
        for name in self.names:
            for location in self.locations:
                text = text + name + "/" + location + "\n"
        infile = open("Storage\ProjectLinks.csv", 'w')
        infile.write(text)
        infile.close()

    def buildSidebar(self):
        sidebarHTML = '<div class="sidebarProject">\n<ul>\n'
        for name in self.names:
            for location in self.locations:
                values = {"name": name, "location": location}
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
        while (len(line) > 0):
            self.footer = self.footer + line
            line = infile.readline()

    def aassembleHTML(self):
        self.htmlDoc = self.header + self.sideBar + self.article + self.sideTable + self.footer
        print(self.htmlDoc)


#htmlDoc = HTMLDocument("https://github.com/tylerbro93/Multicast-Chat-System")

