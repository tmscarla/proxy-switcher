import requests
import pandas as pd


def get_proxy_list(country='', https='', anonymity='', n_proxy=2, last_check=60, verbose=True):
    """
    Get a list of publicly available proxies using Poubproxy API.
    :param country: country code of the proxies (e.g. 'US')
    :param https: ['true', 'false'] proxies with https enabled
    :param anonymity: ['elite', 'anonymous'] level of anonimity of proxies
    :param n_proxy: number of proxies to retrieve
    :param last_check: minutes from the last check of the proxies
    :return: proxy_df: a Dataframe of proxies
    """
    proxy_df_list = []

    if verbose:
        print('Requesting proxy list...')

    payload = {'limit': n_proxy, 'last_check': last_check, 'type': 'http',
               'country': country, 'https': https, 'proxy_level': anonymity}
    r = requests.get('http://pubproxy.com/api/proxy', params=payload)

    for p in r.json()['data']:
        proxy_df_list.append({'IP': p['ip'],
                              'PORT': p['port'],
                              'COUNTRY': p['country'],
                              'ANONIMITY': p['proxy_level'],
                              'HTTPS': p['support']['https'],
                              'GOOGLE': p['support']['google']})

    proxy_df = pd.DataFrame(proxy_df_list)
    proxy_df = proxy_df[['IP', 'PORT', 'COUNTRY', 'ANONIMITY', 'HTTPS', 'GOOGLE']]

    return proxy_df

