from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from .terrain import generate_reference_and_limits

# Defining the constants
K_d =  0.6
K_p = 0.15
e_0 = 0

# Define control function
def control_submarine(y_1, r_1):
    e_1 = r_1 - y_1
    u_1 = K_p * e_1 + K_d * (e_1 - e_0)
    e_0 = e_1
    return u_1

