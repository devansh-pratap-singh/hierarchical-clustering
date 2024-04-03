import numpy as np

#Distance between two points
def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

#Clustering function
def hClustering(data, k):
    n = len(data)
    distances = np.zeros((n, n))
    for i in range(n):
        distances[i, i+1:] = [dist(data[i], data[j]) for j in range(i+1, n)]
        distances[i+1:, i] = distances[i, i+1:]
    
    clusters = [{i} for i in range(n)]
    
    while len(clusters) > k:
        # Find the two closest clusters
        min_distance = np.inf
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                distance = np.max([distances[x,y] for x in clusters[i] for y in clusters[j]])
                if distance < min_distance:
                    min_distance = distance
                    merge_i, merge_j = i, j

        # Merge the two closest clusters
        clusters[merge_i] = clusters[merge_i].union(clusters[merge_j])
        del clusters[merge_j]

    return clusters

if __name__ == "__main__":
    #Example
    data = np.array([[3,2], [7,4], [5,2], [2,7], [9,3], [1,2], [0,4], [2,3], [2,7], [2,9]])
    clusters = hClustering(data, 3)
    print(clusters)