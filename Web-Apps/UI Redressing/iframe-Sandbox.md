# iframe Sandbox

`<iframe sandbox src=""></iframe>` runs an iframe in a sandboxed container, and prevents framebusting scripts from detecting if the iframe's page is running as the top page or as an iframe. However, using the `sandbox` attribute restricts all functionality, unless explicitly mentioned.

### Attributes

| Value | 	Description   |
| ------|---------------------|
| **(no value)** | 	Applies all restrictions | 
| **allow-forms** | 	Allows form submission | 
| **allow-modals** | 	Allows to open modal windows | 
| **allow-orientation-lock** | 	Allows to lock the screen orientation | 
| **allow-pointer-lock** | 	Allows to use the Pointer Lock API | 
| **allow-popups** | 	Allows popups | 
| **allow-popups-to-escape-sandbox** | Allows popups to open new windows without inheriting the sandboxing | 
| **allow-presentation** | 	Allows to start a presentation session | 
| **allow-same-origin** | 	Allows the iframe content to be treated as being from the same origin | 
| **allow-scripts** | 	Allows to run scripts | 
| **allow-top-navigation** | 	Allows the iframe content to navigate its top-level browsing context | 
| **allow-top-navigation-by-user-activation** | 	Allows the iframe content to navigate its top-level browsing | context, but only if initiated by user | 
