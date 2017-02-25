from bs4 import BeautifulSoup
import requests

r = requests.get("https://en.wikipedia.org/wiki/List_of_insurance_companies_in_India")

data = r.text

soup = BeautifulSoup(data, "lxml")

print("List of Insurance Companies")

for companies in soup.find_all('a'):
	if(companies.parent.name == "li"):
		company = companies.get('title')
		print(company)
