from modules.myModule import TextComparer
import timeit

import matplotlib as mpl
mpl.use("pdf")
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt



urls = []
urls.append("https://www.gutenberg.org/files/84/84-0.txt")
urls.append("https://www.gutenberg.org/files/1342/1342-0.txt")
urls.append("https://www.gutenberg.org/files/11/11-0.txt")
urls.append("https://www.gutenberg.org/cache/epub/64317/pg64317.txt")
urls.append("https://www.gutenberg.org/files/5199/5199-0.txt")
urls.append("https://www.gutenberg.org/files/2542/2542-0.txt")
urls.append("https://www.gutenberg.org/files/98/98-0.txt")
urls.append("https://www.gutenberg.org/cache/epub/174/pg174.txt")
urls.append("https://www.gutenberg.org/files/1661/1661-0.txt")
urls.append("https://www.gutenberg.org/cache/epub/25344/pg25344.txt")
urls.append("https://www.gutenberg.org/cache/epub/26184/pg26184.txt")
urls.append("https://www.gutenberg.org/files/1260/1260-0.txt")
urls.append("https://www.gutenberg.org/files/1400/1400-0.txt")
urls.append("https://www.gutenberg.org/files/1952/1952-0.txt")
urls.append("https://www.gutenberg.org/files/345/345-0.txt")
urls.append("https://raw.githubusercontent.com/mdjac/dat4-Python-myNotebooks/main/Chapter06/Exercise01/test_input_file_DONTDELETE.txt")

#urls.append("https://raw.githubusercontent.com/mdjac/dat4-Python-myNotebooks/main/outputsadaqewq.txt")

tc = TextComparer(urls)

tc.multi_download()

my_iterable = tc.__iter__()

print(tc.filenames)

print(next(my_iterable))
print(next(my_iterable))
#print(next(my_iterable))


my_generator = tc.urllist_generator()

print(next(my_generator))
print(next(my_generator))
#print(next(my_generator))


time_without_multi = timeit.timeit(tc.hardest_read, number=1)
print("Without multiprocessing! \n",time_without_multi)



time_with_multi = timeit.timeit(tc.hardest_read_multiprocessing, number=1)
print("With multiprocessing! \n",time_with_multi)

#ex2 - 3
data = tc.hardest_read_multiprocessing(return_all=True)
print(data)
x_values = []
y_values = []
for element in data:
    x_values.append(element[0])
    y_values.append(element[1])

plt.bar(x_values, y_values,width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
plt.ylim(min(y_values)-1, max(y_values)+1)

plt.savefig('barplot.png', bbox_inches='tight')

