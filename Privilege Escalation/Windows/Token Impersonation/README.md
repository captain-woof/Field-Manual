# Token Impersonation

### Table of contents
- [Introduction](#introduction)
- [FullPowers](#fullpowers)
- [List of exploits](#list-of-exploits)
  - [Local](#local)

### Introduction
> “if you have SeAssignPrimaryToken or SeImpersonate privilege, you are SYSTEM”.
~ @decoder_it

*This is something to keep in mind*

Here, you will find a list of some of the exploits that you can use to elevate to SYSTEM provided that you have the required impersonation privileges. Take a look at this list, find out which exploit will work for you based on the prerequisite criteria, then use it.

In this same folder, you will find the usage instructions of the same exploits, plus the overall working in a nutshell. (I am too noob to understand the full working...yet, so I wrote stuff from my perspective. Sources are included at the bottom of the pages).

### FullPowers
If you popped a service user shell but you do not have the required privileges, use itm4n's [FullPowers](https://github.com/itm4n/FullPowers) to get the missing privileges.

Download from the [FullPowers releases](https://github.com/itm4n/FullPowers/releases).
```
Optional arguments:
  -v              Verbose mode, used for debugging essentially
  -c <CMD>        Custom command line to execute (default is 'C:\Windows\System32\cmd.exe')
  -x              Try to get the extended set of privileges (might fail with NETWORK SERVICE)
  -z              Non-interactive, create a new process and exit (default is 'interact with the new process')
```

### List of exploits:
#### LOCAL:
- **Juicy Potato**
  - Privileges needed: `SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege`
- **Rogue Potato**
  - Privileges needed: `SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege`
- **PrintSpoofer**
  - Privileges needed: `SeImpersonatePrivilege`
- **RogueWinRM**
  - Privileges needed: `SeImpersonatePrivilege`
  - WinRM must be disabled. This is the default on Windows 10 but NOT on Windows Servers.
  - BITS must not be already running. If a background transfer job is in progress, this could take a long time for waiting it to finish (imagine a Windows Update…)
  
