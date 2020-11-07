# SSH Tunneling

### With ssh

 - Local ssh tunnel
 `ssh -L 4444:google.com:80 IP_OF_SSH_SERVER`
 This binds port 4444 of whatever host you're executing this from, makes it a listener, and routes any data sent to this port (4444) to google.com:80 via the ssh server you mentioned. The ssh server is a middle man in this case. This middle man is the one that resolves google.com and then requests for it, then relays the response back to port 4444 of the other end of the tunnel.
 
 - Remote ssh tunnel
 `ssh -R 4444:google.com:80 IP_OF_SSH_SERVER`
 This binds port 4444 of the host where the ssh server is set up, to google.com:80, where the command-invoking host actually accesses and relays data from google.com to IP_OF_SSH_SERVER:4444
