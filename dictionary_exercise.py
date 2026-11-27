letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

letter_to_points = {letter:point for letter, point in zip(letters, points)}

for letter,point in zip(letters, points):
  letter_to_points[letter.lower()] = point

print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

print(score_word("ALEX"))

brownie_points = score_word("BROWNIE")

print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

#print(player_to_points)

def play_word(player, word):
  player_to_words[player] += [word]
  return player_to_words

print(play_word("player1", "ALEX"))
print(play_word("player1", "ALEX"))
play_word("wordNerd", "CUREA")
play_word("Lexi Con", "BENCH")
play_word("Prof Reader", "GIGEL")
play_word("player1", "john")

print(update_point_totals())
