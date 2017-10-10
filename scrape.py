import csv
import requests
from BeautifulSoup import BeautifulSoup
from itertools import izip

url = 'https://en.wikipedia.org/wiki/Rockwell_Collins'
page_content = requests.get(url)

page_html = page_content.content
clean_html = BeautifulSoup(page_html)

info_table = clean_html.find('table', attrs={'class':'infobox vcard'})
title = info_table.findAll('caption')
print title
logo = 0
count = 0
list_of_headers = []
list_of_data = []

for row in info_table.findAll('tr'):
	for cell in row.findAll('th'):
		heading =  cell.text.replace('&ndsp;','')
		heading = cell.text.replace('&#160;',' ')
		heading = heading.encode(clean_html.originalEncoding);
		list_of_headers.append(heading)
	for cell in row.findAll('td'):
		if(logo):
			data = cell.text.replace('&ndsp;','')
			data = data.encode(clean_html.originalEncoding);
			list_of_data.append(data)
		logo =  1

outfile = open("./company_data.csv","ab")
writer = csv.writer(outfile)
writer.writerows(izip(list_of_headers, list_of_data))
			
