from sklearn.datasets import load_wine
import numpy as np
import pandas as pd
wine = load_wine()
data = wine.data
data=pd.DataFrame(data=np.c_[wine['data'],wine['target']],columns=wine['feature_names']+['target'])
print(data.head())