[Andrea Fortuna](https://www.andreafortuna.org/ "Andrea Fortuna") 
 Just some random thoughts about the Meaning of Life, The Universe, and Everything
==================================================================================

-   [Home](https://www.andreafortuna.org/)
-   [About](https://www.andreafortuna.org/about/)
-   [Cybersecurity](https://www.andreafortuna.org/category/cybersecurity/)
-   [Music](https://www.andreafortuna.org/category/lifestyle/music/)
-   [Technology](https://www.andreafortuna.org/category/technology/)
-   [TLDR](https://www.andreafortuna.org/category/tldr/)
-   [Weekly RoundUp](https://www.andreafortuna.org/category/weekly-roundup/)

May 8, 2019

Whether you’re a novice user or a system administrator, iptables is a mandatory knowledge!

**iptables**is the userspace command line program used to configure the Linux 2.4.x and later packet filtering ruleset.
When a connection tries to establish itself on your system, iptables looks for a rule in its list to match it to.
If it doesn’t find one, it resorts to the default action.

### How it works

iptables uses three different chains to allow or block traffic: **input**, **output**and **forward**

-   **Input**– This chain is used to control the behavior for incoming connections.
-   **Output**– This chain is used for outgoing connections.
-   **Forward** – This chain is used for incoming connections that aren’t actually being delivered locally like routing and NATing.

### Let’s start to configure rules

By default all chains are configured to the accept rule, so during the hardening process the suggestion is to start with a deny all configuration and then open only needed ports:

``` {.wp-block-code}
iptables --policy INPUT DROP
iptables --policy OUTPUT DROP
iptables --policy FORWARD DROP
```

* * * * *

### Display rules

#### Verbose print out **all active iptables rules**

``` {.wp-block-code}
# iptables -n -L -v
```

…same output with line numbers:

``` {.wp-block-code}
# iptables -n -L -v --line-numbers
```

Finally, same data output but related to INPUT/OUTPUT chains:

``` {.wp-block-code}
# iptables -L INPUT -n -viptables -L OUTPUT -n -v --line-numbers
```

#### **List Rules as for a specific chain**

``` {.wp-block-code}
# iptables -L INPUT
```

same data with rules specifications:

``` {.wp-block-code}
# iptables -S INPUT
```

rules list with packet count

``` {.wp-block-code}
# iptables -L INPUT -v
```

* * * * *

### Delete/Insert rules

#### **Delete Rule by Chain and Number**

``` {.wp-block-code}
# iptables -D INPUT 10
```

#### **Delete Rule by Specification**

``` {.wp-block-code}
# iptables -D INPUT -m conntrack --ctstate INVALID -j DROP
```

#### **Flush All Rules, Delete All Chains, and Accept All**

``` {.wp-block-code}
# iptables -P INPUT ACCEPT
# iptables -P FORWARD ACCEPT
# iptables -P OUTPUT ACCEPT
# iptables -t nat -F
# iptables -t mangle -F
# iptables -F
# iptables -X
```

#### **Flush All Chains**

``` {.wp-block-code}
# iptables -F
```

#### **Flush a Single Chain**

``` {.wp-block-code}
# iptables -F INPUT
```

#### **Insert Rule**

``` {.wp-block-code}
# iptables -I INPUT 2 -s 202.54.1.2 -j DROP
```

* * * * *

Rules examples
--------------

#### **Allow Loopback Connections**

``` {.wp-block-code}
# iptables -A INPUT -i lo -j ACCEPTiptables -A OUTPUT -o lo -j ACCEPT
```

#### **Allow Established and Related Incoming Connections**

``` {.wp-block-code}
# iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

#### **Allow Established Outgoing Connections**

``` {.wp-block-code}
# iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Internal to External**

``` {.wp-block-code}
# iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
```

#### **Drop Invalid Packets**

``` {.wp-block-code}
# iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
```

#### **Block an IP Address**

``` {.wp-block-code}
# iptables -A INPUT -s 192.168.1.10 -j DROP
```

#### **Block and IP Address and Reject**

``` {.wp-block-code}
# iptables -A INPUT -s 192.168.1.10 -j REJECT
```

#### **Block Connections to a Network Interface**

``` {.wp-block-code}
# iptables -A INPUT -i eth0 -s 192.168.1.10 -j DROP
```

#### **Allow All Incoming SSH**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow Incoming SSH from Specific IP address or subnet**

``` {.wp-block-code}
# iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow Outgoing SSH**

``` {.wp-block-code}
# iptables -A OUTPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A INPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow Incoming Rsync from Specific IP Address or Subnet**

``` {.wp-block-code}
# iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 873 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 873 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow Incoming HTTP**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow Incoming HTTPS**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 443 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow Incoming HTTP and HTTPS**

``` {.wp-block-code}
# iptables -A INPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow MySQL from Specific IP Address or Subnet**

``` {.wp-block-code}
# iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 3306 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 3306 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow MySQL to Specific Network Interface**

``` {.wp-block-code}
# iptables -A INPUT -i eth1 -p tcp --dport 3306 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -o eth1 -p tcp --sport 3306 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow PostgreSQL from Specific IP Address or Subnet**

``` {.wp-block-code}
# iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 5432 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 5432 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow PostgreSQL to Specific Network Interface**

``` {.wp-block-code}
# iptables -A INPUT -i eth1 -p tcp --dport 5432 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -o eth1 -p tcp --sport 5432 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Block Outgoing SMTP Mail**

``` {.wp-block-code}
# iptables -A OUTPUT -p tcp --dport 25 -j REJECT
```

#### **Allow All Incoming SMTP**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 25 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 25 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow All Incoming IMAP**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 143 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 143 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow All Incoming IMAPS**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 993 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 993 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow All Incoming POP3**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 110 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 110 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Allow All Incoming POP3S**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport 995 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -A OUTPUT -p tcp --sport 995 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

#### **Drop Private Network Address On Public Interface**

``` {.wp-block-code}
# iptables -A INPUT -i eth1 -s 192.168.1.0/24 -j DROP
# iptables -A INPUT -i eth1 -s 10.0.0.0/8 -j DROP
```

#### **Drop All Outgoing to Facebook Networks**
Get Facebook AS:

``` {.wp-block-code}
# whois -h v4.whois.cymru.com " -v $(host facebook.com | grep "has address" | cut -d " " -f4)" | tail -n1 | awk '{print $1}'
```

Drop:

``` {.wp-block-code}
# for i in $(whois -h whois.radb.net -- '-i origin AS1273' | grep "^route:" | cut -d ":" -f2 | sed -e 's/^[ \t]*//' | sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | cut -d ":" -f2 | sed 's/$/;/') ; do  iptables -A OUTPUT -s "$i" -j REJECTdone
```

#### **Log and Drop Packets**

``` {.wp-block-code}
# iptables -A INPUT -i eth1 -s 10.0.0.0/8 -j LOG --log-prefix "IP_SPOOF A: "
# iptables -A INPUT -i eth1 -s 10.0.0.0/8 -j DROP
```

By default everything is logged to `/var/log/messages` file:

``` {.wp-block-code}
# tail -f /var/log/messagesgrep --color 'IP SPOOF' /var/log/messages
```

#### **Log and Drop Packets with Limited Number of Log Entries**

``` {.wp-block-code}
# iptables -A INPUT -i eth1 -s 10.0.0.0/8 -m limit --limit 5/m --limit-burst 7 -j LOG --log-prefix "IP_SPOOF A: "
# iptables -A INPUT -i eth1 -s 10.0.0.0/8 -j DROP
```

#### **Drop or Accept Traffic From Mac Address**

``` {.wp-block-code}
# iptables -A INPUT -m mac --mac-source 00:0F:EA:91:04:08 -j DROP
# iptables -A INPUT -p tcp --destination-port 22 -m mac --mac-source 00:0F:EA:91:04:07 -j ACCEPT
```

#### **Block or Allow ICMP Ping Request**

``` {.wp-block-code}
# iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
# iptables -A INPUT -i eth1 -p icmp --icmp-type echo-request -j DROP
```

#### **Specifying Multiple Ports with `multiport`**

``` {.wp-block-code}
# iptables -A INPUT -i eth0 -p tcp -m state --state NEW -m multiport --dports ssh,smtp,http,https -j ACCEPT
```

#### **Load Balancing with `random*` or `nth*`**

``` {.wp-block-code}
_ips=("172.31.250.10" "172.31.250.11" "172.31.250.12" "172.31.250.13")for ip in "${_ips[@]}" ; do  iptables -A PREROUTING -i eth0 -p tcp --dport 80 -m state --state NEW -m nth --counter 0 --every 4 --packet 0 \    -j DNAT --to-destination ${ip}:80done
```

or

``` {.wp-block-code}
_ips=("172.31.250.10" "172.31.250.11" "172.31.250.12" "172.31.250.13")for ip in "${_ips[@]}" ; do  iptables -A PREROUTING -i eth0 -p tcp --dport 80 -m state --state NEW -m random --average 25 \    -j DNAT --to-destination ${ip}:80done
```

#### **Restricting the Number of Connections with `limit` and `iplimit*`**

``` {.wp-block-code}
# iptables -A FORWARD -m state --state NEW -p tcp -m multiport --dport http,https -o eth0 -i eth1 -m limit --limit 20/hour --limit-burst 5 -j ACCEPT
```

or

``` {.wp-block-code}
# iptables -A INPUT -p tcp -m state --state NEW --dport http -m iplimit --iplimit-above 5 -j DROP
```

#### **Maintaining a List of recent Connections to Match Against**

``` {.wp-block-code}
# iptables -A FORWARD -m recent --name portscan --rcheck --seconds 100 -j DROPiptables -A FORWARD -p tcp -i eth0 --dport 443 -m recent --name portscan --set -j DROP
```

#### **Matching Against a `string*` in a Packet’s Data Payload**

``` {.wp-block-code}
# iptables -A FORWARD -m string --string '.com' -j DROP
# iptables -A FORWARD -m string --string '.exe' -j DROP
```

#### **Time-based Rules with `time*`**

``` {.wp-block-code}
# iptables -A FORWARD -p tcp -m multiport --dport http,https -o eth0 -i eth1 -m time --timestart 21:30 --timestop 22:30 --days Mon,Tue,Wed,Thu,Fri -j ACCEPT
```

#### **Packet Matching Based on TTL Values**

``` {.wp-block-code}
# iptables -A INPUT -s 1.2.3.4 -m ttl --ttl-lt 40 -j REJECT
```

#### **Protection against port scanning**

``` {.wp-block-code}
# iptables -N port-scanningiptables -A port-scanning -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s --limit-burst 2 -j RETURNiptables -A port-scanning -j DROP
```

#### **SSH brute-force protection**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --setiptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 10 -j DROP
```

#### **Syn-flood protection**

``` {.wp-block-code}
# iptables -N syn_floodiptables -A INPUT -p tcp --syn -j syn_floodiptables -A syn_flood -m limit --limit 1/s --limit-burst 3 -j RETURN
# iptables -A syn_flood -j DROPiptables -A INPUT -p icmp -m limit --limit  1/s --limit-burst 1 -j ACCEPT
# iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 1 -j LOG --log-prefix PING-DROP:
# iptables -A INPUT -p icmp -j DROPiptables -A OUTPUT -p icmp -j ACCEPT
```

#### **Mitigating SYN Floods With SYNPROXY**

``` {.wp-block-code}
# iptables -t raw -A PREROUTING -p tcp -m tcp --syn -j CT --notrack
# iptables -A INPUT -p tcp -m tcp -m conntrack --ctstate INVALID,UNTRACKED -j SYNPROXY --sack-perm --timestamp --wscale 7 --mss 1460
# iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
```

#### **Block New Packets That Are Not SYN**

``` {.wp-block-code}
# iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
```

or

``` {.wp-block-code}
# iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP
```

#### **Force Fragments packets check**

``` {.wp-block-code}
# iptables -A INPUT -f -j DROP
```

#### **XMAS packets**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
```

#### **Drop all NULL packets**

``` {.wp-block-code}
# iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
```

#### **Block Uncommon MSS Values**

``` {.wp-block-code}
# iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP
```

#### **Block Packets With Bogus TCP Flags**

``` {.wp-block-code}
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,FIN FIN -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL ALL -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL FIN,PSH,URG -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,FIN,PSH,URG -j DROP
# iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP
```

#### **Block Packets From Private Subnets (Spoofing)**

``` {.wp-block-code}
_subnets=("224.0.0.0/3" "169.254.0.0/16" "172.16.0.0/12" "192.0.2.0/24" "192.168.0.0/16" "10.0.0.0/8" "0.0.0.0/8" "240.0.0.0/5")for _sub in "${_subnets[@]}" ; do  iptables -t mangle -A PREROUTING -s "$_sub" -j DROPdoneiptables -t mangle -A PREROUTING -s 127.0.0.0/8 ! -i lo -j DROP
```

* * * * *

### **Saving Rules**

On Debian Based systems:

``` {.wp-block-code}
# netfilter-persistent save
```

On RedHat Based systems

``` {.wp-block-code}
# service iptables save
```

* * * * *

### References

-   [Linux 2.4 Packet Filtering HOWTO](https://www.netfilter.org/documentation/HOWTO//packet-filtering-HOWTO.html)

Related posts
-------------

1.  [Cybersecurity Roundup \#15](https://www.andreafortuna.org/2020/07/30/cybersecurity-roundup-15/)
2.  [Why Huawei USB stick setup on linux adds a strange “Huawei Autorun” script in system start?](https://www.andreafortuna.org/2020/07/29/why-huawei-usb-stick-setup-on-linux-adds-a-strange-huawei-autorun-script-in-system-start/)
3.  [LinuxCheck: Linux information gathering tool](https://www.andreafortuna.org/2020/06/18/linuxcheck-linux-information-gathering-tool/)
4.  [Quick mount of iOS Apps documents on Linux, using iFuse and bash](https://www.andreafortuna.org/2020/05/20/quick-mount-of-ios-apps-documents-on-linux-using-ifuse-and-bash/)
5.  [i3: how to make a pretty lock screen with a small bash script](https://www.andreafortuna.org/2020/04/09/i3-how-to-make-a-pretty-lock-screen-with-a-four-lines-of-bash-script/)

Proudly developed by [Andrea Fortuna](https://www.andreafortuna.org/about/ "Credits")

We use cookies to ensure that we give you the best experience on our website. If you continue to use this site we will assume that you are happy with it.[Ok](#)[](javascript:void(0);)

![:)](iptables:%20a%20simple%20cheatsheet_files/g.gif)
