import math

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

print(valid_normal_approx(400, 0.428))