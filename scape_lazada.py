# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:59:29 2021

@author: shuhaili

https://medium.com/@zfwong.wilson/web-scraping-e-commerce-sites-to-compare-prices-with-python-part-1-360509ee5c62
https://medium.com/@zfwong.wilson/web-scraping-e-commerce-sites-to-compare-prices-with-python-part-2-367140620cb6
"""

# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def scape_lazada(keyword, title_class, price_class):
    Lazada_url = 'https://www.lazada.com.my'
    search_item = keyword # Chose this because I often search for coffee!
    
    # Select custom Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized') 
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    # Open the Chrome browser
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get(Lazada_url)
    
    search_bar = browser.find_element_by_id('q')
    # search_bar.send_keys(search_item).submit()
    search_bar.send_keys(search_item)
    search_bar.submit()
    
    item_titles = browser.find_elements_by_class_name(title_class)
    item_prices = browser.find_elements_by_class_name(price_class)
    
    # Initialize empty lists
    titles_list = []
    prices_list = []
    # Loop over the item_titles and item_prices
    for title in item_titles:
        titles_list.append(title.text)
    for price in item_prices:
        prices_list.append(price.text)
        
    try:
        browser.find_element_by_xpath('//*[@class="ant-pagination-next" and not(@aria-disabled)]').click()
    except NoSuchElementException: 
        browser.quit()
    return {'titles_list':titles_list, 'prices_list':prices_list}
