from discrete_probability import binomial_probability
from continuous_probability import valid_normal_approx, standardize, normalProbabilityDensity
from matplotlib import pyplot as plt
from scipy.integrate import quad
import pandas as pd
import numpy as np

"""
To do:
1. Add a way to find probability x is between 2 values
2. Add a way to find probability x is not between 2 values
"""
def binomial_sample_distribution(sample, success):
    """Graphs the binomial distribution of a discrete random variable.
    Sample is the number of tests and success is the probability of success.
    """

    y = []
    for i in range(0, sample + 1):
        y.append(binomial_probability(sample, i, success))

    x = []
    for i in range(0, sample + 1):
        x.append(i)

    
    if sample < 20:
        for i in range(len(x)):
            plt.text(x[i], y[i] + 0.01, str(y[i]), color='black', rotation=45)

    relevant = []
    for i in range(0, len(y)):
        if y[i] > 0:
            relevant.append(y[i])
    x = x[0:len(relevant)]
    z = [i/sample for i in x]
    plt.xticks(x, z)
    plt.bar(x, relevant)
    # plt.xticks(positions, labels)
    plt.show()
    return None

def greater_or_equal(sample, target, success):
    """Returns the probability of a proportion being greater than
    or equal to the target."""

    num = target * sample
    i = 0
    z = 1
    while i < num:
        z -= binomial_probability(sample, i, success)
        i += 1
    return round(z, 4)

def less_or_equal(sample, target, success):

    """Returns the probability of a proportion being less than
    or equal to the target."""

    num = target * sample
    i = 0
    z = 0
    while i <= num:
        z += binomial_probability(sample, i, success)
        i += 1
    return round(z, 4)

def between(value1, value2, n, p):

    """Plots a normal density curve and denotes the location of the value we are trying to
    find the probability of. Note: The probability is initially set to show the probability it is 
    LESS THAN value and not include a continuity correction
    Code base: https://towardsdatascience.com/how-to-use-and-create-a-z-table-standard-normal-table-240e21f36e53
    """
    
    mean = p
    var = (1/n) * p * (1 - p)
    stddev = var ** 0.5

    minimum = standardize(mean - 3 * stddev, mean, stddev)
    maximum = standardize(mean + 3 * stddev, mean, stddev)
    
    value1 = round(standardize(value1, mean, stddev), 2)
    value2 = round(standardize(value2, mean, stddev), 2)

    x = np.linspace(minimum, maximum, num = 100)
    constant = 1.0 / np.sqrt(2*np.pi)
    pdf_normal_distribution = constant * np.exp((-x**2) / 2.0)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, pdf_normal_distribution)
    ax.set_ylim(0)
    ax.set_title('Normal Distribution', size = 20)
    ax.set_ylabel('Probability Density', size = 20)

    plt.plot([value1, value1], [0, 0.35], color='red', linestyle='-')
    plt.plot([value2, value2], [0, 0.35], color='red', linestyle='-')
    v1 = round(quad(normalProbabilityDensity, np.NINF, value1)[0], 4)
    v2 = round(quad(normalProbabilityDensity, np.NINF, value2)[0], 4)
    plt.text((value1 + value2) / 2, 0.2, "Area between = " + str((0.5-v1)+(v2-0.5)))
    
    plt.show()

def between_meanstddev(value1, value2, mew, stddev):

    """Plots a normal density curve and denotes the location of the value we are trying to
    find the probability of. Note: The probability is initially set to show the probability it is 
    LESS THAN value and not include a continuity correction
    Code base: https://towardsdatascience.com/how-to-use-and-create-a-z-table-standard-normal-table-240e21f36e53
    """
    
    mean = mew
    stddev = stddev

    minimum = standardize(mean - 3 * stddev, mean, stddev)
    maximum = standardize(mean + 3 * stddev, mean, stddev)
    
    value1 = round(standardize(value1, mean, stddev), 2)
    value2 = round(standardize(value2, mean, stddev), 2)

    x = np.linspace(minimum, maximum, num = 100)
    constant = 1.0 / np.sqrt(2*np.pi)
    pdf_normal_distribution = constant * np.exp((-x**2) / 2.0)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, pdf_normal_distribution)
    ax.set_ylim(0)
    ax.set_title('Normal Distribution', size = 20)
    ax.set_ylabel('Probability Density', size = 20)

    plt.plot([value1, value1], [0, 0.35], color='red', linestyle='-')
    plt.plot([value2, value2], [0, 0.35], color='red', linestyle='-')
    v1 = round(quad(normalProbabilityDensity, np.NINF, value1)[0], 4)
    v2 = round(quad(normalProbabilityDensity, np.NINF, value2)[0], 4)
    plt.text((value1 + value2) / 2, 0.2, "Area between = " + str((0.5-v1)+(v2-0.5)))
    
    plt.show()

# binomial_sample_distribution(40, 0.0521)
#x = greater_or_equal(36, 2/36, 0.041) 
# y = less_or_equal(40, 0.05, 0.0521)
# z = between(0.5, 0.7, 2000, 0.6)
# m = between_meanstddev(2400, 3900, 3301, 512)
# print(y)