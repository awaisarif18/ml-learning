import numpy as np

# --- 1. From a Python list ---
arr_from_list = np.array([1, 2, 3, 4, 5])
print("1) From a list:", arr_from_list)
print("   dtype:", arr_from_list.dtype)
print()

# --- 2. From a list of floats (dtype auto-detected as float) ---
arr_floats = np.array([1.5, 2.5, 3.5])
print("2) From float list:", arr_floats)
print("   dtype:", arr_floats.dtype)
print()

# --- 3. Forcing a specific dtype ---
arr_forced = np.array([1, 2, 3], dtype=np.float64)
print("3) Forced float64:", arr_forced)
print("   dtype:", arr_forced.dtype)
print()

# --- 4. All zeros ---
zeros = np.zeros(5)
print("4) np.zeros(5):", zeros)
print()

# --- 5. All ones ---
ones = np.ones(5)
print("5) np.ones(5):", ones)
print()

# --- 6. A range of numbers ---
ranged = np.arange(0, 10, 2)
print("6) np.arange(0, 10, 2):", ranged)
print()

# --- 7. Evenly spaced numbers between two points (INCLUSIVE of both ends) ---
spaced = np.linspace(0, 1, 5)
print("7) np.linspace(0, 1, 5):", spaced)
print()

# --- 8. An "empty" array (uninitialized memory - values are garbage!) ---
empty = np.empty(4)
print("8) np.empty(4) - random garbage values:", empty)
print()

# --- 9. 2D array from a list of lists ---
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("9) 2D array:")
print(arr_2d)
print("   shape:", arr_2d.shape)
print()

# --- 10. Identity matrix ---
identity = np.eye(3)
print("10) np.eye(3) - identity matrix:")
print(identity)