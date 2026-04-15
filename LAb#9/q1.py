import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]
print(deck)

face_cards = [card for card in deck if card[0] in ['Jack', 'Queen', 'King']]

red_count = 0
heart_given_red = 0
red_subset_count = 0
diamond_given_face = 0
spade_or_queen_given_face = 0

trials = 100000


for _ in range(trials):
    
    card = random.choice(deck)
    if card[1] in ['Hearts', 'Diamonds']:
        red_count += 1

    card_q2 = random.choice(deck)
    if card_q2[1] in ['Hearts', 'Diamonds']:
        red_subset_count += 1
        if card_q2[1] == 'Hearts':
            heart_given_red += 1
        
    faceCard = random.choice(face_cards)
    if faceCard[1] == 'Diamonds':
        diamond_given_face += 1
    
    if faceCard[1] == 'Spades' or faceCard[0] == 'Queen':
        spade_or_queen_given_face += 1

print(f"Simulated P(Red): {red_count/trials}")
print(f"Simulated P(Heart | Red): {heart_given_red/red_subset_count}")
print(f"Simulated P(Diamond | Face): {diamond_given_face/trials}")
print(f"Simulated P(Spade or Queen | Face): {spade_or_queen_given_face/trials}")