import random
FIGURES_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}


def shuffle_deck():
    """combine 52 card decks by figure+colour e.g. "A♦" and divide into player and cpu
    then convert player and cpu deck each figure into value e.g. "5♦" = 5 or "Q♣" = 12

    Returns:
        list: returns two dictionaries?
    """

    figures = ["2", "3", "4", "5", "6", "7",
               "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["♠", "♦", "♥", "♣"]
    deck = [(str(f)+c) for f in figures for c in colours]
    random.shuffle(deck)
    player_deck = []
    cpu_deck = []
    for num, card in enumerate(deck):
        if num % 2 == 0:
            player_deck.append(card)
        else:
            cpu_deck.append(card)
    player_values = [FIGURES_VALUES[card[:-1]] for card in player_deck]
    cpu_values = [FIGURES_VALUES[card[:-1]] for card in cpu_deck]
    return [player_deck, cpu_deck], [player_values, cpu_values]


def divide_cards():
    """parts figure and value decks for player and cpu

    Returns:
        _type_: _description_
    """

    cards = shuffle_deck()
    player_cards = cards[0][0]
    player_values = cards[1][0]
    cpu_cards = cards[0][1]
    cpu_values = cards[1][1]
    return [player_cards, player_values], [cpu_cards, cpu_values]

# def main():
#     deck = shuffle_deck()
#     print(deck)

# if __name__ == '__main__':
#     main()


a = divide_cards()
