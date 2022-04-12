import random

numbers_per_line = 6
minimum = 1
maximum = 45

def main():
    number_of_picks = int(input("How many quick picks? : "))
    while number_of_picks < 0:
        print("That is meaningless!")
        number_of_picks = int(input(("How many quick picks? : ")))
    for i in range(number_of_picks):
        pick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum,maximum)
            while number in pick:
                number = random.randint(minimum,maximum)
            pick.append(number)
        pick.sort()
        print(" ".join("{}".format(number) for number in pick))

main()