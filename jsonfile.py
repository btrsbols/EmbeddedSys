import json

j = open("test4.json")
dic = json.load(j)
times = []
for i in range(len(dic)):
	times.append(dic[i]["_source"]["layers"]["frame"]["frame.time_delta"])

times.sort()
print(times)
m = 0
for i in range(len(times)):
	m += float(times[i])
	print(m)
	
m = m/len(times)
print(m)