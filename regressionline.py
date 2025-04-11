import matplotlib.pyplot as plt
from scipy import stats

x = [1,1,2,3,4,8,13,21]
y = [98.1504,98.1504,97.3917,96.6330,95.8743,92.8391,88.0456,1.0133]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()