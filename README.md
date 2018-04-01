# gess
# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print('Well,' + myName + ',I am thinking of a number between 1 and  20.')

while guessesTaken < 6:
    print('请输入数字')
    guess = input()
    guess = int(sprint('你的数字太小')

    if guess > number :
        print('你的数字太大')

    if guess == number:
        break

if guess == number :
    guessesTaken = str( guessesTaken)
    print('Good job ,' + '! You guessed my number in' + guessesTaken + 'guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number i was thinking of was ' + number)
