Github_Webscraper = __import__("Github Webscraper")
class HTMLDocument():
    header = ""
    footer = ""
    sideBar = ""
    article = ""
    sideTable = ""
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 1}
    url = ""

    def __init__(self, url, commands=""):
        self.parseCommands(commands)
        self.url = url
        self.readmeData = Github_Webscraper.GithubReadmeHTML(self.url)
        print(self.readmeData.githubData)


    def parseCommands(self, commands):
        commands.lower()
        if("-nosidebar" not in commands):
            self.loadSidebar()
        if("-noheader" not in commands):
            self.loadHeader()
        if("-nofooter" not in commands):
            self.loadFooter()

    def loadSidebar(self):
        pass
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
    def activateWebSrapper(self):
        pass


htmlDoc = HTMLDocument("https://github.com/tylerbro93/Multicast-Chat-System")

