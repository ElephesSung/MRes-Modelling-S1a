#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:30:45 2023

@author: Elephes
"""



import numpy as np
import matplotlib.pyplot as plt

k1 = 0.1
k2 = 0.2
k3 = 0.05
k4 = 0.4

X0_values = np.linspace(0, 7.0, 10000)  

concentration_A = []
concentration_B = []
concentration_C = []
concentration_D = []


for X0 in X0_values:
    A_eq = X0
    B_eq = 0
    C_eq = 0
    D_eq = 0
    

    concentration_A.append(A_eq)
    concentration_B.append(B_eq)
    concentration_C.append(C_eq)
    concentration_D.append(D_eq)

plt.figure(figsize=(10, 6))
plt.plot(X0_values, concentration_A, label='A', linewidth=3)
plt.plot(X0_values, concentration_B, label='B', linewidth=3)
plt.plot(X0_values, concentration_C, label='C', linewidth=3)
plt.plot(X0_values, concentration_D, label='D', linewidth=3)

plt.xlim(0, 7)
plt.ylim(0, 4)
plt.xlabel('X0', fontsize=25)
plt.ylabel('Concentration', fontsize = 25)
plt.legend()
plt.grid(True)

dpi = 1000


plt.show()
    