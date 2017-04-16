import requests
from bs4 import BeautifulSoup

r = requests.get("https://tspace.library.utoronto.ca/handle/1807/24488")
print r.content
