#### foot hold

http://exfiltrated.offsec/panel.aspx
Subrion CMS v4.2.1

cannot find practical exploit file. use msf to get shell

#### Lteral move and Privi Escalate
only find a crontab task 
```
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* *	* * *	root	bash /opt/image-exif.sh
```
it is executed by root.

`ls -la /opt/image-exif.sh`
```
ls -la /opt/image-exif.sh
-rwxr-xr-x 1 root root 437 Jun 10  2021 /opt/image-exif.sh
```

`cat /opt/image-exif.sh`
```
cat /opt/image-exif.sh
#! /bin/bash
#07/06/18 A BASH script to collect EXIF metadata 

echo -ne "\\n metadata directory cleaned! \\n\\n"


IMAGES='/var/www/html/subrion/uploads'

META='/opt/metadata'
FILE=`openssl rand -hex 5`
LOGFILE="$META/$FILE"

echo -ne "\\n Processing EXIF metadata now... \\n\\n"
ls $IMAGES | grep "jpg" | while read filename; 
do 
    exiftool "$IMAGES/$filename" >> $LOGFILE 
done

echo -ne "\\n\\n Processing is finished! \\n\\n\\n"
```
exiftool ran by root.
and CVE-2021-22204  https://github.com/bilkoh/POC-CVE-2021-22204

set reverse shell as payload.
use this exp to generate a jpg file, cp to the dir collected by script. and get root shell, also the user.
