# define personal data
name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

# write to a file
file = open("z12.txt",'w')
file.write(name+"\n"+university+"\n"+field+"\n")
file.close()
