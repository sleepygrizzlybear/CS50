    # Python Blackjack Game Walkthrough For CS50 Course
    #### Video Demo: https://www.youtube.com/watch?v=CZ4iWjmWuXw
    #### Description:
    This Python project is a simple implementation of the classic Blackjack card game. The game is built using object-oriented programming principles and utilizes the emoji library for displaying card suits as emojis.

    ####Table of Contents
    Initialization <a name="initialization"></a>
    The BlackJack class is initialized with attributes for the card deck, player's hand, and dealer's hand.

    Card Deck <a name="card-deck"></a>
    The initialize_deck method creates a standard deck of 52 playing cards, each represented as a dictionary containing the card's value and suit.

    Dealing Cards <a name="dealing-cards"></a>
    The deal_card method pops a card from the deck, simulating the process of dealing cards in the game.

    Scoring System <a name="scoring-system"></a>
    The get_score method calculates the score for a given hand, considering the values of cards and the special scoring rules for Aces.

    Game Flow <a name="game-flow"></a>
    The show_hand method displays the current state of the game, showing the player's and dealer's hands with relevant information.

    Result Display <a name="result-display"></a>
    The reveal_result method displays the outcome of the game based on the final scores.

    Playing a Round <a name="playing-a-round"></a>
    The play_round method orchestrates the gameplay, allowing the player to hit or stand and managing the dealer's actions.

    Starting the Game <a name="starting-the-game"></a>
    The start_game method initiates the game loop, prompting the user to start a new round or exit the game.

    Reinitializing for a New Round <a name="reinitializing-for-a-new-round"></a>
    After revealing the results, the end_game method reinitializes the deck and hands for a new round, preparing for the next game iteration.

    ####Features
    Emoji Cards: The game uses emoji to display cards for a visually appealing experience.
    Multiple Rounds: Players can choose to play additional rounds after completing a game.
    User-Friendly Interface: The game provides clear instructions and prompts for user interactions.
    Deck Initialization: The deck is initialized with 52 cards and shuffled.

    ####Getting Started
    Requirements: Ensure you have Python installed on your machine and install the emoji and pytest packages.
    Run the Game: Execute the script blackjack.py to start the game.
    Game Instructions: Follow the on-screen prompts to play. Choose y to hit or n to stand during your turn.

    ####How to Play
    When prompted, enter 'y' to start a new game or 'n' to exit.
    Each round, you'll receive two cards, and the dealer will also receive two cards, with one hidden.
    Choose to 'hit' (receive another card) or 'stand' (keep your current hand) during your turn.
    The dealer will then play its turn automatically.
    The game will announce the winner based on the final scores.

    ####Exiting the Game
    If you decide not to play another round, enter 'n' when asked after a game.
