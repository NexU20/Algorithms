import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater_equal = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater_equal)

def measure_time(sort_function, arr):
    start = time.time()
    sort_function(arr.copy())
    end = time.time()
    return end - start

# Generate performance data
array_sizes = [10, 100, 1000, 10000]
bubble_times = []
quick_times = []

for size in array_sizes:
    test_array = [random.randint(1, 1000) for _ in range(size)]
    bubble_times.append(measure_time(bubble_sort, test_array))
    quick_times.append(measure_time(quick_sort, test_array))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, bubble_times, label='Bubble Sort (Brute Force)', marker='o')
plt.plot(array_sizes, quick_times, label='Quick Sort', marker='s')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (s)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()