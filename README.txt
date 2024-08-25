==========================================================
ASCII Art Block Letter Initials
==========================================================
Jeremy Clark
2024-08-25

From Codecademy Learn Python Course:
Write a Python program that displays the initials of your name in block letters as
shown and dip your toes into ASCII art.

Prompt user for their initials
Store initials as string
Use the string to display user's initials as ASCII Art Block letters

Implementation:
1. Each letter is represented by a 5x7 matrix, with is letter either "on" or "off" in each cell.
2. Each line of that matrix is then stored in a dictionary, representing each letter as a key and the line as the value.
   ex: Line1{ A: "    A     "}
3. The display function will iterate over each character in the user-provided string, concatenating the appropriate
   line of each letter so that the initials will be displayed correctly in the console output.
