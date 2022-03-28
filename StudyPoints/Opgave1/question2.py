import pandas as pd
import numpy as np

def main(data):
    #Spørgsmål - 2

    #Filter so only european countries remain
    data_european_countries = data[data["continent"] == "Europe"].copy()

    #Filter so only july 2021 till now
    data_european_countries.date = pd.to_datetime(data_european_countries.date).dt.to_period('m')
    from_month = pd.to_datetime('2021-06').to_period('m')
    data_european_countries = data_european_countries[data_european_countries["date"] > from_month]


    #Sum af test pr 1000 for alle lande
    data_european_countries = data_european_countries.groupby(["location"])["new_tests_per_thousand"].sum().reset_index()


    #Renamer column og sortere
    data_european_countries = data_european_countries.set_index(["location"])
    data_european_countries = data_european_countries.rename(columns = {"new_tests_per_thousand":"tests_per_thousand"})
    data_european_countries = data_european_countries.sort_values(by="tests_per_thousand", ascending=False)

    
    print(data_european_countries)
