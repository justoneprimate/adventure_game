import random

dice_set = {
    'd4': lambda: random.randint(1, 4),
    'd6': lambda: random.randint(1, 6),
    'd8': lambda: random.randint(1, 8),
    'd10': lambda: random.randint(1, 10),
    'd12': lambda: random.randint(1, 12),
    'd20': lambda: random.randint(1, 20),
    'd100': lambda: random.randint(1, 100),
}

roll_tally = list()


print("Welcome to the dice roller. You can roll d4, d6, d8, d10, d12, d20 or d100. \n"
      "You may roll up to 10 times per set.")

while len(roll_tally) <= 10:
    choose_dice = input("Please choose a die to roll or type quit if you are finished: ")
    if choose_dice == 'quit':
        break
    if choose_dice in dice_set:
        rolled_dice = dice_set.get(choose_dice)()
        roll_tally.append((str(choose_dice) + ':' + str(rolled_dice)))
        for roll in roll_tally:
            print(roll)
    else:
        print("Choose a valid die")

print("All finished. Your roll set is:")
for roll in roll_tally:
    print(roll)
