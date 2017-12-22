import csv
import json

file_name = "starbucks_owned_locations"
locs = []
with open('{0}.csv'.format(file_name), 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			locs.append(((row['Latitude'], row['Longitude']), row['Address']))


json_str = json.dumps(locs)
f = open("{0}_out.json".format(file_name.split(".")[0]),"w")
f.write(json_str)