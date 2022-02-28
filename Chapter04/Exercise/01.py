# read data from csv file into 2d numpy array
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")


filename = '../../../data/befkbhalderstatkode.csv'


data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

#3 & 4
year = 2015
_dict = {}
for x in neighb.keys():
    output = (data[:,0] == year) & (data[:,1] == x)
    total = np.sum(data[output][:,4])
    _dict[x] = total

sorted_dict = {_key: _dict[_key] for _key in sorted(_dict, key=_dict.get)}

print(sorted_dict)

n = len(sorted_dict.keys())
x2 = np.arange(n)

plt.bar(x2,sorted_dict.values(),width=0.5, align='center')
plt.xticks(x2,sorted_dict.keys())
plt.title("Population in each Copenhagen city areas in "+str(year))
plt.savefig('4.png', bbox_inches='tight')


#5
year = 2015
output = (data[:,0] == year) & (data[:,2] > 65)
total = np.sum(data[output][:,4])
print(total)

#6
year = 2015
nordic_countries = [5101,5105,5104,5120,5110]
total = 0
for x in nordic_countries:
    output = (data[:,0] == year) & (data[:,2] > 65) & (data[:,3] == x)
    total += int(np.sum(data[output][:,4]))
print("Nordic countries (exept DK) aged above 65: ",total)

#7
oesterbro = 2
vesterbro = 4

set_of_years = np.unique(data[:,0])
print(set_of_years)
oesterbro_data = np.array([np.sum(data[(data[:,1] == oesterbro) & (data[:,0] == y)][:,4]) for y in set_of_years])
vesterbro_data = np.array([np.sum(data[(data[:,1] == vesterbro) & (data[:,0] == y)][:,4]) for y in set_of_years])


plt.figure()
plt.plot(set_of_years,oesterbro_data, color='green', label='Østerbro')
plt.plot(set_of_years,vesterbro_data, color='red', label='Vesterbro')
plt.legend()

# Set chart title and label axes. 
plt.title("Population development", fontsize=24)

x_steps = np.linspace(1992,2015,5,dtype=int)
print(x_steps)

plt.xticks(x_steps)


plt.savefig('7.png', bbox_inches='tight')



