# trying to decide how best to use functions and random to roll dice sets
# the idea is to ask the user how many of each sided dice they want to roll
# and then print out that roll into a list


def d4():
    import random
    roll = random.randint(1, 4)
    return roll


def d6():
    import random
    roll = random.randint(1, 6)
    return roll


def d10():
    import random
    roll = random.randint(1, 10)
    return roll


def d12():
    import random
    roll = random.randint(1, 12)
    return roll


def d20():
    import random
    roll = random.randint(1, 20)
    return roll


def d100():
    import random
    roll = random.randint(1, 100)
    return roll

# example of a dictionary for dice
#

# import random
#
# diceDict = {'d4': random.randint(1, 4), 'd6': random.randint(1, 6), 'd10': random.randint(1, 10),
#             'd12': random.randint(1, 12), 'd20': random.randint(1, 20), 'd100': random.randint(1, 100)}


# * d4 = random.randint(1, 4)    #
# * d6 = random.randint(1, 6)    #
# * d10 = random.randint(1, 10)  #
# * d12 = random.randint(1, 12)  #
# * d20 = random.randint(1, 20)  #
# * d100 = random.randint(1, 100)#


roll_list = list()

dice_choice = input("Which dice would you like to roll?: ")


if dice_choice == 'd6':
    while len(roll_list) <= 5:
        if input("Press enter to roll your dice, or q to quit: ") == 'q':
            print(roll_list)
            break
        else:
            roll_list.append(d6())
            print(roll_list)
    print("All finished. Your roll set is:")
    print(roll_list)

# if dice_choice == 'd4':
#     print(d4())
# if dice_choice == 'd6':
#     print(d6())
# if dice_choice == 'd10':
#     print(d10())
# if dice_choice == 'd12':
#     print(d12())
# if dice_choice == 'd20':
#     print(d20())
# if dice_choice == 'd100':
#     print(d100())


# roll_list = list()
# roll_list.append(d100())
# print(roll_list)



















