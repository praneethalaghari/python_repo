from bs4 import BeautifulSoup as bs
import requests

base_url = "https://en.wikipedia.org/wiki/Web_scraping"
website = requests.get(base_url)

data = bs(website.text,"html.parser")

for title in data.find_all('title'):
    print(title.text)

print('\n')

index_num = [elem.text for elem in data.find_all(class_="tocnumber")]
index_txt = [elem.text for elem in data.find_all(class_="toctext")]


index_head_1 = [elem.text for elem in data.find_all("h1")]
print("H1 list :",index_head_1)
index_head_2 = [elem.text for elem in data.find_all("h2")]
print("H2 list :",index_head_2)
index_head_3 = [elem.text for elem in data.find_all("h3")]
print("H3 list :",index_head_3)
index_head_4 = [elem.text for elem in data.find_all("h4")]
print("H4 list :",index_head_4)
index_head_5 = [elem.text for elem in data.find_all("h5")]
print("H5 list :",index_head_5)
index_head_6 = [elem.text for elem in data.find_all("h6")]
print("H6 list :",index_head_6)

print('\n')

#for i in range(0,len(index_num)):
#   print(index_num[i],index_txt[i])

for i,j in zip(index_num,index_txt):
    print(i,j)

paragraph = [elem.text for elem in data.find_all("p")]
for para in paragraph:
    print(para)
