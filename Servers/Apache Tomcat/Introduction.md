# Apache Tomcat 9
## Introduction

### Table of Contents

* [Introduction](#introduction)
* [Terminology](#terminology)
* [Directories and Files](#directories-and-files)
* [CATALINA_HOME and CATALINA_BASE](#catalina-home-and-catalina-base)
  1. [Why Use CATALINA_BASE](#why-use-catalina-base)
  2. [Contents of CATALINA_BASE](#contents-of-catalina-base)
  3. [How to Use CATALINA_BASE](#how-to-use-catalina-base)
* [Configuring Tomcat](#configuring-tomcat)
* [Where to Go for Help](#where-to-go-for-help)

### Introduction

For administrators and web developers alike, there are some important bits
of information you should familiarize yourself with before starting out. This
document serves as a brief introduction to some of the concepts and
terminology behind the Tomcat container. As well, where to go when you need
help.

### Terminology

In the course of reading these documents, you will run across a number of
terms; some specific to Tomcat, and others defined by the
[Servlet and JSP specifications](https://wiki.apache.org/tomcat/Specifications).

* **Context** - In a nutshell, a Context is a    web application.

That is it. If you find any more terms we need to add to this section, please
do let us know.

### Directories and Files

These are some of the key tomcat directories:

* **/bin** - Startup, shutdown, and other scripts. The `*.sh` files (for Unix systems) are functional duplicates of    the `*.bat` files (for Windows systems).  Since the Win32    command-line lacks certain functionality, there are some additional    files in here.
* **/conf** - Configuration files and related DTDs.  The most    important file in here is server.xml.  It is the main configuration file    for the container.
* **/logs** - Log files are here by default.
* **/webapps** - This is where your webapps go.

### CATALINA_HOME and CATALINA_BASE

Throughout the documentation, there are references to the two following
    properties:

* **CATALINA_HOME**: Represents the root of your Tomcat        installation, for example `/home/tomcat/apache-tomcat-9.0.10`        or `C:\Program Files\apache-tomcat-9.0.10`.
* **CATALINA_BASE**: Represents the root of a runtime        configuration of a specific Tomcat instance. If you want to have        multiple Tomcat instances on one machine, use the `CATALINA_BASE`        property.

If you set the properties to different locations, the CATALINA_HOME location
    contains static sources, such as `.jar` files, or binary files.
    The CATALINA_BASE location contains configuration files, log files, deployed
    applications, and other runtime requirements.

#### Why Use CATALINA_BASE

By default, CATALINA_HOME and CATALINA_BASE point to the same directory.
      Set CATALINA_BASE manually when you require running multiple Tomcat
      instances on one machine. Doing so provides the following benefits:

1. Easier management of upgrading to a newer version of Tomcat. Because all        instances with single CATALINA_HOME location share one set of `.jar` files and binary files, you can easily upgrade the files to newer version and have the change propagated to all Tomcat instances using the same CATALIA_HOME directory.

2. Avoiding duplication of the same static `.jar` files.

3. The possibility to share certain settings, for example the `setenv` shell        or bat script file (depending on your operating system).

#### Contents of CATALINA_BASE
Before you start using CATALINA_BASE, first consider and create the
      directory tree used by CATALINA_BASE. Note that if you do not create
      all the recommended directories, Tomcat creates the directories
      automatically. If it fails to create the necessary directory, for example
      due to permission issues, Tomcat will either fail to start, or may not
      function correctly.

Consider the following list of directories:

* The `bin` directory with the `setenv.sh`,`setenv.bat`, and `tomcat-juli.jar` files. <i>Recommended:</i> No. <i>Order of lookup:</i> CATALINA_BASE is checked first; fallback is provided to CATALINA_HOME.
* The `lib` directory with further resources to be added on
            classpath. <i>Recommended:</i> Yes, if your application depends on external libraries. <i>Order of lookup:</i> CATALINA_BASE is checked first; CATALINA_HOME is
            loaded second.
* The `logs` directory for instance-specific log files. <i>Recommended:</i> Yes.
* The `webapps` directory for automatically loaded web
            applications. <i>Recommended:</i> Yes, if you want to deploy applications. <i>Order of lookup:</i> CATALINA_BASE only.
* The `work` directory that contains temporary working
            directories for the deployed web applications. <i>Recommended:</i> Yes.
* The `temp` directory used by the JVM for temporary files. <i>Recommended:</i> Yes.

We recommend you not to change the `tomcat-juli.jar` file.
      However, in case you require your own logging implementation, you can
      replace the `tomcat-juli.jar` file in a CATALINA_BASE location
      for the specific Tomcat instance.

We also recommend you copy all configuration files from the
      `CATALINA_HOME/conf` directory into the
      `CATALINA_BASE/conf/` directory. In case a configuration file
      is missing in CATALINA_BASE, there is no fallback to CATALINA_HOME.
      Consequently, this may cause failure.

At minimum, CATALINA_BASE must contain:

* conf/server.xml
* conf/web.xml

That includes the `conf` directory. Otherwise, Tomcat fails
      to start, or fails to function properly.

For advanced configuration information, see the [RUNNING.txt](https://tomcat.apache.org/tomcat-9.0-doc/RUNNING.txt) file.

#### How to Use CATALINA_BASE

The CATALINA_BASE property is an environment variable. You can set it
      before you execute the Tomcat start script, for example:

* On Unix: `CATALINA_BASE=/tmp/tomcat_base1 bin/catalina.sh start`
* On Windows: `CATALINA_BASE=C:\tomcat_base1 bin/catalina.bat start`

### Configuring Tomcat

This section will acquaint you with the basic information used during
the configuration of the container.

All of the information in the configuration files is read at startup,
meaning that any change to the files necessitates a restart of the container.

### Where to Go for Help

While we've done our best to ensure that these documents are clearly
written and easy to understand, we may have missed something.  Provided
below are various web sites and mailing lists in case you get stuck.

Keep in mind that some of the issues and solutions vary between the
major versions of Tomcat.  As you search around the web, there will be
some documentation that is not relevant to Tomcat 9, but
only to earlier versions.

* Current document - most documents will list potential hangups. Be sure    to fully read the relevant documentation as it will save you much time    and effort. There's nothing like scouring the web only to find out that    the answer was right in front of you all along!
* [Tomcat FAQ](https://wiki.apache.org/tomcat/FAQ)
* [Tomcat WIKI](https://wiki.apache.org/tomcat/)
* Tomcat FAQ at [jGuru](http://www.jguru.com/faq/home.jsp?topic=Tomcat)
* Tomcat mailing list archives - numerous sites archive the Tomcat mailing    lists. Since the links change over time, clicking here will search [Google](https://www.google.com/search?q=tomcat+mailing+list+archives).
* The TOMCAT-USER mailing list, which you can subscribe to [here](https://tomcat.apache.org/lists.html). If you don't    get a reply, then there's a good chance that your question was probably    answered in the list archives or one of the FAQs.  Although questions    about web application development in general are sometimes asked and    answered, please focus your questions on Tomcat-specific issues.
* The TOMCAT-DEV mailing list, which you can subscribe to [here](https://tomcat.apache.org/lists.html).  This list is **reserved** for discussions about the development of Tomcat    itself.  Questions about Tomcat configuration, and the problems you run    into while developing and running applications, will normally be more    appropriate on the TOMCAT-USER list instead.

