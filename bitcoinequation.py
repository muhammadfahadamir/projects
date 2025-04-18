import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

Month = [1,2,3,4,5,6,7,8,9,10,11,12,13]
price_per_month_of_bitcoin = [42265,42582,61198,71333,60636,67491,62678,64619,58969,63329,70215,96449,93249]

# Fit the polynomial model
mymodel = numpy.poly1d(numpy.polyfit(Month, price_per_month_of_bitcoin, 3))
myline = numpy.linspace(min(Month), max(Month), 100)

# Predict
speed = mymodel(14)
y_pred = mymodel(Month)

# Plot
plt.scatter(Month, price_per_month_of_bitcoin, label="Observed rates")
plt.plot(myline, mymodel(myline), 'r-', label="Polynomial fit")
plt.xlabel("Month")
plt.ylabel("Bitcoin Price")
plt.legend()
plt.show()

# R² Score
print("R² score:", r2_score(price_per_month_of_bitcoin, y_pred))

# Coefficients
coefficients = mymodel.coefficients
a, b, c, d = coefficients

print("\nCoefficients:")
print(f"a (x³): {a}")
print(f"b (x²): {b}")
print(f"c (x): {c}")
print(f"d (intercept): {d}")

# Full Equation
print("\nPolynomial Regression Equation:")
print(f"y = {a:.3f}x³ + {b:.3f}x² + {c:.3f}x + {d:.3f}")

# Prediction for month 14
print("\nPredicted Bitcoin Price for Month 14:", speed)
