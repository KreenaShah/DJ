import numpy as np


class KDNode:
    def __init__(self, point, split_dim=None, left=None, right=None):
        self.point = point
        self.split_dim = split_dim
        self.left = left
        self.right = right


class KDTree:
    def __init__(self, data):
        self.root = self._build_tree(data)

    def add_node(self, root, datapoint, split_dim):
        if datapoint[split_dim]<root.point[split_dim]:
            if root.left:
                return self.add_node(root.left, datapoint, (split_dim+1)%len(datapoint))
            else:
                root.left = KDNode(
                    point = datapoint,
                    split_dim = split_dim,
                    )
        else:
            if root.right:
                return self.add_node(root.right, datapoint, (split_dim+1)%len(datapoint))
            else:
                root.right = KDNode(
                    point = datapoint,
                    split_dim = split_dim,
                    )
    
    def _build_tree(self, data, index=0, depth=0):
        if data.shape[0] == None:
            return None
        if index==0:
             root = KDNode(
                point = data[index],
                split_dim = 0
                )
        for i in range(1, len(data)):
            self.add_node(root, data[i], 0)
        return root

    def nearest_neighbor(self, query_point):
        best_point, best_dist = self._search(self.root, query_point, float("inf"))
        return best_point

    def _search(self, node, query_point, best_dist):
        if node is None:
            return None, best_dist

        dist = self._euclidean_dist(node.point, query_point)
        if dist < best_dist:
            best_point, best_dist = node.point, dist
        else:
            best_point = None

        split_val = node.point[node.split_dim]
        if query_point[node.split_dim] < split_val:
            near_node = node.left
            far_node = node.right
        else:
            near_node = node.right
            far_node = node.left

        near_best, near_best_dist = self._search(near_node, query_point, best_dist)

        if near_best_dist < best_dist:
            best_point, best_dist = near_best, near_best_dist

        if abs(query_point[node.split_dim] - split_val) < best_dist:
            far_best, far_best_dist = self._search(far_node, query_point, best_dist)

            if far_best_dist < best_dist:
                best_point, best_dist = far_best, far_best_dist

        return best_point, best_dist

    @staticmethod
    def _euclidean_dist(a, b):
        return np.linalg.norm(a - b)

# Generate some random data
data = np.random.rand(100, 3)

# Build a KD tree from the data
tree = KDTree(data)

# Query for the nearest neighbor to a random point
query_point = np.random.rand(3)
nearest_neighbor = tree.nearest_neighbor(query_point)

print("Query point: ", query_point)
print("Nearest neighbor: ", nearest_neighbor)