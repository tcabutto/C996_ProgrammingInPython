# import
import re
import requests
from bs4 import BeautifulSoup as soup
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

html_string = """""

"""

# Use beautful soup
ps = soup(html_string, 'lxml')

#Showing our string has been set to the soup object
print(ps.prettify())

data = []
for site in ps.findAll('a', attrs={'href': re.compile("^(http*|/.)")}):
    
    link = site.get('href').strip()
    
    if link.startswith("/") :
        data.append('https://www.census.gov' + link)
    elif link.endswith('/') :
        data.append(link[:-1])
    else :
        data.append(link)
            
#Creating a pandas dataframe in order to store all of our data.        
links = pd.DataFrame({ 
    'Links' : data,
})
print(links)

links.duplicated('Links')
links = links.drop_duplicates("Links")
print(links)

links.to_csv('C:\_Projects\programming_in_python_C996\Links_Part_G.csv')