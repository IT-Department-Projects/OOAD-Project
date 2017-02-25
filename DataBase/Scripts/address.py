from bs4 import BeautifulSoup

data = open('address.html', 'r').read()

soup = BeautifulSoup(data, "lxml")

addresses = soup.find_all('li')

print('List of Addresses')

for address in addresses:
	print("\n".join(address.contents))
