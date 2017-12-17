
class HTMLDocument():
    header = ""
    footer = ""
    sideBar = ""
    article = ""
    sideTable = ""
    commandSequence = {"sidebar": 1, "header": 1, "footer": 1, "sideTable": 1}

    def __init__(self, commands=""):
        self.parseCommands(commands)

    def parseCommands(self, commands):
        commands.lower()
        if("-nosidebar" not in commands):
            pass
    def loadSidebar(self):




