# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define y = Character("You", color="#dbcd51")
define n = Character ("...", color="#A60909")
define v = Character("Veronica", color="#A60909")

#sprites
image veronica_sleepy = "veronica sleepy.png"
image veronica_concerned = "veronic concern"
image veronica_slight = "veronica slight concern"
image veronica_casual= "veronica casual"

#backgrounds

image door_rain = "bg1.png"
image inside_house = "veronica house inside"

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
    "*while you wait you're relivied to be saved from the rain under the porch*"
    show veronica_sleepy
    n "Hello? Who's there at this hour?"
    hide veronica_sleepy
    show veronica_concerned
    n "Oh my god, you're soaked! Do you have anywhere to go?"
    y "No, where am I?"
    y "What time is it?"
    hide veronica_concerned
    show veronica_slight
    v "Oh dear, my name is Veronica, it's late and you're drenched."
    v "Come in, you can warm up and we can figure things out from there."
    jump scene2


label no_open_door:
    y "*it's really late and your cold, lost, and confused. You have nowhere else to go*"
    menu:
        "open the door":
            jump open_door
    

label scene2:
    scene inside_house with fade
    "*you step inside Veronicas warm and dry house, despite the clutter it's oddly comforting*"
    show veronica_casual
    v "Here, drink this! I made you some chamomile tea"
    v "It'll warm you up!"
    "*do you want to take up her offer?*"
    menu:
        "take the tea":
            jump accept_tea
        "refuse":
            jump refuse_tea

label accept_tea:
    y "*you take the tea, it feels warm and soothing for your shivering body*"
    y "Thank you, the tea is great. I really needed this"
    v "No problem, it's the least I could do for you"

label refuse_tea:
    hide veronica_casual
    show veronica_slight
    v "Oh, are you sure?"
    y "Yes, sorry for making you go through the trouble of making it"
    v "Alright, if you're sure"
    hide veronica_slight with dissolve
    "*as veronica walks off you wonder if you were being rude*"
    y "/it's better not to accept anything to eat or drink from a stranger anyway/ you mumble to yourself"


    return
