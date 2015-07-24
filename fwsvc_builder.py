#!/usr/bin/python

# A minimal script to create firewalld service xml files
# One and only arg should be the location of the csv file
# The csv file should have the following format:
# service description, service name, service port, service protocol[, port, proto]
# The service xml file will be written to '/usr/lib/firewalld/services'

import sys
import firewall.core.io.service as fcisvc

def openFile(infile):
	with open(infile) as in_f:
		for i in in_f.readlines():
			i = i.rstrip('\n')
			i = i.split(',')
			sublst = i[2:]
			tuplst = []
			for indx in range(0, len(sublst), 2):
				tuplst.append((sublst[indx], sublst[indx+1]))
			createService(i[0], i[1], tuplst)

def createService(desc, name, svcpp):
	svc = fcisvc.Service()
	svc.description = desc
	svc.short = name
	svc.name = name
	svc.ports = svcpp
	fcisvc.service_writer(svc, '/usr/lib/firewalld/services')

(scriptname, infile) = sys.argv

def main():
	openFile(infile)

if __name__ == '__main__':
	main()
