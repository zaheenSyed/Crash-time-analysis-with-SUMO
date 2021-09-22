## beautiful soup library to read XML


import pandas as pd
from bs4 import BeautifulSoup

file = open("file.xml", 'r')
soup = BeautifulSoup(file, 'lxml')
df = pd.DataFrame({'ids': [x.text for x in soup.find_all('id')]})
df.to_excel('data.xls')