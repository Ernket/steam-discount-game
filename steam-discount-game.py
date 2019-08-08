# -*- coding: UTF-8 -*-
import requests
import bs4
import urllib
import sys
import re
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
pageid = 1
hd="Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
header={"User-Agent":hd}

while pageid<4: #只爬取3页
	url = "https://store.steampowered.com/search/?specials=1&page="+str(pageid)

	res = requests.get(url,headers=header)

	soup = bs4.BeautifulSoup(res.text,'html5lib')

	contents=soup.find_all("span",class_="title") #游戏名
	money=soup.find_all("div",class_="col search_price discounted responsive_secondrow") #原价+打折后
	emoney=soup.find_all("strike") #原价

	a=0
	y_money=[]
	d_money=[]
	game_name=[]

	for i in money:
		#获取文本
		i=i.get_text() 
		discount=emoney[a].get_text()
		contest=contents[a].get_text()

		i=i.replace(discount,'') #原价+打折后的价格，通过replace来将原价删除，只剩打折后
		ym=re.findall('\d+',i) #正则匹配数字,原价
		dm=re.findall('\d+',discount) #打折后
		y_money.append(ym)
		d_money.append(dm)
		game_name.append(contest)
		a+=1
	a=0

	file = open("steam.txt","a",encoding="gb18030")

	for i in range(25):
		text=("游戏名: "+game_name[a]+"  原价为: "+d_money[a][0]+"  打折后: "+y_money[a][0])
		#print(text)
		file.write("\n"+text+"\n")
		a+=1
	file.close()
	pageid+=1
