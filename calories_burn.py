import matplotlib.pyplot as plt
from scipy import stats

x=[1.5,2.2,0.8,3.0]
y=[95,130,55,170]

slope,intercept,r,p,std_err= stats.linregress(x,y)

def myfun(x):
    return slope * x +  intercept

mymodel=list(map(myfun,x))

equation = f"y = {slope:.2f}x + {intercept:.2f}"
info = (
    f"Slope: {slope:.2f}\n"
    f"Intercept: {intercept:.2f}\n"
    f"R-value: {r:.2f}\n"
    f"P-value: {p:.4f}\n"
    f"Std Err: {std_err:.2f}\n"
    f"{equation}"
)
plt.gcf().text(0.15, 0.75, info, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
plt.scatter(x,y)
plt.plot(x,mymodel,color="yellow")
plt.xlabel("calories")
plt.ylabel("kilometer walked")
plt.show()