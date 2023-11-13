#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 1 2023
Modified on Wed Nov 8 2023

@author: Elephes Sung 
Research Postgraduate, DoLS, FoNS, Imperial
02480474
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k1 = 0.1
k2 = 0.2
k3 = 0.05
k4 = 0.4

init_A = float(input("Initial concentration of A is "))
init_B = float(input("Initial concentration of B is "))
init_C = float(input("Initial concentration of C is "))
init_D = float(input("Initial concentration of D is "))
X0 = init_A+init_B+init_C+init_D
initial_conditions = [init_A, init_B, init_C, init_D]  


def model(concentrations, t):
    A, B, C, D = concentrations
    dA_dt = k4 * D - k1 * A * B
    dB_dt = k1 * A * B - k2 * B
    dC_dt = k2 * B - k3 * C
    dD_dt = k3 * C - k4 * D
    return [dA_dt, dB_dt, dC_dt, dD_dt]


t = np.linspace(0, 120, 10000)  


concentrations_over_time = odeint(model, initial_conditions, t)


A_over_time, B_over_time, C_over_time, D_over_time = concentrations_over_time.T


plt.figure(figsize=(10, 6))
plt.plot(t, A_over_time, label='A', linewidth=3)
plt.plot(t, B_over_time, label='B', linewidth=3)
plt.plot(t, C_over_time, label='C', linewidth=3)
plt.plot(t, D_over_time, label='D', linewidth=3)

plt.xlabel('Time (t)', fontsize=25)
plt.ylabel('Concentration', fontsize=25)
plt.legend()
plt.grid(True)


plt.savefig('concentration_plot.png')
plt.show()

A_at_t_120, B_at_t_120, C_at_t_120, D_at_t_120 = concentrations_over_time[-1]

print("Concentration of A at t=120:", A_at_t_120)
print("Concentration of B at t=120:", B_at_t_120)
print("Concentration of C at t=120:", C_at_t_120)
print("Concentration of D at t=120:", D_at_t_120)
    