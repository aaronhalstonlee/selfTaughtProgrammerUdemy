'''assignment 1'''
num = input("please type in a number")
try:
    print(int(num))
except ValueError:
    print("you must type in a number")
