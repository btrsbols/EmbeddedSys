import socket 
import sys
import pickle
import time
import utils 


def FetchPublicKey():
	return utils.RSAFetchKeyFromFile("publicKey")

def main():
	PublicKey = FetchPublicKey()
	
	
	soc = socket.socket()  
	if len(sys.argv) != 3:
		print("You have to put an IP address and a port")
		sys.exit(1)
	else:
		host = sys.argv[1]
		port = int(sys.argv[2])
	name = socket.gethostname()
	ip = socket.gethostbyname(name)
	print(ip)
	soc.bind((ip, port)) # Bind IP address to the port
	print(socket.gethostname())
	soc.listen(5)
	client, address = soc.accept()     # Establish connection with client.
	print("Connected to ",address)
	while True:
		try:
			msg = client.recv(1000)
			state, sig = pickle.loads(msg)
			utils.RSAVerify(PublicKey, state, sig)
			print(state)
			
		except EOFError or KeyboardInterrupt :
			client.close()
			soc.close()
			sys.exit(1)
		
		
if __name__ == '__main__':	
	
	main()