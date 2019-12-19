from pip._vendor import requests
import json
import os
from bs4 import BeautifulSoup

# html = requests.get("https://www.liberation.fr/")
# print("Statut :", html.status_code)
# print("Headers :", html.headers)
# print("Text :", html.text)
# html = requests.get("http://localhost:8080/formext/avions/avions")
# print("Statut :", html.status_code)
# print("Headers :", html.headers)
# print("Text :", html.text)
dataset = []


def printseparator():
    """ Fonction qui affiche une ligne de séparation """
    print("-" * 50)


F_URL = "url"
F_STATUS = "status_code"
F_HTML = "content"
F_TITLE = "title"


def writetodict(html, is_verbose):
    title = search_title(html.text)
    dict = {F_URL: html.url, F_STATUS: html.status_code, F_HTML: html.text[:1000], F_TITLE: title}
    global dataset 
    dataset.append(dict)

    # affiche le nom du fichier .py
    print(__file__)
    # affiche le repertoire absolue pour le système d'exploitation
    print(os.path.abspath(__file__))
    # affiche le repertoire contenant le fichier .py
    print(os.path.dirname(__file__))
    # recupere le nom du fichier dans la configuration du systeme d'exploitation
    basedir = os.path.dirname(os.path.abspath(__file__))
    print(basedir)
    # creation du fichier chekurl.json dans le repertoire scrap
    filename = basedir + "/" + "checkurl.json"
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset, f)
        print(f"file {filename} created !")


def search_title_by_bs4(text):
    soup = BeautifulSoup(text)
    print(soup.title.string)
    return soup.title.String


def search_title(text):  
    """ fonction qui cherche le titre d'une page HTML """ 
    return search_title_by_bs4(text)
    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title: {begin}, {end}, {retbuffer}")
    return retbuffer


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
    headerdict = {"User-Agent": user_agent_text}
    html = requests.get(url, headers=headerdict)
    html.raise_for_status()
    return html


def get_urls(arglist, is_verbose=True):
    """ recuperer tout les urls listés dans listedesurls[ ] """
    for url_en_arg in arglist:
        try:
            html = get(url_en_arg)
        except Exception as e:
            print(f"Erreur de request vers {url_en_arg}")
            print(str(e))
            html = None
        if html:
            displayurl(html, is_verbose)
            writetodict(html, is_verbose)
            

def displayurl(html, is_verbose):
    print(f"--> Il y a {len(html.text)} octets dans {html.url}")
    if is_verbose:
        printseparator()
        print("Statut :", html.status_code)
        printseparator()
        print("Headers :", html.headers)
        printseparator()
        # print("Text :", html.text)
    else:
        print(f"Erreur de request vers {html.url} ---- avec code : {html.status_code}")
        for key, value in html.headers.items():
            print(f"{key} : {value}")
    # def writetofile(html):
    #     file = open("monfile.txt", "w")
    #     file.write(f"Url : {F_URL} Code : {F_STATUS} Texte : {F_HTML}")
    #     file.close()

    if __name__ == "__main__":
        letempsquipasse = ["matin", "midi", "soir", "minuit", "aube"]
    for item in letempsquipasse:
        print(item)
    listedesurls = [
        # "http://localhost:8080/formext/avions/avions",
        "https://www.dealabs.com",
        "https://www.ouest-france.fr/",
    ]
    get_urls(listedesurls)

    
print(len(dataset))
with open("test.json", "w+", encoding="utf8") as f:
    json.dump(dataset, f)