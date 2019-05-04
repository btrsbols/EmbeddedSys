import socket 
import sys
import pickle
import time
import RPi.GPIO as GPIO
import utils

state = [None]
def gasDetected(channel):
	state[0] = "Action is comming"
	print(state[0])

def FetchPrivateKey():
	return utils.RSAFetchKeyFromFile("privateKey")
	
def main():
	state[0] = "stable"
	privateKey = FetchPrivateKey()
	
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
			sig = utils.RSASign(privateKey, state[0])
			msg = pickle.dumps([state[0], sig])
			soc.send(msg)
			time.sleep(2)
			state[0] = "stable"
		except KeyboardInterrupt:
			soc.close()
			GPIO.cleanup()
			sys.exit(1)
		
		
if __name__ == '__main__':	
	
	main()