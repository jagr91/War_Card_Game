def create_deck():
    """combine 52 card decks by figure+colour e.g. "A♦" and shuffle it"""
    import random
    figures = ["2", "3", "4", "5", "6", "7",
               "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["♠", "♦", "♥", "♣"]
    deck = [(str(f)+c) for f in figures for c in colours]
    random.shuffle(deck)
    return deck
