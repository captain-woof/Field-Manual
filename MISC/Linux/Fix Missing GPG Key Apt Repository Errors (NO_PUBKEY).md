# NO_PUBKEY error and fix

### The error

You might see a missing public GPG key error ("NO_PUBKEY") on Debian, Ubuntu or Linux Mint when running apt update / apt-get update. This can happen when you add a repository, and you forget to add its public key, or maybe there was a temporary key server error when trying to import the GPG key.

Example:

```
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://ppa.launchpad.net/linuxuprising/apps/ubuntu bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY EA8CACC073C3DB2A

W: Failed to fetch http://ppa.launchpad.net/linuxuprising/apps/ubuntu/dists/bionic/InRelease  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY EA8CACC073C3DB2A

W: Some index files failed to download. They have been ignored, or old ones used instead.
```

### Solution 1:

If you're only missing one public GPG repository key, you can run this command on your Ubuntu / Linux Mint / Pop!_OS / Debian system to fix it:

```
sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys THE_MISSING_KEY_HERE
```

You'll have to replace THE_MISSING_KEY_HERE with the missing GPG key. The key is shown in the apt update / apt-get update log, after NO_PUBKEY. For example, in the error message I posted above, the missing GPG key that must be used in this command is EA8CACC073C3DB2A.

### Solution 2:

When you're missing multiple public OpenPGP keys you can use a this one-liner to import all of them in one go:

```
sudo apt update 2>&1 1>/dev/null | sed -ne 's/.*NO_PUBKEY //p' | while read key; do if ! [[ ${keys[*]} =~ "$key" ]]; then sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys "$key"; keys+=("$key"); fi; done
```
