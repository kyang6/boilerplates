# -*- coding: utf-8 -*-
"""[application description here]"""

import json

file_name = "contacts.json"
contacts_file = open(file_name,'r').read()
contacts_dict = json.loads(contacts_file)


json_str = json.dumps(contacts_dict)
f = open("{0}_out.json".format(file_name.split(".")[0]),"w")
f.write(json_str)


