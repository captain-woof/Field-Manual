# RogueWinRM

### Table of Contents
- [Download](#download)
- [How it works](#how-it-works)
- [Prerequisite Privileges needed](#prerequisite-privileges-needed)
- [Parameters](#parameters)
- [References](#references)

### Download
[RogueWinRM Releases](https://github.com/antonioCoco/RogueWinRM/releases)

### How it works:
Briefly, it will listen for incoming connection on port 5985 faking a real WinRM service.

It's just a minimal webserver that will try to negotiate an NTLM authentication with any service that are trying to connect on that port.

Then the BITS service (running as Local System) is triggered and it will try to authenticate to our rogue listener. Once authenticated to our rogue listener, we are able to impersonate the Local System user spawning an arbitrary process with those privileges.

### Prerequisite Privileges needed
`SeImpersonatePrivilege`

### Parameters
**Note:** Bits normally shouts to port 5985, but it has been noticed that on some versions it shouts to port 47001 (WinRM service with no listener configured)
```
Mandatory args:
-p <program>: program to launch

Optional args:
-a "<argument>": command line argument to pass to program (default NULL)
-l <port>: listening port (default 5985 WinRM)
-d : Enable Debugging output
```

### References
- [https://github.com/antonioCoco/RogueWinRM](https://github.com/antonioCoco/RogueWinRM)
