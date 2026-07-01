import numpy as np

# ============================================
# PART A: 1D array indexing
# ============================================
arr = np.array([10, 20, 30, 40, 50])

print("--- 1D indexing ---")
print("arr[0]  (first element):", arr[0])
print("arr[4]  (last element): ", arr[4])
print("arr[-1] (last, negative index):", arr[-1])
print("arr[-2] (second-to-last):", arr[-2])
print()

print("Negative index cheat sheet for this array:")
for i in range(len(arr)):
    print(f"  arr[{i}] == arr[{i - len(arr)}]  ->  {arr[i]} == {arr[i - len(arr)]}")
print()


# ============================================
# PART B: 2D array indexing
# ============================================
arr_2d = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
])

print("--- 2D indexing ---")
print("Full array:")
print(arr_2d)
print()

print("arr_2d[1][2]  (chained, works but not preferred):", arr_2d[1][2])
print("arr_2d[1, 2]  (comma style, the NumPy way):        ", arr_2d[1, 2])
print()

print("arr_2d[0]     (entire row 0):", arr_2d[0])
print("arr_2d[:, 0]  (entire column 0):", arr_2d[:, 0])
print()

print("arr_2d[0:2, 1:3]  (rows 0-1, cols 1-2):")
print(arr_2d[0:2, 1:3])
print()


# ============================================
# PART C: Boolean indexing (filtering)
# ============================================
print("--- Boolean indexing ---")
arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25
print("mask = arr > 25  ->", mask)
print("arr[mask]        ->", arr[mask])
print("arr[arr > 25]    ->", arr[arr > 25])
print()


# ============================================
# PART D: Modifying via indexing
# ============================================
print("--- Modifying via indexing ---")
arr = np.array([10, 20, 30, 40, 50])
arr[0] = 999
print("After arr[0] = 999:", arr)

arr[1:3] = [111, 222]
print("After arr[1:3] = [111, 222]:", arr)

arr[arr > 200] = 0
print("After arr[arr > 200] = 0:", arr)