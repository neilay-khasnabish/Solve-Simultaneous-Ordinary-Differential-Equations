from scipy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Define interms of state space
def vdp(t, z):
    x, y, z = z
    u0 = np.sin(t) + np.cos(t)
    u1 = np.cos(t) * 10
    u2 = 1 # Kept constnt
    return [-x - y*z + u0, -y + x*z + u1, -z - x*y + u2]

def genData(a, b, c) : 
  t = linspace(0, 20, 200)
  u0 = np.sin(t) + np.cos(t)
  u1 = np.cos(t) * 10
  u2 = 1 # Kept constnt

  # Solve
  sol = solve_ivp(vdp, y0 = [a, b, c], t_span = [0, 20], t_eval=t)
  finalOP_y = sol.y[0] + sol.y[1] + sol.y[2]
  finalOP_y = finalOP_y / 3.0

  return u0, u1, u2, finalOP_y