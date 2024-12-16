import numpy as np
import matplotlib.pyplot as plt

def random_colors(k):
    np.random.seed(50)
    colors = []
    while len(colors) < k:
        r, g, b = np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)
        if not (g > r * 1.2 and g > b * 1.2):
            colors.append((r, g, b))
    return np.array(colors) / 255.0

def visualize(centroids, points, classification = [], k = 0, title = "") ->None:
    plt.title(title)
    if len(classification) == 0:
        plt.scatter(centroids[:, 0], centroids[:, 1], c='green', marker='o')
        plt.scatter(points[:, 0], points[:, 1], c='blue', marker='o')
    else:
        colors = random_colors(k)
        for i, point in enumerate(points):
            plt.scatter(point[0], point[1], color=colors[classification[i]], marker='o')
        plt.scatter(centroids[:, 0], centroids[:, 1], c='green', marker='o')
    plt.show()

def init_centroids(k: int, points: np.ndarray) -> np.ndarray:
    n: int = len(points) // k
    indicies: np.ndarray = np.arange(len(points))
    np.random.shuffle(indicies)
    init_centroids: np.ndarray = np.array([np.mean(points[indicies[n * i:n *(i + 1)]], axis = 0) for i in range(0, k)])
    return init_centroids

def k_means(points, centroids, k):
    classification = []
    new_centroids: np.ndarray = np.zeros((k, points.shape[1]))
    clusters: list = [[] for _ in range(k)]
    for point in points:
        distances = [np.linalg.norm(point- centroid) for centroid in centroids]
        classification.append(np.argmin(distances))
        clusters[classification[-1]].append(point)

    #visualize(centroids, points, classification,k, title = "New Clusters")
    for i in range(len(centroids)):
        if len(clusters[i]) == 0:
            new_centroids[i] = points[np.random.randint(0, points.shape[0])]
        else:
            new_centroids[i] = np.mean(clusters[i], axis = 0)
    #visualize(new_centroids, points, classification,k, title = "Moved Centoids")
    return classification, new_centroids

def is_not_converged(last_centroids: np.ndarray, current_centroids: np.ndarray, e: float = 1e-20) -> bool:
    dist: float = 0
    for  i in range(len(last_centroids)):
        dist += np.sqrt(np.sum((last_centroids[i] - current_centroids[i]) ** 2))
    print(dist)
    return dist > e

def outlying_distances(points: np.ndarray) -> list:
    mean_val: np.ndarray = np.mean(points, axis = 0)
    dist: list = [np.linalg.norm(point - mean_val) for point in points]
    return dist

k = 5
n_points_per_cl = 200
clusters = []
n = 20
centroids = np.zeros((k,2))
classification = []

n_clusters = 1
pos = [[n,n], [-n,n], [n,-n], [-n,-n]]

#Ensures that the random numbers are the same every time the algorithm is run
np.random.seed(2104013275)

for i in range(n_clusters):
    clusters.append(np.random.randn(n_points_per_cl, 2) + np.array(pos[i]))
points = np.vstack(clusters)
print(outlying_distances(points))
centroids = init_centroids(k, points)

last_centroids = np.zeros_like(centroids)
while is_not_converged(last_centroids, centroids):
    last_centroids = centroids
    classification, centroids = k_means(points,centroids,k)

