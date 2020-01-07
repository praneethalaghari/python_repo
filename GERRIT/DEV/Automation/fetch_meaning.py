import webbrowser
import requests
from bs4 import BeautifulSoup

def meaning(word):
	word = 'meaning of ' + word
	url = "https://google.com/search?q=" + word
	#webbrowser.open(url)
	data = requests.get(url)     # Using requests
	soup = BeautifulSoup(data.content,"html5lib")
	
	#This also works
	#class_retriever = soup.select("div[class='v9i61e']")
	#for a in class_retriever:
	#	print(a.text.encode('utf-8'))
	
	class_retriever = soup.findAll('div',attrs = {'class':'v9i61e'})
	print(class_retriever[0].text)
	return class_retriever[0].text
	
	
