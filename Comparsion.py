#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:20:01 2023

@author: Elephes
"""

import numpy as np
import matplotlib.pyplot as plt

# Given data
data = {
    4: [2.00577568472849, 0.36272232691959244, 1.4502002057204477, 0.18130178263146965],
    12: [1.9999991776426194, 1.8181777959871503, 7.272731390854373, 0.9090916355158543],
    20: [1.9999999844113827, 3.27272728783736, 13.090909092735684, 1.6363636350155715],
    28: [2.0000000004863163, 4.727272726483391, 18.909090909305576, 2.3636363637247277]
}

# Constants
k1 = 0.1
k2 = 0.2
k3 = 0.05
k4 = 0.4

# Generate X0 values between 4 and 30
X0_values = np.arange(2, 31)

# Calculate A, B, C, and D for the given X0 values
A_calculated = k2 / k1
B_calculated = (X0_values - k2 / k1) / (1 + k2 / k3 + k2 / k4)
C_calculated = (k2 / k3) * (X0_values - k2 / k1) / (1 + k2 / k3 + k2 / k4)
D_calculated = (k2 / k4) * (X0_values - k2 / k1) / (1 + k2 / k3 + k2 / k4)

plt.figure(figsize=(10, 6))

# Plot data points
plt.scatter(data.keys(), [data[x][0] for x in data], label='A_simulated')
plt.scatter(data.keys(), [data[x][1] for x in data], label='B_simulated')
plt.scatter(data.keys(), [data[x][2] for x in data], label='C_simulated')
plt.scatter(data.keys(), [data[x][3] for x in data], label='D_simulated')

# Plot calculated lines
plt.plot(X0_values, [A_calculated] * len(X0_values), label='A_calculated')
plt.plot(X0_values, B_calculated, label='B_calculated')
plt.plot(X0_values, C_calculated, label='C_calculated')
plt.plot(X0_values, D_calculated, label='D_calculated')

plt.axvline(x=2, color='r', linestyle='--', label='X0=k2/k1')

# Set axis labels and legend
plt.xlabel('X0', fontsize = 20)
plt.ylabel('Concentration at Steady State', fontsize = 20)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
