#1
import matplotlib.pyplot as plt
from scipy import stats
x=[7,8,3,12,3,6,7,8,9,7,13,8]
y=[17,21,11,27,12,17,20,23,25,18,29,22]
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel, color='yellow')


plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
