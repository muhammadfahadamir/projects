import matplotlib.pyplot as plt
from scipy import stats
x=[16,8,9,13,17,19,2,5,17,12,20,1,5]
y=[8,16,13,9,7,5,22,19,7,12,4,23,19]
slope,intercept,r,p,std_err=stats.linregress(x,y)
def myfun(x):
    return slope*x+intercept
mymodel=list(map(myfun,x))
plt.scatter(x,y)
plt.plot(x,mymodel,color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.show()