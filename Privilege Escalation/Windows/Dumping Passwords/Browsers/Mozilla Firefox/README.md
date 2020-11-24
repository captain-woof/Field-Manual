# Dumping Firefox Creds

These files are required to decrypt the passwords stored by Firefox. **All required files are stored here:**

`%LocalAppData%\Mozilla\Firefox\Profiles\randomString.Default\`

For instance, `C:\Users\jessie\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\`

**Required files:**

  - cert9.db
  - cookies.sqlite
  - key4.db
  - logins.json

Tools: 
  - [LaZagne](https://github.com/AlessandroZ/LaZagne)
  - [FirefoxDecrypt]()  
  Gather these 4 files, then put them all in a **single folder**, then use [FirefoxDecrypt](https://github.com/unode/firefox_decrypt) to get the passwords.

  `python3 firefox_decrypt.py /path/to/the/files`
