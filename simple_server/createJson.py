import json
import collections
import random
dicObj = collections.defaultdict()

nodes_num = 50
hours = 24

for i in range(nodes_num):
	dicObj["P" + str(i)] = collections.defaultdict()
	for j in range(hours):
		dicObj["P" + str(i)]['t' + str(j)] = collections.defaultdict()
		temp = dicObj["P" + str(i)]['t' + str(j)]
		temp["voltage"] = 100*random.random()
		temp["real power"] = 100*random.random()
		temp["reactive power"] = 100*random.random()
		temp["phases"] = "A" if random.random() > 0.5 else "B"

jsObj = json.dumps(dicObj, indent = 2)
 
fileObject = open('jsonFile.json', 'w')
fileObject.write(jsObj)
fileObject.close()








