import requests
from bs4 import BeautifulSoup as bs

webpage = requests.get("https://www.worldometers.info/coronavirus/country/canada/")
s = bs(webpage.text, "html.parser")
data = s.find_all('div', class_ = "maincounter-number")

print("Total cases     : " + data[0].text.strip())
print("Total death     : " + data[1].text.strip())
print("Total recovered : " + data[2].text.strip())

