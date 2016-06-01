backup-scripts
==============

Backup Scripts - A collection of useful backup scripts that will backup network infrastructure items starting with:

    * Sonicwall Firewalls
    
Configuration
--------------

### sonicwall.py:

This script can backup any number of sonicwalls on your network to a given FTP server, simply schedule it with
cron. 

The filename for the backup is: 
      
      prefs_[description]_[datetimestamp].exp
      
Where [description] is the description you assign in the appliance declaration, and [datetimetamp] is the
timestamp in the format yyyymmddhhmmss.


#### Defining appliances within your csv target file:

	0.0.0.0,admin,pass,client_gateway,host_name,2016
	1.1.1.1,admin,pass,client_gateway,host_name,2015
	2.2.2.2,admin,pass,client_gateway,host_name,2012
	3.3.3.3,admin,pass,client_gateway,host_name,2010
	
Return down to add new padding when adding a host in to be remotely backed up with ftp/ssh.

      
The tuple items are automatically parsed from the reader + list to the following tuple format as follows:

      ('IP Address','username', 'password', 'host-description', 'System Name')
      
System Name *MUST* match the host name when you log into the system e.g.

      NSA 2400>
      
In the above default NSA 2400 config, the system name *MUST* be NSA 2400 otherwise the backup will fail to run.


#### Defining FTP Server Details:

      FTP_SERVER = '10.xxx.xxx.xxx'   						   #FTP Server Address
      FTP_USERNAME = 'myftpusername'							#FTP Username
      FTP_PASSWORD = 'mystrongpassword'						#FTP Password
      
Simply replace the above strings with your details at the top of the file before running.


#### Prerequisites: 

sonicwall.py requires pexcept by Noah, this can be downloaded from http://www.noah.org/wiki/pexpect

****
      




    
Licensing
----------

All the Above are licensed under the MIT license, please see the license file for details!



