import random
import matplotlib.pyplot as plt

# Brute Force: hitung jumlah perbandingan
def brute_force_count(arr):
    minimum = arr[0]
    maximum = arr[0]
    comparisons = 0

    for i in range(1, len(arr)):
        # satu perbandingan untuk min
        comparisons += 1
        if arr[i] < minimum:
            minimum = arr[i]
        # satu perbandingan untuk max
        comparisons += 1
        if arr[i] > maximum:
            maximum = arr[i]

    return comparisons

# Divide and Conquer: hitung jumlah perbandingan dan hasil min/max
def dac_count(arr, low, high):
    # kasus dasar satu elemen
    if low == high:
        return arr[low], arr[low], 0

    # kasus dasar dua elemen
    if high == low + 1:
        comparisons = 1
        if arr[low] < arr[high]:
            return arr[low], arr[high], comparisons
        else:
            return arr[high], arr[low], comparisons

    # rekursi
    mid = (low + high) // 2
    lmin, lmax, lcmp = dac_count(arr, low, mid)
    rmin, rmax, rcmp = dac_count(arr, mid + 1, high)

    # gabungkan hasil
    comparisons = lcmp + rcmp
    comparisons += 1  # perbandingan untuk min
    current_min = lmin if lmin < rmin else rmin
    comparisons += 1  # perbandingan untuk max
    current_max = lmax if lmax > rmax else rmax

    return current_min, current_max, comparisons

# Wrapper untuk memanggil D&C
def divide_and_conquer_count(arr):
    _, _, comparisons = dac_count(arr, 0, len(arr) - 1)
    return comparisons

# Uji berbagai ukuran array
sizes = [1000, 10000, 100000, 1000000, 10000000]
bf_counts = []
dc_counts = []

for N in sizes:
    arr = [random.randint(1, 10000000) for _ in range(N)]
    bf_counts.append(brute_force_count(arr))
    dc_counts.append(divide_and_conquer_count(arr))

# Plot hasil
plt.figure()
plt.plot(sizes, bf_counts, label='Brute Force')
plt.plot(sizes, dc_counts, label='Divide and Conquer')
plt.xlabel('Panjang Array (N)')
plt.ylabel('Jumlah Komparasi')
plt.title('Perbandingan Jumlah Komparasi Algoritma BF vs D&C')
plt.legend()
plt.tight_layout()
plt.show()