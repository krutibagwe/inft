import numpy as np
# Function to compute the Euclidean distance
def euclidean_distance(x1, x2):
    return np.abs(x1 - x2)

# K-means clustering algorithm
def kmeans(data, k, max_iterations=100):
    # Step 1: Randomly initialize centroids
    centroids = np.random.choice(data, k, replace=False)
    print("Initial centroids:", centroids)

    for iteration in range(max_iterations):
        print(f"\nIteration {iteration + 1}:")
        
        # Step 2: Assign each point to the closest centroid
        clusters = {i: [] for i in range(k)}
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid = np.argmin(distances)
            clusters[closest_centroid].append(point)

        # Step 3: Update centroids
        new_centroids = np.array([np.mean(clusters[i]) if len(clusters[i]) > 0 else centroids[i] for i in range(k)])

        # Step 4: Display the clusters and new centroids
        print("Clusters:", clusters)
        print("New centroids:", new_centroids)

        # Step 5: Check if centroids don't change
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, clusters

data = np.array([2, 25, 10, 15, 5, 20, 4, 40])
# Number of clusters (k)
k = 2
final_centroids, final_clusters = kmeans(data, k)

# Final output
print("\nFinal centroids:", final_centroids)
print("Final clusters:", final_clusters)
print("STOP as clusters are the same.")
