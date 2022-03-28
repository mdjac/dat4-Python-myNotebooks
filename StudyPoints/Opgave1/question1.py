import pandas as pd


def main(data):
    #Spørgsmål - 1
    #Formats date column to pandas datetime and only keeps year-month
    data.date = pd.to_datetime(data.date).dt.to_period('m')
    #Finds the sum of new_cases pr country pr month
    data_grouped_monthly = data.groupby(["location","date"])["new_cases"].sum().reset_index()
    #for each location, then finds the index of the month with the highest new_cases
    #hich returns list of index numbers, which i use loc to filter original data on
    max_values_per_country = data_grouped_monthly.loc[data_grouped_monthly.groupby(["location"])["new_cases"].idxmax()]

    
    print(max_values_per_country)

    #Only for verification
    boolean_mask = data_grouped_monthly["location"] == "Afghanistan"
    print(data_grouped_monthly[boolean_mask])