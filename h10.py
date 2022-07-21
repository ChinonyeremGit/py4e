tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

# What was that?
print(tabby_cat + "{}".format("that's_great\nnice"))
# SyntaxError: unexpected character after line continuation character
