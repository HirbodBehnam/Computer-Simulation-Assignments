import math
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_standard_normal():
    """
    Generate a random normal variable with mu = 0 and std = 1
    """
    r1 = random.random()
    r2 = random.random()
    # As far as i read, one of the equations are enough. I choose the first one.
    return math.sqrt(-2 * math.log(r1)) * math.cos(2 * math.pi * r2)

def poisson_generator(poisson_lambda: float, count: int) -> list[int]:
    """
    Generate some poisson variables
    """
    result: list[int] = []
    if poisson_lambda > 15:
        for _ in range(count):
            n = math.ceil(poisson_lambda + math.sqrt(poisson_lambda) * generate_standard_normal() - 0.5)
            if n < 0:
                result.append(0)
            else:
                result.append(n)
    else:
        exp_lambda = math.exp(-poisson_lambda)
        for _ in range(count):
            n = 0
            P = 1
            while True:
                P *= random.random()
                if P < exp_lambda:
                    result.append(n)
                    break
                n += 1
    return result

poisson_lambda = float(input("Enter poisson distribution lambda: "))
samples_count = int(input("Enter number of samples you want to generate: "))

our_samples = poisson_generator(poisson_lambda, samples_count)
np_samples = np.random.poisson(poisson_lambda, samples_count)

# Just like https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html
plt.figure(1)
plt.subplot(211).set_title("Our RNG")
plt.hist(our_samples, max(max(our_samples), max(np_samples)))
plt.subplot(212).set_title("Numpy RNG")
plt.hist(np_samples, max(max(our_samples), max(np_samples)))
plt.show()