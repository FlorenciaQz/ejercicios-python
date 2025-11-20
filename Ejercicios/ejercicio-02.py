# Write a function to create a new list from an existing list using list slicing.
def list_slicing(lst, start_index, end_index):
    return lst[start_index:end_index]

# Example usage
my_list = [10, 2, 30, 40, 50, 60, 7, 80, 90]
start = 2   
end = 7
print(list_slicing(my_list, start, end))