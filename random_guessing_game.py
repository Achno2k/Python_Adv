from random import randint

answer = randint(1, 10) #generating a random number

while True:
    try:
        guess = int(input("Enter a number 1~10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius!")
                break
        else:
            print("Please enter a number between 1~10")

    except ValueError:
        print("Enter a number bro!!")
        continue

    
    