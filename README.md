# proxy-switcher
A http proxy switcher written in Python for public and personal proxy lists. It includes a setup tutorial using Squid 3 on a set of Azure virtual machines.

## Overview
Proxy switcher allows you to modify your proxy settings "on the fly" within your Python program. It is useful when you want to perform several http requests to an API using different IPs or when you want to simulate requests from a group of clients. Furthermore, it enables anonimity if anonyms or elite proxies are adopted.

## Basic usage
Basic usage examples are available in the file *example.py*. Once you have set and configured your proxy list, you just need to invoke this method before performing any http request:

```python
pm = ProxyManager(PROXY_LIST, PORT_LIST)
pm.setproxy(mode='rr')
```

## Intro

### What is a proxy?
According to Wikipedia, proxy server is a server that acts as an intermediary for requests from clients seeking resources from other servers. We can distinguish between three different types of proxy servers:

* **Tunneling proxy:** is a proxy that passes unmodified requests and responses
* **Forward proxy:** is an Internet-facing proxy used to retrieve from a wide range of sources
* **Reverse proxy:** is usually an internal-facing proxy used as a front-end to control and protect access to a server on a private network. A reverse proxy commonly also performs tasks such as load-balancing, authentication, decryption or caching.

<p align="center"><img src="https://deepwebitalia.com/wp-content/uploads/2016/11/proxy.png" height=150px></p>

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
Now we have to change the following lines: 

