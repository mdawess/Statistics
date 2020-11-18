from matplotlib import pyplot as plt
import math

def factorial(n):
   if n < 1:   # base case
       return 1
   else:
       returnNumber = n * factorial(n - 1)  # recursive call
       return returnNumber

def binomial_probability(sample, num, success):
    """Calculates the binomial probability for a single occurance. 
    Sample is the number of tests, num is the number which we are 
    looking to find the probability of occurance for and success 
    is the probability of success (p)."""

    term1 = factorial(sample)/(factorial(num)*factorial(sample - num))
    term2 = success ** num
    term3 = (1 - success) ** (sample - num)
    prob = term1 * term2 * term3

    return round(prob, 4)

def binomial_prob_greater_than(sample, num, success):
    """Finds the probability that the outcome is successful num 
    times or greater."""

    base = 1
    i = num - 1
    while i >= 0:
        base -= binomial_probability(sample, i, success)
        i -= 1

    return round(base, 4)

def binomial_distribution(sample, success):
    """Graphs the binomial distribution of a discrete random variable.
    Sample is the number of tests and success is the probability of success.
    """

    y = []
    #if len(y) == 0:
        #y.append(binomial_probability(sample, 0, success))
    for i in range(0, sample + 1):
        y.append(binomial_probability(sample, i, success))

    x = []
    for i in range(0, sample + 1):
        x.append(i)

    plt.bar(x, y)
    # for i, v in enumerate(y):
    #     plt.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')
    if sample < 20:
        for i in range(len(x)):
            plt.text(x[i], y[i] + 0.01, str(y[i]), color='black', rotation=45)
    plt.show()
    return None

def discrete_distribution(values, probablities):
    """Takes a list of values and their probabilities and graphs them and
    calculates the mean and standard deviation.""" #plot std as well

    mean = 0
    for i in range(0, len(values)):
        mean += values[i] * probablities[i]
    mean = round(mean, 5)
    
    var = 0
    for i in range(0, len(values)):
        var += ((values[i] - mean) ** 2) * probablities[i]
    
    stddev = math.sqrt(var)
    stddev = round(stddev, 5)

    standardized = []
    for i in range(0, len(values)):
        standardized.append((values[i] - mean)/stddev)

    plt.bar(values, probablities)
    plt.title("Mean = " + str(mean) + ", Stddev = " + str(stddev) + ", Var = " + str(round(stddev ** 2, 3)))
    plt.xticks(values)
    
    # Uncomment to view the standardized plot
    # plt.bar(standardized, probablities)
    # plt.title("Standardized Plot")
    plt.show()
    return None

y = binomial_probability(1400, 868, 0.65)
x = binomial_prob_greater_than(25, 5, 0.12)
#z = binomial_distribution(10, 0.60)
print(y)

values = [0.99, 1.99, 2.99, 3.99, 4.99]
probablities = [0.4823, 0.3858, 0.1157, 0.0154, 0.0008]
#k = discrete_distribution(values, probablities)
#print(k)



