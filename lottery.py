import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))
print(lottery_numbers)
# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

temp = 0
for player in players:
    numbers_matched = len(lottery_numbers.intersection(player["numbers"]))
    if numbers_matched > temp:
        winner = player["name"]
        temp = numbers_matched
        winnings = 100 ** numbers_matched

print(f"{winner} won {winnings}.")

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

############################################
#official solution
# top_player = players[0]  # start by saying "the top matching player is the first one"
#
# for player in players:  # Go over each player
#     matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
#     if matched_numbers > len(
#             top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
#         top_player = player  # Say this player is the new top player