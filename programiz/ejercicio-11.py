# Write a function to check if all numbers on a given list are prime
def all_primes(numbers):
    for n in numbers:
        if not is_prime(n):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Example usage
list_of_numbers = [2, 3, 5, 7, 11, 13]
print(all_primes(list_of_numbers)) 