## Host Manager App -- Text Interface

### Table of Contents

* [Introduction](#introduction)
* [Configuring Manager Application Access](#configuring-manager-application-access)
* [List of Commands](#list-of-commands)
  1. [List command](#list-command)
  2. [Add command](#add-command)
  3. [Remove command](#remove-command)
  4. [Start command](#start-command)
  5. [Stop command](#stop-command)
  6. [Persist command](#persist-command)

### Introduction

The **Tomcat Host Manager** application enables you to create,     delete, and otherwise manage virtual hosts within Tomcat. This how-to guide is best accompanied by the following pieces of documentation:

* [Virtual Hosting How-To](virtual-hosting-howto.html) for more      information about virtual hosting.
* [The Host Container](config/host.html) for more information      about the underlying xml configuration of virtual hosts and description      of attributes.

The **Tomcat Host Manager** application is a part of Tomcat installation, by default available using the following    context: `/host-manager`. You can use the host manager in the  following ways:

*   Utilizing the graphical user interface, accessible at: `{server}:{port}/host-manager/html`.
*   Utilizing a set of minimal HTTP requests suitable for scripting.      You can access this mode at: `{server}:{port}/host-manager/text`.

Both ways enable you to add, remove, start, and stop virtual hosts. Changes     may be presisted by using the `persist` command. This document     focuses on the text interface. For further information about the graphical     interface, see [Host Manager App -- HTML Interface](html-host-manager-howto.html).

### Configuring Manager Application Access

The description below uses `$CATALINA_HOME` to refer the    base Tomcat directory. It is the directory in which you installedTomcat, for example `C:\tomcat9`, or `/usr/share/tomcat9`.

The Host Manager application requires a user with one of the following roles:

* `admin-gui` - use this role for the graphical web interface.
* `admin-script` - use this role for the scripting web interface.

To enable access to the text interface of the Host Manager application, either grant your Tomcat user the appropriate role, or create a new one with the correct role. For example, open `${CATALINA_BASE}/conf/tomcat-users.xml` and enter the following:
```
<user username="test" password="chang3m3N#w" roles="admin-script"/>
```
No further settings is needed. When you now access     `{server}:{port}/host-manager/text/${COMMAND}`,you are able to log in with the created credentials. For example:
```
$ curl -u ${USERNAME}:${PASSWORD} http://localhost:8080/host-manager/text/list
OK - Listed hosts
localhost:
```
Note that in case you retrieve your users using the`DataSourceRealm`, `JDBCRealm`, or  `JNDIRealm` mechanism, add the appropriate role in the database     or the directory server respectively.
### List of Commands
The following commands are supported:

* list
* add
* remove
* start
* stop
* persist

In the following subsections, the username and password is assumed to be     **test:test**. For your environment, use credentials created in the previous sections.

#### List command

Use the **list** command to see the available virtual hosts on your Tomcat instance.

***Example command***:
`curl -u test:test http://localhost:8080/host-manager/text/list`

***Example response***:

```
OK - Listed hosts
localhost:
```

#### Add command

Use the **add** command to add a new virtual host. Parameters used for the **add** command:

* String ***name***: Name of the virtual host.**REQUIRED**
* String ***aliases***: Aliases for your virtual host.
* String ***appBase***: Base path for the application that will be      served by this virtual host. Provide relative or absolute path.
* Boolean ***manager***: If true, the Manager app is added to the      virtual host. You can access it with the ***/manager*** context.
* Boolean ***autoDeploy***: If true, Tomcat automatically redeploys      applications placed in the appBase directory.
* Boolean ***deployOnStartup***: If true, Tomcat automatically deploys      applications placed in the appBase directory on startup.
* Boolean ***deployXML***: If true, the ***/META-INF/context.xml***      file is read and used by Tomcat.
* Boolean ***copyXML***: If true, Tomcat copies ***/META-INF/context.xml***      file and uses the original copy regardless of updates to the application's ***/META-INF/context.xml*** file.

***Example command***:

```
curl -u test:test http://localhost:8080/host-manager/text/add?name=www.awesomeserver.com&aliases=awesomeserver.com&appBase/mnt/appDir&deployOnStartup=true
```

***Example response***:

```
add: Adding host [www.awesomeserver.com]
```
#### Remove command

Use the **remove** command to remove a virtual host. Parameters used       for the **remove** command:
* String **name**: Name of the virtual host to be removed.**REQUIRED**

***Example command***:

```
curl -u test:test http://localhost:8080/host-manager/text/remove?name=www.awesomeserver.com
```

***Example response***:

```
remove: Removing host [www.awesomeserver.com]
```

#### Start command

Use the **start** command to start a virtual host. Parameters used  for the **start** command:

* String **name**: Name of the virtual host to be started.**REQUIRED**

***Example command***:

```
curl -u test:test http://localhost:8080/host-manager/text/start?name=www.awesomeserver.com
```

***Example response***:

```
OK - Host www.awesomeserver.com started
```

#### Stop command

Use the **stop** command to stop a virtual host. Parameters used for the **stop** command:

* String **name**: Name of the virtual host to be stopped.**REQUIRED**

***Example command***:

```
curl -u test:test http://localhost:8080/host-manager/text/stop?name=www.awesomeserver.com
```

***Example response***:

```
OK - Host www.awesomeserver.com stopped
```

#### Persist command

Use the **persist** command to persist a virtual host into **server.xml**. Parameters used for the **persist** command:

* String **name**: Name of the virtual host to be persist.**REQUIRED**

This functionality is disabled by default. To enable this option, you must       configure the `StoreConfigLifecycleListener` listener first.      To do so, add the following listener to your ***server.xml***:

```
<Listener className="org.apache.catalina.storeconfig.StoreConfigLifecycleListener"/>
```

***Example command***:

```
curl -u test:test http://localhost:8080/host-manager/text/persist?name=www.awesomeserver.com
```

***Example response***:

```
OK - Configuration persisted
```

***Example manual entry***:
```
<Host appBase="www.awesomeserver.com" name="www.awesomeserver.com" deployXML="false" unpackWARs="false">
</Host>
```

