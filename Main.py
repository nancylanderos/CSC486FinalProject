import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify
import matplotlib.dates as dates
from datetime import datetime

import timestamp as timestamp
#%matplotlib inline

data = pd.read_csv(r'C:/Users/landerosn/Documents/Berea College Schoolwork/Year 2022/CSC 486/2019-Nov.csv')
print(data.shape)
print(data.head(10))

cor2=data.corr()
print(cor2)

# df2=pd.DataFrame(cor2)
# df2.to_csv(r'C:/Users/landerosn/Documents/Berea College Schoolwork/Year 2022/CSC 486/2019-Nov.csv')

#Users and status on viewing for items
# x = data['user_id']
# y = data['event_type']
# plt.xlabel("user_id")
# plt.ylabel("event_type")
# plt.scatter(x,y)
# plt.show()

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

#what items are purchased?
purchase = data.loc[data['event_type'] == "purchase"]
purchase1 = purchase.dropna(axis = 'rows')
print (purchase1)
#what items are viewed?

#is there a correlation between the ones viewed and purchased?

#brands that customers purchase
topsellers = purchase.groupby('brand')['brand'].agg(['count']).sort_values('count', ascending=False)
topsellers.head(20)
print(topsellers)