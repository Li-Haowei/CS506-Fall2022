import math
import itertools
#from numpy.linalg import norm

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(a, b):
     return math.sqrt(sum([a1**2 + b1**2 for a1, b1 in zip(a, b)]))


def jaccard_dist(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def cosine_sim(a, b):
    return dot(a, b)/((a)*(b))
def dot(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))
# Feel free to add more
