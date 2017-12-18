HTML_Assembler = __import__("HTML Assembler")


class HTMLDocuments():
    htmlDocuments = []
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 0, "update": 1, "lastCall": 0}
    commands = ""
    urls = []

    def __init__(self, commands="", url=""):
        self.commands = commands
        self.commandParser(self.commands)


    def commandParser(self, commands):
        if(commands == "" or "-lastcall" in commands):
            self.loadLastCall()

    def loadLastCall(self):
        infile = open("Storage\lastCall.dat")
        lastCall = infile.readline().strip() + " "
        infile.close()
        self.commandParser(lastCall)

    def buildHTMLDocs(self, url, commands):
        if(url != ""):
            pass

    def loadMonitoredRepos(self):
        infile = open("Storage\Monitored Repos.txt")
        url = infile.readline().strip()
        while(len(url) > 0):
            self.urls.append(url)
        infile.close()

    def fetchHTMLDocument(self, url, commands=""):
        htmlDoc = HTML_Assembler.HTMLDocument(url)
        self.htmlDocuments.append(htmlDoc)

    def addToMonitoredRepos(self):
        infile = open("Storage\Monitored Repos.txt")

htmlDocuments = HTMLDocuments()