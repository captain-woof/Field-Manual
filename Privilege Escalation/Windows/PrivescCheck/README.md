# PrivescCheck

### Table of contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Features](#features)

### Introduction
[PrivescCheck](https://github.com/itm4n/PrivescCheck) is a script by itm4n that aims to enumerate common Windows security misconfigurations that can be leveraged for privilege escalation. It also gathers various information that might be useful for exploitation and/or post-exploitation.

### Usage
**In all the following command examples, the first . (dot) is important!**

From a command prompt:
```
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

From a PowerShell prompt:
```
PS C:\Temp\> Set-ExecutionPolicy Bypass -Scope process -Force
PS C:\Temp\> . .\PrivescCheck.ps1; Invoke-PrivescCheck
```

### Features
- **All below mentioned checks**
```
Invoke-PrivescCheck - Does all the checks
```

- **Current User**
```
Invoke-UserCheck - Gets the usernane and SID of the current user
Invoke-UserGroupsCheck - Enumerates groups the current user belongs to except default and low-privileged ones
Invoke-UserPrivilegesCheck - Enumerates the high potential privileges of the current user's token
Invoke-UserEnvCheck - Checks for sensitive data in environment variables
```

- **Services**
```
Invoke-InstalledServicesCheck - Enumerates non-default services
Invoke-ServicesPermissionsCheck - Enumerates the services the current user can modify through the service control manager
Invoke-ServicesPermissionsRegistryCheck - Enumerates services that can be modified by the current user in the registry
Invoke-ServicesImagePermissionsCheck - Enumerates all the services that have a modifiable binary (or argument)
Invoke-ServicesUnquotedPathCheck - Enumerates services with an unquoted path that can be exploited
Invoke-DllHijackingCheck - Checks whether any of the system path folders is modifiable
Invoke-HijackableDllsCheck - Lists hijackable DLLs depending on the version of the OS
```

- **Applications**
```
Invoke-InstalledProgramsCheck - Enumerates the applications that are not installed by default
Invoke-ModifiableProgramsCheck - Enumerates applications which have a modifiable EXE of DLL file
Invoke-ProgramDataCheck - Checks for modifiable files and folders under non default ProgramData folders
Invoke-ApplicationsOnStartupCheck - Enumerates the applications which are run on startup
Invoke-ApplicationsOnStartupVulnCheck - Enumerates startup applications that can be modified by the current user
Invoke-RunningProcessCheck - Enumerates the running processes
```

- **Scheduled tasks**
```
Invoke-ScheduledTasksImagePermissionsCheck - Enumerates scheduled tasks with a modifiable path
Invoke-ScheduledTasksUnquotedPathCheck - Enumerates scheduled tasks with an exploitable unquoted path
```

- **Credentials**
```
Invoke-SamBackupFilesCheck - Checks common locations for the SAM/SYSTEM backup files
Invoke-UnattendFilesCheck - Enumerates Unattend files and extracts credentials 
Invoke-WinlogonCheck - Checks credentials stored in the Winlogon registry key
Invoke-CredentialFilesCheck - Lists the Credential files that are stored in the current user AppData folders
Invoke-VaultCredCheck - Enumerates credentials saved in the Credential Manager
Invoke-VaultListCheck - Enumerates web credentials saved in the Credential Manager
Invoke-GPPPasswordCheck - Lists Group Policy Preferences (GPP) containing a non-empty "cpassword" field
Invoke-PowerShellHistoryCheck - Searches for interesting keywords in the PowerShell history of the current user
```

- **Hardening**
```
Invoke-UacCheck - Checks whether UAC (User Access Control) is enabled
Invoke-LapsCheck - Checks whether LAPS (Local Admin Password Solution) is enabled
Invoke-PowershellTranscriptionCheck - Checks whether PowerShell Transcription is configured/enabled
Invoke-LsaProtectionsCheck - Checks whether LSASS is running as a Protected Process (+ additional checks)
Invoke-BitlockerCheck - Checks whether BitLocker is enabled on the system drive
```

- **Configuration**
```
Invoke-RegistryAlwaysInstallElevatedCheck - Checks whether the AlwaysInstallElevated key is set in the registry
Invoke-WsusConfigCheck - Checks whether the WSUS is enabled and vulnerable (Wsuxploit)
Invoke-SccmCacheFolderCheck - Checks whether the ccmcache folder is accessible
```

- **Network**
```
Invoke-TcpEndpointsCheck - Enumerates unusual TCP endpoints on the local machine (IPv4 and IPv6)
Invoke-UdpEndpointsCheck - Enumerates unusual UDP endpoints on the local machine (IPv4 and IPv6)
Invoke-WlanProfilesCheck - Enumerates the saved Wifi profiles and extract the cleartext key/passphrase when applicable
```

- **Updates**
```
Invoke-WindowsUpdateCheck - Checks the last update time of the machine
Invoke-HotfixCheck - Gets a list of installed updates and hotfixes
Invoke-HotfixVulnCheck - Checks whether hotfixes have been installed in the past 31 days
```

- **Misc**
```
Invoke-EndpointProtectionCheck - Gets a list of security software products
Invoke-SystemInfoCheck - Gets the name of the operating system and the full version string
Invoke-LocalAdminGroupCheck - Enumerates the members of the default local admin group
Invoke-UsersHomeFolderCheck - Enumerates the local user home folders
Invoke-MachineRoleCheck - Gets the role of the machine (workstation, server, domain controller)
Invoke-SystemStartupHistoryCheck - Gets a list of system startup events 
Invoke-SystemStartupCheck - Gets the last system startup time
Invoke-SystemDrivesCheck - Gets a list of local drives and network shares that are currently mapped
```
