# /etc/shadow file fields

![/etc/shadow](https://drive.google.com/uc?export=download&id=1Ucm0JGFrzC_SpBonEpVahY0L3FlkjH6v)

1. **Username** : It is your login name.
2. **Password** : It is your encrypted password. The password should be minimum 8-12 characters long including special characters, digits, lower case alphabetic and more. Usually password format is set to $id$salt$hashed, The $id is the algorithm used On GNU/Linux as follows:
	- $1$ is MD5
	- $2a$ is Blowfish
	- $2y$ is Blowfish
	- $5$ is SHA-256
	- $6$ is SHA-512
3. **Last password change (lastchanged)** : Days since Jan 1, 1970 that password was last changed
4. **Minimum**: The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
5. **Maximum** : The maximum number of days the password is valid (after that user is forced to change his/her password)
6. **Warn** : The number of days before password is to expire that user is warned that his/her password must be changed
7. **Inactive** : The number of days after password expires that account is disabled
8. **Expire** : Days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.

The last 6 fields provides password aging and account lockout features. You need to use the chage command to setup password aging. According to man page of shadow – the password field must be filled. The encrypted password consists of 13 to 24 characters from the 64 character alphabet a through z, A through Z, 0 through 9, \. and /. Optionally it can start with a “$” character. This means the encrypted password was generated using another (not DES) algorithm. For example if it starts with “$1$” it means the MD5-based algorithm was used. Please note that a password field which starts with a exclamation mark (!) means that the password is locked. The remaining characters on the line represent the password field before the password was locked.
