import socket 
import sys
import pickle
import time
import RPi.GPIO as GPIO
import utils
import math

state = [None]
def gasDetected(channel):
	state[0] = "Action is comming"
	print(state[0])

def FetchPrivateKey(file):
	return utils.RSAFetchKeyFromFileTxt("d"+str(file)), utils.RSAFetchKeyFromFileTxt("n"+str(file))
	
def main():
	state[0] = "stable"
	keyNumb = 1100
	d, n = FetchPrivateKey(keyNumb)
	
	soc = socket.socket()  
	if len(sys.argv) != 3:
		print("You have to put an IP address and a port")
		sys.exit(1)
	else:
		host = sys.argv[1]
		port = int(sys.argv[2])
	
	soc.connect((host, port)) # connect IP address to the port
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	GPIO.add_event_detect(7, GPIO.RISING)
	GPIO.add_event_callback(7, gasDetected)
	while True:
		try:
			time.sleep(.2)
			sig = pow(132, d, n)
			msg = pickle.dumps([132, sig])
			soc.send(msg)
			
			state[0] = "stable"
		except KeyboardInterrupt:
			soc.close()
			GPIO.cleanup()
			sys.exit(1)
		
		
if __name__ == '__main__':	
	
	main()