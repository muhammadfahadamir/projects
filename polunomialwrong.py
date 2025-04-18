import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

Month = [1,2,3,4,5,6,7,8,9,10,11,12,13]
price_per_month_of_bitcoin = [42265,42582,61198,71333,60636,67491,62678,64619,58969,63329,70215,96449,93249]

mymodel = numpy.poly1d(numpy.polyfit(Month, price_per_month_of_bitcoin, 3))  
myline = numpy.linspace(min(Month), max(Month), 100)            
plt.scatter(Month, price_per_month_of_bitcoin, label="Observed rates")
plt.plot(myline, mymodel(myline), 'r-', label="Polynomial fit")
plt.xlabel("Month")
plt.ylabel("USD → PKR")
speed = mymodel(14)
y_pred = mymodel(Month)
print("R² score:", r2_score(price_per_month_of_bitcoin, y_pred))
print(speed)
plt.show()
