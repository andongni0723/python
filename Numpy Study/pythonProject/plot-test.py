import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# 繪製折線圖
plt.plot(data['date_column'], data['value_column'])
plt.title('Value Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
