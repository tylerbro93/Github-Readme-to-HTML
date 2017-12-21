HTML_Assembler = __import__("HTML Assembler")


class HTMLDocuments():
    htmlDocuments = []
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 0, "update": 1, "lastCall": 0}
    commands = ""
    urls = []

    def __init__(self, commands="", url=""):
        self.commands = commands
        self.commandParser(self.commands)
        self.loadMonitoredRepos()
        if(type(url) == str):
            self.buildHTMLDocs(url, commands)
        if(type(url) != str):
            for link in url:
                self.buildHTMLDocs(link, commands)
        if(self.commandSequence["sidebar"] == 1 and self.commandSequence["update"] == 1):
            self.updateAllSidebars()
        self.saveHTMLDoc()

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
            print(HTMLDoc.htmlDoc)
            self.htmlDocuments.append(HTMLDoc)
            if(self.commandSequence["update"] == 1):
                self.rebuildAllHTMLDocs(commands)
            if(url not in self.urls):
                self.addToMonitoredRepos(url)
                self.urls.append(url)

        elif(url == "" and self.commandSequence["update"] == 1):
            self.rebuildAllHTMLDocs(commands)
        print(self.urls)

    def rebuildAllHTMLDocs(self, commands):
        for url in self.urls:
            self.fetchHTMLDocument(url, commands)

    def loadMonitoredRepos(self):
        infile = open("Storage\Monitored Repos.txt")
        url = infile.readline().strip()
        while(len(url) > 0):
            self.urls.append(url)
            url = infile.readline().strip()
        infile.close()

    def fetchHTMLDocument(self, url, commands):
        htmlDoc = HTML_Assembler.HTMLDocument(url, commands)
        self.htmlDocuments.append(htmlDoc)

    def addToMonitoredRepos(self, url):
        if(url not in self.urls):
            infile = open("Storage\Monitored Repos.txt", 'a')
            infile.write(url + "\n")
            infile.close()

    def updateAllSidebars(self):
        for document in self.htmlDocuments:
            document.loadSidebar()
            document.buildSidebar()
            document.assembleHTML()
            print(document.htmlDoc)

    def saveHTMLDoc(self):
        for document in self.htmlDocuments:
            infile = open(document.htmlName, 'w')
            infile.write(document.htmlDoc)
            infile.close()

# htmlDocuments = HTMLDocuments("", "https://github.com/tylerbro93/Multicast-Chat-System")
# htmlDocuments = HTMLDocuments("", "")