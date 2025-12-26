# Write a function to return the last letter of each number on a list
def last_letters(numbers):
    last_letters_list = []
    for number in numbers:
        last_letters_list.append(str(number)[-1])
    return last_letters_list

# Example usage
numbers_list = [123, 456, 789, 1011, 1213]
print(last_letters(numbers_list))