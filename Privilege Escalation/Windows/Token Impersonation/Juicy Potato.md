# Juicy Potato

### Table of Contents
- [Download](#download)
- [How it works, from a noob's perspective](#how-it-works-from-a-noobs-perspective)
- [Prerequisite Privileges needed](#prerequisite-privileges-needed)
- [Parameters](#parameters)
- [References](#references)

### Download
[Juicy Potato Releases](https://github.com/ohpe/juicy-potato/releases)

### How it works, from a noob's perspective:
1. COM (running as SYSTEM) is told that we want an instance of the BITS (or any COM server) object and we want to load it from 127.0.0.1 (or any ip) on port 6666 (or any port).
2. COM tries to talk to us (with RPC protocol) on port 6666 where a local TCP listener (Man-in-the-Middle) is set up.
3. MitM forwards all received messages to the local Windows RPC listener on TCP port 135, and reads the reply to know which template to follow to appropriately reply to COM.
4. This reply to COM makes it authenticate to the MitM with its Token (SYSTEM) in a series of packet exchanges.
5. This Token is now simply used to spawn a process with SYSTEM.

### Prerequisite Privileges needed
`SeImpersonatePrivilege` or `SeAssignPrimaryToken`

### Parameters
**Get a list of CLSIDs here**: [https://ohpe.it/juicy-potato/CLSID/](https://ohpe.it/juicy-potato/CLSID/)

**Process spawning mode:** Depending on the impersonated user’s privileges you can choose from:
- CreateProcessWithToken (needs `SeImpersonatePrivilege`)
- CreateProcessAsUser (needs `SeAssignPrimaryToken`)
- Automated (checks both)

```
Mandatory args:
-t createprocess call: <t> CreateProcessWithTokenW, <u> CreateProcessAsUser, <*> try both
-p <program>: program or script to launch
-l <port>: define COM listening (MitM) port you prefer (instead of the marshalled hardcoded 6666)

Optional args:
-m <ip>: COM server listen address (MitM) (default 127.0.0.1)
-a <argument>: command line argument to pass to program (default NULL)
-k <ip>: Windows RPC server ip address (default 127.0.0.1)
-n <port>: Windows RPC server listen port (default 135)
-c <{clsid}>: CLSID (default BITS:{4991d34b-80a1-4291-83b6-3328366b9097})
-z only test CLSID and print token's user
```

### References
- [https://foxglovesecurity.com/2016/09/26/rotten-potato-privilege-escalation-from-service-accounts-to-system/](https://foxglovesecurity.com/2016/09/26/rotten-potato-privilege-escalation-from-service-accounts-to-system/)
- [https://ohpe.it/juicy-potato/](https://ohpe.it/juicy-potato/)
