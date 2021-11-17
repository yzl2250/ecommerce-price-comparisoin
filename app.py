# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 01:25:24 2021

@author: shuhaili
"""

import streamlit as st
import pandas as pd
import numpy as np
# import plotly_express as px
import pandas as pd
import re
from scape_lazada import scape_lazada
from scape_shopee import scape_shopee
import matplotlib.pyplot as plt
import seaborn as sns


'''
# e-commerce price scraping
## Welcome to e-commerce price comparison portal!
'''

'''
#### Here is a price comparison between most popular e-commerce platform at Malaysia. (Shopee & Lazada)
'''

product = st.text_input("Enter product keyword")

st.sidebar.title("Lazada class scraping")
st.sidebar.write("How do identify which elements to find? " \
                 "An easy way to do this is to use Chrome’s very own inspect tool. " \
                 "Use the element selector to hover around elements of title and price for each product. " \
				 "* For default use the value as in box, but if encounter with error, please refer the value at "\
				 "https://www.lazada.com.my/ inspect")
lazadatitleclass = st.sidebar.text_input("Enter title class", "_8JShU")
lazadapriceclass = st.sidebar.text_input("Enter price class","Q78Jz")

if(st.button('Submit')):
    st.text("")
    # listsS = scape_shopee('tp link deco e4 mesh wifi 2 pack')
    listsS = scape_shopee(product)
    titles_listS = listsS['titles_list']
    prices_listS = listsS['prices_list']
        
    dfS = pd.DataFrame(zip(titles_listS, prices_listS), columns=['ItemName', 'Price'])
    
    # Remove the ‘RM’ string from Price and change column type to float
    dfS['Price'] = dfS['Price'] / 100000
    dfS.sort_values(by=['Price'], inplace=True)
    dfS = dfS.reset_index(drop=True)
    dfS.index = dfS.index + 1
    
    listsL = scape_lazada(product, lazadatitleclass, lazadapriceclass)
    titles_listL = listsL['titles_list']
    prices_listL = listsL['prices_list']
     
    dfL = pd.DataFrame(zip(titles_listL, prices_listL), columns=['ItemName', 'Price'])
    dfL['Price'] = dfL['Price'].str.replace(',', '')
    dfL['Price'] = dfL['Price'].str.replace('RM', '').astype(float)
    dfL.sort_values(by=['Price'], inplace=True)
    dfL = dfL.reset_index(drop=True)
    dfL.index = dfL.index + 1   
    
    # Add column [‘Platform’] for each platforms
    dfL['Platform'] = 'Lazada'
    dfS['Platform'] = 'Shopee'
	
    # Concatenate the Dataframes
    df = pd.concat([dfL,dfS])
    df.sort_values(by=['Price'], inplace=True)
    df = df.reset_index(drop=True)
    df_group = df.groupby(['Platform']).describe()
    
    st.write("Data overview")
    st.write(df) 
    
    st.write("Summarization for means, maximum and minimum prices between Shopee and Lazada Platform")
    st.write(df_group) 
    
    st.text("")
    
    st.write("Here is a box-plot for price comparison between Shopee and Lazada")

    st.text("")
    sns.set()
    _ = sns.boxplot(x='Platform', y='Price', data=df)
    _ = plt.title('Comparison prices between e-commerce platforms in Malaysia')
    _ = plt.ylabel('Price (RM)')
    _ = plt.xlabel('E-commerce Platform')
    # Show the plot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
 