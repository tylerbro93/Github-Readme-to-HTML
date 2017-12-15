from bs4 import BeautifulSoup
from urllib.request import urlopen


class GithubReadmeHTML():
    githubData = ""
    url = ""

    def __init__(self, url):
        self.url = url
        client = urlopen(self.url, timeout=2000)
        page = client.read()
        soup_page = BeautifulSoup(page, "html.parser")
        self.githubData = soup_page.find_all("article", {"class": "markdown-body entry-content"})
        


githubreadmedata = GithubReadmeHTML("https://github.com/tylerbro93/Multicast-Chat-System")
