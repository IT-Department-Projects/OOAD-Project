from bs4 import BeautifulSoup

import requests

r = requests.get("https://en.wikipedia.org/wiki/List_of_hospitals_in_India")

data = r.text

soup = BeautifulSoup(data, "lxml")

print("List of Hospitals")

for hospitals in soup.find_all('a'):
	if hospitals.parent.name == 'li':
		hospital = hospitals.get('title')
		print(hospital)
