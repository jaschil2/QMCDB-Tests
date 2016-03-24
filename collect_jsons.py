import json
import os


def add_jsons(directory,j_list):
	for d in os.listdir(directory):
		if os.path.isfile(directory+'/'+d) and 'json' in d and d.split('.')[1] == 'json':
			j_list.append(json.load(open(directory+'/'+d,'r')))
		elif os.path.isdir(d):
			j_list = add_jsons(os.getcwd()+'/'+d,j_list)
	return j_list

j_list  = []
j_list = add_jsons(os.getcwd(),j_list)
json.dump(j_list,open('all_files.json','w'))
