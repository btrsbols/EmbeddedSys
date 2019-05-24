import time
import utils
import pickle
from Crypto.PublicKey import RSA

n = 372617761212548636542793613830924007038242935841378113952445697040083535746423016289832509197203030137686352037882045642718036698809318089783443592471
e = 271033439918587416563130136875815904313632747882015479585151305206731014129512112406876615039726606140096339580817530717886231619834329512171834885033
d = 0

average_time = 0.2196830608844757

while True:
	time_begin = time.time()

	a = pow(132, d, n)

	time_end = time.time()
	elapsed = time_end - time_begin
	inc = 10000000000000000000
	dec = 100000
	if elapsed < average_time:
		d += inc
	elif elapsed > average_time:
		print("whatever")
		inc = inc // dec
		dec = dec // 10
	else :
		print(d)