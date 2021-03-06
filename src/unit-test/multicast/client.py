import socket
import struct

multicast_group = '224.3.29.71'
multicast = (multicast_group, 10000)
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('=4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
# Receive/respond loop
while True:
	print 'Waiting to receive message'
	try:
		data, address = sock.recvfrom(1024)
	except socket.timeout:
		print "Closing Receive Socket. Done here."
		sock.close()
		break
	print 'received %s bytes from %s' % (len(data), address)
	print data
	print 'sending acknowledgement to', address
	# sock.sendto('ack', address)
	sock.sendto('ack', multicast)
	sock.settimeout(1)
