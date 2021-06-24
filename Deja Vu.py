"""you aren't paying attention and you accidently type a bunch of random letters on your keyboard.
you want to know if you typed the same letters twice, or if they are all unique.
"""

letters = input("> ")
count = 0

for i in letters:
    count = count + letters.count(i)

if count==len(letters):
    print("Unique")
else:
    print("Not Unique")
