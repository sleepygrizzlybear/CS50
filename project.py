import emoji
import random
import sys


class BlackJack:
    def __init__(self):
        self.deck = self.initialize_deck()
        self.player_hand = []
        self.dealer_hand = []

    def initialize_deck(self):
        cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = [emoji.emojize(':heart_suit:', variant="emoji_type"),
                 emoji.emojize(':diamond_suit:', variant="emoji_type"),
                 emoji.emojize(':club_suit:', variant="emoji_type"),
                 emoji.emojize(':spade_suit:', variant="emoji_type")]

        deck = [{'suit': suit, 'card': card, } for card in cards for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def get_score(self, hand, player_turn=True):
        score = 0
        num_aces = 0

        for card in hand:
            value = card["card"]
            if value == 'Ace':
                num_aces += 1
                score += 11
            elif value in ['Jack', 'Queen', 'King']:
                score += 10
            else:
                score += int(value)

        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1

        return score

    def reveal_result(self, player_score, dealer_score):
        if player_score == dealer_score:
            print("It's a draw!")
        elif dealer_score == 21:
            print("You lose! Dealer has a Blackjack!")
        elif player_score == 21:
            print(emoji.emojize(":fireworks:", variant="emoji_type"), "You win with a Blackjack!")
        elif player_score > 21:
            print("You went over. You lose!")
        elif dealer_score > 21:
            print("Dealer went over. You win!")
        elif player_score > dealer_score:
            print(emoji.emojize(":fireworks:", variant="emoji_type"), "Congratulations! You win!")
        else:
            print(emoji.emojize(":face_with_crossed-out_eyes:", variant="emoji_type"), "Sorry, you lose! Better luck next time!")

    def display_emoji_cards(self, hand, player_turn=True):
        if player_turn:
            cards_string = ', '.join([f"{card['suit']} {card['card']}" for card in hand])
        else:
            cards_string = f"{hand[0]['suit']} {hand[0]['card']}, *Hidden*"
        return cards_string

    def show_hand(self, player_turn=True):
        print("Your hand:", self.display_emoji_cards(self.player_hand))
        print("Your score:", self.get_score(self.player_hand))

        if player_turn:
            print("Dealer's first card:", self.dealer_hand[0]["suit"], self.dealer_hand[0]["card"])
            if len(self.player_hand) > 2:
                print("Dealer's second card: *Hidden*")

        else:
            print("Dealer's hand:", self.display_emoji_cards(self.dealer_hand))
            print("Dealer's score:", self.get_score(self.dealer_hand))

    def end_game(self, player_score, dealer_score):
        print("\n", emoji.emojize(':joker:', variant="emoji_type"), "Game Over")
        print("Your hand:", self.display_emoji_cards(self.player_hand))
        print("Your score:", player_score)
        print("Dealer's hand:", self.display_emoji_cards(self.dealer_hand))
        print("Dealer's score:", dealer_score)

    def play_round(self):

        for _ in range(2):
            self.player_hand.append(self.deal_card())
            self.dealer_hand.append(self.deal_card())

        game_over = False

        player_score = self.get_score(self.player_hand)
        dealer_score = self.get_score(self.dealer_hand)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True

        while not game_over:
            self.show_hand()
            user_choice = input("Hit or stand, type 'y' or 'n': ").lower()

            if user_choice == 'y':
                print(emoji.emojize(":check_mark_button:", variant="emoji_type"), "You drew a card")
                self.player_hand.append(self.deal_card())

                # Check if player has gone over 21
                player_score = self.get_score(self.player_hand)
                if player_score > 21:
                    game_over = True

            elif user_choice == 'n':
                print("You chose to stand. Dealer is playing...")
                while dealer_score < 17:
                    self.dealer_hand.append(self.deal_card())
                    dealer_score = self.get_score(self.dealer_hand)
                    self.show_hand(player_turn=False)

                game_over = True

            else:
                print("Invalid input. Please type 'y' for hit or 'n' for stand: ")

        # If the game is over, reveal results
        self.reveal_result(player_score, dealer_score)
        self.end_game(player_score, dealer_score)
        # Reinitialize the deck for the next round
        self.deck = self.initialize_deck()
        self.player_hand = []
        self.dealer_hand = []

    def start_game(self):
        while True:
            user_start = input(emoji.emojize(":winking_face:", variant="emoji_type") + " Are you ready to play a game: 'y' or 'n' ")

            if user_start == "n":
                sys.exit("Goodbye!")
            elif user_start == "y":
                print(emoji.emojize(":money_bag:", variant="emoji_type"), "Welcome!")
                self.play_round()
            else:
                print("Invalid input. Please type 'y' for yes or 'n' for exit: ")

def main():
    blackjack = BlackJack()
    blackjack.start_game()
    
if __name__ == "__main__":
    main()
