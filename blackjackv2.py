import random
# from art import logo
import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_choices = []
computer_choices = []
player_total = 0
computer_total = 0
play_game = True


def player():
    """Selects random card, appends it to player_choices"""
    player = random.choice(cards)
    player_choices.append(player)


def computer():
    """Computer hand, random card"""
    computer = random.choice(cards)
    computer_choices.append(computer)


def final_score():
    """Show final Player/Computer hand and scores"""
    print(
        f"Your final hand {player_choices}, final score: {player_total}")
    print(
        f"Computers final hand {computer_choices}, final score: {computer_total}")


def another_card():
    """play = input(Type 'y' to get another card, type 'n' to pass: ").lower())"""
    play = input(
        "Type 'y' to get another card, type 'n' to pass: ").lower()
    return play


def compare_for_winner(player_total, computer_total):
    """Compare the player total with the computer total to declare winner or draw """
    if player_total > 21:
        print("You lose")
    elif computer_total > 21:
        print("You win")
    elif computer_total == player_total:
        print("Draw")
    elif player_total > computer_total:
        print("Player wins")
    else:
        print("Computer wins")


# variables
player_choices = []
computer_choices = []
player_total = 0
computer_total = 0

# Clear the terminal - https://www.geeksforgeeks.org/clear-screen-python/
os.system('clear')
play = input(
    "Do you want to play a game of Blackjack? 'y' or 'n': ").lower()


if play == 'y':
    play_game = True

    print(logo.blackjack)
    # Initial player and computer hands
    player()
    player()
    player_total += sum(player_choices)
    print(f"Your cards: {player_choices}, current score: {player_total}")
    computer()
    computer()
    computer_total += sum(computer_choices)
    print(f"Computer's first card? {computer_choices[0]}")
    # Check for blackjack (21) for first 2 cards - declare winner!
    if player_total == 21 and computer_total == 21:
        # final_score()
        print(f"Blackjack! Casino Wins")
        play_game = False
    if player_total == 21:
        # final_score()
        print("Blackjack! You Win!")
        play_game = False
    if computer_total == 21:
        # final_score()
        print("Blackjack! Casino Wins")
        play_game = False

    # track player score and cards
    while play_game:
        play = another_card()
        if play == 'y':
            player()
            player_total += player_choices[-1]
            # List comprehension. Checking the if the sum of the list is greater than 21 and it contains an 11.  If yes, convert the 11 to 1, else keep list as is.
            player_choices = [
                1 if sum(player_choices) > 21 and x == 11 else x for x in player_choices]
            player_total = sum(player_choices)
            print(f" Your current cards are: {player_choices}")
            print(f" Your current total is: {player_total}")
            if player_total > 21:
                play_game = False
        elif play == 'n':
            play_game = False
    # track computer score and cards
    while computer_total < 17:
        computer()
        computer_total += computer_choices[-1]
    # final score and winner!
    final_score()
    # function declaring the winner.
    compare_for_winner(player_total, computer_total)
else:
    print("Player declined to play!")
