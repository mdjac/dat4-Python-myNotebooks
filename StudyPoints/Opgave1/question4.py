import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")
def main(data,from_date,*countries):
    if not countries:
        print("You need to add countries as arguments")
    else:
        print("it works")
        #Filter so only april 2021 till now
        data.date = pd.to_datetime(data.date)
        from_month = pd.to_datetime(from_date)
        data = data[data["date"] > from_month]
        print(data)

        for country_name in countries:
            boolean_mask = data["location"] == country_name
            masked_data = data[boolean_mask]
            masked_data["percentage_death"] = (masked_data["total_deaths"] / masked_data["total_cases"]) * 100
            print(masked_data[:10])
            y_values = masked_data["percentage_death"].tolist()
            x_values = masked_data["date"].tolist()
            plt.plot(x_values, y_values, label = country_name)
        
        plt.title(f"% death of total infected from: {from_date}")
        plt.legend()
        plt.savefig('question4.png', bbox_inches='tight')
        

        ##total_death / total_cases * 100