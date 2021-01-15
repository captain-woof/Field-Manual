# Windows Paths And Ways

### Table of Contents
- [Startup Programs](#startup-programs)
- [Services](#services)
- [AppInit DLLs](#appinit-dlls)
- [Hosts File](#hosts-file)
- [UAC](#uac)
- [WinLogon](#winlogon)

### Startup Programs
```
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
```

### Services
All services data are stored under:
```
HKLM\SYSTEM\CurrentControlSet\Services\NameOfTheService
```
**Adding a service (ADMIN NEEDED):**
- **Native methods**:
  ```
  sc.exe create <new_service_name> binPath= "<path_to_the_service_executable>"

  New-Service -Name "MyService" -BinaryPathName "C:\Path\to\myservice.exe"
  ```
  *You must have quotation marks around the actual exe path, and a space after the binPath=.*

  Note that it will not work for just any executable: the executable must be a Windows Service (i.e. implement ServiceMain). When registering a non-service executable as a service, you'll get the following error upon trying to start the service:

  ```
  Error 1053: The service did not respond to the start or control request in a timely fashion.
  ``````
  
### AppInit DLLs

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows`

### Hosts File

`C:\windows\system32\drivers\etc\hosts`

### UAC

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`

The value of **EnableLua** is 0x1 for UAC enabled, 0x0 for disabled (REG_DWORD)

### WinLogon

` HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon`

`reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d "Userinit.exe, <PATH_TO_BACKDOOR>" /f`

When a user logs in Userinit.exe will be executed and then our backdoor.
