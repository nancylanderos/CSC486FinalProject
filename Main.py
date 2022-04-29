import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify
import matplotlib.dates as dates
from datetime import datetime

import timestamp as timestamp
#%matplotlib inline

data = pd.read_csv('C:\Users\landerosn\Documents\Berea College Schoolwork\Year 2022\CSC 486')
print(data.shape)
print(data.head(10))
data['event_date'] = data['event_time'].apply(lambda s: convert_time_to_date(s))
visitor_by_date = data[['event_date','user_id']].drop_duplicates().groupby(['event_date'])['user_id'].agg(['count']).sort_values(by=['event_date'], ascending=True)
