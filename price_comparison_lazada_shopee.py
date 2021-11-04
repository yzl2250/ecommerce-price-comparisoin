# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 01:25:24 2021

@author: shuhaili
"""

import pandas as pd
import re
from scape_lazada import scape_lazada
from scape_shopee import scape_shopee
import matplotlib.pyplot as plt
import seaborn as sns

# scape_lazada(keyword, title_class, price_class)
listsL = scape_lazada('tp link deco e4 mesh wifi 2 pack', '_8JShU', 'Q78Jz')
titles_listL = listsL['titles_list']
prices_listL = listsL['prices_list']
    
dfL = pd.DataFrame(zip(titles_listL, prices_listL), columns=['ItemName', 'Price'])
dfL['Price'] = dfL['Price'].str.replace('RM', '').astype(float)
# Remove false entries i.e. those which are not mesh E4
dfL = dfL[dfL['ItemName'].str.contains('E4') == True] # Poor search function Shopee!!!
# Some of the items are actually 3 packs. Remove them too
dfL = dfL[dfL['ItemName'].str.contains('3', flags=re.IGNORECASE, regex=True) == False]



listsS = scape_shopee('tp link deco e4 mesh wifi 2 pack')
titles_listS = listsS['titles_list']
prices_listS = listsS['prices_list']
    
dfS = pd.DataFrame(zip(titles_listS, prices_listS), columns=['ItemName', 'Price'])

# Remove the ‘RM’ string from Price and change column type to float
dfS['Price'] = dfS['Price'] / 100000
# Remove false entries i.e. those which are not mesh E4
dfS = dfS[dfS['ItemName'].str.contains('E4') == True] # Poor search function Shopee!!!
# Some of the items are actually 3 packs. Remove them too
dfS = dfS[dfS['ItemName'].str.contains('3', flags=re.IGNORECASE, regex=True) == False]


# Add column [‘Platform’] for each platforms
dfL['Platform'] = 'Lazada'
dfS['Platform'] = 'Shopee'
# Concatenate the Dataframes
df = pd.concat([dfL,dfS])

print(df.groupby(['Platform']).describe())

sns.set()
_ = sns.boxplot(x='Platform', y='Price', data=df)
_ = plt.title('Comparison of Nescafe Gold Refill 170g prices between e-commerce platforms in Malaysia')
_ = plt.ylabel('Price (RM)')
_ = plt.xlabel('E-commerce Platform')
# Show the plot
plt.show()