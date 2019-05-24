import socket 
import sys
import pickle
import time
import utils
import math


def FetchPrivateKey(file):
	return utils.RSAFetchKeyFromFileTxt("d"+str(file)), utils.RSAFetchKeyFromFileTxt("n"+str(file))
	
	
	
def main():
	keyNumb = 1500
	d, n = FetchPrivateKey(keyNumb)
	
	
	soc = socket.socket()  
	if len(sys.argv) != 3:
		print("You have to put an IP address and a port")
		sys.exit(1)
	else:
		host = sys.argv[1]
		port = int(sys.argv[2])
	
	soc.connect((host, port)) # connect IP address to the port
	
	while True:
		time_begin = time.time()
		for i in range(500):
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
		average = elapsed / 500
		print(average)
		
	
	
if __name__ == '__main__':	
	
	main()