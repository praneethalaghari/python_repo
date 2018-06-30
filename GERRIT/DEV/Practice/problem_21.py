import requests
import os

from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

print(os.getcwd())
file_name = input("Enter the name of the file :")
with open(file_name,"w+") as f:

  for story_heading in soup.find_all(class_="story-heading"):
      if story_heading.a:
          print(story_heading.a.text.replace("\n", " ").strip())
          f.write(story_heading.a.text.replace("\n", " ").strip())
      else:
          print(story_heading.contents[0].strip());
          f.write(story_heading.contents[0].strip())