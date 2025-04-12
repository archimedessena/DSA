import random
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    # point1 and point2 are lists like [x, y]
    total = 0
    for i in range(len(point1)):
        total += (point1[i] - point2[i]) ** 2  # (x1 - x2)^2 + (y1 - y2)^2
    return math.sqrt(total)  # Square root of the sum

# K-means algorithm function
def kmeans(data, k, max_iterations=100):
    # Step 1: Randomly pick k points as starting centroids
    centroids = random.sample(data, k)  # Choose k random points from data
    
    # Keep track of clusters for each point
    for _ in range(max_iterations):
        # Step 2: Create empty clusters
        clusters = [[] for _ in range(k)]  # List to store points for each cluster
        
        # Step 3: Assign each point to the nearest centroid
        for point in data:
            # Find the closest centroid
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid_index = distances.index(min(distances))  # Get index of smallest distance
            clusters[closest_centroid_index].append(point)  # Add point to that cluster
        
        # Save old centroids to check if they move
        old_centroids = centroids.copy()
        
        # Step 4: Update centroids to the mean of each cluster
        for i in range(k):
            if clusters[i]:  # Only update if cluster isn't empty
                # Calculate average (mean) of all points in the cluster
                new_centroid = []
                for dimension in range(len(data[0])):  # For each x, y, etc.
                    avg = sum(point[dimension] for point in clusters[i]) / len(clusters[i])
                    new_centroid.append(avg)
                centroids[i] = new_centroid
        
        # Step 5: Check if centroids stopped moving (convergence)
        centroid_moved = False
        for i in range(k):
            if euclidean_distance(old_centroids[i], centroids[i]) > 0.0001:  # Small threshold
                centroid_moved = True
                break
        if not centroid_moved:
            break  # Stop if centroids didn't move
    
    return clusters, centroids

# Example usage
if __name__ == "__main__":
    # Sample data: list of [x, y] points
    data = [
        [1, 2], [1, 4], [1, 0],
        [10, 2], [10, 4], [10, 0],
        [5, 3], [5, 5], [5, 1]
    ]
    
    # Run k-means with k=3 clusters
    k = 3
    clusters, centroids = kmeans(data, k)
    
    # Print results
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}: {cluster}")
    print(f"Final centroids: {centroids}")