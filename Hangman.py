import random
HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
 ========''','''

 +---+
 |   |
 o   |
     |
     |
     |
 ========''','''

 +---+
 |   |
 o   |
 |   |
     |
     |
 ========''','''

 +---+
 |   |
 o   |
/|   |
     |
     |
 ========''','''

 +---+
 |   |
 o   |
/|\  |
     |
     |
 ========''','''

 +---+
 |   |
 o   |
/|\  |
/    |
     |
 ========''','''

 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
 ========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyota crow deer dog donky duck eagle ferret fox frog goat goose hawk lion lizard monkey moose rat raven seal'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HUANGMANPICS, missedletters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()


    print('Missed letter:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if sceretWord[i] in corre1ctLetter:
            blanks = blanks[:i] + sceretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end='')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGessed:
            print('You have alredy guessed that letter.Choose again.')
        elif guess not in 'abcdefghijklmnmopqrstuvwxyz':
                print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want ti play again？(yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetter =''
correctLetter = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetter, correctLetter, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLettters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundALLLettters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is '' ' + scretWord + ' ''! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetter + guess

        if len(missedLetters) == len(HANGAMEPICS) - 1:
            displayBoard(HANGAME_PICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guess!\nAfter ' + str(len(missedLetter))+ 'missed guesses and ' + str(len(correctLettterd)) + 'correct guesses, the word was '' ' + secretWord + ' ''' )
            gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break



S

            













    











        


