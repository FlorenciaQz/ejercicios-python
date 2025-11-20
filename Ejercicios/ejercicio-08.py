# Write a function to calculate the probability of a basketball player making a free throw
def free_throw_probability(made_shots, total_shots):
    if total_shots == 0:
        return 0.0
    return made_shots / total_shots

# Example usage
made = 5
total = 10
print(free_throw_probability(made, total))