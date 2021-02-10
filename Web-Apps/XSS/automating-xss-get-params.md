# Automating XSS For Params in GETs

If params in GET requests are vulnerable to reflective injection and special character injection, those params may be vulnerable to XSS.

Steps to automate:
1. Use `kxss` tool, and pipe newline-separated URLs (with the queries intact) into this tool. It will show all vulnerable pages.
2. Extract only URLs from output and feed it to `dalfox` tool that automatically tests these URLs with dynamically generated payloads.
	**NOTE: `dalfox` requires the URLs to have the params, but not the values**
	**NOTE: Use command `dalfox pipe` to open the tool in piping mode **
	**NOTE: Also, `dalfox` has a `-b` arg that can test for blind XSS, give it your XSS Hunter URL**
