'''
Given a link to a Facebook Post of an Image, get the link to the image, when the post was posted
and the number of likes, comments, shares

Note, for some reason we can't use BeautifulSoup as info/links are often not found. My workaround 
was to get the raw html of the page as a string and use regex to extract the desired information.
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json
import re
import csv


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding': 'none',
	'Accept-Language': 'en-US,en;q=0.8',
	'Connection': 'keep-alive'}


def dataploi_regex(content):
	'''
	Regex to extract the img_link
	'''
	m = re.search(r"(?:data-ploi)[^\s]+", content)
	try:
		img_link = m.group()
	except:
		print("No image link found for link:{}".format(content))
		return

	# process image link
	img_link = img_link.replace("data-ploi=\"","")
	img_link = img_link[:-1]
	img_link = img_link.replace("amp;", "")

	return img_link

def timestamp_regex(content):
	'''
	Regex to extract the timestamp
	'''
	m = re.search(r"(?:timestampContent)[^</]+", content)
	try:
		timestamp = m.group()
	except:
		print("No image link found for link:{}".format(content))
		return

	# process image link
	timestamp = timestamp.replace("timestampContent\">","")

	return timestamp


def like_comment_share_count(content):
	'''
	Regex to extract the like, comment, and share count reduced
	'''
	lcs = ["likecountreduced", "commentcountreduced", "sharecountreduced"]
	lcs_stats = []
	for stat in lcs:
		m = re.search(r"(?:{})[^,]+".format(stat), content)
		try:
			found_stat = m.group()
		except:
			print("{} not found for link:{}".format(stat, content))
			return

		# process image link
		found_stat = found_stat.replace("\"","")
		found_stat = found_stat.replace("likecountreduced:","")
		found_stat = found_stat.replace("commentcountreduced:","")
		found_stat = found_stat.replace("sharecountreduced:","")
		lcs_stats.append(found_stat)

	return lcs_stats


def scrape_image_url(link):
	'''
	Extract all the information for one Facebook Post at link
	'''
	try:
		req = Request(link, headers=hdr)
	except:
		print("{} not found".format(link))
		return

	try:
		url = urlopen(req)
	except:
		print("{} does not open").format(link)
		return

	content = url.read().decode('utf-8')

	img_link = dataploi_regex(content)
	timestamp = timestamp_regex(content)
	lcs = like_comment_share_count(content)

	url.close()

	return link, img_link, timestamp, lcs


if __name__ == '__main__':
	# Useful if you need to restart at a certain index
	RESTART_IDX = 0 

	file_name = "links_to_posts.txt"
	berkeley_links = open(file_name,'r').read()
	berkeley_links = json.loads(berkeley_links)

	imglinks_and_info = []
	for img_count, berkeley_link in enumerate(berkeley_links):
		if img_count < RESTART_IDX:
			continue
		print("Image count at: {}".format(img_count))
		imglinks_and_info.append(scrape_image_url(berkeley_link))
		
		# save a file every 100 images
		if img_count % 100 == 0:
			with open("imglinks_and_info_{}.csv".format(img_count), 'w') as csvfile:
				fieldnames = ['berkeley_link','img_link', 'timestamp', 'like', 'comment', 'share']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()

				for idx, imglink_and_info in enumerate(imglinks_and_info):
					try:
						writer.writerow({
							"berkeley_link":imglink_and_info[0],
							"img_link":imglink_and_info[1],
							"timestamp":imglink_and_info[2],
							"like":imglink_and_info[3][0],
							"comment":imglink_and_info[3][1],
							"share":imglink_and_info[3][2],
							"img_name":"UCB{}_{}".format(img_count, idx+1)
						})
					except:
						print("Something doesn't exist while writing")
						continue
			imglinks_and_info = []
			



