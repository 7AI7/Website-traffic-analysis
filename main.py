import math
from scipy.stats import norm
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from IPython.core.display import HTML

import os
for dirname,_, filenames in os.walk("D:\daily-website-visitors.csv"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("D:\daily-website-visitors.csv", index_col = 'Date', thousands = ',', parse_dates=True)
df.head()

df.plot(figsize=(14,7))

def prob(t, n, lmbda):
    return math.pow(lmbda * t, n)/math.factorial(n)*math.exp(-lmbda*t)

mean = df['Page.Loads'].mean()
print( "mean loads per day:", mean)

std = df['Page.Loads'].std()
print( "std deviation of loads per day:", std)

n = 1
px = np.linspace(1, 8000, 50)
py = np.zeros(50)
for i in range(0, 50):
    x = (px[i]-mean)/std
    p = norm.pdf(x)
    py[i] = 1000*p
    fig, ax1 = plt.subplots()
df['Page.Loads'].plot.hist(ax = ax1, label='Page.Loads')

plt.plot([mean, mean], [0, 480], label='mean')

plt.plot(px, py, label='normal', color='red')
plt.legend()
plt.show()

HTML('<h3>using normal approximation to binomial distribution</h3>')

fig, ax1 = plt.subplots()
df['Page.Loads'].plot(ax = ax1, label='Page.Loads')
plt.plot([df.index[0], df.index[-1]], [mean, mean], color='red')
upper = mean + 1.96*std
lower = mean - 1.96*std
plt.plot([df.index[0], df.index[-1]], [upper, upper], color='green')
plt.plot([df.index[0], df.index[-1]], [lower, lower], color='green')
plt.show()
