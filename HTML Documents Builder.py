HTML_Assembler = __import__("HTML Assembler")


class HTMLDocuments():
    htmlDocuments = []
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 0, "update": 1, "lastCall": 0}
    commands = ""
    urls = []

    def __init__(self, commands="", url=""):
        self.commands = commands
        self.commandParser(self.commands)
        self.buildHTMLDocs(url, commands)

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
            HTMLDoc = HTML_Assembler.HTMLDocument(url, commands)
            self.htmlDocuments.append(HTMLDoc)
            if(self.commandSequence["update"] == 1):
                self.rebuildAllHTMLDocs(commands)

            self.urls.append(url)
            self.addToMonitoredRepos(url)
        elif(url == "" and self.commandSequence["update"] == 1):
            self.rebuildAllHTMLDocs(commands)

    def rebuildAllHTMLDocs(self, commands):
        self.loadMonitoredRepos()
        for url in self.urls:
            self.fetchHTMLDocument(url, commands)

    def loadMonitoredRepos(self):
        infile = open("Storage\Monitored Repos.txt")
        url = infile.readline().strip()
        while(len(url) > 0):
            self.urls.append(url)
        infile.close()

    def fetchHTMLDocument(self, url, commands):
        htmlDoc = HTML_Assembler.HTMLDocument(url, commands)
        self.htmlDocuments.append(htmlDoc)

    def addToMonitoredRepos(self, url):
        if(url not in self.urls):
            infile = open("Storage\Monitored Repos.txt", 'a')
            infile.write(url)
            infile.close()


htmlDocuments = HTMLDocuments("", "https://github.com/tylerbro93/Multicast-Chat-System")