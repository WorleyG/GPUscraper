import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=desktop+graphics+cards&ignorear=0&N=-1&isNodeId=1'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
table = soup.find("div", attrs={'class':'items-view is-grid'})


# Price
items = []
for price in table.findAll(attrs={"class" : "price-current"}):
	priceDollars = []
	for dollarValue in price.findAll("strong"):
		text1 = dollarValue.get_text()
		for centValue in price.findAll("sup"):
			text2 = centValue.get_text()
			priceDollars.append(text1 + text2)
	items.append(priceDollars)


# Writing to File
outfile = open("./inmates.csv","wb")
writer = csv.writer(outfile)
writer.writerows(items)