import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from itertools import cycle
import sklearn
from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
mpl.use("pdf")


centers = [[2, 1], [0, 0], [1, -1]]
data_2d, target = make_blobs(n_samples=2500, centers=centers, cluster_std=0.1)

print(data_2d)
print(target)


def mean_shift(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.15, 
                                   n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))
    
    return labels, cluster_centers, n_clusters

labels, cluster_centers, n_clusters = mean_shift(data_2d)


_labels = labels.tolist()
_target = target.tolist()


result = adjusted_rand_score(_target, _labels)
print(result)

# Plot the clusters in different colors
fig = plt.figure()
ax = fig.add_subplot(111)

colors = cycle('bgrcmy')
print(list(zip(range(3),colors)))
for k, col in zip(range(n_clusters), colors):
    my_members = (labels == k)
    cluster_center = cluster_centers[k]
    
    x, y = data_2d[my_members,0], data_2d[my_members,1]
    ax.scatter(x, y, c=col, linewidth=0.2)
    ax.scatter(cluster_center[0], cluster_center[1], c='k', s=50, linewidth=0.2)
    
plt.title('Estimated number of clusters: {}'.format(n_clusters))

fig.savefig('test.png', bbox_inches='tight')
