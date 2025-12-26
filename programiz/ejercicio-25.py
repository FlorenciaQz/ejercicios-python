# Return the central binomial coefficient of the input number

def central_binomial_coefficient(n):
    return factorial(2 * n) // factorial(n) ** 2

def factorial(n):
    sol = 1
    for i in range(1, n+1):
        sol *= i
    return sol