'''
    Program name: Wordle Solver (main.py) 
    Author: Alexander Perez 
    Date created: 9/16/2022 
    A program that can help guess logical words for you in the game Wordle. 
    I Alexander Perez agree to the honor code. 
''' 

#This opens the csv file you provided us 
with open("words_freqs.csv", "r") as freq:
    words_freq = freq.read().splitlines()
#This opens the words you provided us
with open("words.txt", "r") as words:
    words_list = words.read().splitlines()

def welcome():
  print("Welcome to Wordle Solver!")
  print("Wordle Solver will give you the most effective words to guess!")
welcome()

freq_array = [] 
for line in words_freq:
    line = line.split(",")
    freq_array.append(line)

def find_word(freq_array):
    prev_word = ["", -1]
    for word_array in freq_array:
      word = word_array[0]
      freq = float(word_array[1])
      if freq > float(prev_word[1]):
        prev_word = word_array

    return prev_word[0]

def find_first_word(freq_array):
    # The theoretically best word should have the most vowels, highest popularity,and no repeats
    vowel_threshold = 4 # How many vowels does the first word need?
    prev_word = ["", -1]

    for word_array in freq_array:
        word = word_array[0]
        freq = float(word_array[1])
        vowels = vowel_count(word)
        prev_freq = float(prev_word[1])
        if freq > prev_freq and not find_repeats(word) and vowels >= vowel_threshold:
            prev_word = word_array

    return prev_word[0]

def remove_words_by_letter(letter, array):
    # Remove all words that contain a given letter from an array
    # Using list comprehensions
    return [word_array for word_array in array if word_array[0].count(letter) == 0]

def force_letter(letter, position, array):
    # Remove all words that don't contain a given letter
    return [word_array for word_array in array if word_array[0].count(letter) > 0 and word_array[0][position] != letter]

def force_letter_position(letter, position, array):
    # Remove all words that don't contain a given letter at a given position
    return [word_array for word_array in array if position in [pos for pos, char in enumerate(word_array[0]) if char == letter]]

def vowel_count(word):
    # Return the number of vowels in a word
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    # Iterate through letters, seeing if they are vowels
    for letter in word:
        if letter in vowels:
            count += 1

    return count

def find_repeats(word):
    # Return whether or not the given word has repeats
    letter_count = {}
    for letter in word:
        try:
            if letter_count[letter] > 0:
                return True
        except KeyError:
            letter_count[letter] = 1

    return False

def make_guess(freq_array, is_first):
    if is_first:
        guess = find_first_word(freq_array)
    else:
        guess = find_word(freq_array)

    print(f"Guess: {guess}\n")
    states = []
    for i, letter in enumerate(guess):
        state = str(input(f"{letter} g/y/n? "))
        states.append(state)

        if state == "n": # Letter does not appear, should be removed from possible words
            freq_array = remove_words_by_letter(letter, freq_array)
        elif state == "g":
            freq_array = force_letter_position(letter, i, freq_array)
        elif state == "y":
            freq_array = force_letter(letter, i, freq_array)

    print("\n")
    return freq_array

attempts = 5
attempt_count = 0
while len(freq_array) > 1:
    if attempt_count > attempts:
        print("Oops! We couldn't get the word in time!")
        break

    freq_array = make_guess(freq_array, attempt_count == 0)
    if len(freq_array) == 1:
        print(f"The word is {freq_array[0][0]}")
    elif len(freq_array) < 1:
        print("No valid possibilities. YOU DID SOMETHING WRONG ")

    attempt_count += 1