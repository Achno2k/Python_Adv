from random import randint
def input_guess(guess, answer):
    if 0 < guess < 11:
            if guess == answer:
                print("You are a genius!")
                return True
    else:
        print("Please enter a number between 1~10")
        return False    

if __name__ == '__main__':
    answer = randint(1, 10) #generating a random number
    while True:
        try:
            guess = int(input("Enter a number 1~10: "))
            if(input_guess(guess, answer)):
                break
        except ValueError:
            print("Enter a number bro!!")
            continue

    
    