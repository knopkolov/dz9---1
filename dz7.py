import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Задание 1

data = pd.Series([10, 30, 20, 50, 40], index=['A', 'B', 'C', 'D', 'E'])
data.plot.bar(color='k')
plt.show()

# Задание 2

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))

s.plot(
    style='ko--',
    alpha=1,
    kind='line',
    rot=0,
    grid=True,
    title='ДЗ 7')

plt.show()
