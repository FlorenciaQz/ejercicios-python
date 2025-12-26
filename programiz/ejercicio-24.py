# Write a function to calculate de digit distance between two integers

def digit_distance(num1, num2):
    result = 0

    digits1 = [int(d) for d in str(num1)]
    digits2 = [int(d) for d in str(num2)]

    for d1, d2 in zip(digits1, digits2):
        result += abs(d1 - d2)
    return result
