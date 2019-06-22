
from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256
import random
import math
import sympy
import egcd
import time


def hammingWeight(key):
	"""
	return the Hamming Weight of the key
	"""
	c = 0
	while Key :
		c += 1
		key &= key - 1
	return c

def saveInFileBit(fileName, data):
	"""
	fileName : string, name of the file in which we are going to save data in. 
	(data could be the RSA key)
	"""
	file = open(fileName+".pem", "wb")
	file.write(data)
	file.close()

def saveInFile(fileName, data):
	"""
	fileName : string, name of the file in which we are going to save data in. 
	(data could be the RSA key)
	"""
	file = open(fileName+".pem", "w")
	file.write(data)
	file.close()	
	
	
def RSAKeyCreation(PW = None):
	"""
	PW : String, password for the file, None by default  
	return : exported key protected key ready to be saved, 
	the key it-self(private and public) and the public key  
	and 
	"""
	key = RSA.generate(1024)
	publicKey = key.publickey()
	
	return key.exportKey("PEM", PW), publicKey.exportKey("PEM", PW), key
	
def RSAFetchKeyFromFile(fileName, PW = None):
	"""
	fileName : string, name of the file in which the RSA key is saved
	PW : String, password for the file, None by default  
	return : the key it self(private and public) and the public key
	"""
	file = open(fileName+".pem", "rb")
	key = RSA.importKey(file.read(), PW)
	file.close()
	return key
	
def RSAFetchKeyFromFileTxt(fileName):
	"""
	fileName : string, name of the file in which the RSA key is saved
	PW : String, password for the file, None by default  
	return : the key it self(private and public) and the public key
	"""
	file = open(fileName+".pem", "r")
	key = int(file.read())
	file.close()
	return key	
	
	
	
def RSASign(key, message):
	"""
	Key: RSA private key
	message: list that contains strings
	return signature encoded as a string
	"""	
	h = SHA256.new()
	#message = ''.join(message)
	h.update(message.encode())
	signer = PKCS1_PSS.new(key)
	signature = signer.sign(h)
	return signature
	
def RSAVerify(key, message, signature):
	"""
	Key: RSA public key
	message: list that contains strings
	signature : signature encoded as a string
	return bool
	"""			
	h = SHA256.new()
	#message = ''.join(message)
	h.update(message.encode())
	verifier  = PKCS1_PSS.new(key)
	if verifier.verify(h, signature):
		print("The signature is authentic.")
		print(message)
		return True
	else:
		print("The signature is not authentic!")
		return False
		


# Second implementation
def get_big_prime(length: int):
		p = random.getrandbits(length)
		p = p | 1
		while not sympy.isprime(p):
			p += 2
		return p
def generate_keys(length):
		"""
		Generate RSA keys
		:param length: int, bitlength of RSA keys
		:return: n, e, d
		"""
		p = get_big_prime(length // 2)
		q = get_big_prime(length // 2)

		n = p * q
		phi_n = (p - 1) * (q - 1)

		e = random.randint(2, phi_n - 1)
		while not math.gcd(e, phi_n) == 1:
			e = random.randint(2, phi_n - 1)

		_, x, _ = egcd.egcd(e, phi_n)
		d = x % phi_n

		return n, e, d


def main():	
	
	"""
	## Key creation
			
	exportedPrivateKey, exportedPublicKey, key = RSAKeyCreation()
	saveInFile("privateKey", exportedPrivateKey)
	saveInFile("publicKey", exportedPublicKey)
	"""	
	n, e, d = generate_keys(4096)
	print(n, e, d)
	time.sleep(100000)
	#saveInFile("n1", str(n))
	#saveInFile("e1", str(e))
	#saveInFile("d1", str(d))
	
	#n = RSAFetchKeyFromFileTxt("n1100")
	#e = RSAFetchKeyFromFileTxt("e1100")
	#d = RSAFetchKeyFromFileTxt("d1100")
	#for i in range(10000):
	#	a  = pow(132, d, n)
	#key = RSAFetchKeyFromFile("privateKey")
	#pub = RSAFetchKeyFromFile("publicKey")
	#msg = "132"
	#start = time.time()
	
	#a = RSASign(key, msg)
	#print(a)
	#t = time.time() - start

	 #Measure-Command {start-process python utils.py -Wait}


	"""
	print(a)
	print("******************************")
	print(b)

	RSAVerify(pub, msg, a)
	RSAVerify(pub, msg, b)
	
	10000 132 d
	3018.2578   no sig
	35027.0176  all
	33028.3306  sig + one time all - sig
	1016.5637   one time all
	
	30000 132 d
	.   no sig
	.  all
	33028.3306  sig + one time all - sig
	.   one time all
	
	30000 132 d1 smaller 
	.   no sig
	.  all
	33028.3306  sig + one time all - sig
	.   one time all
	
	"""

	
	
#if __name__ == "__main__":
#	main()