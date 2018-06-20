"""Implement k-nearest neighbors.
1) https://members.loria.fr/MOBerger/Enseignement/Master2/Exposes/beyer.pdf
describes which situations KNN works or doesn't work.

2) https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
If a constant number of examples is distributed uniformly in a 
high-dimensional hypercube, beyond some dimensionality most examples are closer
to a face of the hypercube than to their nearest neighbor. And if we 
approximate a hypersphere by inscribing it in a hypercube, in high dimensions
almost all the volume of the hypercube is outside the hypersphere.

3) https://bib.dbvis.de/uploadedFiles/155.pdf
The Manhattan distance metric (L1) is the most preferable for high 
dimensional applications, followed by the Euclidean metric (L2).
"""

import math
from collections import Counter

def classify_knn(points, p, k=3):
    """Classify a point using KNN.
    Parameters:
    points: Dictionary of training points having keys indicating classes.
             Each key have a list of training data points belong to it
    p: Test data point in the form of (x,y)
    k: Number of nearest neighbours to consider, default is 3
    """
    distances = []
    for key in points:
        for point in points[key]:
            # Compute Manhattan distance
            distance = calculate_distance(point, p, 1)
            distances.append((distance, key))
    top_k_dist = sorted(distances)[:k]
    counts = Counter(x[1] for x in top_k_dist)
    return max(counts, key=lambda x: counts[x])

def calculate_distance(a, b, k=1/2):
    """Calculate the distance between two points a and b.
    k = 1: Manhattan distance
    k = 2: Euclidean distance
    k < 1: fractional distance, proposed by the "Surprising Behavior" paper 
    (https://bib.dbvis.de/uploadedFiles/155.pdf). "Fractional norms" exhibit 
    the property of increasing the contrast between farthest and nearest 
    points. This may be useful in some contexts, however there is a caveat:
    these "fractional norms" are not proper distance metrics because they
    violate the triangle inequality. If the triangle inequality is an important
    quality to have in your research, then fractional metrics are not going
    to be tremendously useful. (https://stats.stackexchange.com/a/99191)
    """
    result = 0
    for i in range(len(a)):
        result += math.pow(abs(a[i] - b[i]), k)
    return math.pow(result, 1/k)


if __name__ == "__main__":
    # Dictionary of training points belonging to either 0 or 1 class
    points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2)]}
    # Number of neighbours 
    k = 3
    assert classify_knn(points, (2.5, 7),k) == 0
    assert classify_knn(points, (10, 1), k) == 1
 