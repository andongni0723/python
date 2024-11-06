import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

taxi = pd.read_csv('taxi_data.csv', low_memory=False)

taxi = taxi[['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
             'passenger_count', 'trip_distance', 'fare_amount',
             'PULocationID', 'DOLocationID']]

taxi = taxi.rename(columns={
    "tpep_pickup_datetime": "pickup_dt",
    "tpep_dropoff_datetime": "dropoff_dt"
})

# new Column
taxi['pickup_dt'] = pd.to_datetime(taxi['pickup_dt'])
taxi['dropoff_dt'] = pd.to_datetime(taxi['dropoff_dt'])
taxi['duration'] = taxi['dropoff_dt'] - taxi['pickup_dt']
taxi['sec'] = taxi['duration'].dt.seconds
taxi['hour'] = taxi['sec'] / 60 / 60
taxi['isWeekend'] = taxi['pickup_dt'].dt.weekday >= 5
filt3 = (taxi['duration'] >= pd.to_timedelta('1min')) & (taxi['duration'] <= pd.to_timedelta('3hour'))
# print(taxi)
# taxi = taxi.loc[filt3, :]

taxi['hour'].plot.hist(bins=300)
plt.show()

print(taxi.head())
