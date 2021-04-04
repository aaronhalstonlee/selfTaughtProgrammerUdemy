"""Assignment 2"""
list = [3,4,5]
while True:
    guess = input("pick a number between 1 and 10")
    if guess == 'q':
        print('bye!')
        break
    elif int(guess) in list:
        print("you got it!")
    else:
        print("nope, try again")
