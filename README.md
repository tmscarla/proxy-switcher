# proxy-switcher
A HTTP proxy switcher written in Python for public and personal proxy lists. Change your proxy on the fly!

## Overview
Proxy switcher allows you to modify your proxy settings "on the fly" within your Python program. It is useful when you want to perform several http requests to an API using different IPs or when you want to simulate requests from a group of clients. Furthermore, it enables anonimity if anonyms or elite proxies are adopted.

## Basic usage
Basic usage examples are available in the file *example.py*. Once you have set and configured your proxy list, you just need to invoke this method before performing any http request:

```python
pm = ProxyManager(PROXY_LIST, PORT_LIST)
pm.setproxy(mode='round')
```
It basically sets environment variables for both http and https proxies. There are three ways to select a proxy from the list:
* Select a specific proxy in the list providing its position
* Select proxies iteratively in a round-robin fashion
* Select proxies randomly from the list

## Intro

### What is a proxy?
According to Wikipedia, proxy server is a server that acts as an intermediary for requests from clients seeking resources from other servers. We can distinguish between three different types of proxy servers:

* **Tunneling proxy:** is a proxy that passes unmodified requests and responses
* **Forward proxy:** is an Internet-facing proxy used to retrieve from a wide range of sources
* **Reverse proxy:** is usually an internal-facing proxy used as a front-end to control and protect access to a server on a private network. A reverse proxy commonly also performs tasks such as load-balancing, authentication, decryption or caching.

<p align="center"><img src="https://www.drupal.org/files/project-images/proxy.png" height=200px></p>

Among forwarding proxies, is possible to differentiate them according to the degrees of anonymity that they offer:

* *Transparent:* declare that you are using a proxy and pass real IP address of the user in the HTTP headers
* *Anonymous:* notify that the proxy is used, but it does not convey the real IP address of the user
* *Elite:* is not notify that a proxy was used and do not convey the real IP address of the user

What type they are basically just comes down to which HTTP Headers they include about who you are.

### Squid Proxy
Squid is a caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages.  Squid has extensive access  controls and makes a great server accelerator. It runs on most available operating systems, including Windows and is licensed under the GNU GPL.


## Proxy list setup 
In the following lines we will see how to install and configure Squid on a set of Linux machines in order to create our personal proxy list. I used Microsoft Azure to create a set of Ubuntu instances organized in a master-slaves architecture. One node is the master, and is in charge of performing all the business logic of our program, including sending http requests. The remaining nodes are proxies (slaves) which forward the requests of the master and return back responses.

<p align="center"><img height=400px src="https://github.com/tmscarla/proxy-switcher/blob/master/img/proxy_diagram.png"></p>

Installing Squid is easy, we just need to run this command on the terminal:

```bash
$ sudo apt-get install squid
```

Once the installation is completed, we need to configure the proxy. The configuration file is stored by default in **‘/etc/squid/squid.conf‘**. Choose your favorite editor and open the file:

```bash
$ sudo nano /etc/squid/squid.conf
```
Now if we want to use a different TCP port rather than the default 3128, we must change the line:
```bash
http_port 8888
```
We can optionally change the visible_hostname directive to give to our proxy a specific hostname:
```bash
visible_hostname proxy_0
```
We need then to manage accesses to the proxy. In my case, since Azure gives the possibility to setup a virtual private network for the instances, I specified an ACL (Access Control List) granting access only from within the VLAN.
```bash
acl vlan src 10.0.1.0/255.255.255.0
http_access allow vlan
http_access deny all
```
Finally, if we want to make our proxy an anonymous proxy, we need to add to the bottom of the configuration file the following lines:
```bash
# ANONYMOUS PROXY
forwarded_for off
request_header_access Allow allow all
request_header_access Authorization allow all
request_header_access WWW-Authenticate allow all
request_header_access Proxy-Authorization allow all
request_header_access Proxy-Authenticate allow all
request_header_access Cache-Control allow all
request_header_access Content-Encoding allow all
request_header_access Content-Length allow all
request_header_access Content-Type allow all
request_header_access Date allow all
request_header_access Expires allow all
request_header_access Host allow all
request_header_access If-Modified-Since allow all
request_header_access Last-Modified allow all
request_header_access Location allow all
request_header_access Pragma allow all
request_header_access Accept allow all
request_header_access Accept-Charset allow all
request_header_access Accept-Encoding allow all
request_header_access Accept-Language allow all
request_header_access Content-Language allow all
request_header_access Mime-Version allow all
request_header_access Retry-After allow all
request_header_access Title allow all
request_header_access Connection allow all
request_header_access Proxy-Connection allow all
request_header_access User-Agent allow all
request_header_access Cookie allow all
request_header_access All deny all
```

That's all! Now restart Squid with the command:

```bash
$ sudo service squid restart
```

Then save the list of the proxies IPs and the ports in the variables PROXY_LIST and PORT_LIST in *definitions.py* and you can run the proxy-switcher on your own proxy list!


