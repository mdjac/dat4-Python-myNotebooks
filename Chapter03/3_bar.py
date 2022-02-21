import matplotlib as mpl
mpl.use("pdf")
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt

data_dict = {'Holger':25,'Helga':54,'Hasse':76,'Halvor':12,'Hassan':43,'Hulda':31,'Hansi':102}

max_y_key = max(data_dict, key=data_dict.get) #get key to the max value of a dictionary
max_y_val = data_dict[max_y_key]

plt.bar(data_dict.keys(),data_dict.values(),width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

plt.savefig('test.png', bbox_inches='tight')


new_dict = {"key1":1,"key2":2,"key3":3}
plt.figure()
plt.bar(new_dict.keys(),new_dict.values(),width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
plt.savefig('test1.png', bbox_inches='tight')

