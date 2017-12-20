HTML_Document_Builder = __import__("HTML Document Builder")


def getUserRequest():
    print("what would you like to do:\n1. Turn single readme to HTML Document\n2. Turn multiple readmes to HTML "
          "Documents\n3. Advance Mode\n4. Help")
    choice = input("Perform Option Number: ")

    if(choice == "1"):
        results = getUrlandCommand()
        HTML_Document_Builder.HTMLDocuments(results[1], results[0])
    if(choice == "2"):
        url = "first run"
        while(url != ""):
            print("If you do not want to enter a url then hit Enter to skip!")
            url = input("What is the url: ")


def getUrlandCommand():
    results = []
    print("If you do not want to enter a url then hit Enter to skip!")
    url = input("What is the url: ")
    results.append(url)
    print("If you do not want to enter commands to call then hit Enter to skip!")
    commands = input("What is the commands you want to run: ")
    results.append(commands)
    return results


if __name__ == "__main__":
    getUserRequest()