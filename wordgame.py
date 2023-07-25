# Mapping letters to their corresponding points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Creating a dictionary to map letters to their points
letter_to_points = {letter: point for letter, point in zip(letters, points)}

def score_word(word):
    # Calculate the total points for a given word
    point_total = 0
    for letter in word:
        # Check if the letter exists in the letter_to_points dictionary
        if letter in letter_to_points:
            point_total += letter_to_points[letter]
    return point_total

# Player words and their corresponding points
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}

def update_point_totals():
    # Calculate total points for each player and update player_to_points dictionary
    for player, words in player_to_words.items():
        player_points = 0
        for player_word in words:
            player_points += score_word(player_word)
        player_to_points[player] = player_points
    print(player_to_points.items())

def play_word(new_player, new_word):
    if new_player in player_to_words:
        # Convert the new word to uppercase and add it to the player's list of words
        player_to_words[new_player].append(new_word.upper())
    else:
        print("This is not a registered player")

# Test the play_word function
play_word("player1", "Furqan")
print(player_to_words.get("player1"))

# Update the point totals after playing a new word
update_point_totals()
