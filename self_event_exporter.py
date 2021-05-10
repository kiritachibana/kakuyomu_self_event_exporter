import requests
from bs4 import BeautifulSoup

target_url = 'https://kakuyomu.jp/user_events/16816452219415195483'
delim = "\t"

header = ["Title","Author","URL","Genre","Status","Episodes","Characters"]
print(delim.join(header))

noMoreContent = False
idx = 1
while(noMoreContent == False):
    r = requests.get(target_url + "?page=" + str(idx))
    soup = BeautifulSoup(r.text, 'lxml')
    if(soup.find("div", attrs={"class":"widget-emptyMessage"})):
        exit()

    for card in soup.find_all("div", attrs={"class": "enterdWork"}):
        cols = list()

        work = card.find("a", attrs={"class": "widget-workCard-titleLabel"})

        cols.append(work.text) # Title
        cols.append(card.find("a", attrs={"class": "widget-workCard-authorLabel"}).text) # Author
        cols.append("https://kakuyomu.jp" + work.get("href")) # URL
        cols.append(card.find(itemprop="genre").text) #genre

        cols.append(card.find("span", attrs={"class": "widget-workCard-statusLabel"}).text) # Status
        cols.append(card.find("span", attrs={"class": "widget-workCard-episodeCount"}).text.replace("話","")) # Number of episodes
        cols.append(card.find("span", attrs={"class": "widget-workCard-characterCount"}).text.replace('文字',"").replace(',', "")) # Number of characters
        cols.append(card.find("a", attrs={"class": "widget-workCard-reviewPoints"}).text.replace("★", "")) # review

        print(delim.join(cols))
    idx += 1
