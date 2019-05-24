import socket 
import sys
import pickle
import time
import utils 


def FetchPublicKey(file):
	return utils.RSAFetchKeyFromFileTxt("e"+str(file)), utils.RSAFetchKeyFromFileTxt("n"+str(file))
	
def RSAVerify(e, n, message, signature):
	"""
	Key: RSA public key
	message: list that contains strings
	signature : signature encoded as a string
	return bool
	"""			
	verifier = pow(signature, e, n)
	if verifier == message:
		print("The signature is authentic.")
		print(message)
		return True
	else:
		#print("The signature is not authentic!")
		return False

def main():
	keyNumb = 1500
	e, n = FetchPublicKey(keyNumb)
	
	
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
			msg = client.recv(1024)
			state, sig = pickle.loads(msg)
			RSAVerify(e, n, int(state), sig)
			
		except KeyboardInterrupt or EOFError  :
			client.close()
			soc.close()
			sys.exit()
		
		
if __name__ == '__main__':	
	
	main()