# Write a function to divide a certain number of chocolates among a group of children.

def divide_chocolates(total_chocolates, num_children):
    if num_children == 0:
        return "Cannot divide by zero children."
    chocolates_per_child = total_chocolates // num_children
    remaining_chocolates = total_chocolates % num_children
    return chocolates_per_child, remaining_chocolates

# Example usage
total_chocolates = 25
num_children = 4
print(divide_chocolates(total_chocolates, num_children))