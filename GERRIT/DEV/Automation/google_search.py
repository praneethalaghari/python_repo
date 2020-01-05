from bs4 import BeautifulSoup 
import webbrowser
import requests
import json
import re
from urllib.request import Request,urlopen


google_url = 'https://google.com/search?q='
to_search = 'clothes'
url = google_url + to_search


data = requests.get(url)     # Using requests
soup = BeautifulSoup(str(data.text),"html.parser")


# This is usin urllib library

	#url_search = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	#data = urlopen(url_search).read()
	#soup = BeautifulSoup(str(data),"html.parser")

# To print prettified html content
	#print(soup.prettify())

class_retrieve = soup.find_all('div',attrs={'class' : 'kCrYT'})

for cr in class_retrieve:
	links = cr.find_all('a')
	for link in links:
		print(link.get('href'))
