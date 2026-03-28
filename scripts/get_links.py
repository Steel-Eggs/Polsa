import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

url = "https://skif-avto.ru"
resp = requests.get(url, verify=False)
soup = BeautifulSoup(resp.content, 'html.parser')
links = set()
for a in soup.find_all('a', href=True):
    href = a['href']
    if href.startswith('/'):
        links.add(href)

catalog_links = [l for l in links if '/catalog/' in l and l != '/catalog/']
other_links = [l for l in links if l not in catalog_links]

print("Main Links:", other_links[:5])
print("Catalog Links:", catalog_links[:10])
