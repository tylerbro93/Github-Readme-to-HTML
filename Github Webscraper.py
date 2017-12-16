from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, URLError
from os import mkdir



class GithubReadmeHTML():
    githubData = ""
    url = ""
    links = []
    projectName = ""

    def __init__(self, url):
        self.url = url
        client = urlopen(self.url, timeout=2000)
        page = client.read()
        soup_page = BeautifulSoup(page, "html.parser")
        self.githubData = soup_page.find_all("article", {"class": "markdown-body entry-content"})
        self.findProjectName()
        self.getImages()

    def findProjectName(self):
        self.projectName = self.url.rsplit("/", 1)[1]
        self.projectName = self.projectName.replace("-", " ")

    def getImages(self):
        text = self.githubData[0]
        for i in text:
            line = str(i)
            if(line is not None):
                if("<img" in line):
                    data, linkdata = line.split("<img")
                    linkwork1 = linkdata.split('src=', 1)[-1]
                    linkwork2 = str(linkwork1).split(' ', 1)[-1]
                    link = str(linkwork1).replace(str(linkwork2), "")
                    link = link.replace('"', '')
                    new_link = "https://raw.githubusercontent.com" + link
                    new_link = new_link.replace("/raw/", "/")
                    #print(new_link)
                    downloadError = self.downloadImage(new_link)
                    if(downloadError != 1):
                        if(link in line):
                            print("true")
                        linkdata = linkdata.replace(link, new_link)
                        print(link)
                        print(linkdata)

    def downloadImage(self, new_link):
        errorState = 0
        try:
            imageName = str(new_link).rsplit("/", 1)[1]
            print(imageName)
            backspace = "\\"
            try:
                pass
                # urlretrieve(new_link, self.projectName + backspace + imageName)
            except FileNotFoundError:
                mkdir(self.projectName)
                urlretrieve(new_link, backspace + self.projectName + backspace + imageName)

        except URLError:
            errorState = 1

        return errorState








githubreadmedata = GithubReadmeHTML("https://github.com/tylerbro93/Multicast-Chat-System")
