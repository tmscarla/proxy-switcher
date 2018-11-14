# proxy-switcher
A http proxy switcher written in Python for public and personal proxy lists. It includes a setup tutorial using Squid 3 on a set of Azure virtual machines.

## Overview
Proxy switcher allows you to modify your proxy settings "on the fly" within your Python program. It is useful when you want to perform several http requests to an API using different IPs or when you want to simulate requests from a group of clients. Furthermore, it enables anonimity if anonyms or elite proxies are adopted.

## Basic usage
Basic usage examples are available in the file *example.py*. Once you have set and configured your proxy list, you just need to invoke this method before performing any http request:

```python
pm = ProxyManager(PROXY_LIST, PORT_LIST)

pm.setproxy(mode='rr')
http_request()
```

## Intro

### What is a proxy?
According to Wikipedia, proxy server is a server that acts as an intermediary for requests from clients seeking resources from other servers. We can distinguish between three different types of proxy servers:

* Tunneling proxy:
* Forward proxy:
* Reverse proxy:

<p align="center"><img src="https://deepwebitalia.com/wp-content/uploads/2016/11/proxy.png" height=150px></p>

Among forwarding proxies, is possible to differentiate them according to the degrees of anonymity that they offer:

* Transparent:
* Anonymous:
* Elite:




### Squid Proxy


## Proxy list setup 
