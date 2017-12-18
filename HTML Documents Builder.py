HTML_Assembler = __import__("HTML Assembler")


class HTMLDocuments():
    htmlDocuments = []
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 0, "update": 1, "lastCall": 0}
    commands = ""

    def __init__(self, url="", commands=""):
        self.commands = commands
        self.commandParser(self.commands)

    def commandParser(self, commands):
        if(commands == "" or "-lastcall" in commands):
            self.loadLastCall()

    def loadLastCall(self):
        infile = open("Storage\lastCall.dat")
        lastCall = infile.readline().strip() + " "
        self.commandParser(lastCall)


htmlDocuments = HTMLDocuments()