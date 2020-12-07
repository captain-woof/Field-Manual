# FTP with Python

- **ftplib library:**
Use `ftplib` library's FTP class to communicate with an FTP server.
`from ftplib import FTP`

- **Connecting:**
  ```
  ftp = FTP('server-ip')

  OR

  ftp = FTP()
  ftp.connect(host='server-ip', port=21, timeout=None, source_address=('source_ip',source_port))
  ```

- **Getting the Welcome message:**
  ```
  ftp.getwelcome()
  ```

- **Logging in**
  ```
  ftp.login(user='username', passwd = 'password')
  ```

- **Directory listing:**
  ```
  files = []
  ftp.dir(files.append)
  print(files)
  ```

- **Print working directory:**
  ```
  print(ftp.cwd())
  ```

- **Change working directory:**
  ```
  ftp.cwd('/whyfix/')
  ```

- **Making a directory:**
  ```
  ftp.mkd('newdir') 
  ```

- **Getting size of a file:**
  ```
  # ftp.sendcmd('TYPE A') for ASCII file
  # ftp.sendcmd('TYPE I') for binary file
  size = ftp.size('debian/README')
  print(size)
  ```

- **Running protocol commands directly:**
  ```
  ftp.sendcmd('command')
  ```

- **Downloading a file:**
  ```
  filename = 'example.txt'
  localfile = open(filename, 'wb' or 'w')

  ftp.retrbinary('RETR ' + filename, localfile.write, 1024) # For binary

  ftp.retrlines('RETR ' + filename, localfile.write)
  ```

- **Uploading a file:**
  ```
  filename = 'example.txt'
  localfile = open(filename, 'rb' or 'r')
  
  ftp.storbinary('STOR ' + filename, localfile) # for binary

  ftp.storlines("STOR " + filename, localfile) # for text files
  ```

- **Deleting a file:**
  ```
  ftp.delete('file_path')
  ```

- **Renaming a file:**
  ```
  ftp.rename('from_name','to_name')
  ```

- **Closing connection:**
  ```
  ftp.quit()
  ```
