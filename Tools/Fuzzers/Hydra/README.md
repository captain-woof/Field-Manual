# Hydra Cheatsheet

#### Syntax
`hydra [options] host_to_attack`

#### Common flags:
- -h: see the help menu
- -l username: Pass single username/login
- -L users.txt: Pass multiple usernames/logins
- -p password: Pass single known password
- -P passwords.tx: Pass a password list or wordlist (ex.: rockyou.txt)
- -s num: Use custom port
- -f: Exit as soon as at least one a login and a password combination is found
- -R: Restore previous session (if crashed/aborted)
- -t: Number of threads

#### SSH
`hydra -f -l user -P passwords.txt <IP> ssh`
OR
`hydra -f -l user -P passwords.txt ssh://<IP>`
#### MySQL
`hydra -f -l user -P passwords.txt <IP> mysql`
#### FTP
`hydra -f -l user -P passwords.txt <IP> ftp`
#### SMB
`hydra -f -l user -P passwords.txt <IP> smb`
#### HTTP POST FORM
**Format:**
`hydra -l user -P passwords.txt <IP> http-post-form "<Login Page Relative URL>:<POST Request Body>:<Error Message Indicator>"`
**Example:**
`hydra -l user -P passwords.txt 10.10.3.6 http-post-form "/login.php:username=^USER^&password=^PASS^:Login Failed"`
#### Windows RDP
`hydra -f -l user -P passwords.txt rdp://<IP>`
