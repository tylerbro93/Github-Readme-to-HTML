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

    def __init__(self, url, commands=""):
        self.url = url
        self.readmeData = Github_Webscraper.GithubReadmeHTML(self.url)
        self.article = self.readmeData.article
        self.projectName = self.readmeData.projectName
        self.createFileName()
        self.parseCommands(commands)

    def createFileName(self):
        self.htmlName = (self.projectName.replace(" ", "_").lower()) + ".html"

    def parseCommands(self, commands):
        commands.lower()
        if("-nosidebar" not in commands):
            self.loadSidebar()
            self.checkIfSidebarHasCurrentProject()
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



htmlDoc = HTMLDocument("https://github.com/tylerbro93/Multicast-Chat-System")

