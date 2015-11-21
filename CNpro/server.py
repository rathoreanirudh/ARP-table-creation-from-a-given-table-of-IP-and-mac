import socket
import time
#put address
host = '192.168.159.16'
port = 5000

clients=[]

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host,port))
s.setblocking(0)

quitting = False
print 'Server Started'

while not quitting:
	try:
		data,addr=s.recvfrom(1024)
		#print data
		if "Quit" in str(data):
			quitting =True
		if addr not in clients:
			clients.append(addr)
		text_file = open("read_it.txt","r")
		lines = text_file.readlines()
		cc=0
		for line in lines:
			#print line
			ss=[]
			ss=line.split()
			xx= data.strip()
			n=len(xx)
			yy= str(ss[0])
			m=len(yy)
			for i in range(0,n):
				print xx[i],
			print " "
			for i in range(0,m):
				print yy[i],
			print " "
			print n,m
			print xx,yy
			#print yy,str(ss[1]),str(data),len(str(data)),len(yy),( str(data) == yy )
			if xx == yy :
				cc = 1
				y=ss[1]
				print "y->   " + str(y)
			print "cc->",cc
			if cc == 0:
				y="404 NOT FOUND"
		print time.ctime(time.time()) + str(addr) + ": :"+ str(data)+ " -> "+ str(y)
		
		for client in clients:
			s.sendto(str(xx+' '+str(y)), client)
	except:
		pass
s.close()

