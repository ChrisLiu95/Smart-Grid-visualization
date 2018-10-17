import json
import collections

dicObj = collections.defaultdict()

nodes_num = 10
hours = 24

for i in range(nodes_num):
	dicObj["node " + str(i)] = collections.defaultdict()
	for j in range(hours):
		dicObj["node " + str(i)]['t' + str(j)] = collections.defaultdict()
		temp = dicObj["node " + str(i)]['t' + str(j)]
		temp["voltage"] = 100
		temp["real power"] = 100
		temp["reactive power"] = 100
		temp["phases"] = "A"

jsObj = json.dumps(dicObj, indent = 2)
 
fileObject = open('jsonFile.json', 'w')
fileObject.write(jsObj)
fileObject.close()








