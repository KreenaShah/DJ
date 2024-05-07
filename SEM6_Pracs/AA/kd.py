from sklearn.neighbors import KDTree
import numpy as np

data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])

kdtree = KDTree(data, leaf_size=30)

query_point = np.array([[9, 2]])
distances, indices = kdtree.query(query_point, k=2)

print("Query Point:", query_point)
print("Nearest Neighbors:")
for i, idx in enumerate(indices[0]):
	print(f"Neighbor {i + 1}: {data[idx]}, Distance: {distances[0][i]}")
