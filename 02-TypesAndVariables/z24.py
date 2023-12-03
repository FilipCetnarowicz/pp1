regis=input("registration number of your car please (with Capital Numbers!): ")
krkCheck= regis[:2]=="KR" or regis[:2]=="KK"
print(f"your car is from Krakow = {krkCheck}")