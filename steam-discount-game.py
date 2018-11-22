# -*- coding: UTF-8 -*-
import requests
import bs4
import urllib

pageid = 1

file = open("steam.txt","a")
while pageid<10:
    url = "https://store.steampowered.com/search/?specials=1&page=" + str(pageid)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text)
    contents = soup.select('div[class="responsive_search_name_combined"]')

    for content in contents:
        try:
            name = content.find("span",class_="title").string.strip()
            print(name)
            file.write(name+"\n")
            file.close
        except:
            print(name.encode('utf-8'))
            urlname = name.encode('utf-8')
            file.write(str(urlname)+"\n")
            file.close
    pageid = pageid + 1
