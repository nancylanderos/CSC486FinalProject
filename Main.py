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
topcateg = 30
topcateg1 = data['category_code'].value_counts()[:topcateg].sort_values(ascending=False)
df = pd.DataFrame({'count':topcateg1, "topcateg1":topcateg1})
squarify.plot(sizes=topcateg1, label=topcateg1.index.array, color=["red","blue","green","grey","cyan"], alpha=.7)
plt.axis('off')
plt.show()

# data['event_date'] = data['event_time'].apply(lambda s: convert_time_to_date(s))
# visitor_by_date = data[['event_date','user_id']].drop_duplicates().groupby(['event_date'])['user_id'].agg(['count']).sort_values(by=['event_date'], ascending=True)
