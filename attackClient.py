import socket 
import sys
import pickle
import time
import utils
import math


def FetchPrivateKey(file):
	return utils.RSAFetchKeyFromFileTxt("d"+str(file)), utils.RSAFetchKeyFromFileTxt("n"+str(file))
	
	
	
def main():
	
	dec = 100000
	average_time = 0.2196830608844757
	keyNumb = 1500
	d, n = FetchPrivateKey(keyNumb)
	inc = len(str(n))
	inc = pow(10, inc)
	
	soc = socket.socket()  
	if len(sys.argv) != 3:
		print("You have to put an IP address and a port")
		sys.exit(1)
	else:
		host = sys.argv[1]
		port = int(sys.argv[2])
	
	soc.connect((host, port)) # connect IP address to the port
	
	d = 0
	
	while True:
		time_begin = time.time()
		for i in range(10):
			try:
				time.sleep(.2)
				sig = pow(132, d, n)
				msg = pickle.dumps([132, sig])
				soc.send(msg)
				
			except KeyboardInterrupt:
				soc.close()
				sys.exit(1)
		time_end = time.time()
		elapsed = time_end - time_begin	
		average = elapsed / 10
		print(average)
		if average < average_time:
			d += inc
		elif average > average_time:
			print("-------------------")
			d -= inc
			inc = inc // 10
			print(d)
		else :
			print(d)
			break
		
	
	
if __name__ == '__main__':	
	
	main()