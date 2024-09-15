import numpy as np
import random
import matplotlib.pyplot as plt
from texttable import Texttable

# Sample data extracted from the article
data = {
    'Produk': [
        'Nugget Fiesta', 'Nugget So Good', 'Nugget Kanzler', 'Nugget Belfoods', 'Nugget Champ',
        'Nugget Sunny Gold', 'Nugget Goldstar', 'Nugget Ciki Wiki', 'Nugget Akumo', 'Nugget Hato',
        'Baso Sapi Cap Mantap', 'Baso Sapi Cap Oke', 'Baso Sapi Cap Manja', 'Baso Ayam',
        'Baso Ikan', 'Sosis Kanzler', 'Sosis Champ', 'Sosis Fiesta', 'Sosis Curah', 'Karage Fiesta',
        'Ayam Beku', 'Ayam Cincang', 'Drumb Stick', 'Karage Kanzler', 'Karage So Good',
        'Karage Champ', 'Dimsum Ayam', 'Dimsum Sapi', 'Dimsum Udang', 'Beef Kanzler',
        'Stick crab', 'Tofu Cap Ena', 'Tofu Cap Nikmat', 'Spicy Wings So Good', 'Spicy Wings Kanzler',
        'Spicy Wings Fiesta', 'French Fries Golden Star', 'French Fries So Good', 'French Fries Champ',
        'French Fries Kanzler', 'Bakso Tahu', 'Bakso Cireng', 'Cireng Isi ayam', 'Cireng Rujak',
        'Cireng Isi Daging'
    ],
    'Penjualan': [
        5281, 6992, 768, 23706, 18795, 16979, 33249, 2143, 3578, 201,
        410, 49, 103, 45, 56, 6069, 245, 409, 21, 23,
        112, 32, 182, 3177, 308, 669, 14, 3, 110, 602,
        758, 422, 553, 394, 579, 347, 60, 40, 22, 225,
        11, 97, 5, 6, 30
    ],
    'Rata-rata': [
        660.125, 874, 104.75, 2963.25, 2349.375, 2122.375, 4156.125, 267.875, 447.25, 25.125,
        51.25, 6.125, 12.875, 5.625, 7, 758.625, 30.625, 51.125, 2.625, 2.875,
        48, 4, 22.75, 397.125, 46.05, 83.625, 1.75, 0.375, 13.75, 75.25,
        94.75, 52.75, 69.125, 49.25, 72.375, 43.375, 7.5, 5, 2.75, 28.125,
        1.375, 12.125, 0.625, 0.75, 3.75
    ]
}

# Create data matrix
X = np.array(list(zip(data['Penjualan'], data['Rata-rata'])))

# Number of clusters
k = 2

# Initialize centroids randomly
centroids = X[random.sample(range(X.shape[0]), k)]

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Function to perform k-means clustering
def k_means(X, centroids, k):
    clusters = np.zeros(len(X))
    prev_centroids = np.zeros(centroids.shape)
    diff = euclidean_distance(centroids, prev_centroids)

    while diff != 0:
        for i in range(len(X)):
            distances = np.array([euclidean_distance(X[i], c) for c in centroids])
            cluster = np.argmin(distances)
            clusters[i] = cluster

        prev_centroids = centroids.copy()

        for j in range(k):
            points = [X[i] for i in range(len(X)) if clusters[i] == j]
            centroids[j] = np.mean(points, axis=0)

        diff = euclidean_distance(centroids, prev_centroids)

    return clusters, centroids

clusters, centroids = k_means(X, centroids, k)

cluster_counts = np.bincount(clusters.astype(int))

t = Texttable()
items =[]

for i in range(k):
    print(f"Cluster {i + 1} memiliki jumlah produk = {cluster_counts[i]} items.")
    cluster_items = [data['Produk'][j] for j in range(len(clusters)) if clusters[j] == i]
    items.append(', '.join(cluster_items))

t.add_rows([["Cluster", "Jumlah", "Items"], [1, cluster_counts[0], items[0]], [2, cluster_counts[1], items[1]]])
print(t.draw(), '\n')

# plt.scatter(data['Penjualan'], data['Rata-rata'])
# plt.show()

# Print centroids
print("Final Centroids:\n", centroids)

# Plotting
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='red')
plt.grid()
plt.xlabel('Penjualan')
plt.ylabel('Rata-rata')
plt.title('K-Means Clustering Pada Penjualan Frozen Food')
plt.show()