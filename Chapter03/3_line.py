print("----- EXERCISE 01 -----")
#%matplotlib notebook
# %matplotlib notebook necessary to show the plot in ipython notebook (or use plt.show())
import matplotlib as mpl
mpl.use("pdf")
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}
days = list(student_attendance.keys())
numbers = list(student_attendance.values())

plt.figure()
plt.plot(days,numbers)

# Set chart title and label axes. 
plt.title("title", fontsize=24)
plt.xlabel("x1-label", fontsize=14)
plt.ylabel("y22-label", fontsize=14)
# Set size of tick labels.
#plt.tick_params(axis='both', labelsize=14)

#plt.show()
# in a program you would have to call plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')

print("----- END -----")