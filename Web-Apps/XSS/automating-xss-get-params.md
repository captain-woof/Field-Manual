# Automating XSS For Params in GETs

If params in GET requests are vulnerable to reflective injection and special character injection, those params may be vulnerable to XSS.

Steps to automate:
1. Get URLs with parameters with `gau` or `paramspider`

2. Feed these to `dalfox` tool that automatically tests these URLs with dynamically generated payloads.
	**NOTE: Use command `dalfox pipe` to open the tool in piping mode **
	**NOTE: Also, `dalfox` has a `-b` arg that can test for blind XSS, give it your XSS Hunter URL**
	
3. If something works, use `XSStrike` to improve impact of the XSS.
