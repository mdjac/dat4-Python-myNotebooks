''' 
https://www.kaggle.com/georgesaavedra/covid19-dataset

1. Hvilken måned var der flest smittede af corona for hvert land (location)?

2. Hvilket land i europa har test flest personer pr. tusinde indbyggere (total_tests_per_thousand), siden juli 2021 til nu?

3. Vis en graph af de ti lande med flest døde til dags dato.

4. Vælg tre lande og vis udviklingen af døde i forhold til total antal smittede i procent fra d. 1 april 2020 til dags dato.
'''

import pandas as pd
import question1
import question2
import question3
import question4

data = pd.read_csv("./owid-covid-data.csv", skiprows=0)
#Filters out continents, low income groups etc. so only real countries remains.
filtered_data = data[~data["iso_code"].str.startswith("OWID_")]


#Copies the data, and doesn't keep reference to old dataframe
copied_data = filtered_data.copy(deep=True)
question2.main(copied_data)
#question4.main(copied_data,'2021-03-31',"Denmark","Sweden","Norway")









