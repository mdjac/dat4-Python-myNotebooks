print("hejNYT!!!MIKKEL!")

movies = [("Citizen Kane", 1941),("Test",2000),("test2",2010)]

print(movies[0])
print(movies[1])
pre2k = [title for (title,year) in movies if year < 2001]

print(pre2k)
