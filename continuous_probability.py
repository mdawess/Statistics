import math
from matplotlib import pyplot as plt

def valid_normal_approx(sample, success):
    condition1 = False
    condition2 = False
    c1 = ((sample * success) - 3 * (math.sqrt(sample * success * (1 - success))))
    c2 = ((sample * success) + 3 * (math.sqrt(sample * success * (1 - success))))
    if (sample * success >= 10) and (sample * (1 - success) >= 10):
        condition1 = True

    elif (c1 >= 0) and (c2 <= sample):
        condition2 = True

    valid = False
    if condition1 or condition2 == True:
        valid = True

    return valid

def nrfactorial(n):
    r = 1
    i = 2
    while i <= n:
        # Use shorter version
        r *= i
        i += 1
    return r

def nrbin_prob(sample, num, success):
    """Returns the binomial probability using the non-recursuive factorial
    to allow for much greater sample sizes."""
    term1 = nrfactorial(sample)/(nrfactorial(num)*nrfactorial(sample - num))
    term2 = pow(success, num)
    term3 = (1 - success) ** (sample - num)
    prob = term1 * term2 * term3

    return round(prob, 4)

def standardize(value, mean, stddev):
    """Standardizes the values to allow for more efficient calculations
    of probability and graphing."""

    z = (value - mean)/stddev

    return z

def normal_probability(sample, mean, stddev):
    """Plots a normal density curve and denotes the location of the point we are trying to
    find the probability of."""
    success = mean/sample
    x = [i for i in range(mean - 3 * stddev, mean + 3 * stddev)]
    z = []
    for i in x:
        x.append(standardize(i, mean, stddev))

    y = []
    for i in z:
        y.append(nrbin_prob(sample, i, success))

    # plt.bar(x, y)
    # plt.show()
    return x, y

#print(valid_normal_approx(400, 0.428))
# print(nrfactorial(20))
print(normal_probability(100, 458, 5)[0])