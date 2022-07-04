import numpy as np
import math

s_old = 205
s_new = 196
T = 13

x = np.exp(-(s_old-s_new)/T)
print(x)
print(-(s_old-s_new))


y = (-(s_old-s_new))/math.log(0.5)
print(y)