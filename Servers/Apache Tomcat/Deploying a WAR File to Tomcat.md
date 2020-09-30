# How to Deploy a WAR File to Tomcat
## **1. Overview**

[Apache Tomcat](https://tomcat.apache.org/) is one of the most popular web servers in the Java community. It ships as a **servlet container** capable of serving Web ARchives with the WAR extension.

**It provides a management dashboard** from which you can deploy a new web application, or undeploy an existing one without having to restart the container. This is especially useful in production environments.

In this article, we will do a quick overview of Tomcat and then cover various approaches to deploying a WAR file.

## **2. Tomcat Structure**

Before we begin, we should familiarize ourselves with some terminology and environment variables.
** **2.1. Environment Variables****

If you have worked with Tomcat before, these will be very familiar to you:

_**$CATALINA_HOME**_

This variable points to the directory where our server is installed.

_**$CATALINA_BASE**_

This variable points to the directory of a particular instance of Tomcat, you may have multiple instances installed. If this variable is not set explicitly, then it will be assigned the same value as _$CATALINA_HOME_.

Web applications are deployed under the _$CATALINA_HOME\webapps_ directory.
** **2.2. Terminology****

**Document root**. Refers to the top-level directory of a web application, where all the application resources are located like JSP files, HTML pages, Java classes, and images.

**Context path**. Refers to the location which is relative to the server's address and represents the name of the web application.

For example, if our web application is put under the _$CATALINA_HOME\webapps\myapp_ directory, it will be accessed by the URL _http://localhost/myapp_, and its context path will be <i>/myapp</i>.

**WAR**. Is the extension of a file that packages a web application directory hierarchy in ZIP format and is short for Web Archive. Java web applications are usually packaged as WAR files for deployment. These files can be created on the command line or with an IDE like Eclipse.

After deploying our WAR file, Tomcat unpacks it and stores all project files in the _webapps_ directory in a new directory named after the project.

## **3. Tomcat Setup**

The Tomcat Apache web server is free software that can be [downloaded from their website](https://tomcat.apache.org/). It is required that there is a JDK available on the user's machine and that the _JAVA_HOME_ environment variable is set correctly.
** **3.1. Start Tomcat****

We can start the Tomcat server by simply running the _startup_ script located at _$CATALINA_HOME\bin\startup_. There is a _.bat_ and a _.sh_ in every installation.

Choose the appropriate option depending on whether you are using a Windows or Unix based operating system.
** **3.2. Configure Roles****

During the deployment phase, we'll have some options, one of which is to use Tomcat's management dashboard. To access this dashboard, we must have an admin user configured with the appropriate roles.

To have access to the dashboard the admin user needs the _manager-gui_ role. Later, we will need to deploy a WAR file using Maven, for this, we need the _manager-script_ role too.

Let's make these changes in _$CATALINA_HOME\conf\tomcat-users_:

```xml
<role rolename="manager-gui"/>
<role rolename="manager-script"/>
<user username="admin" password="password" roles="manager-gui, manager-script"/>
```

More details about the different Tomcat roles can be found by following [this official link](https://tomcat.apache.org/tomcat-6.0-doc/manager-howto.html).
** **3.3. Set Directory Permissions****

Finally, ensure that there is read/write permission on the Tomcat installation directory.
** **3.4. Test Installation****

To test that Tomcat is setup properly run the startup script (_startup.bat_/ _startup.sh_), if no errors are displayed on the console we can double-check by visiting _http://localhost:8080_.

If you see the Tomcat landing page, then we have installed the server correctly.
** **3.5. Resolve Port Conflict****

By default, Tomcat is set to listen to connections on port _8080_. If there is another application that is already bound to this port, the startup console will let us know.

To change the port, we can edit the server configuration file _server.xml_ located at _$CATALINA_HOME\conf\server.xml._ By default, the connector configuration is as follows:

```xml
<Connector port="8080" protocol="HTTP/1.1"
  connectionTimeout="20000" redirectPort="8443" />
```

For instance, if we want to change our port to _8081_, then we will have to change the connector's port attribute like so:

```xml
<Connector port="8081" protocol="HTTP/1.1"
  connectionTimeout="20000" redirectPort="8443" />
```

Sometimes, the port we have chosen is not open by default, in this case, we will need to open this port with the appropriate commands in the Unix kernel or creating the appropriate firewall rules in Windows, how this is done is beyond the scope of this article.

## **4. Deploy From Maven**

If we want to use Maven for deploying our web archives, we must configure Tomcat as a server in Maven's _settings.xml_ file.

There are two locations where the _settings.xml_ file may be found:

* The Maven install: _${maven.home}/conf/settings.xml_
* A user's install: _${user.home}/.m2/settings.xml_

Once you have found it add Tomcat as follows:

```xml
<server>
    <id>TomcatServer</id>
    <username>admin</username>
    <password>password</password>
</server>
```

We will now need to create a basic web application from Maven to test the deployment. Let's navigate to where we would like to create the application.

Run this command on the console to create a new Java web application:

```powershell
mvn archetype:generate -DgroupId=com.baeldung -DartifactId=tomcat-war-deployment
  -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```

This will create a complete web application in the directory _tomcat-war-deployment_ which, if we deploy now and access via the browser, prints _hello world!_.

But before we do that we need to make one change to enable Maven deployment. So head over to the _pom.xml_ and add this plugin:

```xml
<plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat7-maven-plugin</artifactId>
    <version>2.2</version>
    <configuration>
        <url>http://localhost:8080/manager/text</url>
        <server>TomcatServer</server>
        <path>/myapp</path>
    </configuration>
</plugin>
```

Note that we are using the Tomcat 7 plugin because it works for both versions 7 and 8 without any special changes.

The configuration _url_ is the url to which we are sending our deployment, Tomcat will know what to do with it. The _server_ element is the name of the server instance that Maven recognizes. Finally, the _path_ element defines the **context path** of our deployment.

This means that if our deployment succeeds, we will access the web application by hitting _http://localhost:8080/myapp_.

Now we can run the following commands from Maven.

To deploy the web app:

```bash
mvn tomcat7:deploy
```

To undeploy it:

```bash
mvn tomcat7:undeploy
```

To redeploy after making changes:

```bash
mvn tomcat7:redeploy
```

## **5. Deploy With Cargo Plugin**

[Cargo](http://cargo.codehaus.org/) is a versatile library that allows us to manipulate the various type of application containers in a standard way.
** **5.1. Cargo Deployment Setup****

In this section, we will look at how to use Cargo's Maven plugin to deploy a WAR to Tomcat, in this case, we will deploy it to a version 7 instance.

To get a firm grip on the whole process, we will start from scratch by creating a new Java web application from the command line:

```bash
mvn archetype:generate -DgroupId=com.baeldung -DartifactId=cargo-deploy
  -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```

This will create a complete Java web application in the _cargo-deploy_ directory. If we build, deploy and load this application as is, it will print _Hello World!_ in the browser.

Unlike the Tomcat7 Maven plugin, the Cargo Maven plugin requires that this file is present.

Since our web application does not contain any servlets, our _web.xml_ file will be very basic. So navigate to the _WEB-INF_ folder of our newly created project and create a _web.xml_ file with the following content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://java.sun.com/xml/ns/javaee"
    xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
      http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
        id="WebApp_ID" version="3.0">

    <display-name>cargo-deploy</display-name>
    <welcome-file-list>
        <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>
</web-app>
```

To enable Maven to recognize Cargo's commands without typing the fully qualified name, we need to add the Cargo Maven plugin to a plugin group in Maven's _settings.xml._

As an immediate child of the root _<settings></settings>_ element, add this:

```xml
<pluginGroups>
    <pluginGroup>org.codehaus.cargo</pluginGroup>
</pluginGroups>
```

** **5.2. Local Deploy****

In this subsection, we will edit our _pom.xml_ to suit our new deployment requirements.

Add the plugin as follows:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.cargo</groupId>
            <artifactId>cargo-maven2-plugin</artifactId>
            <version>1.5.0</version>
            <configuration>
                <container>
                    <containerId>tomcat7x</containerId>
                    <type>installed</type>
                    <home>Insert absolute path to tomcat 7 installation</home>
                </container>
                <configuration>
                    <type>existing</type>
                    <home>Insert absolute path to tomcat 7 installation</home>
                </configuration>
            </configuration>
       </plugin>
    </plugins>
</build>
```

The latest version, at the time of writing, is _1.5.0_. However, the latest version can always be found [here](https://codehaus-cargo.github.io/cargo/Downloads.html).

Notice that we explicitly define the packaging as a WAR, without this, our build will fail. In the plugins section, we then add the cargo maven2 plugin. Additionally, **we add a configuration section where we tell Maven that we are using a Tomcat container and also an existing installation.**

By setting the container type to _installed_, we tell Maven that we have an instance installed on the machine and we provide the absolute URL to this installation.

By setting the configuration type to _existing_, we tell Tomcat that we have an existing setup that we are using and no further configuration is required.

The alternative would be to tell cargo to download and setup the version specified by providing a URL. However, our focus is on WAR deployment.

It's worth noting that whether we are using Maven 2.x or Maven 3.x, the cargo maven2 plugin works for both.

We can now install our application by executing:

```bash
mvn install
```

and deploying it by doing:

```bash
mvn cargo:deploy
```

If all goes well we should be able to run our web application by loading _http://localhost:8080/cargo-deploy._
** **5.3. Remote Deploy****

To do a remote deploy, we only need to change the configuration section of our _pom.xml_. Remote deploy means that we do not have a local installation of Tomcat but have access to the manager dashboard on a remote server.

So let's change the _pom.xml_ so that the configuration section looks like this:

```xml
<configuration>
    <container>
        <containerId>tomcat8x</containerId>
        <type>remote</type>
    </container>
    <configuration>
        <type>runtime</type>
        <properties>
            <cargo.remote.username>admin</cargo.remote.username>
            <cargo.remote.password>admin</cargo.remote.password>
            <cargo.tomcat.manager.url>http://localhost:8080/manager/text
              </cargo.tomcat.manager.url>
        </properties>
    </configuration>
</configuration>
```

This time, we change the container type from _installed_ to _remote_ and the configuration type from _existing_ to _runtime_. Finally, we add authentication and remote URL properties to the configuration.

Ensure that the roles and users are already present in _$CATALINA_HOME/conf/tomcat-users.xml_ just as before.

If you are editing the same project for _remote_ deployment, first un-deploy the existing WAR:

```bash
mvn cargo:undeploy
```

clean the project:

```bash
mvn clean
```

install it:

```bash
mvn install
```

finally, deploy it:

```bash
mvn cargo:deploy
```

That's it.

## **6. Deploy From Eclipse**

Eclipse allows us to embed servers to add web project deployment in the normal workflow without navigating away from the IDE.
** **6.1. Embed Tomcat in Eclipse****

We can embed an installation into eclipse by selecting the _window_ menu item from taskbar and then _preferences_ from the drop down.

We will find a tree grid of preference items on the left panel of the window that appears. We can then navigate to _eclipse -> servers_ or just type _servers_ in the search bar.

We then select the installation directory, if not already open for us, and choose the Tomcat version we downloaded.

On the right-hand-side of the panel, a configuration page will appear where we select the Enable option to activate this server version and browse to the installation folder.

We apply changes, and the next time we open the servers view from Eclipse's _windows -> show view_ submenu, the newly configured server will be present and we can start, stop and deploy applications to it.
** **6.2. Deploy Web Application in Embedded Tomcat****

To deploy a web application to Tomcat, it must exist in our workspace.

Open the _servers_ view from _window -> show view_ and look for servers. When open, we can just right click on the server we configured and select _add deployment_ from the context menu that appears.

From the _New Deployment_ dialog box that appears, open the _project_ drop down and select the web project.

There is a _Deploy Type_ section beneath the _Project_ combo box when we select _Exploded Archive(development mode)_, **our changes in the application will be synced live without having to redeploy**, this is the best option during development as it is very efficient.

Selecting _Packaged Archive(production mode)_ will require us to redeploy every time we make changes and see them in the browser. This is best only for production, but still, Eclipse makes it equally easy.
** **6.3. Deploy Web Application in External Location****

We usually choose to deploy a WAR through Eclipse to make debugging easier. There may come a time when we want it deployed to a location other than those used by Eclipse's embedded servers. The most common instance is where our production server is online, and we want to update the web application.

**We can bypass this procedure by deploying in production mode and noting the _Deploy Location_ in the _New Deployment_ dialog box and picking the WAR from there.**

During deployment, instead of selecting an embedded server, we can select the _<Externally Launched>_ option from the _servers_ view alongside the list of embedded servers. We navigate to the _webapps_ directory of an external Tomcat installation.

## **7. Deploy From IntelliJ IDEA**

To deploy a web application to Tomcat, it must exist and have already been downloaded and installed.
** **7.1. Local Configuration****

Open the _Run_ menu and click the _Edit Configurations_ options.

In the panel on the left search for _Tomcat Server_, if it is not there click the + sign in the menu, search for _Tomcat_ and select _Local_. In the name field put _Tomcat 7/8_ (depending on your version).

Click the _Configure..._ button and in _Tomcat Home_field navigate to the home location of your installation and select it.

Optionally, set the _Startup_ page to be _http://localhost:8080/_and _HTTP port: 8080_, change the port as appropriate.

Go to the _Deployment_ tab and click on the + symbol, select artifact you want to add to the server and click OK

** **7.2. Remote Configuration****

Follow the same instructions as for local Tomcat configurations, but in the server tab, you must enter the remote location of the installation.

## **8. Deploy by Copying Archive**

We have seen how to export a WAR from Eclipse. One of the things we can do is to deploy it by simply dropping it into the _$CATALINA_HOME\webapps_ directory of any Tomcat instance. If the instance is running, the deployment will start instantly as Tomcat unpacks the archive and configures its context path.

If the instance is not running, then the server will deploy the project the next time it is started.

## **9. Deploy From Tomcat Manager**

Assuming we already have our WAR file to hand and would like to deploy it using the management dashboard. You can access the manager dashboard by visiting: _http://localhost:8080/manager_.

The dashboard has five different sections: _Manager_, _Applications_, _Deploy_, _Diagnostics_, and _Server Information._If you go to the _Deploy_ section, you will find two subsections.
** **9.1. Deploy Directory or WAR File Located on Server****

If the WAR file is located on the server where the Tomcat instance is running, then we can fill the required _Context Path_ field preceded by a forward slash "/".

**Let's say we would like our web application to be accessed from the browser with the URL _http://localhost:8080/myapp_, then our context path field will have _/myapp._**

We skip the _XML Configuration file URL_ field and head over to the _WAR or Directory URL_ field. Here we enter the absolute URL to the Web ARchive file as it appears on our server. Let's say our file's location is _C:/apps/myapp.war_, then we enter this location. Don't forget the WAR extension.

After that, we can click _deploy_ button. The page will reload, and we should see the message:

```plaintext
OK - Deployed application at context path /myapp
```

at the top of the page.

Additionally, our application should also appear in the _Applications_ section of the page.
** **9.2. WAR File to Deploy****

Just click the _choose file_ button, navigate to the location of the WAR file and select it, then click the _deploy_ button.

In both situations, if all goes well, the Tomcat console will inform us that the deployment has been successful with a message like the following:

```plaintext
INFO: Deployment of web application archive \path\to\deployed_war has finished in 4,833 ms
```
