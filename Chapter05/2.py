import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")


print("Exercise 02")

import requests

# url = 'http://api.worldbank.org/v2/en/country/DNK;URY' 
# response = requests.get(url, params={'downloadformat': 'csv'})
url = 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv'
response = requests.get(url)

print(response.headers)

# get the filename
fname = response.headers['Content-Disposition'].split('=')[1]
fname = 'data/'+fname
# write content to file (zip file writing bytes)
if response.ok:  # status_code == 200:
    with open(fname, 'wb') as f:
        f.write(response.content)   
print('-----------------')
print('Downloaded {}'.format(fname))

import zipfile
# extract content of zip file in current folder
zipfile.ZipFile(fname, 'r').extractall('./data')
fname = fname.replace('.zip',".csv")

data = pd.read_csv(fname, skiprows=4)
#data = data.set_index("Country Code")

#1
exercise_01 = pd.Series(data=data["2014"].values,index=data["Country Code"])
#exercise_01 = pd.Series(data=data["2014"])
print("Printing ex01\n",exercise_01)

#2
exercise_02 = exercise_01.sort_values(ascending=False)
print("Printing ex02\n",exercise_02[:10])

#3
country_codes = pd.read_csv("/home/jovyan/data/country_codes.csv", delimiter="\t", header=None)
country_codes = country_codes.iloc[:,2]
country_codes = country_codes.str.strip()
country_codes = country_codes.tolist()
exercise_03 = exercise_02[(exercise_02.index.isin(country_codes))]
print("Printing ex03\n")
print(exercise_03[:10])


#4

data = data.set_index("Country Code")
usa_emission = data.loc["USA"][3:-3]
chn_emission = data.loc["CHN"][3:-3]

#just for testing concat, isnt used
test = pd.concat([usa_emission,chn_emission], axis=1, keys=["USA","CHN"])


plt.figure()
plt.plot(chn_emission.index.astype(dtype="int64"),chn_emission.values, color='red', label='China')
plt.plot(usa_emission.index.astype(dtype="int64"),usa_emission.values, color='blue', label='USA')
plt.legend()

# Set chart title and label axes. 
plt.title("Emission development", fontsize=24)


plt.savefig('2.png', bbox_inches='tight')
