import emoji
import pytest
from project import BlackJack


def test_initialize_deck():
    blackjack = BlackJack()
    assert (len(blackjack.deck)) == 52


def test_deal_card():
    blackjack = BlackJack()
    initial_deck_size = len(blackjack.deck)
    blackjack.deal_card()
    assert len(blackjack.deck) == initial_deck_size - 1


def test_get_score():
    blackjack = BlackJack()
    hand = [{'suit': emoji.emojize(':heart_suit:', variant="emoji_type"), 'card': 'Ace'}, {
        'suit': emoji.emojize(':heart_suit:', variant="emoji_type"), 'card': '10'}]
    assert blackjack.get_score(hand) == 21
