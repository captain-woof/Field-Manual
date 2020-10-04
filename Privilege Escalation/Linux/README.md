# Readme

In this directory, you'll find stuff that may help you get privilege escalation on a linux system. I collect these tricks/quirks/stuff here so that I can refer to it in case I encounter these again. And below, I am writing the list of things to enumerate before jumping straight to some auto-enum script.

## Checklist
- In which groups do I belong, and what's my username?
   ```
   id
   ```

- What am I allowed to run as some other user?
  ```
  sudo -l
  ```
- What is in the home directory?
  ```
  cd ~
  ls -al
  ```
- Which files have SUID bit set?
  ```
  find / -perm /4000 2>/dev/null
  OR
  find / -perm -u=s 2>/dev/null
  ```
- Which files have SGID bit set?
  ```
  find / -perm /2000 2>/dev/null
  OR
  find / -perm -g=s 2>/dev/null
  ```
- Which files are owned by user 'someuser'?
  ```
  find / -user someuser
  ```
- Which files belong to 'someuser' group?
  ```
  find / -group someuser
  ```
- Any backup files?
  ```
  find / -name "*backup*"
  ```
  ```
  find / -name "*bak*"
  ```
- Any files that contain usernames/passwords?
  ```
  cd /
  grep -inHEr -d recurse --colour=auto "password|user|someuser"
  ```
  *Be creative and add interesting substrings*
- What processes are running?
  ```
  ps aux | grep someuser
  ```
- What shared objects (libraries) is a binary using, and can I replace them?
  ```
  ldd name-of-binary
  ```
  *Then check for the permissions*

