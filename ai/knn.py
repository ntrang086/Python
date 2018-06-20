"""Implement k-nearest neighbors."""

import math
from collections import Counter

def classify_knn(points, p, k=3):
    """Classify a point in a two-dimensional space using KNN.
    Parameters:
    points: Dictionary of training points having keys indicating classes.
             Each key have a list of training data points belong to it
    p: Test data point in the form of (x,y)
    k: Number of nearest neighbours to consider, default is 3
    This paper https://members.loria.fr/MOBerger/Enseignement/Master2/Exposes/beyer.pdf
    says that the Manhattan distance metric (L1) is the most preferable for high 
    dimensional applications, followed by the Euclidean metric (L2).
    """
    distances = []
    for key in points:
        for point in points[key]:
            distance = manhattan_distance(point, p)
            distances.append((distance, key))
    top_k_dist = sorted(distances)[:k]
    counts = Counter(x[1] for x in top_k_dist)
    return max(counts, key=lambda x: counts[x])
    
def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points a and b."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def manhattan_distance(a, b):
    """Calculate the Manhattan distance between two points a and b."""
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))


if __name__ == "__main__":
    # Dictionary of training points belonging to either 0 or 1 class
    points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2)]}
    # Number of neighbours 
    k = 3
    assert classify_knn(points, (2.5, 7),k) == 0
    assert classify_knn(points, (10, 1), k) == 1
 