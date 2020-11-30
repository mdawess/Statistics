import math
from matplotlib import pyplot as plt
from scipy.integrate import quad
import numpy as np
import pandas as pd

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

def normalProbabilityDensity(x):
    """Integrates the normal probability curve and finds the area under the
    curve less than x."""
    constant = 1.0 / np.sqrt(2*np.pi)

    return(constant * np.exp((-x**2) / 2.0))

def continuity_correction(action, value):
    """Applies a continuity correction based on whether you are looking to
    find the proportion GREATER than or LESS than the inputted value."""

    if action == "GREATER".lower():
        value -= 0.5

    elif action == "LESS".lower():
        value += 0.5

    else:
        print('Please enter either GREATER or LESS')

    return value

# Main functions for class
"""
To do:
1. Add a check to see if normal approx is valid
"""
def normal_probability_proportions(p_hat, n, p, cc=False, greater=False):

    """Plots a normal density curve and denotes the location of the value we are trying to
    find the probability of. Note: The probability is initially set to show the probability it is 
    LESS THAN value and not include a continuity correction
    Code base: https://towardsdatascience.com/how-to-use-and-create-a-z-table-standard-normal-table-240e21f36e53
    """
    
    mean = n * p
    var = n * p * (1 - p)
    stddev = var ** 0.5
    value = p_hat * n
    if cc == True:
        if greater == False:
            value = continuity_correction("less", value)

        elif greater == True:
            value = continuity_correction("greater", value)

    minimum = standardize(mean - 3 * stddev, mean, stddev)
    maximum = standardize(mean + 3 * stddev, mean, stddev)
    
    value = round(standardize(value, mean, stddev), 2)
    print(value)
    x = np.linspace(minimum, maximum, num = 100)
    constant = 1.0 / np.sqrt(2*np.pi)
    pdf_normal_distribution = constant * np.exp((-x**2) / 2.0)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, pdf_normal_distribution)
    ax.set_ylim(0)
    ax.set_title('Normal Distribution, mean= '+str(mean)+', stddev= '+str(round(stddev, 3)), size = 20)
    ax.set_ylabel('Probability Density' , size = 20)
    
    plt.plot([value, value], [0, 0.30], color='red', linestyle='-')
    x = round(quad(normalProbabilityDensity, np.NINF, value)[0], 4)
    if greater == False:
        x = round(0.5 - (1 - x - 0.5), 4)
        plt.text(value, 0.33, str(x))
    elif greater == True:
        x = round(1 - x, 4)
        plt.text(value, 0.33, str(x))
        
    
    plt.show()

def normal_probability_given(target, mean, stddev, cc=False, greater=False):
    """Plots a normal density curve and denotes the location of the value we are trying to
    find the probability of. Note: The probability is initially set to show the probability it is 
    LESS THAN value and not include a continuity correction"""
    
    mean = mean
    stddev = stddev
    value = target

    if cc == True:
        if greater == False:
            value = continuity_correction("less", value)

        elif greater == True:
            value = continuity_correction("greater", value)

    minimum = standardize(mean - 3 * stddev, mean, stddev)
    maximum = standardize(mean + 3 * stddev, mean, stddev)
    
    value = round(standardize(value, mean, stddev), 2)

    x = np.linspace(minimum, maximum, num = 100)
    constant = 1.0 / np.sqrt(2*np.pi)
    pdf_normal_distribution = constant * np.exp((-x**2) / 2.0)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, pdf_normal_distribution)
    ax.set_ylim(0)
    ax.set_title('Normal Distribution, mean= '+str(mean)+', stddev= '+str(stddev), size = 20)
    ax.set_ylabel('Probability Density', size = 20)

    plt.plot([value, value], [0, 0.30], color='red', linestyle='-')
    x = round(quad(normalProbabilityDensity, np.NINF, value)[0], 4)
    if greater == False:
        x = round(0.5 - (1 - x - 0.5), 4)
        plt.text(value, 0.33, str(x))
    elif greater == True:
        x = round(1 - x, 4)
        plt.text(value, 0.33, str(x))
    
    plt.show()
    
"""Loaded Functions"""
# x = normal_probability_proportions(0.375, 40, 0.35, True)
# normal_probability_given(300, 400, 0.0521)

