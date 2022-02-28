''' load the csv file: befkbhalderstatkode.csv into a numpy ndarray
How many german children of 0 years were there in Copenhagen in 2015?
create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data
create a new function like previous so that it can sum values for all ages if age is not provided to the function
further add functionality to sum values if citizenship or area was not provided to function.
create a new function that can also give average values for each year if year whas not provided.
create a function, that given year and nationality can return which area had the most of these nationals by that year. Test it by finding out which area had the most Moroccan people in both 1992 and 2015
Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
Find out what age most French people have in 2015 '''

# read data from csv file into 2d numpy array
import numpy as np
filename = '../../data/befkbhalderstatkode.csv'


data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

#2
#german_mask_age0 = (data[:,0] == 2015) & (data[:,3] == 5180) & (data[:,2] == 0)

#print(data[german_mask_age0][:,4].sum())


#3
def create_mask_task3(dataset,aar,bydel,alder,statkode):
    output = (dataset[:,0] == aar) & (dataset[:,1] == bydel) & (dataset[:,2] == alder) & (dataset[:,3] == statkode)
    return int(sum(dataset[output][:,4]))

#print(create_mask_task3(data,1992,1,10,5100))

#4
def create_mask_task4(dataset,aar,bydel,statkode,alder=None):
    if(alder == None):
        output = (dataset[:,0] == aar) & (dataset[:,1] == bydel) & (dataset[:,3] == statkode)
    else:
        output = (dataset[:,0] == aar) & (dataset[:,1] == bydel) & (dataset[:,2] == alder) & (dataset[:,3] == statkode)
    return int(sum(dataset[output][:,4]))

#print(create_mask_task4(data,1992,1,5100))


#5
def pop_data_con(dataset,aar=None,bydel=None,alder=None,stat=None):
        alder_mask = dataset[:,2] == alder if alder != None else True
        bydel_mask = dataset[:,1] == bydel if bydel != None else True
        aar_mask = dataset[:,0] == aar if aar != None else True
        stat_mask = dataset[:,3] == stat if stat != None else True

        return np.sum(dataset[aar_mask & bydel_mask & alder_mask & stat_mask][:,4])
#print(pop_data_con(data,aar=1992,stat=5100))


#6
def mask_task_6(dataset,bydel,alder,statkode,aar=None):
    if (aar == None):
        output = (dataset[:,1] == bydel) & (dataset[:,2] == alder) & (dataset[:,3] == statkode)
        num_rows, num_cols = dataset[output].shape
        total_people = sum(dataset[output][:,4])
        avg_per_year = int(total_people / num_rows)
        return "Average pr year: ",avg_per_year
    else:
        output = (dataset[:,0] == aar) & (dataset[:,1] == bydel) & (dataset[:,2] == alder) & (dataset[:,3] == statkode)
        return int(sum(dataset[output][:,4]))

#print(mask_task_6(data,4,10,5100))

#7
def mask_task_7(dataset,aar,statkode):
    output = (dataset[:,0] == aar) & (dataset[:,3] == statkode)
    #Filters out so only bydel and amount is kept
    finaldata = dataset[output][:,[1,4]]

    #Makes a dict of city codes
    city_codes = np.unique(finaldata[:,0])
    city_codes_dict = {}
    for c in city_codes:
        city_codes_dict[c] = 0
    
    for row in finaldata:
        city_codes_dict[row[0]] += int(row[1])
    print(city_codes_dict)
    highest_city_code = max(city_codes_dict, key=city_codes_dict.get)
    return "City code "+str(highest_city_code)+" wins with: "+str(city_codes_dict[highest_city_code])
#print(mask_task_7(data,2015,5244))

#8
def mask_task8(dataset,aar):
    dk_statcode = 5100
    output = (dataset[:,0] == aar) & (dataset[:,3] != dk_statcode)
    #Filters out so only bydel and amount is kept
    finaldata = dataset[output][:,[1,4]]

    #Makes a dict of city codes
    city_codes = np.unique(finaldata[:,0])
    city_codes_dict = {}
    for c in city_codes:
        city_codes_dict[c] = 0
    
    for row in finaldata:
        city_codes_dict[row[0]] += int(row[1])
    print(city_codes_dict)
    
    lowest_city_code = min(city_codes_dict, key=city_codes_dict.get)
    return int(lowest_city_code)

#print(mask_task8(data,2015))

#9
def mask_task9(dataset,statcode,aar):
    output = (dataset[:,0] == aar) & (dataset[:,3] == statcode)
    finaldata = dataset[output][:,[2,4]]

    ages = np.unique(finaldata[:,0])
    ages_dict = {}

    for age in ages:
        ages_dict[age] = 0

    for row in finaldata:
        ages_dict[row[0]] += int(row[1])
    print(ages_dict)
    return max(ages_dict,key=ages_dict.get)


fra_statcode = 5130
print(mask_task9(data,fra_statcode,2015))