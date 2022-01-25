import requests
from bs4 import BeautifulSoup

url = 'https://www.bol.com/nl/nl/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')