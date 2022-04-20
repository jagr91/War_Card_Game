from deck import create_deck
from random import *

def deal_cards(deck):
    """deal deck into player and cpu"""

    p1_deck = []
    cpu_deck = []
    for num, card in enumerate(deck):
        if num % 2 == 0:
            p1_deck.insert(0, card)
        else:
            cpu_deck.insert(0, card)
    return [p1_deck, cpu_deck]


def value(card):
    """checks card figure and returns its value e.g. "5♦" = 5 or "Q♣" = 12"""

    figures_values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value = figures_values[card[:-1]]
    return value


def print_round(number):
    round = f"Round {number} started:"
    underline = "=" * len(round)
    print(f"\n{round}\n{underline}")


def p1_card(deck):
    card = deck[0][0]
    return card


def cpu_card(deck):
    card = deck[1][0]
    return card


def print_card(card_deck):
    p1card = p1_card(card_deck)
    cpucard = cpu_card(card_deck)
    print(f"P1: {p1card} \nCPU: {cpucard}")


def print_card_len(card_deck):
    p1_deck = len(card_deck[0])
    cpu_deck = len(card_deck[1])
    print(f"P1: {p1_deck} \nCPU: {cpu_deck}")


def compare_cards(card_deck):
    round = 1
    pile = []
    while len(card_deck[0]) != 0 or len(card_deck[1]) != 0:
        print_round(round)
        round += 1
        p1card = p1_card(card_deck)
        cpucard = cpu_card(card_deck)
        print_card(card_deck)
        if value(p1card) > value(cpucard):
            print('P1 card higher')
            card_deck[0] = card_deck[0] + win(card_deck) + pile
            pile = []
            print_card_len(card_deck)
        elif value(p1card) < value(cpucard):
            print("CPU card higher")
            card_deck[1] = card_deck[1] + win(card_deck) + pile
            pile = []
            print_card_len(card_deck)
        else:
            print("WAR! You're taking one face-down card and the battle continues...")
            pile += (tie(card_deck))
            continue
        check_winner(card_deck)


def win(card_deck):
    cards = []
    cards.append(card_deck[0].pop(0))
    cards.append(card_deck[1].pop(0))
    shuffle(cards)
    return cards


def tie(card_deck):
    cards = []
    cards.append(card_deck[0].pop(0))
    cards.append(card_deck[1].pop(0))
    cards.append(card_deck[0].pop(0))
    cards.append(card_deck[1].pop(0))
    shuffle(cards)
    return cards


def check_winner(deck_values):
    if len(deck_values[0]) == 0 or len(deck_values[1]) == 0:
        if len(deck_values[0]) == 0:
            print("\n\nYou do not have any cards left... CPU WINS!")
            exit()
        elif len(deck_values[1]) == 0:
            print("\n\nCPU do not have any cards left... YOU WON!")
            exit()


def main():
    cards = deal_cards(create_deck())
    compare_cards(cards)


if __name__ == '__main__':
    main()
