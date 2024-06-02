# Normal: All Hints | Hard: Hints 1, 2, 3 | Extra Hard:Hints 1 & 2 | Expert: Hint 1
import random
from art import logo


# Our Blackjack House Rules:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# Requirements | http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# FlowChart | https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)


# 1: deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# 3: calculate_score() that takes a List of cards as input and returns the score. sum() function
def calculate_score(card):
    # 4:check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 (blackjack) instead of the actual score.
    if sum(card) == 21 and len(card) == 2:
        return 0
    # 5:check for an 11 (ace). If the score is already over 21, remove 11 and replace it with 1. append() & remove().
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


# 10: compare() and pass in the user_score and computer_score. If same score (draw) | computer 0 (loses) | user  0 (wins) | user over 21 (loses) | computer over 21 (wins) | none (highest score player) wins
def compare(user_scores, computer_scores):
    # Bug fix. If you and the computer are both over, you lose.
    if user_scores > 21 and computer_scores > 21:
        return "You went over. You lose 😤"
    if user_scores == computer_scores:
        return "Draw"
    elif computer_scores == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_scores == 0:
        return "Win with a Blackjack 😎"
    elif user_scores > 21:
        return "You went over. You lose 😭"
    elif computer_scores > 21:
        return "Opponent went over. You win 😁"
    elif user_scores > computer_scores:
        return "You win 😃"
    else:
        return "You lose 😤"


computer_score = 0
user_score = 0


def play_game():
    global computer_score, user_score
    print(logo)

    # 2: Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # 8: Score rechecked with every new card drawn and the checks in 6 need to be repeated until the game ends.
    while not is_game_over:
        # 6: Call calculate_score(). If computer/user 0 or user over 21 (game ends)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_deal = input("Type 'yes' to get another card or 'no' to pass: ")
            if user_deal == "yes":
                user_cards.append(deal_card())
            elif user_deal == "no":
                is_game_over = True
    # 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# 11: Restart the game or not ?.
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    clear()
    play_game()
