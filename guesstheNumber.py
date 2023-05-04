secretNumber = 9;
guessCount = 0
guessLimit = 3;

while guessCount < guessLimit:
    guess = int(input("Guess a number between 1 and 10 you have 3 chances please begin: "));
    guessCount += 1;
    if guess == secretNumber:
        print('You got it! You are awesome!')
        break
    else:
        print('I am sorry you did not get it please try again!');

