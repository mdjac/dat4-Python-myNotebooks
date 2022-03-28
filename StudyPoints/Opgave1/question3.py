import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")


def main(data):
    #Spørgsmål 3

    #Filter out so only rows 1 row with total death pr country
    data.date = pd.to_datetime(data.date)
    total_death_pr_country = data.groupby(["location"])["total_deaths"].max()
    

    #sort, Filter top10 & Get country names
    total_death_pr_country = total_death_pr_country.sort_values(ascending=False)
    print(total_death_pr_country)
    top10_country_names = total_death_pr_country[:10].index.values.tolist()
    print(top10_country_names)

    #Use initial dataset to draw graph for the top10 countries
    for country_name in top10_country_names:
        boolean_mask = data["location"] == country_name
        masked_data = data[boolean_mask]
        dates = masked_data["date"]
        total_death = masked_data["total_deaths"]
        x_values = dates.tolist()
        y_values = total_death.tolist()
        plt.plot(x_values, y_values, label = country_name)
   
    start_date = data["date"].min()
    end_date = data["date"].max()
    x_steps = pd.date_range(start=start_date, end=end_date,periods=6)
    plt.xticks(x_steps)
    plt.legend()
    plt.savefig('question3.png', bbox_inches='tight')

    