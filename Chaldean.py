counter = 0
numb = 0

print("Decode the word: ")
word = input()
for element in range(0, len(word)):
  if word[element] == " ":
    print("")
  elif word[element] == "A" or word[element] == "a" or word[element] == "I" or word[element] == "i" or word[element] == "J" or word[element] == "j" or word[element] == "Q" or word[element] == "q" or word[element] == "Y" or word[element] == "y":
      counter = counter + 1
      numb = 1
  elif word[element] == "B" or word[element] == "b" or word[element] == "K" or word[element] == "k" or word[element] == "R" or word[element] == "r":
    counter = counter + 2
    numb = 2
  elif word[element] == "C" or word[element] == "c" or word[element] == "G" or word[element] == "g" or word[element] == "L" or word[element] == "l" or word[element] == "S" or word[element] == "s":
    counter = counter + 3
    numb = 3
  elif word[element] == "D" or word[element] == "d" or word[element] == "M" or word[element] == "m" or word[element] == "T" or word[element] == "t":
    counter = counter + 4
    numb = 4
  elif word[element] == "E" or word[element] == "e" or word[element] == "H" or word[element] == "h" or word[element] == "N" or word[element] == "n" or word[element] == "X" or word[element] == "x":
    counter = counter + 5
    numb = 5
  elif word[element] == "U" or word[element] == "u" or word[element] == "V" or word[element] == "v" or word[element] == "W" or word[element] == "w":
    counter = counter + 6
    numb = 6
  elif word[element] == "O" or word[element] == "o" or word[element] == "Z" or word[element] == "z":
    counter = counter + 7
    numb = 7
  elif word[element] == "F" or word[element] == "f" or word[element] == "P" or word[element] == "p":
    counter = counter + 8
    numb = 8
  if numb == 0:
    numb = 0
  else:
    print(word[element]," ",numb)
  numb = 0
print(counter)