import random

options = ("rock", "paper", "scissors")
running = True
games_to_play = 0
player_score = 0
computer_score = 0

while running:
    if games_to_play == 0:
        games_to_play = int(input("How many games would you like to play? "))

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print("\nPlayer:", player.capitalize())
    print("Computer:", computer.capitalize())

    if player == computer:
        print("\nIt's a tie!")
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        print("\nYou win!")
        player_score += 1
    else:
        print("\nYou lose!")
        computer_score += 1

    games_to_play -= 1

    if games_to_play == 0:
        print("\nFinal score:")
        print("Player:", player_score)
        print("Computer:", computer_score)
        if not input("\nPlay again? (y/n): ").lower() == "y":
            running = False
    else:
        print("\nGames left:", games_to_play)

print("\nThanks for playing!")
