import random
FIGURES_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}
P1 = 0
CPU = 1


def create_and_shuffle_deck():
    """combine 52 card decks by figure+colour e.g. "A♦" and shuffle it"""

    figures = ["2", "3", "4", "5", "6", "7",
               "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["♠", "♦", "♥", "♣"]
    deck = [(str(f)+c) for f in figures for c in colours]
    random.shuffle(deck)
    return deck


def deal_cards(deck):
    """divide deck into player and cpu"""

    player_deck = []
    cpu_deck = []
    for num, card in enumerate(deck):
        if num % 2 == 0:
            player_deck.append(card)
        else:
            cpu_deck.append(card)
    return player_deck, cpu_deck


def create_values_deck(deck):
    """convert player and cpu deck each figure into value e.g. "5♦" = 5 or "Q♣" = 12"""

    player_deck = deck[0]
    cpu_deck = deck[1]
    player_values = [FIGURES_VALUES[card[:-1]] for card in player_deck]
    cpu_values = [FIGURES_VALUES[card[:-1]] for card in cpu_deck]
    return player_values, cpu_values

def compare_cards(deck, deck_values):
    card_count = 0
    your_score = 0
    cpu_score = 0
    for card in deck[0]:
        print(f"Your card: {deck[0][card_count]}")
        print(f"Opponents card: {deck[1][card_count]}")
        if deck_values[0][card_count] > deck_values[1][card_count]:
            print('Your card is higher')
            your_score += 1
        elif deck_values[0][card_count] == deck_values[1][card_count]:
            print('WAAAR!!!!')
        else:
            print("Opponent's card is higher")
            cpu_score += 1
        print(f"Cards left:")
        print(f"You: {your_score}")
        print(f"CPU: {cpu_score}")
        print("=" * 20)
        card_count += 1
    if your_score > cpu_score:
        print("YOU WON")
    elif your_score == cpu_score:
        print("It's draw")
    else:
        print("CPU WON")

# def main():
#     play_deck = create_and_shuffle_deck()
#     deal = deal_cards(play_deck)
#     cards = create_values_deck(deal)
#     compare_cards(deal, cards)

# if __name__ == '__main__':
#     main()

def p1_win(card_list):
    card_list[0].append(card_list[0][0])
    card_list[0].append(card_list[1][0])
    card_list[0].remove(card_list[0][0])
    card_list[1].remove(card_list[1][0])

def cpu_win(card_list):
    card_list[1].append(card_list[1][0])
    card_list[1].append(card_list[0][0])
    card_list[0].remove(card_list[0][0])
    card_list[1].remove(card_list[1][0])

list_a = [[4, 6, 8, 11],[18, 2, 3, 5]]
while list_a[0] or list_a[1]:
    if len(list_a[0]) == 0:
        print("CPU WINS!")
        break
    elif len(list_a[1]) == 0:
        print("P1 WINS!")
        break
    else:
        if list_a[0][0] > list_a[1][0]:
            p1_win(list_a)
        elif list_a[0][0] < list_a[1][0] or list_a[0][0] == list_a[1][0]:
            cpu_win(list_a)
        print(f"P1 cards left: {len(list_a[0])}")
        print(f"CPU cards left: {len(list_a[1])}")
