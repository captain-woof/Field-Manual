# Windows Paths And Ways

### Table of Contents
- [Startup Programs](#startup-programs)
- [Services](#services)
- [AppInit DLLs](#appinit-dlls)

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


- **nssm method**:
  Download nssm from [here](https://nssm.cc/download), and use it.

  Please note that the actual program entered into the services database is nssm itself so you must not move or delete nssm.exe after installing a service. If you do wish to change the path to nssm.exe you can either remove and reinstall the service or edit `HKLM\System\CurrentControlSet\Services\servicename\ImagePath` to reflect the new location.

  **Usage:**
  
  - ***New service:***
    ```
    nssm install <servicename> <program_exe_path> [<arguments>]
    ```
  - ***Delete service***
    ```
    nssm remove <servicename> confirm
    ```
  
  - ***Controlling service***
    ```
    nssm start <servicename>

    nssm stop <servicename>

    nssm restart <servicename>

    nssm status <servicename>

    nssm pause <servicename>

    nssm continue <servicename>

    nssm rotate <servicename>
    ```
  
  - ***Seeing and editing service***
    ```
    nssm get <servicename> <parameter>
    nssm get <servicename> <parameter> <subparameter>

    nssm set <servicename> <parameter> <value>
    nssm set <servicename> <parameter> <subparameter> <value>
    ```

  For more, head [here.](https://nssm.cc/commands)
  
### AppInit DLLs
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows
