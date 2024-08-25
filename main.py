# Jeremy Clark
# ASCII Art Block Letter Initials
# 2024-08-25

# Write a python program that can print the user's initials in ASCII Art block Letters

# Hard code first initial to test that the renderLetter function works
firstInitial = "Q"

# =====================================================
# Store each line of the alphabet into a dictionary.
# =====================================================

''' Instead of storing each line into dictionary, may try testing whether can store 2D array as values in dict.'''


# First line of each letter:
firstline = {
  #  : "1 2 3 4 5"
  'A': "    A    ",
  #  : "1 2 3 4 5"
  'B': "B B B B  ",
  #  : "1 2 3 4 5"
  'C': "  C C C  ",
  #  : "1 2 3 4 5"
  'D': "D D D D  ",
  #  : "1 2 3 4 5"
  'E': "E E E E E",
  #  : "1 2 3 4 5"
  'F': "F F F F F",
  #  : "1 2 3 4 5"
  'G': "  G G G  ",
  #  : "1 2 3 4 5"
  'H': "H       H",
  #  : "1 2 3 4 5"
  'I': "I I I I I",
  #  : "1 2 3 4 5"
  'J': "J J J J J",
  #  : "1 2 3 4 5"
  'K': "K       K",
  #  : "1 2 3 4 5"
  'L': "L        ",
  #  : "1 2 3 4 5"
  'M': "M       M",
  #  : "1 2 3 4 5"
  'N': "N       N",
  #  : "1 2 3 4 5"
  'O': "  O O O  ",
  #  : "1 2 3 4 5"
  'P': "P P P P  ",
  #  : "1 2 3 4 5"
  'Q': "  Q Q Q  ",
  #  : "1 2 3 4 5"
  'R': "R R R R  ",
  #  : "1 2 3 4 5"
  'S': "  S S S  ",
  #  : "1 2 3 4 5"
  'T': "T T T T T",
  #  : "1 2 3 4 5"
  'U': "U       U",
  #  : "1 2 3 4 5"
  'V': "V       V",
  #  : "1 2 3 4 5"
  'W': "W       W",
  #  : "1 2 3 4 5"
  'X': "X       X",
  #  : "1 2 3 4 5"
  'Y': "Y       Y",
  #  : "1 2 3 4 5"
  'Z': "Z Z Z Z Z",
}

# Second line of each letter:
secondline = {
  #  : "1 2 3 4 5"
  'A': "   A A   ",
  #  : "1 2 3 4 5"
  'B': "B       B",
  #  : "1 2 3 4 5"
  'C': "C       C",
  #  : "1 2 3 4 5"
  'D': "D      D ",
  #  : "1 2 3 4 5"
  'E': "E        ",
  #  : "1 2 3 4 5"
  'F': "F        ",
  #  : "1 2 3 4 5"
  'G': "G       G",
  #  : "1 2 3 4 5"
  'H': "H       H",
  #  : "1 2 3 4 5"
  'I': "    I    ",
  #  : "1 2 3 4 5"
  'J': "    J    ",
  #  : "1 2 3 4 5"
  'K': "K     K  ",
  #  : "1 2 3 4 5"
  'L': "L        ",
  #  : "1 2 3 4 5"
  'M': "M M   M M",
  #  : "1 2 3 4 5"
  'N': "N N     N",
  #  : "1 2 3 4 5"
  'O': " O     O ",
  #  : "1 2 3 4 5"
  'P': "P       P",
  #  : "1 2 3 4 5"
  'Q': " Q     Q ",
  #  : "1 2 3 4 5"
  'R': "R       R",
  #  : "1 2 3 4 5"
  'S': "S       S",
  #  : "1 2 3 4 5"
  'T': "    T    ",
  #  : "1 2 3 4 5"
  'U': "U       U",
  #  : "1 2 3 4 5"
  'V': " V     V ",
  #  : "1 2 3 4 5"
  'W': "W       W",
  #  : "1 2 3 4 5"
  'X': " X     X ",
  #  : "1 2 3 4 5"
  'Y': " Y     Y ",
  #  : "1 2 3 4 5"
  'Z': "        Z",
}

# Third line of each letter:
thirdline = {
  #  : "1 2 3 4 5"
  'A': " A     A ",
  #  : "1 2 3 4 5"
  'B': "B       B",
  #  : "1 2 3 4 5"
  'C': "C        ",
  #  : "1 2 3 4 5"
  'D': "D       D",
  #  : "1 2 3 4 5"
  'E': "E        ",
  #  : "1 2 3 4 5"
  'F': "F        ",
  #  : "1 2 3 4 5"
  'G': "G        ",
  #  : "1 2 3 4 5"
  'H': "H       H",
  #  : "1 2 3 4 5"
  'I': "    I    ",
  #  : "1 2 3 4 5"
  'J': "    J    ",
  #  : "1 2 3 4 5"
  'K': "K   K    ",
  #  : "1 2 3 4 5"
  'L': "L        ",
  #  : "1 2 3 4 5"
  'M': "M  M M  M",
  #  : "1 2 3 4 5"
  'N': "N  N    N",
  #  : "1 2 3 4 5"
  'O': "O       O",
  #  : "1 2 3 4 5"
  'P': "P       P",
  #  : "1 2 3 4 5"
  'Q': "Q       Q",
  #  : "1 2 3 4 5"
  'R': "R       R",
  #  : "1 2 3 4 5"
  'S': "S        ",
  #  : "1 2 3 4 5"
  'T': "    T    ",
  #  : "1 2 3 4 5"
  'U': "U       U",
  #  : "1 2 3 4 5"
  'V': " V     V ",
  #  : "1 2 3 4 5"
  'W': "W       W",
  #  : "1 2 3 4 5"
  'X': "  X   X  ",
  #  : "1 2 3 4 5"
  'Y': "  Y   Y  ",
  #  : "1 2 3 4 5"
  'Z': "      Z  ",
}

# Fourth line of each letter:
fourthline = {
  #  : "1 2 3 4 5"
  'A': "A A A A A",
  #  : "1 2 3 4 5"
  'B': "B B B    ",
  #  : "1 2 3 4 5"
  'C': "C        ",
  #  : "1 2 3 4 5"
  'D': "D       D",
  #  : "1 2 3 4 5"
  'E': "E E E    ",
  #  : "1 2 3 4 5"
  'F': "F F F    ",
  #  : "1 2 3 4 5"
  'G': "G   G G G",
  #  : "1 2 3 4 5"
  'H': "H H H H H",
  #  : "1 2 3 4 5"
  'I': "    I    ",
  #  : "1 2 3 4 5"
  'J': "    J    ",
  #  : "1 2 3 4 5"
  'K': "K K      ",
  #  : "1 2 3 4 5"
  'L': "L        ",
  #  : "1 2 3 4 5"
  'M': "M   M   M",
  #  : "1 2 3 4 5"
  'N': "N   N   N",
  #  : "1 2 3 4 5"
  'O': "O       O",
  #  : "1 2 3 4 5"
  'P': "P P P P  ",
  #  : "1 2 3 4 5"
  'Q': "Q       Q",
  #  : "1 2 3 4 5"
  'R': "R R R R  ",
  #  : "1 2 3 4 5"
  'S': "  S S S  ",
  #  : "1 2 3 4 5"
  'T': "    T    ",
  #  : "1 2 3 4 5"
  'U': "U       U",
  #  : "1 2 3 4 5"
  'V': " V     V ",
  #  : "1 2 3 4 5"
  'W': "W   W   W",
  #  : "1 2 3 4 5"
  'X': "    X    ",
  #  : "1 2 3 4 5"
  'Y': "    Y    ",
  #  : "1 2 3 4 5"
  'Z': "    Z    ",
}

fifthline = {
  #  : "1 2 3 4 5"
  'A': "A       A",
  #  : "1 2 3 4 5"
  'B': "B       B",
  #  : "1 2 3 4 5"
  'C': "C        ",
  #  : "1 2 3 4 5"
  'D': "D       D",
  #  : "1 2 3 4 5"
  'E': "E        ",
  #  : "1 2 3 4 5"
  'F': "F        ",
  #  : "1 2 3 4 5"
  'G': "G       G",
  #  : "1 2 3 4 5"
  'H': "H        H",
  #  : "1 2 3 4 5"
  'I': "    I    ",
  #  : "1 2 3 4 5"
  'J': "J   J    ",
  #  : "1 2 3 4 5"
  'K': "K   K    ",
  #  : "1 2 3 4 5"
  'L': "L        ",
  #  : "1 2 3 4 5"
  'M': "M       M",
  #  : "1 2 3 4 5"
  'N': "N    N  N",
  #  : "1 2 3 4 5"
  'O': "O       O",
  #  : "1 2 3 4 5"
  'P': "P        ",
  #  : "1 2 3 4 5"
  'Q': "Q       Q",
  #  : "1 2 3 4 5"
  'R': "R   R    ",
  #  : "1 2 3 4 5"
  'S': "        S",
  #  : "1 2 3 4 5"
  'T': "    T    ",
  #  : "1 2 3 4 5"
  'U': "U       U",
  #  : "1 2 3 4 5"
  'V': "  V   V  ",
  #  : "1 2 3 4 5"
  'W': "W  W W  W",
  #  : "1 2 3 4 5"
  'X': "  X   X  ",
  #  : "1 2 3 4 5"
  'Y': "    Y    ",
  #  : "1 2 3 4 5"
  'Z': "  Z      ",
}

sixthline = {
  #  : "1 2 3 4 5"
  'A': "A       A",
  #  : "1 2 3 4 5"
  'B': "B       B",
  #  : "1 2 3 4 5"
  'C': "C       C",
  #  : "1 2 3 4 5"
  'D': "D      D ",
  #  : "1 2 3 4 5"
  'E': "E        ",
  #  : "1 2 3 4 5"
  'F': "F        ",
  #  : "1 2 3 4 5"
  'G': " G     G ",
  #  : "1 2 3 4 5"
  'H': "H        H",
  #  : "1 2 3 4 5"
  'I': "    I    ",
  #  : "1 2 3 4 5"
  'J': " J  J    ",
  #  : "1 2 3 4 5"
  'K': "K     K  ",
  #  : "1 2 3 4 5"
  'L': "L        ",
  #  : "1 2 3 4 5"
  'M': "M       M",
  #  : "1 2 3 4 5"
  'N': "N     N N",
  #  : "1 2 3 4 5"
  'O': " O     O ",
  #  : "1 2 3 4 5"
  'P': "P        ",
  #  : "1 2 3 4 5"
  'Q': " Q     Q ",
  #  : "1 2 3 4 5"
  'R': "R     R  ",
  #  : "1 2 3 4 5"
  'S': "S       S",
  #  : "1 2 3 4 5"
  'T': "    T    ",
  #  : "1 2 3 4 5"
  'U': " U     U ",
  #  : "1 2 3 4 5"
  'V': "   V V   ",
  #  : "1 2 3 4 5"
  'W': "W W   W W",
  #  : "1 2 3 4 5"
  'X': " X     X ",
  #  : "1 2 3 4 5"
  'Y': "    Y    ",
  #  : "1 2 3 4 5"
  'Z': "Z        ",
}

# Last line of each letter
seventhline = {
  #  : "1 2 3 4 5"
  'A': "A       A",
  #  : "1 2 3 4 5"
  'B': "B B B B  ",
  #  : "1 2 3 4 5"
  'C': "  C C C  ",
  #  : "1 2 3 4 5"
  'D': "D D D D  ",
  #  : "1 2 3 4 5"
  'E': "E E E E E",
  #  : "1 2 3 4 5"
  'F': "F        ",
  #  : "1 2 3 4 5"
  'G': "  G G G  ",
  #  : "1 2 3 4 5"
  'H': "H        H",
  #  : "1 2 3 4 5"
  'I': "I I I I I",
  #  : "1 2 3 4 5"
  'J': "  J J    ",
  #  : "1 2 3 4 5"
  'K': "K       K",
  #  : "1 2 3 4 5"
  'L': "L L L L L",
  #  : "1 2 3 4 5"
  'M': "M       M",
  #  : "1 2 3 4 5"
  'N': "N       N",
  #  : "1 2 3 4 5"
  'O': "  O O    ",
  #  : "1 2 3 4 5"
  'P': "P        ",
  #  : "1 2 3 4 5"
  'Q': "  Q Q  Q ",
  #  : "1 2 3 4 5"
  'R': "R       R",
  #  : "1 2 3 4 5"
  'S': "  S S S  ",
  #  : "1 2 3 4 5"
  'T': "    T    ",
  #  : "1 2 3 4 5"
  'U': "  U U U  ",
  #  : "1 2 3 4 5"
  'V': "    V    ",
  #  : "1 2 3 4 5"
  'W': "W       W",
  #  : "1 2 3 4 5"
  'X': "X       X",
  #  : "1 2 3 4 5"
  'Y': "    Y    ",
  #  : "1 2 3 4 5"
  'Z': "Z Z Z Z Z",
}




# Define renderLetter Function
''' Given the provided initial(s), print each line to the console.
    Since console prints line-by-line, concatenating individual lines for each block letter and printing them vertically
    is the best solution I've come up with so far.'''

''' Current state can take one alphabetical character and retrieve the value from dictionary.'''
def renderLetter(l):
  initial = l.upper()
  line1 = firstline.get(initial)
  line2 = secondline.get(initial)
  line3 = thirdline.get(initial)
  line4 = fourthline.get(initial)
  line5 = fifthline.get(initial)
  line6 = sixthline.get(initial)
  line7 = seventhline.get(initial)
  wholeLetter = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7
  print(wholeLetter)
  # End renderLetter function

# Call renderLetter function.

renderLetter(firstInitial)
