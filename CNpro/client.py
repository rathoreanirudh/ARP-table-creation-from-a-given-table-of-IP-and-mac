import socket
import threading
import time

tlock = threading.Lock()
shutdown = False
f=open("maclist.txt","w")
def receiving (name,sock):
	while not shutdown:
		try:
			tlock.acquire()
			while True:
				data,add = sock.recvfrom(1024)
				print str(data)
				#text_file=open("maclist.txt","w")
				f.write(data + "\n")
				#text_file.close()
				
		except:
			pass
		finally:
			tlock.release()
host = '192.168.159.16'
port = 0
server = ('192.168.159.16',5000)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)
rT = threading.Thread(target=receiving,args=('recvFrom',s))
rT.start()


text_file = open("iplist.txt","r")
lines = text_file.readlines()
n = len(lines)
for i in range(0,n):
	print lines[i]
	#ss=[]
	#ss=line.split()
	#print ss[0]
	s.sendto(lines[i],server)
	print "sent"
	time.sleep(0.2)
#alias = raw_input("Name: ")
#message = raw_input(alias + "->")
#while message != '':
#	if message != '':
#		s.sendto(alias+ ": " + message, server)
#	tlock.acquire()
#	message=raw_input(alias + "->")
#	tlock.release()
#	time.sleep(0.2)
f.close()
shutdown = True
rT.join()

s.close()

				
