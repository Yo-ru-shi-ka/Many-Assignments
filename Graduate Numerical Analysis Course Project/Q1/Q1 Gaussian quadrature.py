import numpy as np

# Given data
r = np.array([0, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00])
V = np.array([10, 9.80, 9.60, 9.30, 9.06, 8.68, 8.18, 7.41, 0])
rho = 1.2
R = 8.00

# Define the integrand
def f(r):
    return rho * V * 2 * np.pi * r

# Use Gaussian Legendre quadrature to approximate the flow_rate
x, w = np.polynomial.legendre.leggauss(len(r))
flow_rate = np.sum(w * f((R - r[0]) * x + r[0])) * (R - r[0]) / 2

# Print the result
print("The flow rate is approximately", flow_rate, "kg/s")

