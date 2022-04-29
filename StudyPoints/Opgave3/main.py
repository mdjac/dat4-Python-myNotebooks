from sklearn.datasets import load_wine
import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score
import seaborn as sb


wine = load_wine()
data = wine.data
data=pd.DataFrame(data=data, columns=wine["feature_names"])


def mean_shift(data, n_samples=1000, quantile=0.20):
    bandwidth = estimate_bandwidth(data, quantile, 
                                   n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    
    return labels, cluster_centers, n_clusters


#Normalizing data
''' scaler = preprocessing.MinMaxScaler()
names = data.columns
d = scaler.fit_transform(data)
scaled_df = pd.DataFrame(d, columns=names) '''


#Finds the best quantile to reach highest silhouette score
current_quantile = 0.10
best_silhouette_score = 0
best_quantile = 0
labels = 0
cluster_centers = 0
n_clusters = 0

while (current_quantile <= 0.30):
    #Makes the clusters
    #labels, cluster_centers, n_clusters = mean_shift(scaled_df)
    _labels, _cluster_centers, _n_clusters = mean_shift(data,quantile=current_quantile)
    #Calculating the silhouette coefficeint to see how the clustering performed - the closter to 1 the better.
    silhouette_avg = metrics.silhouette_score(data, _labels)
    if (silhouette_avg > best_silhouette_score):
        best_silhouette_score = silhouette_avg
        best_quantile = current_quantile
        labels = _labels
        cluster_centers = _cluster_centers
        n_clusters = _n_clusters
    current_quantile = current_quantile + 0.01

print("Best silhouette score: ",best_silhouette_score)
print("Best quantile: ",best_quantile)
print("Number of clusters: ",n_clusters)


#add the labels to the dataframe as a column
data_with_labels = data.copy()
data_with_labels['cluster'] = labels

#Grouping wines by Cluster and keeping column values as the mean for the cluster
wine_data_cluster = data_with_labels.groupby(['cluster']).mean()
wine_data_cluster["wines in cluster"] = pd.Series(data_with_labels.groupby(['cluster']).size())
print(wine_data_cluster)


#Comparing the clusters against real targets
_labels = labels.tolist()
_target = wine["target"].tolist()
result = adjusted_rand_score(_target, _labels)
print("Score when comparing clusters against targets: ",result)


#Find unique cluster labels
unique_labels = np.unique(labels)

#make a dataframe containing all rows with cluster = 0
for label in unique_labels:
    _cluster_data = data_with_labels[data_with_labels['cluster'] == label]


#Analyzing Linear regression on data
''' mpl.use("pdf")
print("line 95")
fig = plt.figure()
print("line 97")
pplot = sb.pairplot(data_with_labels, hue="cluster")
print("Line 99")
fig.add_subplot(pplot)
print("line 101")
fig.set_tight_layout(True)
print("Line 103")
fig.savefig("./cluster_pairplot.png") '''

mpl.use("pdf")
df = sb.load_dataset('iris')
sns_plot = sb.pairplot(df, hue='species', height=2.5)
plt.savefig('output_new.png')








