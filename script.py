import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.atan(x) - 4/(1+x**2)

def dg(x):
    return (x**2 + 8*x + 1)/(1+x**2)**2

def newthon(x0, eps, func, dfunc):
    while True:
        x1 = x0 - func(x0)/ dfunc(x0)
        if np.abs(func(x1)) < eps:
            return x1
        x0 = x1

x_extr = newthon(1, 0.00001, g, dg)

def f(x):
    return np.exp(-x/4)*np.atan(x)
print(x_extr)
print(f(x_extr))

x = np.linspace(0, 20, 400)
y = f(x)

plt.figure(figsize=(8,5))
plt.scatter(x_extr, f(x_extr), color='red', label=f'({x_extr}, {f(x_extr)})')
plt.plot(x, y, label=r'$f(x) = e^{-x/4} \cdot \arctan(x)$', color='blue')

plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
