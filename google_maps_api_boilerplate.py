# -*- coding: utf-8 -*-
"""[application description here]"""

from BeautifulSoup import BeautifulSoup
import urllib2 
import json


# Pass in an array of keywords and if google maps api finds a location return the lat and lng of that location
def get_lat_lng(keywords, api_key="AIzaSyCC8EASan34DBx6PbPW2j9K66mGUyoLpoE"):
	keywords = "+".join(keywords)

	link = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key={1}".format(keywords,api_key)
	print(link)
	try:
		req = urllib2.Request(link)
		url = urllib2.urlopen(req)
		content = url.read()
		content = json.loads(content)
	except:
		print("Google maps did not find anything from the search query: {0}. Try another query").format("".join(keywords))
		return 
	try:
		content['results'][0]['name']
	except:
		print("Content failed, probably exceeded quota")
		return
	if content['results'][0]['name'] == "Starbucks":
		return (content['results'][0]['geometry']['location']['lat'],content['results'][0]['geometry']['location']['lng'])
	else:
		return "Location is not Starbucks"

if __name__ == '__main__':
	
	loc = "Tully & King "
	query = loc.split(" ")

	misc = ["starbucks","san","jose"]
	[misc.append(word) for word in query]
	print(get_lat_lng(misc))
