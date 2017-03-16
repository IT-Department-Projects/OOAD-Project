from bs4 import BeautifulSoup
import re

data = open('HospitalDepartments.html', 'r').read()

soup = BeautifulSoup(data, "lxml")

hospitals = soup.find_all('b')

print("List of Departments")

for hospital in hospitals:
	print("\n".join(hospital.contents))