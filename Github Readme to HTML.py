HTML_Documents_Builder = __import__("HTML Documents Builder")
HTML_Renamer = __import__("HTML Renamer")

urls = []
command = ""
repos = []


def getUserRequest():
    print("what would you like to do:\n1. Turn single readme to HTML Document\n2. Turn multiple readmes to HTML "
          "Documents and update\n3. Edit Sidebar Names\n4. Help")
    choice = input("Perform Option Number: ")

    if(choice == "1"):
        url = getUrl()
        getCommand()
        HTML_Documents_Builder.HTMLDocuments(command, url)
    elif(choice == "2"):
        keepGoing = True
        #loadMonitoredRepos()
        getCommand()
        while(keepGoing == False):
            url = getUrl()
            if(url != "" and url not in repos):
                urls.append(url)
            else:
                keepGoing = False
        HTML_Documents_Builder.HTMLDocuments(command, urls)
    elif(choice == "3"):
        oldName = input("What is the name of the sidebar element you want to replace\n\tEXAMPLE: Personal "
                        "Webapage\nName to Replace: ")
        newName = input("What do you want to change the sidebar Element Name to\n\tEXAMPLE: Webpage\nNew Name: ")
        HTML_Renamer.Renamer(oldName, newName)


def getUrl():
    print("If you do not want to enter a url then hit Enter to skip!")
    url = input("What is the url: ")
    urls.append(url)
    return url


def getCommand():
    global command
    print("If you do not want to enter commands to call then hit Enter to skip!")
    command = input("What is the commands you want to run: ")

'''
def performHTMLConstrution():
    pass


def loadMonitoredRepos():
    infile = open("Storage\Monitored Repos.txt")
    line = infile.readline().strip()
    while(len(line) > 0):
        repos.append(line)
        line = infile.readline().strip()
    infile.close()


def addToMonitoredRepo():
    infile = open("Storage\Monitored Repos.txt", 'a')
    text = ""
    for url in urls:
        text = text + url + "\n"
    infile.write(text)
    infile.close()
'''
if __name__ == "__main__":
    getUserRequest()