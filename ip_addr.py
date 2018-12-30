import numpy as np
import socket as sock
import ipaddress
from netaddr import *

# input the ip
input_str = '192.23.3.12'

# enter the ip into the ipaddress library to validate and use features
# use two libraries to process- each has useful features
ip1 = IPAddress(input_str)

ip = ipaddress.ip_address(input_str)
print('IP Address :', ip)

# input handling to make sure its a valid IP is built into the library

# convert input ip to bits
ip_binary = ip1.bits()
ip_binary = ip_binary.replace(".", " ")
print ('IP Address Bits:', '\t', ip_binary)

# use first octet to determine class and subnet
oct_arr = input_str.split(".")
first_oct = (int(oct_arr[0]))

# determine class based on first octet of ip
# create new varialble to use for network
# determine addr bytes
# determine host bytes
if (1 <= first_oct <= 127):	#included 127 in classA to mimmick the template. Its the looback
	ip_class = 'A'
	bits = '/8'
	net_ip = IPNetwork(input_str + bits)
	ip_net = ipaddress.ip_interface(input_str + bits)
	addr_byte = 1
	host_byte = 3
elif (128 <= first_oct <= 191):
	ip_class = 'B'
	bits = '/16'
	net_ip = IPNetwork(input_str + bits)
	ip_net = ipaddress.ip_interface(input_str + bits)
	addr_byte = 2
	host_byte = 2
elif (192 <= first_oct <= 223):
	ip_class = 'C'
	bits = '/24'
	net_ip = IPNetwork(input_str + bits)
	ip_net = ipaddress.ip_interface(input_str + bits)
	addr_byte = 3
	host_byte = 1

print ("IP Address Class:", "Class", ip_class, "Subnet Mask:")

# determine subnet based on class
ip_netmask = net_ip.netmask
print ('\t\t\t',ip_netmask)

# convert subnet to bits
net_binary = (ip_netmask.bits())
net_binary = net_binary.replace(".", " ")
print('Subnet Mask Bits:', net_binary)

# print addr bytes
print ("Address Bytes:", '\t\t', addr_byte)

# determine network addr
net_ip = net_ip.network
print ("Network Address:", '\t', str(net_ip) + "" + bits)

# private addr- y / n?
ip_priv = ip1.is_private()
if (ip_priv == True):
	print('\t', "Private Address:", "YES - Class", ip_class)
elif (ip_priv == False):
	print('\t', "Private Address:", "NO - Class", ip_class)	

# print host bytes
print ('\t', "Host Bytes:", '\t', host_byte)

# define variables to determine host addr
parse_ip = input_str.split(".")	 #array of strings that make up ip
count = len(parse_ip) 
selection = host_byte - 2
host_addr_end = []

# loop to determine the number of zeros to add to host addr
# adds a zero for each byte in ip
start = 0
while start != addr_byte:
	start = start + 1
	host_addr_end.append("0")
	if start != addr_byte:
		start = start + 1
		host_addr_end.append("0")
		if start != addr_byte:
			start = start + 1
			host_addr_end.append("0")

# loop to output only the host addr values
# parser-  count backwards from 4 octets in ip. select the number of bytes in host addrress (#) 
for i in parse_ip[-(host_byte):count]:		# ex. list[-2:4]
	host_addr_end.append(i)

print("Host Address:", '\t\t', (".".join(host_addr_end)))

# determine max hosts
ip_max_hosts = (2 ** (8 * host_byte)) - 2
print('\t', "Max Hosts:", '\t', ip_max_hosts)
