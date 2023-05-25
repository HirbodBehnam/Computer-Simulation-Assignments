import numpy as np

# Read inputs
n = int(input())
p = np.fromstring(input(), dtype=np.float64, sep=' ')
transition = np.array([list(map(lambda x: float(x), input().split())) for _ in range(n)], dtype=np.float64)
epsilon = 0.0001 # max difference to stop the transform

# Multiply in itself until it's less then epsilon
base_transition = transition.copy()
while True:
    new_transition = transition @ base_transition
    if np.any(np.abs(transition - new_transition) > epsilon):
        transition = new_transition
    else:
        break
print(p @ transition)