# Blackjack Game

## Description

The Blackjack Game project is a Python implementation of the classic card game, where the objective is to beat the dealer by having a hand value closest to 21 without exceeding it. This game includes features such as dealing cards, calculating scores, and determining the winner based on Blackjack rules.

### Features

- **Card Dealing**: Randomly deals cards to the player and the dealer.
- **Score Calculation**: Calculates the score based on the cards dealt, accounting for special rules like the Ace counting as either 1 or 11.
- **Game Flow**: Allows the player to choose whether to draw another card or pass.
- **Result Comparison**: Determines the winner based on the final scores, including special conditions for Blackjack.
- **Replay Option**: Players can choose to play multiple rounds.

### How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/blackjack.git
   cd blackjack
   ```

2. **Ensure Dependencies**:
   - The `art.py` file should contain a `logo` for the program's visual representation.

3. **Run the program**:
   ```bash
   python blackjack.py
   ```

4. **Gameplay**:
   - At the start, both the player and the dealer are dealt two cards.
   - The player can see their cards and the dealer's first card.
   - The player decides whether to draw another card or pass.
   - The dealer draws cards until the score is at least 17.
   - The winner is determined based on the final scores and displayed to the player.
   - The player is prompted to play again or exit.

### Example

```
Welcome to the Blackjack Game!
Do you want to play a game of Blackjack? Type 'yes' or 'no': yes
   Your cards: [7, 10], current score: 17
   Computer's first card: 5
Type 'yes' to get another card or 'no' to pass: no
   Your final hand: [7, 10], final score: 17
   Computer's final hand: [5, 9, 3], final score: 17
Draw
Do you want to play a game of Blackjack? Type 'yes' or 'no': no
```

### Benefits

- **Interactive**: Provides an engaging and interactive experience for users to play Blackjack.
- **Educational**: A practical example of implementing game logic and handling user input in Python.
- **Replayability**: Users can play multiple rounds, enhancing the entertainment value.

Enjoy your game of Blackjack with this Python implementation!
