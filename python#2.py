import random
HANGMANPICS = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
========= ''']


word_list = ["azreal","alaska","menaroi","batman"]
collection = []

lives = 6
word = random.choice(word_list)
print(word)

word_len = len(word)
store = ""
for postion in range(word_len):
    store += "_"
print(store)

game_over = False

while not game_over:
    guess = input("Guess the letter\n").lower()

    if guess in collection:
        print(f"You already guessed {guess}")
    display = ""
    
    for letter in word:
        if letter == guess:
            display += letter
            collection.append(letter)
        elif letter in collection:
            display += letter
        else:
            display += "_"
    
    print(f"Word guess: {display}")

    
        
    if "_" not in display:
        print("You win")
        game_over = True
        
        
    if guess not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lost")


    print(HANGMANPICS[lives]) 