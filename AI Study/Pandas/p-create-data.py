import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workout_dict = {
    "speed": [122, 134, 567, 2345],
    "distance": [56, 34, 56, 78],
    "type": ['run', 'walk', 'walk', 'run']
}

workout = pd.DataFrame(workout_dict, index=["d1", "d2", "d3", "d4"])
print(workout)
print()

# print(workout[['c']])
# print(workout.loc[['d1'], :])
# print(workout.at['d1', 'speed'])
# workout.at['d1', 'speed'] = 1111

