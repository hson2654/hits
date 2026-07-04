#### Foot hold
only port 22 and 80 are open.
a CMS service running on 80 after dir fuzz, which is vuln to an RCE. But cannot find valid payload, only MSF exploit works. Get www-data shell.

#### lateral move
a config file under .env of service folder, with mysql credential, get hash of user.

#### Privi Escala  
netstat shows port 23 is listening. uncommon. 
telnet --version, and vuln to RCE

#### lesson learned
- try MSF if hpeless with exploit
- caution for some common service which is open uncommon: telnet, 21 etc.
