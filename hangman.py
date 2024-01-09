import random

def hangman():
    word_list = [
    "time", "year", "people", "way", "day", "man", "government", "company", "hand", "part",
    "place", "case", "problem", "fact", "eye", "friend", "child", "example", "job", "business",
    "word", "team", "number", "home", "body", "woman", "power", "country", "city", "night",
    "morning", "family", "life", "childhood", "world", "system", "water", "school", "food",
    "money", "air", "game", "history", "story", "knowledge", "change", "sound", "voice", "mind",
    "power", "father", "mother", "parent", "man", "woman", "child", "girl", "boy", "brother",
    "sister", "friend", "neighbor", "guest", "person", "doctor", "teacher", "student", "worker",
    "artist", "actor", "actress", "singer", "writer", "author", "scientist", "engineer", "lawyer",
    "policeman", "fireman", "soldier", "captain", "king", "queen", "prince", "princess", "animal",
    "dog", "cat", "horse", "bird", "fish", "rabbit", "turtle", "snake", "lion", "tiger",
    "elephant", "bear", "monkey", "zebra", "giraffe", "dolphin", "whale", "snake", "spider", "bug",
    "flower", "tree", "grass", "cloud", "rain", "snow", "sun", "moon", "star", "sky",
    "earth", "ocean", "river", "mountain", "island", "desert", "forest", "building", "house", "room",
    "door", "window", "floor", "ceiling", "wall", "roof", "bed", "table", "chair", "sofa",
    "desk", "lamp", "book", "pen", "paper", "computer", "phone", "television", "radio", "car",
    "bus", "train", "plane", "bicycle", "boat", "ship", "road", "street", "bridge", "park",
    "garden", "beach", "lake", "river", "forest", "field", "farm", "mountain", "hill", "valley"
]
    word = random.choice(word_list)
    vowels = "aeiou"
    guesses = " "
    attempts = 10
    print("Welcome to hangman, Guess the word in 10 attempts")

    while attempts > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            elif char.lower() in vowels:
                print("x", end=" ")
            else:
                print("_", end=" ")
                failed += 1
        if failed == 0:
            print("\nYou have guessed it right!")
            break
        guess = input("\nGuess a letter or a word: ").lower()

        if len(guess) == 1:
            if guess in guesses:
                print("You have already guessed that letter.")
            else:
                guesses += guess
                if guess in word:
                    print("Correct.")
                else:
                    print("Wrong, try again.")
                    attempts -= 1
                    print("Attempts remaining are", attempts)
        elif len(guess) > 1:
            if guess == word:
                print("You have guessed the word!")
                break
            else:
                print("Wrong word, try again.")
    if attempts == 0:
        print("Game over.")
        print("The word was", word)

hangman()