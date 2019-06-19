#!/usr/bin/python3

#########################################################
# lgtraceroute module that performs route-server or 
# looking glass traceroute for provided IP address 
# from route-server.ip.att.net
#########################################################

from __future__ import print_function
import sys
import argparse
import telnetlib

def lgtraceroute(ip, HOST='route-server.ip.att.net', user='rviews', password='rviews', ttl=16):	
	port = 23
	timeout = 10
	command = 'traceroute ttl %s no-resolve %s' %(ttl, ip)
	print("Try: %s" %command)
	try:
		tn = telnetlib.Telnet(HOST, port, timeout)
		#tn.set_debuglevel(100)
		tn.read_until(b"login: ")
		tn.write(user.encode('ascii') + b"\n")
		if password:
			tn.read_until(b"Password:")
			tn.write(password.encode('ascii') + b"\n")

		print(">traceroute %s is running in background -- Please wait" %ip)
		tn.write(command.encode('ascii') + b"\n")
		tn.write(b"exit\n")
		result=tn.read_all().decode('ascii')
		return(result)
		tn.close()
	except OSError as err:
		sys.exit("\nERROR! - Connection Failed: {0}".format(err))
	except EOFError as eoferr:
		sys.exit("\nERROR! - {0}".format(eoferr))

def main():
	parser = argparse.ArgumentParser(description='Script to run traceroute from route-server')
	parser.add_argument("ip", metavar="ip_addr", help="Specify traceroute IP address")
	parser.add_argument("--ttl", metavar="ttl", default=16, help='Specify TTL [Time to Live] value')
	args = parser.parse_args()

	ttl = args.ttl
	ip = args.ip

	try:
		result = lgtraceroute(ip, ttl=ttl)
		print(result)
	except Exception as err:
		print(err)

if __name__ == "__main__":
	main()
