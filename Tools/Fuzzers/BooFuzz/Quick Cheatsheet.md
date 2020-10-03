# Quick Cheatsheet

### 1. Import BooFuzz
`from boofuzz import *`

### 2. Initialize Session
`Session` needs `Target`, `Target` needs `Connection`.
```
session = Session(target=Target(connection=TCPSocketConnection("127.0.0.1", 8021)))
```
### 3. Create nodes
- #### Initialize node
  `s_initialize(name='name of node')`
  *OR*
  `s_initialize('name of node')`
- #### Mention a fuzzable substring
  `s_string('Any placeholder')`
  *OR*
  `s_string('Any placeholder', name='name')`
- #### Mention a static substring
  `s_static('static string')`
  OR
  `s_static('static string',name='name')`
- #### Mention a delimiter
  `s_delim("DELIM CHAR")`
  *OR*
  `s_delim("DELIM CHAR",name='name')`
- #### Mention a list of substrings from which to choose one
  `s_group(['Substring 1','Substring 2','Substring 3','Substring 4'...])`
  *OR*
  `s_group(['Substring 1','Substring 2','Substring 3','Substring 4'...],name='name')`
### 4. Connect the nodes
```
session.connect(s_get('node1')) # Join 1st node to root node. s_get() gets the node based on its name
session.connect(s_get('node1'),s_get('node2)) # Connect node 1 to node 2
...Keep connecting nodes
```
### 5. Fuzzzz
`session.fuzz()`




