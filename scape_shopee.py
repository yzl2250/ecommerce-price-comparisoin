# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:59:29 2021

@author: shuhaili

https://medium.com/@zfwong.wilson/web-scraping-e-commerce-sites-to-compare-prices-with-python-part-1-360509ee5c62
https://medium.com/@zfwong.wilson/web-scraping-e-commerce-sites-to-compare-prices-with-python-part-2-367140620cb6
"""

import requests


def scape_shopee(keyword):
    Shopee_url = 'https://shopee.com.my'
    keyword_search = keyword
    
    headers = {
     'User-Agent': 'Chrome',
     'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
    }
    
    url = 'https://shopee.com.my/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&order=desc&page_type=search'.format(keyword_search)
    # Shopee API request
    r = requests.get(url, headers = headers).json()
    # Shopee scraping script
    titles_list = []
    prices_list = []
    for item in r['items']:
        titles_list.append(item['name'])
        prices_list.append(item['price_min'])
    
    return {'titles_list':titles_list, 'prices_list':prices_list}

