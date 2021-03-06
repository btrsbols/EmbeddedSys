import socket 
import sys
import pickle
import time
import utils
import math

def FetchPrivateKey(file):
	return utils.RSAFetchKeyFromFileTxt("d"+str(file)), utils.RSAFetchKeyFromFileTxt("n"+str(file))
	
	
	
def main():
	
	average_time = 0.27884094
	keyNumb = 11000     #name of the key
	d, n = FetchPrivateKey(keyNumb)
	inc = len(str(n))-1 # to increment the value of the key
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
	Continue = True
	while Continue:
		time_begin = time.time()
		for i in range(1000):  # average by 1000
			try:
				time.sleep(.2)
				sig = pow(132, d, n)  # 132 is the gas concentration, hard coded
				msg = pickle.dumps([132, sig])
				soc.send(msg)
				
			except KeyboardInterrupt:
				soc.close()
				sys.exit(1)
		time_end = time.time()
		elapsed = time_end - time_begin	
		average = elapsed / 1000
		
		print(average)
		if average < average_time:
			d += inc
			print(d)
		elif average > average_time:
			print("------------------------------------ NEXT")
			inc = inc // 10
			print(d)
		else :
			print("------------------------------------ WTF!!!")
			print(d)
			Continue = False
		
	
	
if __name__ == '__main__':	
	main()