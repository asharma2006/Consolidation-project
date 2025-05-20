# consolidation.py
import random

# Variables
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen']
RANK_VALUES = {rank: i+1 for i, rank in enumerate(RANKS)}

# Classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = RANK_VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(self.cards)

    def draw(self, num):
        drawn = self.cards[:num]
        self.cards = self.cards[num:]
        return drawn

    def reveal_top(self):
        if self.cards:
            return self.cards.pop(0)
        return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self, lead_suit=None):
        print(f"\n{self.name}'s hand:")
        for idx, card in enumerate(self.hand):
            print(f"{idx}: {card}")
        while True:
            try:
                choice = int(input(f"{self.name}, select a card index to play: "))
                chosen = self.hand[choice]
                if lead_suit and any(card.suit == lead_suit for card in self.hand) and chosen.suit != lead_suit:
                    print(f"You must follow suit ({lead_suit}). Try again.")
                    continue
                return self.hand.pop(choice)
            except (ValueError, IndexError):
                print("Invalid choice. Try again.")

def determine_round_winner(card1, card2, lead_suit, p1, p2):
    print(f"\n{p1.name} played: {card1}")
    print(f"{p2.name} played: {card2}")
    if card2.suit == lead_suit:
        winner = p1 if card1.value > card2.value else p2
    elif card1.suit == lead_suit:
        winner = p1
    else:
        winner = p1  # default if none follow suit
    winner.score += 1
    print(f"--> {winner.name} wins the round! (Score: {winner.score})")
    return winner

def should_deal_more(p1, p2):
    return len(p1.hand) == 4 and len(p2.hand) == 4

def check_game_end(p1, p2, rounds_played):
    if rounds_played >= 16:
        return True
    if (p1.score == 0 and p2.score == 16):
        p2.score = 17
        return True
    if (p2.score == 0 and p1.score == 16):
        p1.score = 17
        return True
    if (p1.score >= 9 and p2.score > 0) or (p2.score >= 9 and p1.score > 0):
        return True
    return False

def main():
    deck = Deck()
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    p1.draw_cards(deck.draw(8))
    p2.draw_cards(deck.draw(8))
    current_leader = p1 if random.choice([True, False]) else p2

    rounds_played = 0
    print(f"{current_leader.name} leads the first round.")

    while rounds_played < 11:
        print(f"\n--- Round {rounds_played + 1} ---")
        if current_leader == p1:
            card1 = p1.play_card()
            card2 = p2.play_card(lead_suit=card1.suit)
        else:
            card2 = p2.play_card()
            card1 = p1.play_card(lead_suit=card2.suit)

        lead_suit = card1.suit if current_leader == p1 else card2.suit
        current_leader = determine_round_winner(card1, card2, lead_suit, p1, p2)

        revealed = deck.reveal_top()
        if revealed:
            print(f"Revealed card from deck: {revealed}")
        else:
            print("Deck is empty. No card revealed.")

        rounds_played += 1

        if should_deal_more(p1, p2):
            p1.draw_cards(deck.draw(4))
            p2.draw_cards(deck.draw(4))
            print("Dealt 4 more cards to each player.")

        if check_game_end(p1, p2, rounds_played):
            break

    print("\n=== Game Over ===")
    print(f"{p1.name} score: {p1.score}")
    print(f"{p2.name} score: {p2.score}")
    if p1.score > p2.score:
        print(f"{p1.name} wins!")
    elif p2.score > p1.score:
        print(f"{p2.name} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()