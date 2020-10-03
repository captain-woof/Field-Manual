# How it Works

What follows is my way of understanding the working of BooFuzz. I consider myself a novice at stuff, so if any word or any explanation is unpalatable, please go read the [official documentation](https://boofuzz.readthedocs.io/en/stable/).

That being said, if you are new to BooFuzz, read the below sections in sequence, so that you don't feel like you've thrown right into the Vietnam War with a water gun.

## An Imaginary Test-Case

BooFuzz is a network fuzzer. It fuzzes network protocols, specifically, the inputs. In easier words, let's say that according to some RFC, you know that one of the commands you can send via the protocol to the host/program under testing is the "OPEN" command. Let's assume that this program is a server program, and this aforesaid command just takes one argument, the filename on the server, to show it to you. And this server accepts TCP connections.

So, a basic statement might look like this:
`OPEN weirdo.txt`

Now, let's say that you want to test only the filename parameter to see if it's vulnerable to fuzzing. BooFuzz can help you with that.

## Understanding the Test-Runs:
With the test case in mind, now think how some sample runs might look like. You won't fuzz the Command name itself, you'd just fuzz the parameter, yes? Some sample runs might very well be:
```
OPEN aaaaaaaaaaaaaaaaa
OPEN 88888888888888888888888888888888888
OPEN ))..1111111111
...and so on. (BooFuzz handles this for you.)
```

Observe that in each test run, there is a substring that doesn't change (in other words, it is always Static) - 'OPEN'. There is also a substring that always changes - 'filename' parameter. Also, between the two of them is the delimiting character - a blank space.

## How BooFuzz works:
Having understood the test runs, now let's understand how BooFuzz will actually fuzz.

**BooFuzz treats each test-case as a 'node'**. In other words, each 'statement'is a node, and thus, each node is composed multiple substrings. These substrings always occur in a particular order obviously, otherwise, the commands won't work (Unless the RFCs state otherwise). **There is always a root node, from where BooFuzz connects to your given first node.** First, we connect substrings to form a single node. Then, we connect the nodes to each other based on the protocol logic we want.

Imagine that before the 'OPEN' command, you need to authenticate yourself to the server with 'USER' and 'PASS' commands. Below is a sample run (responses are omitted):
```
USER creep
PASS whatthehellamidoinghere
OPEN lyrics.txt
```
So there are 3 nodes. Let's name them 'user', 'pass' and 'open' nodes respectively. Notice that we only need the 3rd node to be fuzzed, all the others are kinda like static macros.

To arrange this test case in a BooFuzz-understandable manner, imagine that there is a root node, the 0th node. BooFuzz steps on it first before looking forward to any other node.

With this root node now, first we connect it to the 1st node - 'user'. To the 'user' node, we connect the 2nd node - 'pass'. To this node, we finally connect the 3rd node - 'open', what we actually want fuzzed. A pictorial representation would be:

*root --> user --> pass --> open (fuzz this node)*

## The BooFuzz way
So, now we know how BooFuzz works, below is how you'd write your python script to fuzz this server program with this test case.
```
# Making the 'user' node
# USER creep
s_initialize("user")
s_static("USER") # This is the first substring, and is static because you're testing this command
s_delim(" ") # This is the 2nd substring
s_static("creep") # This is the third substring, and is static too because the username is fixed.

# Making the 'pass' node
# PASS whatthehellamidoinghere
s_initialize("pass")
s_static("PASS")
s_delim(" ")
s_static("whatthehellamidoinghere") # This is static because the password is fixed for the user, else, you won't authenticate

# Making the 'open' node
# OPEN filenamezzzz
s_initialize("open")
s_static("OPEN")
s_delim(" ")
s_string("AAAA") # Doesn't matter what you give here; BooFuzz will fuzz at this place
```
Before you can make your test cases though, you need to point the root node to the server, yes? Else, where would the fuzzing start in the first place, yes?

BooFuzz represents each test-case with a 'Session' object, that must be initialized first. This Session object requires a target now, represented with a 'Target' object. This Target object requires a Connection to connect to. {Quite a web there!}. So, a basic Session initialization would look like:
```
session = Session(target=Target(connection=TCPSocketConnection("10.0.0.3",4444)))
```
Before proceeding to the next paragraph, please make sure you understood what I showed above. Read the preceding paragraph and try to see how it maps to the python snippet. One thing links to another.

So now, we have the Session set, we have out test cases laid out. Let's start the fuzzing. Wait a minute... Did we link (connect) the nodes to one another? As far as BooFuzz is concerned, sure you have some nodes created, but they are floating in the limbo. None of them is connected to the Session we made. So, let's connect them now. Remember what we discussed about the node connections, that miserable little arrow diagram I drew above? Visualize it while looking at the following snippet:
```
session.connect(s_get("user")) # Connecting 'user' node to root node.
session.connect(s_get('user'),s_get('pass')) # Connecting 'pass' node to 'user'.
session.connect(s_get('pass'),s_get('open')) # Connecting 'open' to 'pass' node
```

Whew! That was quite a lot of connecting, first the sessions, then each string in each node, then each node with one another. The hard part of scripting is over. Now, the final shot:
`session.fuzz()`

This is what the final script would look like:
```
# basic_fuzz.py
from boofuzz import *

ip = '10.0.0.3'
port = 4444

# Initializing the Session
session = Session(target=Target(connection=TCPSocketConnection(ip,port)))

# Initializing each node

# Making the 'user' node
# USER creep
s_initialize("user")
s_static("USER") # This is the first substring, and is static because you're testing this command
s_delim(" ") # This is the 2nd substring
s_static("creep") # This is the third substring, and is static too because the username is fixed.

# Making the 'pass' node
# PASS whatthehellamidoinghere
s_initialize("pass")
s_static("PASS")
s_delim(" ")
s_static("whatthehellamidoinghere") # This is static because the password is fixed for the user, else, you won't authenticate

# Making the 'open' node
# OPEN filenamezzzz
s_initialize("open")
s_static("OPEN")
s_delim(" ")
s_string("AAAA") # Doesn't matter what you give here; BooFuzz will fuzz at this place.

# Connecting the nodes now, in the order that we discussed

session.connect(s_get("user")) # Connecting 'user' node to root node.
session.connect(s_get('user'),s_get('pass')) # Connecting 'pass' node to 'user'.
session.connect(s_get('pass'),s_get('open')) # Connecting 'open' to 'pass' node

# Firing all cylinders
session.fuzz()
```

## But where are the logs saved?
It'd be saved in the 'boofuzz-results' directory inside the current working directory, in .db files. You will see each test run, plus the fuzzed payload that BooFuzz sent.

## Conclusion
Now, with your basic understanding of how BooFuzz works, read the 'Quick Cheatsheet.md' to see more stuff on BooFuzz, something you can always come back and refer to while writing your scripts.
