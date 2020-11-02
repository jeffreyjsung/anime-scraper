__author__ = "Jeffrey Sung"

import os

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Some modules are not installed. Installing them automatically.")
    os.system("python -m pip install -r requirements.txt")

title = []
link = []


def entry():
    anime_name = input("[+] Enter the name of the anime: ")
    search_url = "https://www12.9anime.to/search?keyword=" + anime_name
    source_code = requests.get(search_url)
    content = source_code.content
    soup = BeautifulSoup(content, features="html.parser")
    choice = input("[+] Do you want details or links? ")
    if choice.lower() == "details":
        get_details(soup)
        details(link[0])
    elif choice.lower() == "links":
        get_details(soup)
        links(title, link)
    else:
        print("[-] Enter a valid choice.")


def get_details(soup):
    raw_soup = soup.find("ul", {"class": "anime-list"}).find_all("li")
    for item in raw_soup:
        temp_soup = item.find('a', {"class": "name"})
        title.append(temp_soup["data-jtitle"])
        link.append(temp_soup["href"])


def links(title, link):
    for i in range(len(title)):
        print("%d. %s: https://www12.9anime.to%s\n" % (i + 1, title[i], link[i]))


def details(link):
    source_code = requests.get("https://www12.9anime.to" + link)
    content = source_code.content
    soup = BeautifulSoup(content, "html.parser")
    container_soup = soup.find("div", {"class": "info"})
    print("\nName of the anime: ", container_soup.find("h1").getText(), "\n")
    titles_detail = container_soup.find_all('p', {'itemprop': 'description'})
    for elem in titles_detail:
        print(elem.getText())
        print("\n")


if __name__ == "__main__":
    entry()
