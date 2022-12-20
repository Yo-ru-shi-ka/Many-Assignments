import numpy as np

# Given data
r = np.array([0, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00])
V = np.array([10, 9.80, 9.60, 9.30, 9.06, 8.68, 8.18, 7.41, 0])
rho = 1.2

# Calculate the flow rate using the Composite Simpson's rule
flow_rate = 0
for i in range(len(r)-2):
    flow_rate += (r[i+1] - r[i]) * (V[i] + 4*V[i+1] + V[i+2]) / 6
flow_rate *= rho * 2 * np.pi

print(f"Flow rate: {flow_rate:.3f} kg/s")
