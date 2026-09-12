# 🔄 Sorting Techniques

<div align="center">

## 🧠 Understanding How Algorithms Sort Data

A collection of **Sorting Algorithms implemented in Python**, with complexity analysis and visual simulations.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![DSA](https://img.shields.io/badge/DSA-Sorting-181717?style=for-the-badge)]()
[![Algorithms](https://img.shields.io/badge/Algorithms-Sorting-blue?style=for-the-badge)]()
[![Practice](https://img.shields.io/badge/Practice-Daily-success?style=for-the-badge)]()

[![GitHub](https://img.shields.io/badge/👨🏻‍💻_GitHub-AravindInish-181717?style=for-the-badge)](https://github.com/AravindInish)
[![Visualizer](https://img.shields.io/badge/🎮_Sorting_Visualizer-Explore-orange?style=for-the-badge)](https://visualgo.net/en/sorting)

</div>

---

## 📌 About

Sorting is one of the most fundamental concepts in **Data Structures & Algorithms**.

This section contains my implementations and practice of different sorting techniques using **Python**, along with their performance characteristics.

> 🎯 **Goal:** Understand how each sorting algorithm works, when to use it, and how efficiently it performs.

---

## 📊 Sorting Algorithms

| 🔢 Algorithm      |   🟢 Best  | 🟡 Average |  🔴 Worst  |  💾 Space | 🔒 Stable |
| :---------------- | :--------: | :--------: | :--------: | :-------: | :-------: |
| 🫧 Bubble Sort    |    O(n)    |    O(n²)   |    O(n²)   |    O(1)   |     ✅     |
| 🎯 Selection Sort |    O(n²)   |    O(n²)   |    O(n²)   |    O(1)   |     ❌     |
| 🃏 Insertion Sort |    O(n)    |    O(n²)   |    O(n²)   |    O(1)   |     ✅     |
| 🔀 Merge Sort     | O(n log n) | O(n log n) | O(n log n) |    O(n)   |     ✅     |
| ⚡ Quick Sort      | O(n log n) | O(n log n) |    O(n²)   | O(log n)* |     ❌     |
| 🏔️ Heap Sort     | O(n log n) | O(n log n) | O(n log n) |    O(1)   |     ❌     |

<sub>*Quick Sort space complexity depends on recursion depth and implementation.</sub>

---

## 🎮 Algorithm Simulation

Seeing an algorithm in action makes the logic much easier to understand.

### 🔬 Try It Yourself

| Algorithm         | Visualization                                       |
| :---------------- | :-------------------------------------------------- |
| 🫧 Bubble Sort    | [▶️ **Visualize**](https://visualgo.net/en/sorting) |
| 🎯 Selection Sort | [▶️ **Visualize**](https://visualgo.net/en/sorting) |
| 🃏 Insertion Sort | [▶️ **Visualize**](https://visualgo.net/en/sorting) |
| 🔀 Merge Sort     | [▶️ **Visualize**](https://visualgo.net/en/sorting) |
| ⚡ Quick Sort      | [▶️ **Visualize**](https://visualgo.net/en/sorting) |
| 🏔️ Heap Sort     | [▶️ **Visualize**](https://visualgo.net/en/sorting) |

> 🎮 **Simulation:** Watch elements compare, swap, divide, merge, and move into their correct positions.

---

## 🧩 Algorithms

### 🫧 Bubble Sort

Repeatedly compares adjacent elements and swaps them when they are in the wrong order.

**Best for:** Understanding the basics of sorting and swapping.

---

### 🎯 Selection Sort

Finds the minimum element from the unsorted portion and places it at its correct position.

**Best for:** Learning selection-based sorting.

---

### 🃏 Insertion Sort

Builds the sorted portion of an array one element at a time.

**Best for:** Small or nearly sorted datasets.

---

### 🔀 Merge Sort

Uses the **Divide & Conquer** approach by splitting the array and merging sorted portions.

**Best for:** Guaranteed `O(n log n)` performance.

---

### ⚡ Quick Sort

Selects a pivot and partitions the array around it.

**Best for:** Efficient in-memory sorting with good average performance.

---

### 🏔️ Heap Sort

Uses a **Binary Heap** to repeatedly extract the largest or smallest element.

**Best for:** Guaranteed `O(n log n)` sorting with `O(1)` auxiliary space.

---

## 🐍 Python

All implementations are written from scratch in **Python** to understand the underlying algorithms instead of relying on Python's built-in `sort()`.

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
```

---

## 🧠 What I'm Learning

Through these algorithms, I'm building an understanding of:

**🔹 Time Complexity**
**🔹 Space Complexity**
**🔹 Stable vs Unstable Sorting**
**🔹 In-place Algorithms**
**🔹 Divide & Conquer**
**🔹 Recursion**
**🔹 Array Manipulation**
**🔹 Algorithm Optimization**

---

## 📚 Resources

🔗 [Visualgo — Algorithm Visualization](https://visualgo.net/en/sorting)

🔗 [Python Documentation](https://docs.python.org/3/)

---

<div align="center">

### 🚀 Learn → Visualize → Implement → Optimize

**Every algorithm understood is another step toward mastering DSA.**

⭐ If you find this useful, consider starring the repository.

</div>
