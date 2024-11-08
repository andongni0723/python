import pandas as pd

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


# print(len(taxi['PULocationID'].unique().tolist()))

def mean_traveltime_mins(x):
    return x['sec'].mean() / 60


taxi.groupby(['PULocationID']).apply(mean_traveltime_mins, include_groups=False)


def filter_gb_count(df, min_trips):
    return len(df) >= min_trips


def filter_gb_count(df, min_trips):
    return len(df) >= min_trips


taxi_bg = taxi.groupby(['PULocationID', 'isWeekend'])
taxi_bg = taxi_bg.filter(filter_gb_count, min_trips=30)
print(taxi_bg)