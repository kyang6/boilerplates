import json
import sys
import csv
import os


# get all files in the current directory and remove spaces from the filename
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file_name in files:
	if(".jpg" in file_name):
		os.rename(file_name, file_name.replace(" ", ""))