#a=[1,2,3,4,5]

#b=[x*2 for x in a]
#print(b)

#x={'a':1,'b':2}
#c=[x for x in x.keys()]
#print(c)
d=[13, 14, 15, 16, 17]

players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]
top_player=players[0]

for i in players:
  matching_results=len(i['numbers'].intersection(d))
  if matching_results>len(top_player['numbers'].intersection(d)):
    top_player=i
print(top_player)