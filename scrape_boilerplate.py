# -*- coding: utf-8 -*-
"""[application description here]"""

from BeautifulSoup import BeautifulSoup
import urllib2 
import json

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding': 'none',
	'Accept-Language': 'en-US,en;q=0.8',
	'Connection': 'keep-alive'}


startup_names = []
def scrape_page(page_num):
	link = "http://www.startupranking.com/top/united-states/"+str(page_num)
	try:
		req = urllib2.Request(link, headers=hdr)
	except:
		print("Link not found")
		return
	try:	
		url = urllib2.urlopen(req)
	except:
		print("Link does not open")
		return

	content = url.read()

	soup = BeautifulSoup(content)

	for i in range(100):
		startup_names.append(soup("a")[39+3*i].text)
		print(soup("a")[39+3*i].text)


for page_num in (range(20)):
	if page_num == 0: continue
	scrape_page(page_num)


json_str = json.dumps(startup_names)
f = open("boilerplate_filename","w")
f.write(json_str)


