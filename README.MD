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
