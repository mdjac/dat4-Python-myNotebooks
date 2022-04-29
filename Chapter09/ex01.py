import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sklearn
from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score
from sklearn.cluster import MeanShift, estimate_bandwidth
mpl.use("pdf")

#Own plot
#Task 1-3
''' load 'data/iris_data.csv' into a dataframe (use decimal=',') and remove the 2 Petal columns. Now we are left with a 2D feature space
get unique labels (Species column)
plot with a scatter plot each iris flower sample colored by label (3 different colors) '''
iris = pd.read_csv('../../data/iris_data.csv', decimal=",")
iris = iris.drop(columns=["Petal length","Petal width"])

#Used for test with christian
iris_copy = iris.copy(deep=True)

d = dict(tuple(iris.groupby("Species")))
print(type(d["I. setosa"]))

fig = plt.figure()
ax = fig.add_subplot(111)
for key,value in d.items():
    x_values = value["Sepal length"].tolist()
    y_values = value["Sepal width"].tolist()
    ax.scatter(x_values,y_values)


#MeanShift cluster centers
#Task 4 & 5
''' use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result)
print out labels, cluster centers and number of clusters (as returned from the MeanShift function) '''
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


iris = iris.drop(columns=["Species"])
labels, cluster_centers, n_clusters = mean_shift(iris)
print(cluster_centers)
print(type(labels))
print(labels)
print(n_clusters)

for i in range(len(cluster_centers)):
    ax.scatter(cluster_centers[i][0],cluster_centers[i][1],c="k", s=100, linewidth=0.2)

fig.savefig('3_1.png', bbox_inches='tight')


#Task 6-9
''' create a new scatter plot where each flower is colored according to cluster label
add a dot for the cluster centers
Compare the 2 plots (colored by actual labels vs. colored by cluster label)
Try changing the 'quantile' argument to 0.15 and see what happens to your cluster plot. '''
iris["cluster"] = labels.tolist()
print(iris)
d_ = dict(tuple(iris.groupby("cluster")))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
for key,value in d_.items():
    x_values = value["Sepal length"].tolist()
    y_values = value["Sepal width"].tolist()
    ax2.scatter(x_values,y_values)


for i in range(len(cluster_centers)):
    ax2.scatter(cluster_centers[i][0],cluster_centers[i][1],c="k", s=100, linewidth=0.2)

fig2.savefig('3_2.png', bbox_inches='tight')


#Test with Christian for 3rd assignment in python

#Label encoding
iris_copy["Species"] = iris_copy["Species"].astype('category')
iris_copy["Category"] = iris_copy["Species"].cat.codes

labels_true = iris_copy["Category"].tolist()
labels_pred = labels.tolist()

print(labels_true)
print(labels_pred)
print('The scikit-learn version is {}.'.format(sklearn.__version__))
result = adjusted_rand_score(labels_true, labels_pred)
print(result)

test1 = [1,1,1,2,2,2,3,0,1,2,3,4,10,6]
test2 = [1,1,1,2,2,2,3,0,1,2,100000,4,10,10]

result2 = adjusted_rand_score(test1, test2)
print(result2)


