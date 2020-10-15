# Importing all the libraries all
import pandas as dp
import numpy as num
from mlxtend.frequent_patterns import apriori

from mlxtend.frequent_patterns import association_rules
df = pd.read_excel('OnlineRetail.xlsx')

# Data Cleanup
df ['Description'] = df['Description'].str.strip()
df.dropna(axis = 0, subset=['InvoiceNo'], inplace= True)
df ['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains("C")]
df= head()

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace= True, axis= 1)
basket_sets

frequent_itemsets = apriori(basket_sets, min_support= 0.07, use_colnames= True)
rules = association_rules(frequent_itemsets, metric= "lift", min_threshold= 1)
rules.head()


rules[(rules['lift']>=6) &
      (rules['confidence']>= 0.8)]
