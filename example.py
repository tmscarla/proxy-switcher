from proxy_manager import ProxyManager
from definitions import PROXY_LIST, PORT_LIST
from proxy_list_generator import *
from json.decoder import JSONDecodeError
import requests
import time


def foo():
    try:
        start = time.time()
        json = requests.get('http://ip-api.com/json').json()
        ip = json['query']
        print('Foo completed by %s in %.3f seconds!\n' % (ip, (time.time() - start)))
    except JSONDecodeError:
        print('Foo not completed. Decoding JSON has failed.\n')


def personal_proxy_example(n_req=10):
    # Set PROXY_LIST and PORT_LIST in definitions.py
    pm = ProxyManager(PROXY_LIST, PORT_LIST)

    for _ in range(n_req):
        pm.set_proxy()
        foo()


def public_proxy_example(n_req=10):
    proxy_df = get_proxy_list(n_proxy=5, anonymity='elite', https='true')
    proxy_list = proxy_df['IP'].values
    port_list = proxy_df['PORT'].values

    pm = ProxyManager(proxy_list, port_list)

    for _ in range(n_req):
        pm.set_proxy()
        foo()


if __name__ == '__main__':
    public_proxy_example()
