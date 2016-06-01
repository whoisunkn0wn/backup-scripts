#!/usr/bin/python
""""
sonicwall.py - Copyright (c) 2013 Will Smith
	     - Modified by whoisunkn0wn 01062016

	Backup Sonicwall Configs to an FTP Server. 

Licensing: MIT style -- Free, open source, and all that good stuff.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.

*** Requirements ***

	* An accessible FTP Server
	* pexcept by Noah (http://www.noah.org/wiki/pexpect)
		
"""

#!/usr/bin/python
#-*- coding: utf-8 -*-

#Import libs and modules
import pexpect, time, csv

#Declare remotehost & FTP credentials
FTP_SERVER = '0.0.0.0'		#FTP Server Address
FTP_USERNAME = 'ftp_usr'		#FTP Username
FTP_PASSWORD = 'ftp_pass'	#FTP Password

#Define list & tuple variables
SONICWALLS = []
BLOCK = ()

#Read row content of in_file - append to list in tuple format
with open("/home/usrnme/Documents/sonicwall_hosts00.csv") as in_file:
	csv_reader = csv.reader(in_file)
	for row in csv_reader:
		SONICWALLS.append(tuple(row))

#Insert list data into tuple pre-formatted from the integer 0: (infinite)
BLOCK = (SONICWALLS[0:])


#Define SSH functions
def connection00(host, username, password, desc, sysname, firmware):

	 sshc = pexpect.spawn('ssh ' + username + '@' + host)
	 sshc.sendline(username)
	 sshc.expect('assword:')
	 sshc.sendline(password)
	 sshc.expect('>')
	 print 'Logged in...'
	 sshc.sendline('export preferences ftp ' + FTP_SERVER + ' ' + FTP_USERNAME + ' ' + FTP_PASSWORD + ' ' + desc + '.exp')	 
	 sshc.sendline('export current-config sonicos ftp ftp://' + FTP_USERNAME +':' + FTP_PASSWORD +'@' +FTP_SERVER + '/' + desc +'.exp')
   	 print 'config dumped & copied...'
	 sshc.expect('>', timeout=120)
	 sshc.sendline('exit')
	 print 'Exiting...'
	 sshc.close()
	 print 'Connection closed...'
	 time.sleep(2)

def connection01(host, username, password, desc, sysname, firmware):

	 sshc = pexpect.spawn('ssh ' + username + '@' + host)
	 sshc.expect('assword:')
	 sshc.sendline(password)
	 sshc.expect('>')
	 print 'Logged in...'
	 sshc.sendline('export preferences ftp ' + FTP_SERVER + ' ' + FTP_USERNAME + ' ' + FTP_PASSWORD + ' ' + desc + '.exp')	 
	 sshc.sendline('export current-config sonicos ftp ftp://' + FTP_USERNAME +':' + FTP_PASSWORD +'@' +FTP_SERVER + '/' + desc +'.exp')
   	 print 'config dumped & copied...'
	 sshc.expect('>', timeout=120)
	 sshc.sendline('exit')
	 print 'Exiting...'
	 sshc.close()
	 print 'Connection closed...'
	 time.sleep(2)

def connection02(host, username, password, desc, sysname, firmware):

	sshc = pexpect.spawn('ssh ' + username + '@' + host)
	sshc.expect('assword:')
	sshc.sendline(password)
	sshc.expect('>')
	print 'Logged in...'
	sshc.sendline('export preferences ftp ' + FTP_SERVER + ' ' + FTP_USERNAME + ' ' + FTP_PASSWORD + ' ' + desc + '.exp')
	sshc.sendline('export current-config sonicos ftp ftp://' + FTP_USERNAME +':' + FTP_PASSWORD +'@' +FTP_SERVER + '/' + desc +'.exp')
	print 'config dumped & copied...'
	sshc.expect('>', timeout=120)
	sshc.sendline('exit')
	print 'Exiting...'
	sshc.close()
	print 'Connection closed...'
	time.sleep(2)

def connection03(host, username, password, desc, sysname, firmware):

	sshc = pexpect.spawn('ssh ' + username + '@' + host)
	sshc.expect('assword:')
	sshc.sendline(password)
	sshc.expect('>')
	print 'Logged in...'
	sshc.sendline('export preferences ftp ' + FTP_SERVER + ' ' + FTP_USERNAME + ' ' + FTP_PASSWORD + ' ' + desc + '.exp')
	sshc.sendline('export current-config sonicos ftp ftp://' + FTP_USERNAME +':' + FTP_PASSWORD +'@' +FTP_SERVER + '/' + desc +'.exp')
	print 'config dumped & copied...'
	sshc.expect('>', timeout=120)
	sshc.sendline('exit')
	print 'Exiting...'
	sshc.close()
	print 'Connection closed...'
	time.sleep(2)


#For every Sonicwall in the tuple at the top of the script, run the backup method.
for i in range(0,len(BLOCK)):
	if "2010" in BLOCK[i][5]:
		print 'backing up ' + BLOCK[i][3]
		connection00(BLOCK[i][0], BLOCK[i][1],BLOCK[i][2],BLOCK[i][3],BLOCK[i][4],BLOCK[i][5])
		print 'backup dumped for ' + BLOCK[i][3]
	elif "2012" in BLOCK[i][5]:
		print 'backing up ' + BLOCK[i][3]
		connection01(BLOCK[i][0], BLOCK[i][1],BLOCK[i][2],BLOCK[i][3],BLOCK[i][4],BLOCK[i][5])
		print 'backup dumped for ' + BLOCK[i][3]
	elif "2015" in BLOCK[i][5]:
		print 'backing up ' + BLOCK[i][3]
		connection02(BLOCK[i][0], BLOCK[i][1],BLOCK[i][2],BLOCK[i][3],BLOCK[i][4],BLOCK[i][5])
		print 'backup dumped for ' + BLOCK[i][3]
	elif "2016" in BLOCK[i][5]:
		print 'backing up ' + BLOCK[i][3]
		connection03(BLOCK[i][0], BLOCK[i][1],BLOCK[i][2],BLOCK[i][3],BLOCK[i][4],BLOCK[i][5])
		print 'backup dumped for ' + BLOCK[i][3]
