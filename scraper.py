import requests
from bs4 import BeautifulSoup

# SETUP CODE
URL = "https://droptracker.ca/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

# FIND BY CENTER TAG
for row in soup.find_all('tr'):
  print(row, end='\n'*2)