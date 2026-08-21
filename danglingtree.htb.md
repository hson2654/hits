PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-08-21 15:28:27Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Not valid before: 2026-08-03T16:32:53
|_Not valid after:  2106-08-03T16:32:53
443/tcp   open  ssl/https?
| tls-alpn: 
|   h2
|_  http/1.1
| ssl-cert: Subject: commonName=danglingtree-DC-CA
| Not valid before: 2026-03-26T05:34:19
|_Not valid after:  2114-03-26T05:44:18
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Not valid before: 2026-08-03T16:32:53
|_Not valid after:  2106-08-03T16:32:53
|_ssl-date: TLS randomness does not represent time
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Not valid before: 2026-08-03T16:32:53
|_Not valid after:  2106-08-03T16:32:53
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Not valid before: 2026-08-03T16:32:53
|_Not valid after:  2106-08-03T16:32:53
3389/tcp  open  ms-wbt-server
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc.danglingtree.htb
| Not valid before: 2026-03-25T05:48:29
|_Not valid after:  2026-09-24T05:48:29
6600/tcp  open  ssl/mshvlm?
| ssl-cert: Subject: commonName=dc.danglingtree.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc.danglingtree.htb
| Not valid before: 2026-03-26T05:41:20
|_Not valid after:  2027-03-26T05:41:20
|_ssl-date: TLS randomness does not represent time
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 403 Forbidden
|     Connection: close
|     Date: Fri, 21 Aug 2026 15:28:46 GMT
|     Cache-Control: no-store
|     Cache-Control: max-age=0
|     Pragma: no-cache
|     Set-Cookie: .AspNetCore.Antiforgery.7Eyhia2WOxE=CfDJ8HsozULo80ZBsxvkNAKguol3D5mjzD88ST4hs9cGuBV56epeQQjkp34Ftv9H-Th86o-_1KZnGAWyNe1-yR6PHfc297hoMEtxXgO8JX96h3dabOJ07WKrQF_e5A2H0-sujJATFdnQQbV5yi6yKDkaiLE; path=/; secure; samesite=none; Partitioned
|     Set-Cookie: WAC-SESSION=f1b2f918a6a845489f84c37068f2acc1; expires=Sat, 22 Aug 2026 15:28:46 GMT; path=/; secure; samesite=lax; httponly
|     Set-Cookie: WAC-TOKEN=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/
|     Set-Cookie: WAC-AAD=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/
|     Set-Cookie: XSRF-TOKEN=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/
|     Strict-Transport-Security: max-age=5184000; includeSubDomains; preload
|     <!DOCTYPE html>
|     <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
|     <head
|   HTTPOptions: 
|     HTTP/1.1 403 Forbidden
|     Connection: close
|     Date: Fri, 21 Aug 2026 15:28:47 GMT
|     Cache-Control: no-store
|     Cache-Control: max-age=0
|     Pragma: no-cache
|     Set-Cookie: .AspNetCore.Antiforgery.7Eyhia2WOxE=CfDJ8HsozULo80ZBsxvkNAKguolUw6ctl-731_bDl2H86G_SSMpJlqNHRkA7G2EQZwvF9XVeHZJZQ1-xQVD3ebhKVSHufeM_7SwtXGL_rpVvg4YH-hrNzpKrgMaMHdxvnvqyTT4DDFx_StrKqlgp-FYujYI; path=/; secure; samesite=none; Partitioned
|     Set-Cookie: WAC-SESSION=4053f2686d2f4168a20966e26bfaaa95; expires=Sat, 22 Aug 2026 15:28:47 GMT; path=/; secure; samesite=lax; httponly
|     Set-Cookie: WAC-TOKEN=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/
|     Set-Cookie: WAC-AAD=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/
|     Set-Cookie: XSRF-TOKEN=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/
|     Strict-Transport-Security: max-age=5184000; includeSubDomains; preload
|     <!DOCTYPE html>
|     <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
|_    <head
| tls-alpn: 
|   h2
|_  http/1.1
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49675/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49687/tcp open  msrpc         Microsoft Windows RPC
49705/tcp open  msrpc         Microsoft Windows RPC
49719/tcp open  msrpc         Microsoft Windows RPC
49780/tcp open  msrpc         Microsoft Windows RPC


└─$ netexec smb 10.129.31.246 -u guest -p '' --shares
SMB         10.129.31.246   445    DC               [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC) (domain:danglingtree.htb) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.31.246   445    DC               [+] danglingtree.htb\guest: 
SMB         10.129.31.246   445    DC               [*] Enumerated shares
SMB         10.129.31.246   445    DC               Share           Permissions     Remark
SMB         10.129.31.246   445    DC               -----           -----------     ------
SMB         10.129.31.246   445    DC               ADMIN$                          Remote Admin
SMB         10.129.31.246   445    DC               C$                              Default share
SMB         10.129.31.246   445    DC               IPC$            READ            Remote IPC
SMB         10.129.31.246   445    DC               IT              READ            
SMB         10.129.31.246   445    DC               NETLOGON                        Logon server share 
SMB         10.129.31.246   445    DC               SYSVOL                          Logon server share 


└─$ smbclient //10.129.31.246/IT --user=guest --password='' 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Apr  5 09:05:09 2026
  ..                                  D        0  Sun Apr  5 08:57:30 2026
  Security                            D        0  Sun Apr  5 09:05:20 2026

		7062015 blocks of size 4096. 2296757 blocks available
smb: \> cd Security\
smb: \Security\> ls
  .                                   D        0  Sun Apr  5 09:05:20 2026
  ..                                  D        0  Sun Apr  5 09:05:09 2026
  DanglingTree_RoE_Assessment.pdf      A    28905  Sat Apr  4 23:50:23 2026

		7062015 blocks of size 4096. 2293844 blocks available
smb: \Security\> mget DanglingTree_RoE_Assessment.pdf 
Get file DanglingTree_RoE_Assessment.pdf? y
getting file \Security\DanglingTree_RoE_Assessment.pdf of size 28905 as DanglingTree_RoE_Assessment.pdf (58.2 KiloBytes/sec) (average 58.2 KiloBytes/sec)

anderson.w

R3dT3am@Acc3ss#01

└─$ netexec smb 10.129.31.246 -u anderson.w -p 'R3dT3am@Acc3ss#01' --users 
SMB         10.129.31.246   445    DC               [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC) (domain:danglingtree.htb) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.31.246   445    DC               [+] danglingtree.htb\anderson.w:R3dT3am@Acc3ss#01 
SMB         10.129.31.246   445    DC               -Username-                    -Last PW Set-       -BadPW- -Description-
SMB         10.129.31.246   445    DC               anderson.w                    2026-04-05 00:00:40 0       
SMB         10.129.31.246   445    DC               [*] Enumerated 1 local users: DANGLINGTREE

└─$ rpcclient -N danglingtree.htb  -U anderson.w --password='R3dT3am@Acc3ss#01' -c "enumdomusers"
user:[anderson.w] rid:[0xa29]

