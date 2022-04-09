import deck

def deal_cards(deck):
    """deal deck into player and cpu"""

    p1_deck = []
    cpu_deck = []
    for num, card in enumerate(deck):
        if num % 2 == 0:
            p1_deck.insert(0, card)
        else:
            cpu_deck.insert(0, card)
    print([p1_deck, cpu_deck])
    return [p1_deck, cpu_deck]


def value(card):
    """checks card figure and returns its value e.g. "5♦" = 5 or "Q♣" = 12"""

    figures_values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value = figures_values[card[:-1]]
    return value


def print_round(number):
    round = f"Round no {number} started:"
    underline = "=" * len(round)
    print(f"{round}\n{underline}")


def compare_cards(card_deck):
    round = 1
    print_round(round)
    round += 1
    p1_card = card_deck[0][0]
    cpu_card = card_deck[1][0]
    print(f"P1: {p1_card}")
    print(f"CPU: {cpu_card}")
    if value(p1_card) > value(cpu_card):
        print('P1 card higher')
        card_deck[0] = card_deck[0] + win(card_deck)
    elif value(cpu_card) > value(p1_card):
        print("CPU card higher")
        card_deck[1] = card_deck[1] + win(card_deck)
    else:
        print("TIE")
    print(card_deck)
    print(len(card_deck[0]))
    print(len(card_deck[1]))


def win(card_deck):
    cards = []
    p1_card = card_deck[0].pop(0)
    cpu_card = card_deck[1].pop(0)
    cards.append(p1_card)
    cards.append(cpu_card)
    print(cards)
    return cards


def tie():
    pass


def check_winner(deck_values):
    if len(deck_values[0]) == 0 or len(deck_values[1]) == 0:
        if len(deck_values[0]) == 0:
            print("\n\nYou do not have any cards left... CPU WINS!")
            exit()
        elif len(deck_values[1]) == 0:
            print("\n\nCPU do not have any cards left... YOU WON!")
            exit()

def main():
    cards = deal_cards(deck.deck())
    compare_cards(cards)


if __name__ == '__main__':
    main()