import random
import sklearn
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")

def create_baby_data(size):
    result = []
    for x in range(size):
        
        
        age_height = {0:(46,53),1:(51,58),2:(54,62),3:(57,65),4:(60,68),5:(62,70),6:(63,72),7:(65,73),8:(66,75),9:(68,76),10:(69,78),11:(70,79),12:(71,80)}
        age_weight = {0:(2.5,4.3),1:(3.4,5.7),2:(4.4,7.0),3:(5.1,7.9),4:(5.6,8.6),5:(6.1,9.2),6:(6.4,9.7),7:(6.7,10.2),8:(7.0,10.5),9:(7.2,10.9),10:(7.5,11.2),11:(7.4,11.5),12:(7.8,11.8)}
        age = random.randrange(0,13)
        height_range = age_height[age]
        weight_range = age_weight[age]
        height = random.randrange(height_range[0],height_range[1])
        weight = random.uniform(weight_range[0],weight_range[1])
        result.append((height,weight,age))
    return result

def plot_data(inputdata):
    inputdata = np.asarray(inputdata)
    x, y, z = inputdata[:,0], inputdata[:,1], inputdata[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, linewidth=0.2)
    ax.set_xlabel("Height")
    ax.set_ylabel("Weight")
    ax.set_zlabel("Age")

    plt.savefig('01.png', bbox_inches='tight')

data = create_baby_data(200)
print(data)
plot_data(data)