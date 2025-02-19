import random
def game():
    print("Welcome to the number guessing game!")
    with open("highscore.txt","r") as f:
        highscore=f.read()
        if highscore=="":
            highscore=int (highscore)
            print(f"The highscore is {highscore}")
        else:
            print(f"The highscore is {highscore}")
    print("I'm thinking of a number between 1 and 100")
    number=random.randint(1,100)
    guess=0
    score=0
    while(guess!=number):
        score+=1
        guess=int(input("Enter your guess:"))
        if guess<number:
            print("Too low!")
        elif guess>number:
            print("Too high!")
        else:
            print("You got it!")
            break
    print(f"Number of guesses you took :{score}")
    if(score > highscore):
        print("Congratulations! You have broken the highscore!")
        with open("highscore.txt","w") as f:
            f.write(str(score))
    else:
        print("You could not break the highscore. Better luck next time!")
    play_again=input("Do you want to play again? (yes/no):")
    if play_again=="yes":
        game()
    else:
        print("Thanks for playing!")


game()
