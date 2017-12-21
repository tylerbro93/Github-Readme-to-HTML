HTML_Document_Builder = __import__("HTML Document Builder")

urls = []
command = ""
repos = []

def getUserRequest():
    print("what would you like to do:\n1. Turn single readme to HTML Document\n2. Turn multiple readmes to HTML "
          "Documents\n3. Advance Mode\n4. Help")
    choice = input("Perform Option Number: ")

    if(choice == "1"):
        url = getUrl()
        getCommand()
        HTML_Document_Builder.HTMLDocuments(command, url)
    elif(choice == "2"):
        keepGoing = True
        loadMonitoredRepos()
        getCommand()
        while(keepGoing == False):
            url = getUrl()
            if(url != "" and url not in repos):
                urls.append(url)
            else:
                keepGoing = False


def getUrl():
    print("If you do not want to enter a url then hit Enter to skip!")
    url = input("What is the url: ")
    urls.append(url)
    return url

def getCommand():
    global command
    print("If you do not want to enter commands to call then hit Enter to skip!")
    command = input("What is the commands you want to run: ")


def performHTMLConstrution():
    pass

def loadMonitoredRepos():
    infile = open("Storage\Monitored Repos.txt")
    line = infile.readline().strip()
    while(line > 0):
        repos.append(line)
        line = infile.readline().strip()


if __name__ == "__main__":
    getUserRequest()