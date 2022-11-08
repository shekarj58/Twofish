# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
import geocoder
from twofish import Twofish
  
print_lock = threading.Lock()

# thread fuction 
def threaded(c): 
    while True: 
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
              
            # lock released on exit 
            print_lock.release() 
            break
  
        # reverse the given string from client 
        #data = data[::-1]
        data = str(data.decode('ascii'))
        if(data == 	'nmrec123'):	
          g = geocoder.ip('me')
          ll1 = (g.latlng)
          latit1 = str(ll1[0])
          longit1 = str(ll1[1])
          for i in range(16-len(latit1)):
            latit1 = latit1 +' ' #Extending the length of latitude to 16 chars, so that it can be provided as input to Twofish tool
          latit2 = latit1.encode('utf-8')
          for i in range(16-len(longit1)):
            longit1 = longit1 +' '
          longit2 = longit1.encode('utf-8')
          str1 = 'nmrec123'
          str2 = str1.encode('utf-8')
          T = Twofish(str2)
          x = T.encrypt(latit2)
          y = T.encrypt(longit2)
          print('GPS Encrypted Latitude is:',x)
          print('GPS Encrypted Longitude is:',y)
          #data1=input("enter secret code of client")
          #if(data1 == 	'nmrec123'):
          print('GPS Latitude is:',T.decrypt(x).decode())
          print('GPS Longitude is:',T.decrypt(y).decode())
          #Both the latitude and longitude are extended to 16-chars and encoded using utf-8, so that they can be
          #provided as inputs to the Two Fish Tool.
          #Note that the secret code for encryption/decryption is:*secret* 
        else:
          print('GPS Details can not be provided as the secret code did not match')		
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = '127.0.0.1' 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1])
        #print(c, addr)        
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 