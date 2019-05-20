import json

j = open("test.json")
dic = json.load(j)
times = []
for i in range(len(dic)):
	times.append(dic[i]["_source"]["layers"]["frame"]["frame.time_delta"])

times.sort()
print(times)
m = 0
for i in range(len(times)-1):
	m += float(times[i+1]) - float(times[i])
	
m = m/len(times)
print(m)