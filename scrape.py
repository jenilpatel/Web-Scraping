import requests
from BeautifulSoup import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Rockwell_Collins'
page_content = requests.get(url)

page_html = page_content.content
clean_html = BeautifulSoup(page_html)

print clean_html
