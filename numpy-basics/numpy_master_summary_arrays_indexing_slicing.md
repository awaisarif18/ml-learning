# NumPy Master Summary: Arrays, Indexing & Slicing

A single reference tying together array creation, indexing, and the views-vs-copies concept.

---

## 1. The Core Idea Underneath Everything

A NumPy array is really **two things bolted together**:

1. **A raw, contiguous block of memory** — numbers packed back-to-back, all the *same* dtype
2. **A small metadata wrapper** — describes shape, dtype, and *where in memory to start reading, and how*

Every single thing in this document — creation, indexing, slicing, views — is a variation on "how do I build or read from that raw block of memory." Keep that picture in your head and everything below stops being a list of facts to memorize and becomes one consistent story.

---

## 2. Creating Arrays — Quick Reference

| Function | What it does | Example | Output |
|---|---|---|---|
| `np.array(list)` | Convert a Python list into a packed array | `np.array([1,2,3])` | `[1 2 3]` |
| `np.zeros(n)` | n zeros | `np.zeros(3)` | `[0. 0. 0.]` |
| `np.ones(n)` | n ones | `np.ones(3)` | `[1. 1. 1.]` |
| `np.arange(start, stop, step)` | Like `range()`, stop excluded | `np.arange(0,10,2)` | `[0 2 4 6 8]` |
| `np.linspace(start, stop, n)` | n evenly spaced values, **stop included** | `np.linspace(0,1,5)` | `[0. 0.25 0.5 0.75 1.]` |
| `np.empty(n)` | Allocates space, values = garbage | `np.empty(3)` | unpredictable |
| `np.eye(n)` | Identity matrix (n×n) | `np.eye(2)` | `[[1,0],[0,1]]` |

**Key distinctions to remember:**
- `arange` = "I know my **step size**" → stop is excluded (same rule as slicing!)
- `linspace` = "I know **how many points** I want" → stop is included
- dtype is auto-detected from your data, but **one dtype applies to the whole array** — this uniformity is *why* the memory can be packed tightly, which is *why* NumPy is fast.

---

## 3. Indexing Basics — Quick Reference

### 1D arrays
```python
arr = np.array([10, 20, 30, 40, 50])
#      index:     0   1   2   3   4
```
| Expression | Meaning | Result |
|---|---|---|
| `arr[0]` | first element | `10` |
| `arr[-1]` | last element | `50` |
| `arr[-2]` | second-to-last | `40` |

**Negative index formula:** `negative_index = positive_index - length`
Negative indexing lets you reach "the end" without knowing the array's length.

### 2D arrays — think **(row, column)**, like a spreadsheet
```python
arr_2d = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
```
| Expression | Meaning | Result |
|---|---|---|
| `arr_2d[1, 2]` | row 1, col 2 (preferred syntax) | `6` |
| `arr_2d[1][2]` | same result, but 2 hidden steps (builds row view, then indexes it) | `6` |
| `arr_2d[0]` | entire row 0 | `[1 2 3]` |
| `arr_2d[:, 0]` | entire column 0 (bare `:` = "every row") | `[1 4 7]` |

### Boolean masking (filtering)
```python
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25          # -> [False False True True True]
arr[mask]                 # -> [30 40 50]
arr[arr > 25] = 0          # conditional assignment — no loop needed
```

---

## 4. Slicing, Views & Copies — Quick Reference

### The syntax: `arr[start:stop:step]`
- `start` defaults to `0`
- `stop` defaults to `len(arr)` — and is **always exclusive**
- `step` defaults to `1`

### The fence-post mental model
```
        10    20    30    40    50
      |     |     |     |     |     |
      0     1     2     3     4     5
```
`arr[1:4]` cuts at post 1 and post 4 → gives you what's *between* them → `20, 30, 40`.

**Missing-number trick:** always mentally fill in the blank before reasoning.
- `arr[:3]` → rewrite as `arr[0:3]`
- `arr[3:]` → rewrite as `arr[3:len(arr)]`
- `arr[:]` → rewrite as `arr[0:len(arr)]`

### THE critical rule: view vs. copy

| Indexing style | Example | View or Copy? | Why |
|---|---|---|---|
| **Basic slicing** (`start:stop:step`) | `arr[1:4]`, `arr[::2]` | **VIEW** | Can be described as a simple formula → same memory, just a different "lens" |
| **Fancy indexing** (list of positions) | `arr[[0,2,4]]` | **COPY** | Arbitrary scattered positions can't be expressed as a formula → must physically gather into new memory |
| **Boolean masking** | `arr[arr > 25]` | **COPY** | Same reason — scattered, condition-based selection |

**Consequence:** editing a *view* mutates the original array. Editing a *copy* does not.

```python
a = arr[1:4]        # VIEW
a[0] = 999           # arr IS affected

b = arr[[1,3]]        # COPY (fancy indexing)
b[0] = 999             # arr is NOT affected
```

**Tools:**
- `.base` — tells you if an array is a view (`.base` points to the original) or owns its data (`.base is None`)
- `.copy()` — force an independent copy even from basic slicing, when you explicitly don't want the shared-memory behavior

---

## 5. The Unified Story (how all three connect)

1. **Creation** builds the raw memory block + metadata wrapper.
2. **Indexing** is how you *read or write* specific locations in that memory, addressed via row/column coordinates or conditions.
3. **Slicing** is a special case of indexing that can be expressed as a simple `start:stop:step` formula — and *because* it's just a formula, NumPy doesn't need to copy anything; it just builds new metadata pointing at the same memory (a **view**).
4. The moment your selection can't be expressed as a simple formula (arbitrary list of positions, or a condition) — NumPy is *forced* to physically copy data into a new memory block, because there's no "lens" formula that could describe it.

**One-line memorization anchor:**
> *"If I can describe my selection with `start:stop:step`, I'm looking through a window into the same house. If I need a scattered list or a condition, I'm getting a photocopy of just those rooms."*

---

## 6. Self-Test — Answer Without Running Code First

```python
arr = np.array([2, 4, 6, 8, 10, 12])
#      index:     0  1  2  3   4   5
```

1. What does `arr[2:5]` return?
2. What does `arr[:4]` return, and what is it secretly rewritten as?
3. What does `arr[::2]` return?
4. Is `arr[2:5]` a view or a copy? Why?
5. `view = arr[2:5]`, then `view[0] = 0`. What is `arr` now?
6. `copy = arr[[0, 2, 4]]`, then `copy[0] = 0`. What is `arr` now? Why is the answer different from #5?
7. What does `arr[arr > 6]` return? Is it a view or copy?
8. `arr_2d = np.array([[1,2],[3,4]])`. What does `arr_2d[:, 1]` return, and in words, what does the bare `:` mean here?
9. How would you check, in code, whether some array `x` is a view or owns its own data?
10. If you wanted to slice out part of an array but guarantee it's completely independent of the original, what would you write?

Send me your answers (with reasoning) and we'll verify each one together.
