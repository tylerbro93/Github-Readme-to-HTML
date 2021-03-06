from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, URLError
from os import mkdir
from time import sleep
from pathlib import Path


class GithubReadmeHTML():
    githubData = ""
    url = ""
    links = []
    projectName = ""
    imageName = ""
    article = ""

    def __init__(self, url):
        self.url = url
        client = urlopen(self.url, timeout=2000)
        page = client.read()
        soup_page = BeautifulSoup(page, "html5lib")
        self.githubData = soup_page.find("article", {"class": "markdown-body entry-content"})
        self.findProjectName()
        self.getImages()

    def findProjectName(self):
        self.projectName = self.url.rsplit("/", 1)[1]
        self.projectName = self.projectName.replace("-", " ")

    def getImages(self):
        text = self.githubData.prettify(formatter="minimal")
        lines = []
        lines = text.splitlines()
        for line in lines:
            if(True):
                if("<img" in line):
                    data, linkdata = line.split("<img")
                    linkwork1 = linkdata.split('src=', 1)[-1]
                    linkwork2 = str(linkwork1).split(' ', 1)[-1]
                    link = str(linkwork1).replace(str(linkwork2), "")
                    link = link.replace('"', '')
                    new_link = "https://raw.githubusercontent.com" + link
                    new_link = new_link.replace("/raw/", "/")
                    downloadError = self.downloadImage(new_link)
                    if(downloadError != 1):
                        link = link.replace(" ", "")
                        linkdata = linkdata.replace(link, self.projectName + "/" + self.imageName)
                        line = data + "<img" + linkdata
            self.article = self.article + line + "\n"

    def downloadImage(self, new_link):
        errorState = 0
        try:
            self.imageName = str(new_link).rsplit("/", 1)[1]
            backspace = "/"
            self.imageName = self.imageName.replace("%20", " ")
            filepath = self.projectName + backspace + self.imageName
            try:
                if((Path(filepath)).is_file() == False):
                    urlretrieve(new_link, filepath)
            except FileNotFoundError:
                mkdir(self.projectName)
                sleep(15)  # prevents folder not being ready because of slow system
                urlretrieve(new_link, filepath)
        except URLError:
            errorState = 1
        return errorState


# githubreadmedata = GithubReadmeHTML("https://github.com/tylerbro93/Multicast-Chat-System")
