# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")


# The game starts here.

label start:
    y "Huh..."
    y "What is this place...? Where am I?"
    "*you wake up in a place you don't recognize, it's pouring hard*"
    "*do you want to knock on the door in front of you?*"

    return
