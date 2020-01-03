from bs4 import BeautifulSoup 
import webbrowser
import requests
import json
import re


google_url = 'https://google.com/search?q='
to_search = 'water'
url = google_url + to_search
data = requests.get(url)

soup = BeautifulSoup(data.text,"lxml")

#print(soup.prettify())

class_retrieve = soup.find_all('div',attrs={'class' : 'rc'})
print(class_retrieve)
#class_retrieve = soup.find_all('div')
#for a in class_retrieve:
#	print(a.class_)

#print(class_retrieve)
#print(class_retrieve)

#for a in class_retrieve:
#	anchors = a.find_all('a')
	#print(anchors)
#	for i in anchors:
#		pass
		#print(i.get('href'))

#anchors = soup.find_all('a', class_ = '')
#print(anchors)

#for i in anchors:
#	print(i.get('href'))
#	print(i.get('class'))



'''
google_url = 'www.google.com'
to_search = ''

url = google_url + to_search 
#webbrowser.open(url)
#print(url)
data = requests.get(url)

print(data)

'''