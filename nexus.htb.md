j.matthew@nexus.htb

N27xh!!2ucY04


krayin
N27xh!!2ucY04

https://github.com/TREXNEGRO/Security-Advisories/blob/main/CVE-2026-38526/poc.md

use burp s catch the post request of png fine name, and change it into php, the reverse shell will be triggereed. and we will receive the response of the file path, which can be reused to trigger the Rev shell.


www-data@nexus:/$ cat /etc/passwd | grep bash
cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
jones:x:1000:1000:,,,:/home/jones:/bin/bash
git:x:111:112:Git Version Control,,,:/home/git:/bin/bash


/var/www/krayin/.env

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=krayin
DB_USERNAME=krayin
DB_PASSWORD=y27xb3ha!!74GbR
DB_PREFIX=


└─$ ssh jones@nexus.htb 

jones@nexus:~$ id
uid=1000(jones) gid=1000(jones) groups=1000(jones),100(users)


╔══════════╣ System timers
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#timers
══╣ Active timers:
NEXT                            LEFT LAST                              PASSED UNIT                           ACTIVATES
Sun 2026-07-12 16:25:17 UTC      28s Sun 2026-07-12 16:24:17 UTC      31s ago gitea-template-sync.timer      gitea-template-sync.service

jones@nexus:~$ systemctl list-timers
NEXT                            LEFT LAST                             PASSED UNIT                        >
Sun 2026-07-12 16:28:20 UTC       9s Sun 2026-07-12 16:27:20 UTC     50s ago gitea-template-sync.timer   >
Sun 2026-07-12 16:30:00 UTC 1min 48s Sun 2026-07-12 16:20:00 UTC    8min ago sysstat-collect.timer       >
Sun 2026-07-12 16:39:00 UTC    10min Sun 2026-07-12 16:09:00 UTC   19min ago phpsessionclean.timer       >
Sun 2026-07-12 16:42:55 UTC    14min Tue 2026-05-12 11:48:03 UTC           - fstrim.timer                >
Sun 2026-07-12 17:28:33 UTC  1h 0min Tue 2026-05-12 11:52:41 UTC           - motd-news.timer             >
Sun 2026-07-12 17:58:50 UTC 1h 30min Sun 2026-07-12 16:02:50 UTC   25min ago fwupd-refresh.timer         >
Sun 2026-07-12 20:17:22 UTC 3h 49min Sun 2026-07-12 16:17:16 UTC   10min ago apt-daily.timer             >
Sun 2026-07-12 23:43:04 UTC       7h Thu 2026-04-23 18:33:27 UTC           - man-db.timer                >
Mon 2026-07-13 00:00:00 UTC       7h Sun 2026-07-12 15:22:03 UTC 1h 6min ago dpkg-db-backup.timer        >
Mon 2026-07-13 00:00:00 UTC       7h Sun 2026-07-12 15:22:03 UTC 1h 6min ago logrotate.timer             >
Mon 2026-07-13 00:07:00 UTC       7h -                                     - sysstat-summary.timer       >
Mon 2026-07-13 06:59:29 UTC      14h Sun 2026-07-12 15:40:30 UTC   47min ago apt-daily-upgrade.timer     >
Mon 2026-07-13 08:46:55 UTC      16h Mon 2026-03-23 10:50:29 UTC           - update-notifier-motd.timer  >
Mon 2026-07-13 15:26:59 UTC      22h Sun 2026-07-12 15:26:59 UTC 1h 1min ago update-notifier-download.tim>
Mon 2026-07-13 15:37:00 UTC      23h Sun 2026-07-12 15:37:00 UTC   51min ago systemd-tmpfiles-clean.timer>
Sun 2026-07-19 03:10:18 UTC   6 days Sun 2026-07-12 15:22:06 UTC 1h 6min ago e2scrub_all.timer   


cat template-sync.py

def sync_template(repo_info):
    owner = repo_info['owner']['login']
    name = repo_info['name'].lower()
    bare_path = os.path.join(REPO_ROOT, owner, "%s.git" % name)
    stage_path = os.path.join(STAGING_DIR, owner, name)
...

def main():
    log("Template sync starting")

...

    for repo in templates:
        name = repo['full_name']
        log("Syncing template: %s" % name)
        sync_template(repo)
