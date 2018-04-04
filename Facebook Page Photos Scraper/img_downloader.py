'''
Utils to download images given links to images
'''
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import json
import re
import csv
from os import listdir
import os


def find_csv_filenames(path_to_dir, suffix=".csv" ):
	'''
	Return all the csv files in a directory
	'''
    file_names = listdir(path_to_dir)
    return [file_name for file_name in file_names if file_name.endswith( suffix )]


def create_directory(directory_name):
	'''
	Creates a directory named directory_name
	'''
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)

	return directory_name

def download_imgs(file_name, directory_name):
	'''
	Opens up a csv file and downloads the images at row['img_link'] and names the images row['img_name']
	'''
	with open(file_name, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			img_name = row['img_name']
			img_link = row['img_link']
			print("Downloading image: {}".format(img_name))

			try:
				urlretrieve(img_link, "{}/{}.jpg".format(directory_name,img_name))
			except:
				print("Failed to download image: {}".format(img_link))

def add_img_name(file_name):
	'''
	Helper function to add a name column to the csv files before hand
	'''	
	file_range = re.sub('[^\d]', '', file_name)
	with open(file_name,'r') as csvinput:
		with open(file_name.replace(".csv","")+"_withname.csv", 'w') as csvoutput:
			writer = csv.writer(csvoutput, lineterminator='\n')
			reader = csv.reader(csvinput)
			all = []
			row = next(reader)
			row.append('img_name')
			all.append(row)

			for idx, row in enumerate(reader):
				row.append("UCB{}_{}".format(file_range, idx+1))
				all.append(row)

			writer.writerows(all)

	os.remove(file_name)


if __name__ == '__main__':
	file_names = find_csv_filenames(".")

	for file_name in file_names:
		# create directory for file_name titled file_name.replace(".csv","")
		directory_name = create_directory(file_name.replace(".csv",""))

		# download all images in file_name into the corresponding directory
		download_imgs(file_name, directory_name)

		# move the file_name csv file into its corresponding directory
		os.rename(file_name, "{}/{}".format(directory_name, file_name))


