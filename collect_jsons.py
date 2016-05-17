import json
import os
from pymatgen.io.cif import CifParser

def add_jsons(directory,j_list):
	for d in os.listdir(directory):
		if os.path.isfile(directory+'/'+d) and 'json' in d and d.split('.')[1] == 'json':
			ext = json.load(open(directory+'/'+d,'r'))
			if type(ext) == list:
				j_list.extend(ext)
			elif type(ext) == dict:
				j_list.append(ext)
			else:
				print('Error, JSON file is of type: ' + str(type(ext)))
 		elif os.path.isdir(d):
			j_list = add_jsons(os.getcwd()+'/'+d,j_list)
	return j_list

j_list  = []
j_list = add_jsons(os.getcwd(),j_list)
for d in j_list:
	cif = d['cif']
	parser=CifParser.from_string(cif)
	struct=parser.get_structures()[0]
	print(struct.formula)
json.dump(j_list,open('all_files.json','w'))
