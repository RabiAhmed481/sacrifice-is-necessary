# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters

define y = Character("You", color="#dbcd51")

#backgrounds

image door_rain = "bg1.png"

# The game starts here.

label start:
    scene door_rain
    y "Huh..."
    y "What is this place...? Where am I?"
    "*you wake up in a place you don't recognize, it's raining hard*"
    "*do you want to knock on the door in front of you?*"
    menu:
        "open the door":
            jump open_door
        "stay put":
            jump no_open_door

label open_door:
    y "*you approach the door and knock*"
    jump start2

label no_open_door:
    y "*it's really late and your cold, lost, and confused. You have nowhere else to go*"
    menu:
        "open the door":
            jump open_door
    

label start2:
    y "start 2"
    return
