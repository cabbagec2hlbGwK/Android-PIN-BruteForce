import os, sys
import hashlib
import sqlite3
import struct
import binascii


  
name_exists = sys.argv[1]

if name_exists:
    salt=(int(name_exists[0]))
    hexsalt=binascii.hexlify((struct.pack('>q',(int(salt))))) 
else:
    print("does not exist")



try:
    file = open("password.key", "rb")
    sha1=(file.read(40))
    md5=(file.read(32))
except Exception as e:
    print("not able to find the password.key file")


passwordhash = md5.decode().lower()
print("MD5 hash read in from password.key: " + passwordhash)
print("Lockscreen Salt read from settings.db: " + str(salt))

codelength = int(sys.argv[2])

for i in range(10**(codelength)):
       if len(str(i)) < (codelength):
           code = (str(i).zfill(codelength))
       else:
            code = str(i)
       passwordguess = (hashlib.md5(code.encode() + hexsalt).hexdigest())
       if passwordguess == passwordhash:
           print("code found: " + code)
       else:
            continue
           
