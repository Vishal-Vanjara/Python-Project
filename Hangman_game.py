import random

words = ["APPLE","BANANA","CHICKOO","MANGO"]
word = random.choice(words)

total_chances = 7
guessed_word = "-"*len(word)

print("Guess the Fruit Name")

while total_chances != 0:
  print(guessed_word)
  letter = input("Guess a letter:").upper()
  if letter in word:
    for index in range(len(word)):
      if word[index] == letter:
        guessed_word = guessed_word[:index]+letter+guessed_word[index +1:]
        print(guessed_word)
    if guessed_word == word:
      print("Game Over")
      print("Congrulation you Won the Game :")
      break
  else:
    total_chances = total_chances - 1
    print("Wrong choice")
    print("The remaining chances are:",total_chances)
else :
  print("Game Over")
  print("You Lose")
  print("All the chances are exhausted")
print("The correct word was: ",word)