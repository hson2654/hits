#### lesson learned
- try /?xxx=  as a LFI, no matter what xxx is
- ssh -o "IdentitiesOnly=yes", tells OpenSSH to only use the identity (key) files explicitly specified via the -i flag, might pass repeated auth failures 
