import random
game_list = ["R", "P", "S"]
Player = input("Enter your name: ").capitalize()

comp_choice = random.choice(game_list)
user_choice = input(
    "Make yor choice (NB: Type R for rock; P for paper or S for scissors): ").capitalize()

try:
    if user_choice == comp_choice:
        print("It is a tie")

    if user_choice == 'R':
        if comp_choice == 'S':
            print(f"{Player}(Rock) : CPU(Scissors)\n{Player} wins")
        if comp_choice == 'P':
            print(f"{Player}(Rock) : CPU(Paper)\nCPU wins")

    elif user_choice == 'P':
        if comp_choice == 'R':
            print(f"{Player}(Paper) : CPU(Rock)\n{Player} wins")
        if comp_choice == 'S':
            print(f"{Player}(Paper) : CPU(Scissors)\nCPU wins")

    elif user_choice == 'S':
        if comp_choice == 'P':
            print(f"{Player}(Scissors) : CPU(Paper)\n{Player} wins")
        if comp_choice == 'R':
            print(f"{Player}(Scissors) : CPU(Rock)\nCPU wins")
except:
    print("Incorrect input, Try Again")
