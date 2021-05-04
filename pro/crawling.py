import requests
from bs4 import BeautifulSoup

def zum() :

   req = requests.get("http://issue.zum.com/")
   soup = BeautifulSoup(req.text, 'html.parser')
   list_zum = []
   list_zum_href = []

   for i in soup.select("#issueKeywordOpenList > li"):
        list_zum.append(i.find("a").text)
        list_zum_href.append(i.find("a")["href"])
   return list_zum,list_zum_href


def today() :

    req = requests.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')
    soup = BeautifulSoup(req.text, 'html.parser')
    list_today = []
    list_today_href=[]

    for i in soup.find_all("td", class_="subject") :
        list_today.append(i.text)
        list_today_href.append("http://www.todayhumor.co.kr"+i.find("a")["href"])
    return list_today,list_today_href


def clien() :
    req = requests.get('https://www.clien.net/service/recommend')

    soup = BeautifulSoup(req.text, 'html.parser')

    list_clien = []
    list_clien_href=[]

    for i in soup.find_all("span", class_="subject_fixed") :
        list_clien.append(i.text)

    for i in soup.find_all("a", class_="list_subject"):
        list_clien_href.append("https://www.clien.net/" + i["href"])

    return list_clien ,list_clien_href
