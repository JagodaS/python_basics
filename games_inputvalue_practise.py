# compatible with python 2.7
# raw_input zwraca dane o typie str
# input analizuje to co sie poda i zwraca zgodny typ z danymi (jezeli podamy 5+5 to zwroci 10)

import random

class games():
    def play_guess(self, number):
        counter = 0
        while True:
            counter += 1
            print "> ",
            guess = input()
            if guess == number:
                break
            else:
                if guess < number:
                    print "Too small"
                else:
                    print "Too big"
        return counter


while True: # emulowana petla do while
    print "Please provide a starting point"
    a = input()
    print "Please provide an ending point"
    b = input()
    if a <= b and isinstance(a, int) and isinstance(b, int):
        break
    else: print "Wrong data provided\n"

_number = random.randint(a, b)

print "Do you want to guess your number? (y/n)"
decision = raw_input()

trials = None
if decision == 'y':
    random_games = games()
    trials = random_games.play_guess(_number)
    print "Guessed after {} trials".format(trials)

print "Your random number is {}".format(_number)
