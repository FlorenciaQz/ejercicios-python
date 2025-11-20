# Write a function to record the highest and lowest temperatures for a week.
def record_temperatures(temps):
    return [max(temps), min(temps)]

# Example usage
temperatures = [23, 19, 25, 30, 18, 22, 20]
print(record_temperatures(temperatures))