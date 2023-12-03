movieTitles=["shrek 1", "shrek 2", "shrek 3", "shrek 4", "shrek 5"]
file=open("z13.txt", 'w')
for i in movieTitles:
    file.write(i+"\n")
file.close()