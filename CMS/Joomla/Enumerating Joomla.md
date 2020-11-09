# Enumerating Joomla

**NOTE**: Some of these have been collected from [HackerTarget.com](http://hackertarget.com)

### Enumeration:

- **Version**
  - ***Meta Generator***: Check the HTML source of the page for a meta generator tag in the HEAD section of the HTML source. This is the simplest way to determine if Joomla is being used.
  
    This example is taken from the source of a default Joomla install.

    `<meta name="generator" content="Joomla! - Open Source Content Management" />`
  - ***joomla.xml***: To identify the version we can check the `joomla.xml` file within the directory `/administrator/manifests/files/`

    Example result:
    ![](https://hackertarget.com/wp-content/uploads/2020/07/Joomla-core-version-detection.png)
  - ***en-GB.xml***: Navigate to `/language/en-GB/en-GB.xml`
  - ***Readme.txt***: If the meta tag has been disabled, check for the presence of `/README.txt` from the web root of the install. Joomla has the major version at the top of the ReadMe file. 

- **Check for admin login page**: `https://exampledomain.com/administrator`

-  **Extension and version Enumeration**
    - ***Metasploit***: auxiliary/scanner/http/joomla_plugins
    - ***[JoomScan (OWASP)](https://github.com/rezasp/joomscan)***
    - ***[JoomlaVS](https://github.com/rastating/joomlavs)***
    - ***[HackerTarget's Online Joomla Enum Tool](https://hackertarget.com/joomla-security-scan/)***
    - ***[CMSmap](https://github.com/Dionach/CMSmap)***

