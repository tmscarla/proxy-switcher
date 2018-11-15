import os
import numpy as np
import requests


class ProxyManager(object):

    def __init__(self, proxy_list, proxy_ports=None):
        """
        Initialize the object with a list of string of proxies and with an optional list
        of ports to connect for each proxy. If not specified is 8080 for all proxies.
        :param proxy_list: list of proxies
        :param proxy_ports: optional list of ports
        """
        assert len(proxy_list) > 0

        if proxy_ports is not None:
            assert len(proxy_list) == len(proxy_ports)
            self.proxy_ports = proxy_ports
        else:
            self.proxy_ports = [8080] * len(proxy_list)

        self.proxy_list = proxy_list
        self.n_proxy = len(self.proxy_list)
        self.current = 0

    def __str__(self):
        return 'Proxies: ' + str(self.proxy_list)

    def set_proxy(self, proxy_pos=None, mode='rr', verbose=True):
        """
        Set environment variables for HTTP and HTTPS proxies using a provided proxy list.
        :param proxy_pos: explicitly set the proxy in the specified position of the list.
        :param mode: ['rand', 'rr'] if rand choses randomly a proxy from the list.
                     If 'rr' (round robin) selects iteratively each proxy from the list.
        :param verbose: add verbosity
        """
        if proxy_pos is not None and int(proxy_pos) > 0 and int(proxy_pos) < len(self.proxy_list):
            proxy = self.proxy_list[proxy_pos]
            port = self.proxy_ports[proxy_pos]
        else:
            if mode is 'rr':
                proxy = self.proxy_list[self.current]
                port = self.proxy_ports[self.current]

                self.current += 1
                if self.current % self.n_proxy is 0: self.current = 0
            else:
                idx = np.random.randint(self.n_proxy)
                proxy = self.proxy_list[idx]
                port = self.proxy_ports[idx]

        os.environ['HTTP_PROXY'] = 'http://' + str(proxy) + ':' + str(port)
        os.environ['HTTPS_PROXY'] = 'https://' + str(proxy) + ':' + str(port)

        if verbose:
            print('Set proxy ' + str(proxy) + ' at port ' + str(port))

    def reset(self):
        """
        Unset environment variables or HTTP and HTTPS proxies
        """
        del os.environ['HTTP_PROXY']
        del os.environ['HTTPS_PROXY']

    def test_proxy(self):
        """
        Test if the proxy is correctly set. If the IP of the environment variable is equal to the
        IP of the HTTP request everything works fine.
        """
        json = requests.get('http://ip-api.com/json')
        ip = json['query']

        print('Environment: ' + str(os.environ.get('HTTP_PROXY')))
        print('IP: ' + ip)

