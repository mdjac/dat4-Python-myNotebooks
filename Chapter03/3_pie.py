import matplotlib as mpl
mpl.use("pdf")
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt

data = {'apple': 10,'banana':2,'citrus':32,'dragon fruit':8}
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


#fig1, ax1 = plt.subplots()

plt.pie(data.values(), labels=data.keys(),autopct=make_autopct(data.values()))

plt.savefig('pie.png', bbox_inches='tight')


