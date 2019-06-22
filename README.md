
## Authors: Pierre Lahdo, Yamani Imad Eddine, Aid Ayman,Sheida Sarvestani, Tanvirul Hoque

# NFO-F-410 - EMBEDDED SYSTEMS DESIGN

Timing-attack on RSA signatures (gas detector), ULB


## Usage

Python3 must be installed.  
The following libraries are required:
- time
- socket
- sys
- pickle
- math
- sympy
- egcd
- random
- pyshark
- pycrypto 
- RPi.GPIO

The input arguments types and values are assumed to be correct.
To start server.py you should provide an IP address and a port
To start SimpleClient.py you should provide the same IP address and port as the server. 
To start attackClient.py you should provide the same IP address and port as the server.

example :
 ` python3 server.py 192.168.X.X 8888`

Same hardware must be used (explained in the report)
### Scripts
- server.py contains a server application, it can verify the signatures sent from SimpleClient.py and attackClient.py
- SimpleClient.py can be considered as a normal client application for a microcontroller 
- attackClient.py is used by the attacker to generate private-keys
- i2c.py and adc.py were provided form https://github.com/Seeed-Studio/grove.py/tree/master/grove
