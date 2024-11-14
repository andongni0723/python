import matplotlib.pyplot as plt
import matplotlib as mplt
import numpy as np

# setting
mplt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
mplt.rcParams['figure.dpi'] = 300

tem = np.random.randint(20, 35, size=30)
day = np.arange(1, 31, 1)
plt.figure(figsize=(12, 5))  # 調整寬度為12，高度為5
plt.plot(day, tem, "b.-")
plt.ylim(0, 40)
plt.grid()
plt.xticks(day)

plt.title("某地區每日溫度變化")
plt.xlabel("日期")
plt.ylabel("溫度（°C）")

maxTemp = np.max(tem)
minTemp = np.min(tem)
maxTempDay = np.argmax(tem) + 1
minTempDay = np.argmin(tem) + 1
plt.scatter(maxTempDay, maxTemp, color="red", marker="o", s=50, label="最高溫度", zorder=5)
plt.scatter(minTempDay, minTemp, color="green", marker="o", s=50, label="最低溫度", zorder=5)

plt.text(maxTempDay, maxTemp + 1, f"最高: {maxTemp}°C", color='red', ha='center')
plt.text(minTempDay, minTemp - 2.5, f"最低: {minTemp}°C", color='green', ha='center')

# 計算平均溫度並添加水平線
average_temp = np.mean(tem)
plt.axhline(y=average_temp, color='orange', linestyle='--', label=f'平均溫度: {average_temp:.2f}°C')

plt.legend()
plt.show()
