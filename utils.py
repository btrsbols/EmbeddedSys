
from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256



def saveInFile(fileName, data):
	"""
	fileName : string, name of the file in which we are going to save data in. 
	(data could be the RSA key)
	"""
	file = open(fileName+".pem", "wb")
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
		return True
	else:
		print("The signature is not authentic!")
		return False
		
"""
## Key creation
		
exportedPrivateKey, exportedPublicKey, key = RSAKeyCreation()
saveInFile("privateKey", exportedPrivateKey)
saveInFile("publicKey", exportedPublicKey)
"""