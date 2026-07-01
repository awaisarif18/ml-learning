import numpy as np

# --- Experiment 1: slicing gives a VIEW ---
original_array = np.array([10, 20, 30, 40, 50])
sliced_array = original_array[1:4]

sliced_array[0] = 9999

print("Experiment 1: slicing = view")
print("Original array:", original_array)
print("Sliced array:  ", sliced_array)
print()

# --- Experiment 2: .copy() gives an independent copy ---
original_array_2 = np.array([10, 20, 30, 40, 50])
safe_copy = original_array_2[1:4].copy()

safe_copy[0] = 9999

print("Experiment 2: .copy() = independent")
print("Original array:", original_array_2)
print("Safe copy:     ", safe_copy)