# Set up Postfix for incoming email
**Source: [https://docs.gitlab.com/ee/administration/reply_by_email_postfix_setup.html](https://docs.gitlab.com/ee/administration/reply_by_email_postfix_setup.html)**

### Table of Contents

-   [Configure your server firewall](#configure-your-server-firewall)
-   [Install packages](#install-packages)
-   [Create user](#create-user)
-   [Test the out-of-the-box setup](#test-the-out-of-the-box-setup)
-   [Configure Postfix to use Maildir-style
    mailboxes](#configure-postfix-to-use-maildir-style-mailboxes)
-   [Install the Courier IMAP server](#install-the-courier-imap-server)
-   [Configure Postfix to receive email from the
    internet](#configure-postfix-to-receive-email-from-the-internet)
-   [Test the final setup](#test-the-final-setup)
-   [Done](#done)

This document will take you through the steps of setting up a basic Postfix mail server with IMAP authentication on Ubuntu, to be used with
[incoming email](incoming_email.html).

The instructions make the assumption that you will be using the email address `incoming@gitlab.example.com`, that is, username `incoming` on host `gitlab.example.com`. Don’t forget to change it to your actual host when executing the example code snippets.

### Configure your server firewal

1.  Open up port 25 on your server so that people can send email into the server over SMTP.
2.  If the mail server is different from the server running GitLab, open up port 143 on your server so that GitLab can read email from the server over IMAP.

### Install packages

1.  Install the `postfix` package if it is not
    installed already:

    ```
    sudo apt-get install postfix
    ```

    When asked about the environment, select ‘Internet Site’. When asked to confirm the hostname, make sure it matches `gitlab.example.com`.

2.  Install the `mailutils` package.

    ```
    sudo apt-get install mailutils
    ```

### Create user

1.  Create a user for incoming email.

    ``` 
    sudo useradd -m -s /bin/bash incoming
    ```

2.  Set a password for this user.

    ``` 
    sudo passwd incoming
    ```

    Be sure not to forget this, you’ll need it later.

### Test the out-of-the-box setup

1.  Connect to the local SMTP server:

    ``` 
    telnet localhost 25
    ```

    You should see a prompt like this:

    ``` 
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    220 gitlab.example.com ESMTP Postfix (Ubuntu)
    ```

    If you get a `Connection refused` error instead, verify that `postfix` is running:

    ``` 
    sudo postfix status
    ```

    If it is not, start it:

    ``` 
    sudo postfix start
    ```

2.  Send the new `incoming` user an email to test SMTP, by entering the following into the SMTP prompt:

    ``` 
    ehlo localhost
    mail from: root@localhost
    rcpt to: incoming@localhost
    data
    Subject: Re: Some issue

    Sounds good!
    .
    quit
    ```

    **NOTE:** The `.` is a literal period on its own line.

    If you receive an error after entering
    `rcpt to: incoming@localhost` then your Postfix `my_network` configuration is not correct. The error will say ‘Temporary lookup failure’. See [Configure Postfix to     receive email from the Internet](#configure-postfix-to-receive-email-from-the-internet).

3.  Check if the `incoming` user received the email:

    ``` 
    su - incoming
    mail
    ```

    You should see output like this:

    ``` 
    "/var/mail/incoming": 1 message 1 unread
    >U   1 root@localhost                           59/2842  Re: Some issue
    ```

    Quit the mail app:

    ``` 
    q
    ```

4.  Sign out of the `incoming` account, and go back to being `root`:

    ``` 
    logout
    ```

### Configure Postfix to use Maildir-style mailboxes

Courier, which we will install later to add IMAP authentication, requires mailboxes to have the Maildir format, rather than mbox.

1.  Configure Postfix to use Maildir-style mailboxes:

    ``` 
    sudo postconf -e "home_mailbox = Maildir/"
    ```

2.  Restart Postfix:

    ``` 
    sudo /etc/init.d/postfix restart
    ```

3.  Test the new setup:

    1.  Follow steps 1 and 2 of *[Test the out-of-the-box setup](#test-the-out-of-the-box-setup)*.
    2.  Check if the `incoming` user received the
        email:

        ``` 
        su - incoming
        MAIL=/home/incoming/Maildir
        mail
        ```

        You should see output like this:

        ``` 
        "/home/incoming/Maildir": 1 message 1 unread
        >U   1 root@localhost                           59/2842  Re: Some issue
        ```

        Quit the mail app:

        ``` 
        q
        ```

    If `mail` returns an error
    `Maildir: Is a directory` then your version of `mail` doesn’t support Maildir style mailboxes. Install `heirloom-mailx` by running `sudo apt-get install  heirloom-mailx`. Then, try the above steps again, substituting `heirloom-mailx` for the `mail` command.

4.  Sign out of the `incoming` account, and go back to being `root`:

    ``` 
    logout
    ```

### Install the Courier IMAP server

1.  Install the `courier-imap` package:

    ``` 
    sudo apt-get install courier-imap
    ```

    And start `imapd`:

    ``` 
    imapd start
    ```

2.  The `courier-authdaemon` isn’t started after installation. Without it, IMAP authentication will fail:

    ``` 
    sudo service courier-authdaemon start
    ```

    You can also configure `courier-authdaemon` to
    start on boot:

    ``` 
    sudo systemctl enable courier-authdaemon
    ```

### Configure Postfix to receive email from the internet

1.  Let Postfix know about the domains that it should consider local:

    ``` 
    sudo postconf -e "mydestination = gitlab.example.com, localhost.localdomain, localhost"
    ```

2.  Let Postfix know about the IPs that it should consider part of the LAN:

    We’ll assume `192.168.1.0/24` is your local LAN.
    You can safely skip this step if you don’t have other machines in
    the same local network.

    ``` 
    sudo postconf -e "mynetworks = 127.0.0.0/8, 192.168.1.0/24"
    ```

3.  Configure Postfix to receive mail on all interfaces, which includes
    the internet:

    ``` 
    sudo postconf -e "inet_interfaces = all"
    ```

4.  Configure Postfix to use the `+` delimiter for sub-addressing:

    ``` 
    sudo postconf -e "recipient_delimiter = +"
    ```

5.  Restart Postfix:

    ``` 
    sudo service postfix restart
    ```

### Test the final setup

1.  Test SMTP under the new setup:

    1.  Connect to the SMTP server:

        ``` 
        telnet gitlab.example.com 25
        ```

        You should see a prompt like this:

        ``` 
        Trying 123.123.123.123...
        Connected to gitlab.example.com.
        Escape character is '^]'.
        220 gitlab.example.com ESMTP Postfix (Ubuntu)
        ```

        If you get a `Connection refused` error
        instead, make sure your firewall is set up to allow inbound traffic on port 25.

    2.  Send the `incoming` user an email to test SMTP, by entering the following into the SMTP prompt:

        ``` 
        ehlo gitlab.example.com
        mail from: root@gitlab.example.com
        rcpt to: incoming@gitlab.example.com
        data
        Subject: Re: Some issue

        Sounds good!
        .
        quit
        ```

        note

        The `.` is a literal period on its own line.

    3.  Check if the `incoming` user received the email:

        ``` 
        su - incoming
        MAIL=/home/incoming/Maildir
        mail
        ```

        You should see output like this:

        ``` 
        "/home/incoming/Maildir": 1 message 1 unread
        >U   1 root@gitlab.example.com                           59/2842  Re: Some issue
        ```

        Quit the mail app:

        ``` 
        q
        ```

    4.  Sign out of the `incoming` account, and go back to being `root`:

        ``` 
        logout
        ```

2.  Test IMAP under the new setup:

    1.  Connect to the IMAP server:

        ``` 
        telnet gitlab.example.com 143
        ```

        You should see a prompt like this:

        ``` 
        Trying 123.123.123.123...
        Connected to mail.gitlab.example.com.
        Escape character is '^]'.
        - OK [CAPABILITY IMAP4rev1 UIDPLUS CHILDREN NAMESPACE THREAD=ORDEREDSUBJECT THREAD=REFERENCES SORT QUOTA IDLE ACL ACL2=UNION] Courier-IMAP ready. Copyright 1998-2011 Double Precision, Inc.  See COPYING for distribution information.
        ```

    2.  Sign in as the `incoming` user to test IMAP, by entering the following into the IMAP prompt:

        ``` 
        a login incoming PASSWORD
        ```

        Replace PASSWORD with the password you set on the
        `incoming` user earlier.

        You should see output like this:

        ``` 
        a OK LOGIN Ok.
        ```

    3.  Disconnect from the IMAP server:

        ``` 
        a logout
        ```

### Done

If all the tests were successful, Postfix is all set up and ready to receive email! Continue with the [incoming email](incoming_email.html) guide to configure GitLab.
