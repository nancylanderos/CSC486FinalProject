import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify
import matplotlib.dates as dates
from datetime import datetime
from pylab import *
import networkx as nx

import timestamp as timestamp
#%matplotlib inline
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

data = pd.read_csv(r'C:/Users/landerosn/Documents/Berea College Schoolwork/Year 2022/CSC 486/2019-Nov.csv')
# print(data.shape)
# print(data.head(10))
#
# cor2=data.corr()
# print(cor2)

# df2=pd.DataFrame(cor2)
# df2.to_csv(r'C:/Users/landerosn/Documents/Berea College Schoolwork/Year 2022/CSC 486/2019-Nov.csv')

#Users and status on viewing for items
x = data['user_session']
y = data['event_type']
plt.xlabel("user_session")
plt.ylabel("event_type")
plt.scatter(x,y)
plt.show()

#category customers find/view
# topcateg = 30
# topcateg1 = data['category_code'].value_counts()[:topcateg].sort_values(ascending=False)
# df = pd.DataFrame({'count':topcateg1, "topcateg1":topcateg1})
# squarify.plot(sizes=topcateg1, label=topcateg1.index.array, color=["red","blue","green","grey","cyan"], alpha=.7)
# plt.axis('off')
# plt.show()


#showing traffic/work on it
# def convert_time_to_date(utc_timestamp):
#     utcdate = datetime.strptime(utc_timestamp[0:10], '%Y-%m-%d').date()
#     return utcdate
#
# data['event_date'] = data['event_time'].apply(lambda s: convert_time_to_date(s))
# visitor_by_date = data[['event_date','user_id']].drop_duplicates().groupby(['event_date'])['user_id'].agg(['count']).sort_values(by=['event_date'], ascending=True)
#
# x = pd.Series(visitor_by_date.index.values)
# y = visitor_by_date['count']
# plt.rcParams['figure.figsize'] = (20,8)
# plt.plot(x,y)
# plt.show()

#purchase behavior
# data['event_type'].value_counts()
# labels = ['view', 'cart', 'purchase']
# size = data['event_type'].value_counts()
# colors = ['lightgreen', 'lightblue', 'coral']
# explode = [0, 0.1, 0.1]
# plt.rcParams['figure.figsize'] = (8,8)
# plt.pie(size, colors= colors, explode=explode, labels=labels, shadow=True, autopct='%.2f%%')
# plt.title('Event_Type', fontsize = 20)
# plt.axis('off')
# plt.legend()
# plt.show()

#what items are purchased? /graph a bar chart showing popular items under purchased
# purchase = data.loc[data['event_type'] == "purchase"]
# purchase1 = purchase.dropna(axis = 'rows')
# print (purchase1)

#example

#what items are viewed? / graph a bar chart showing popular items under viewed

# viewed = data.loc[data['event_type'] == 'view']
# viewed1 = viewed.dropna(axis = 'rows')
# print (viewed1)

#is there a correlation between the ones viewed and purchased?

#brands that customers purchase shown in console
# topsellers = purchase.groupby('brand')['brand'].agg(['count']).sort_values('count', ascending=False)
# topsellers.head(20)
# print(topsellers)
# #brands that customers purchase attempt to create graph
# labels = ['purchase']
# size = data['event_type'].value_counts()
# colors = ['green', 'blue', 'teal', 'pink']
# explode = [0, 0.1, 0.1]
# plt.rcParams['figure.figsize'] = (8,8)
# plt.pie(size, colors=colors, explode=explode, labels=labels)
# plt.title('Purchased items', fontsize=14)
# plt.axis('off')
# plt.legend()
# plt.show()
#example of a user behavior
# user_session = 	513351129
# data.loc[data['user_id'] == user_session]
# print (data.loc[data['user_id'] == user_session])

# g = nx.read_adjlist('C:/Users/landerosn/Documents/Berea College Schoolwork/Year 2022/CSC 486/2019-Nov.csv', delimiter=',')
# nx.draw(g, with_labels=True)
# show()
