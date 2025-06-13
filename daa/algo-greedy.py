import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import time

# Data koordinat dan ID nodes
coordinates_data = {
    'ID': list(range(37)),
    'Latitude': [
        37.775196, 40.771592, 39.755092, 39.090432, 41.879535, 42.330165,
        41.499713, 40.438355, 38.892091, 39.286534, 39.951639, 40.757929,
        47.620716, 45.523104, 38.573659, 34.052187, 36.233048, 32.718834,
        33.448263, 29.425037, 30.268735, 29.759956, 32.781078, 30.042487,
        32.754920, 33.754487, 38.627522, 27.981460, 25.774252, 28.553154,
        35.231402, 35.779748, 37.540778, 38.940575, 42.358880, 44.977482,
        36.158880
    ],
    'Longitude': [
        -122.419204, -111.888189, -104.988123, -94.583653, -87.624333, -83.045913,
        -81.693716, -80.001983, -77.024055, -76.613558, -75.163808, -73.985506,
        -122.347533, -122.670132, -121.487147, -118.243425, -115.246776, -117.163841,
        -112.073821, -98.493722, -97.745209, -95.362534, -96.797111, -90.025126,
        -97.330335, -84.389663, -90.198410, -82.451142, -80.190262, -81.364438,
        -80.845841, -78.643414, -77.433928, -77.174720, -71.056820, -93.264351,
        -86.782097
    ],
    'x': [
        -1.362764e+07, -1.245534e+07, -1.168722e+07, -1.052900e+07, -9.754296e+06, -9.244629e+06,
        -9.094103e+06, -8.905780e+06, -8.574279e+06, -8.528582e+06, -8.367197e+06, -8.236029e+06,
        -1.361967e+07, -1.365558e+07, -1.352389e+07, -1.316280e+07, -1.282921e+07, -1.304262e+07,
        -1.247600e+07, -1.096427e+07, -1.088095e+07, -1.061571e+07, -1.077541e+07, -1.002155e+07,
        -1.093476e+07, -9.394214e+06, -1.004084e+07, -9.178419e+06, -8.926739e+06, -9.057448e+06,
        -8.999718e+06, -8.754545e+06, -8.219905e+06, -8.591051e+06, -7.910009e+06, -1.038214e+07,
        -9.660539e+06
    ],
    'y': [
        4.547717e+06, 4.978710e+06, 4.830416e+06, 4.734633e+06, 5.142951e+06, 5.210566e+06,
        5.086331e+06, 4.929849e+06, 4.706226e+06, 4.762799e+06, 4.858917e+06, 4.976702e+06,
        6.043986e+06, 5.704253e+06, 4.660785e+06, 4.035812e+06, 4.332736e+06, 3.858043e+06,
        3.954956e+06, 3.429856e+06, 3.538140e+06, 3.472732e+06, 3.866282e+06, 3.509012e+06,
        3.862819e+06, 3.995883e+06, 4.668457e+06, 3.246637e+06, 2.971148e+06, 3.318895e+06,
        4.195372e+06, 4.270357e+06, 4.514755e+06, 4.613163e+06, 5.214890e+06, 5.617977e+06,
        4.322505e+06
    ]
}

# Data link dari tabel
link_data = {
    'Link BW': [
        155, 155, 622, 622, 622, 155, 622, 45, 155, 155, 155, 155, 155, 155, 622, 
        155, 45, 155, 155, 622, 622, 155, 155, 622, 155, 622, 45, 622, 45, 155, 
        155, 155, 155, 155, 45, 155, 45, 155, 155, 45, 155, 155, 622, 45
    ],
    'ID Node 1': [
        12, 0, 9, 10, 3, 18, 1, 26, 4, 25, 22, 16, 0, 32, 5, 15, 34, 13, 21, 8, 4, 
        30, 15, 0, 32, 2, 3, 7, 35, 19, 17, 28, 20, 22, 27, 11, 22, 36, 21, 32, 23, 
        29, 5, 12
    ],
    'ID Node 2': [
        13, 14, 10, 11, 4, 19, 2, 36, 26, 30, 25, 1, 15, 8, 6, 17, 7, 14, 23, 9, 5, 
        31, 16, 1, 33, 3, 35, 8, 4, 20, 18, 29, 21, 24, 28, 34, 26, 30, 22, 31, 27, 
        25, 7, 1
    ]
}

# Konversi ke DataFrame
coords_df = pd.DataFrame(coordinates_data)
links_df = pd.DataFrame(link_data)

# Membuat graf dengan NetworkX
G = nx.Graph()

# Menambahkan edges ke graf
for i, row in links_df.iterrows():
    G.add_edge(row['ID Node 1'], row['ID Node 2'], weight=row['Link BW'])

# Mengatur posisi node berdasarkan koordinat x dan y
pos = {row['ID']: (row['x'], row['y']) for _, row in coords_df.iterrows()}

# # Menggambar graf
# plt.figure(figsize=(12, 8))
# nx.draw(G, pos, with_labels=True, node_color='blue', node_size=240, edge_color='black', width=2, font_size=10, font_weight='bold')
# plt.title('Graph of Nodes with Link Bandwidth and Positions')
# plt.show()

start_kruskal = time.perf_counter()
mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal')
end_kruskal = time.perf_counter()
total_kruskal = mst_kruskal.size(weight='weight') 
time_kruskal = (end_kruskal - start_kruskal) * 1000 # ms

# Waktu dan MST Prim
start_prim = time.perf_counter()
mst_prim = nx.minimum_spanning_tree(G, algorithm='prim') 
end_prim = time.perf_counter()
total_prim = mst_prim.size(weight='weight') 
time_prim = (end_prim - start_prim) * 1000 # ms

# Fungsi menggambar dengan label tambahan
def draw_graph(graph, title, pos, color='green', total_weight=None, exec_time=None):
    plt.figure(figsize=(14, 10))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color=color, width=2, font_size=9, font_weight='bold')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Tambahkan label dalam gambar
    plt.text(0.01, 0.98, title, transform=plt.gca().transAxes, fontsize=16, fontweight='bold', color='navy', verticalalignment='top', bbox=dict(facecolor='white', edgecolor='navy', boxstyle='round'))
    if total_weight is not None:
        plt.text(0.01, 0.93, f"Total Bobot: {total_weight}", transform=plt.gca().transAxes, fontsize=13, color='red', bbox=dict(facecolor='white', edgecolor='red'))

    if exec_time is not None:
        plt.text(0.01, 0.88, f"Waktu Eksekusi: {exec_time:.3f} ms", transform=plt.gca().transAxes, fontsize=13, color='darkgreen', bbox=dict(facecolor='white', edgecolor='darkgreen'))

    plt.axis('off')
    plt.show()

draw_graph(G, "Topologi CAIS", pos, color='gray')
draw_graph(mst_kruskal, "MST - Kruskal", pos, color='green', total_weight=total_kruskal, exec_time=time_kruskal)
draw_graph(mst_prim, "MST - Prim", pos, color='orange', total_weight=total_prim, exec_time=time_prim)

# Output terminal
print(f"Total Bobot MST (Kruskal): {total_kruskal}")
print(f"Waktu Eksekusi Kruskal: {time_kruskal:.3f} ms")
print(f"Total Bobot MST (Prim): {total_prim}")
print(f"Waktu Eksekusi Prim: {time_prim:.3f} ms")

