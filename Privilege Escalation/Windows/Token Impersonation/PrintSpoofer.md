# PrintSpoofer

### Table of Contents
- [Download](#download)
- [How it works, from a noob's perspective](#how-it-works-from-a-noobs-perspective)
- [Prerequisite Privileges needed](#prerequisite-privileges-needed)
- [Parameters](#parameters)
- [References](#references)

### Download
[PrintSpoofer Releases](https://github.com/itm4n/PrintSpoofer/releases)

### How it works, from a noob's perspective:
1. A named Pipe is created, which listens for connections. The name of this Pipe is the same as the one used by Print Spooler service - `\\hostname\pipe\spoolss`. This pipe already exists, but through a flaw in the name validation check, 'this same pipe can be made again by using a different name that resolves back to the correct name', thus allowing us to impersonate the actual named Pipe.
2. The Print Spooler service is then passed a single RPC call that coerces SYSTEM to authenticate to the spoofed, named pipe.
3. Since the spoofed named pipe is controlled, we get the impersonation token for SYSTEM. This token is then used to spawn a SYSTEM shell.

### Prerequisite Privileges needed
`SeImpersonatePrivilege`

### Parameters
```
Arguments:
  -c <CMD>    Execute the command *CMD*
  -i          Interact with the new process in the current command prompt (default is non-interactive)
  -d <ID>     Spawn a new process on the desktop corresponding to this session *ID* (check your ID with qwinsta)
  -h          That's me :)
```

### References
- [https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/](https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/)
- [https://github.com/itm4n/PrintSpoofer](https://github.com/itm4n/PrintSpoofer)
