# -*- coding: utf-8 -*-
"""[application description here]"""

import json
import sys
import csv
import os
reload(sys)
sys.setdefaultencoding('utf-8')

# get all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file_name in files:
	if(".txt" in file_name):

		contacts_file = open(file_name,'r').read()
		contacts_dict = json.loads(contacts_file)

		with open(file_name.split('.')[0]+".csv", 'w') as csvfile:
			fieldnames = ['email', 'first_name', 'last_name', 'phone', 'city', 'state', 'job_title']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

			for company in contacts_dict:
				for contact in contacts_dict[company]:
					writer.writerow({"first_name":contact["name"].split(',')[1][1:],
						"last_name":contact["name"].split(",")[0],
						"email":contact["email"],
						"phone":contact["phone"],
						"job_title":contact["role"],
						"city":contact["location"].split(',')[0],
						"state":contact["location"].split(',')[1].split(' ')[1]})

