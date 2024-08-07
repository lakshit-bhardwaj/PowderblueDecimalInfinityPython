lottery_numbers = {13, 21, 22, 5, 8}


players = [ {
    'name': 'Lakshit',
    'numbers': {1, 2, 3, 4, 5}
}, {
    'name': 'Kshitiz',
    'numbers': {1, 2, 3, 4, 5}
}
    ]

#for i in players:
 #   print(f"Player name {i['name']} has got {len(i['numbers'].intersection(lottery_numbers))} numbers right")

d={13, 14, 15, 16, 17}

players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

top_player=players[0]
print(top_player)
for i in players:
    if len(i['numbers'].intersection(d)) > len(top_player['numbers'].intersection(d)):
        top_player=i
print(top_player['name'], len(top_player['numbers'].intersection(d)))