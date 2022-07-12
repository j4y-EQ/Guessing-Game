from random import randint

random_num = randint(0, 100)
turns = 5
diff = 0
diff2 = 0
random_num2 = randint(0, 10)
total_score = 3
no_win = False


class Guess:

    def __init__(self, name, score=0, user_input=0):
        self.name = name
        self.score = score
        self.user_input = user_input

    def check_input(self):
        while True:
            try:
                self.user_input = int(input(f'{self.name}, guess the number: '))
                break
            except ValueError:
                print("Input a number!")

    def check_answer(self):
        if self.user_input > random_num:
            print(f"Oops! {self.name}, It is too high!")
            return False
        if self.user_input < random_num:
            print(f"Oh no! {self.name}, It's too low!")
            return False
        if self.user_input == random_num:
            print(f"Good job! {self.name} won and accomplished a 1/50 chance!")
            return True


print(
    f"Let's play a game! It is called \"Try To Guess The Number\"! Everytime you guess, I give a clue! You have {turns} tries! Best out of 3 wins!")

player1_name = input("First, please enter player 1's name: ")
player2_name = input("Secondly, please enter player 2's name: ")
# Player 1's num
while True:
    try:
        player1_num = int(input(f"{player1_name}, please choose a number from 1 to 10 (Trust me it's important): "))
        if player1_num not in range(1, 11):
            print("Give me a number from 1 to 10.")
        else:
            break
    except ValueError:
        print("Give me a number!")

# Player 2's num
while True:
    try:
        player2_num = int(input(f"{player2_name}, please choose a number from 1 to 10 (Trust me it's important): "))
        if player2_num not in range(1, 11):
            print("Give me a number from 1 to 10.")
        elif player2_num == player1_num:
            print(f"Please choose another number other than {player2_num}. {player1_name} has chosen it.")
        else:
            break
    except ValueError:
        print("Give me a number!")

# Calculate differences
if player1_num > random_num2:
    diff = player1_num - random_num2
elif player1_num < random_num2:
    diff = random_num2 - player1_num

if player2_num > random_num2:
    diff2 = player2_num - random_num2
elif player2_num < random_num2:
    diff2 = random_num2 - player2_num
# Check for differences to the randomly generated number
if diff > diff2:
    print(f"Awh, {player2_name} had the number closer to {random_num2}. {player2_name} starts first! Game started.")
    first_player = 2
if diff < diff2:
    print(f"Awh, {player1_name} had the number closer to {random_num2}. {player1_name} starts first! Game started.")
    first_player = 1

player1 = Guess(player1_name)
player2 = Guess(player2_name)
while total_score > 0:

    while turns > 0:
        if first_player == 1:
            player1.check_input()
            if player1.check_answer():
                player1.score += 1
                print(f"{player1.name} won! They get one point. ")
                random_num = randint(0, 100)
                break
            player2.check_input()
            if player2.check_answer():
                player2.score += 1
                print(f"{player2.name} won! They get one point. ")
                random_num = randint(0, 100)
                break
            print(f"You have {turns} tries left!")
            turns -= 1
        if first_player == 2:
            player2.check_input()
            if player2.check_answer():
                player2.score += 1
                print(f"{player2.name} won! They get one point. ")
                random_num = randint(0, 100)
                break
            player1.check_input()
            if player1.check_answer():
                player1.score += 1
                print(f"{player1.name} won! They get one point. ")
                random_num = randint(0, 100)
                break
            print(f"You have {turns} tries left!")
            turns -= 1
    else:
        print(f"Aw! {player1_name} and {player2_name} didn't get it! None of them won. :( It was {random_num}.")
        random_num = randint(0, 100)
        no_win = True
    if not no_win:
        total_score -= 1
    turns = 5
else:
    if player1.score > player2.score:
        print(f"{player1.name} IS VICTORIOUS! They win with {player1.score} points!")
    if player2.score > player1.score:
        print(f"{player2.name} IS VICTORIOUS! They win with {player2.score} points!")
