import requests

url = 'https://en.wikipedia.org/wiki/Rockwell_Collins'
page_content = requests.get(url)
page_html = page_content.content
print page_html
