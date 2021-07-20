# -*- coding: utf-8 -*-
"""car sales.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13d88EDpAl5UXMt144H3qYsGLQdy3DAyf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

df=pd.read_csv("/content/car_sales.csv")
df

df.head()

data=df
data.isna()
data.isnull()

data['MPG.city']=235/df['MPG.city']
print(data.columns)

data.dtypes

data.Price.unique()
data=data[data.Price!='?']
data.dtypes

data['Length']=data['Length']/data['Length'].max()
data['Width']=data['Width']/data['Width'].max()
bins=np.linspace(min(data['Price']),max(data['Price']),4)
group_names=['Low','Medium','High']       
data['price_binned']=pd.cut(data['Price'],bins,labels=group_names,include_lowest=True)
print(data['price_binned'])
plt.hist(data['price_binned'])
plt.show()

data.describe()

plt.boxplot(data['Price'])
sns.boxplot(x='EngineSize',y='Price',data=data)
plt.show()

plt.scatter(data['EngineSize'],data['Price'])
plt.title('Scatterplot of Enginesize Vs Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.grid()
plt.show()

test=data[['Wheelbase','Price','Weight']]
data_grp=data.groupby(['Wheelbase','Weight'],as_index=False).mean()
data_grp

data_pivot=data_grp.pivot(index='Wheelbase',columns='Weight')
data_pivot

plt.pcolor(data_pivot,cmap='RdBu')
plt.colorbar()
plt.show()

from google.colab import drive
drive.mount('/content/drive')