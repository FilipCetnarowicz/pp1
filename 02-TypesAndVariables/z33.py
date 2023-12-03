# 33.	The password is valid if it is at least 8 characters long. 
# Write a program that checks whether the password read from the keyboard is correct. 
# Sample result:
# Enter password: qwertyXX
# Password is valid: True

password=str(input("type in your passsword to check wether it's correct \n"))
lenCheck= len(password) >= 8
print(f"password is valid: {lenCheck}")
