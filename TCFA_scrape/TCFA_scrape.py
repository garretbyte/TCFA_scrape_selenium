import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.tncenturyfarms.org/farms/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='wp-list-table') #replace with correct class.

data = []

if table:
    headers = [th.text.strip() for th in table.find_all('th')]
    data.append(headers)import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.tncenturyfarms.org/farms/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='wp-list-table') #replace with correct class.

data = []

if table:
    headers = [th.text.strip() for th in table.find_all('th')]
    data.append(headers)
    for row in table.find_all('tr')[1:]:
        cells = [td.text.strip() for td in row.find_all('td')]
        if cells:
            data.append(cells)

    with open('century_farms.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print("Data saved to century_farms.csv")
else:
    print("Table not found.")

    for row in table.find_all('tr')[1:]:
        cells = [td.text.strip() for td in row.find_all('td')]
        if cells:
            data.append(cells)

    with open('century_farms.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print("Data saved to century_farms.csv")
else:
    print("Table not found.")
