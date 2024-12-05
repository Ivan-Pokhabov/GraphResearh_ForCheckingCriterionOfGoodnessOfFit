import matplotlib.pyplot as plt
import numpy as np

# 50-300 +25
res_norm_comp = [
    297.884,
    727.326,
    1343.964,
    2154.271,
    3208.996,
    4444.005,
    5995.057,
    7656.038,
    9602.327,
    11721.536,
    14025.486,
]

# 50-300 +25
res_expon_comp = [
    432.248,
    1065.111,
    1985.574,
    3213.664,
    4708.183,
    6575.349,
    8758.53,
    11380.098,
    14088.168,
    17436.05,
    21010.857,
]

# 50-300 +25
res_uniform_comp = [
    222.233,
    512.257,
    920.37,
    1450.364,
    2097.829,
    2857.974,
    3743.017,
    4758.875,
    5873.975,
    7120.374,
    8472.518,
]

x = np.array(range(50, 301, 25))
y = np.array(res_norm_comp)

coefficients = np.polyfit(x, y, 2)
polynomial = np.poly1d(coefficients)

print(coefficients)
print(polynomial)
plt.scatter(x, y)
plt.plot(x, polynomial(x), color="red")
plt.show()

## norm_edges = 0.202 x^2 - 32.51 x + 5900
## expon_edges = 0.3042 x^2 - 55.89 x + 1.063e+04
## uniform_edges = 0.09483 x^2 + 0.1351 x - 152.8

## norm_max_degree = 0.5266 x - 29.81
## expon_max_degree = 0.8125 x - 37.07
## uniform_max_degree = 0.2146 x + 10.04

## norm_comp = 0.1724 x^2 - 5.372 x + 143.7
## expon_comp = 0.2649 x^2 - 10.88 x + 376.2
## uniform_comp = 0.09514 x^2 - 0.279 x - 2.282
