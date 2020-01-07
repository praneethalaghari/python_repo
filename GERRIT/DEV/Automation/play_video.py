import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



google_url = 'https://www.google.com/search?q='
url = google_url + 'play pogiren'
#webbrowser.open(url)
	
response = requests.get(url)
soup = BeautifulSoup(response.content,'html5lib')

#print(response.content)

class_retriever = soup.find('div',attrs={'class' : 'ZINbbc xpd O9g5cc uUPGi'})

#print(class_retriever.content)


link_retriever = class_retriever.findAll('a')
#print(link_retriever)
print(link_retriever[0].get('href'))

abc = re.search('https(.*?)(?=&)',link_retriever[0].get('href'))
print(abc.group(0))

driver = webdriver.Firefox()
driver.get('https://www.youtube.com/watch?v=3BGOZ9xuyKs')
driver.implicitly_wait(30)


#element = driver.find_elements_by_class_name("ytp-large-play-button ytp-button")
#print(element)
#element = driver.find_element_by_xpath("//button[@aria-label='Play']")
#print(element)
#driver.implicitly_wait(100)

#element.click()

delay = 5
try:
	myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Play']")))
	element = driver.find_element_by_xpath("//button[@aria-label='Play']")
	print("Page is ready!")
	myElem.click()
except TimeoutException:
    print("Loading took too much time!")


print("Done")
#for elem in class_retriever:
#	link_retriever = elem.findAll('a')
#	print(link_retriever)