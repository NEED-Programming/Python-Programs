# create an angle finder utilizing known distance
# Lots of precalculus or physics probably
# hold my beer
import math

g = math.vector(0, -9.8, 0)
r = math.vector(0, 1.2, 0)
theta = 20 * math.pi/180
v = 4 * math.vector(math.cos(theta, math.sin(theta), 0))
a = g
t = 0
dt = 0.01

while t < 0.2:
  v = v + a * dt
  r = r + v * dt
  t = t + dt

print("r = ", r, " m")


# 60mm
# w = 1.24 kg
# min_range = 180 # minimum firing range in meters
# max_range = 1844 # max firing range in km