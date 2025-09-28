# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define y = Character("You", color="#dbcd51")
define n = Character ("...", color="#A60909")
deine u = Character("...", color="#2028B9")
define v = Character("Veronica", color="#A60909")
define b = Character("Ben", color="#2028B9")

#sprites
image veronica_sleepy = "veronica sleepy.png"
image veronica_concerned = "veronic concern"
image veronica_slight = "veronica slight concern"
image veronica_casual= "veronica casual"
image veronica_casual_out = "veronica casual out"
image veronica_slight_out = "pls"
image veronica_laugh_out = "veronica laugh out"

image veronica_casual_ball = "veronica ball 1"
image veronica_slight_ball = "veronica ball 2"
image veronica_angry_ball = "veronica ball 3"
image veronica_vampire = "veronica vamp"
image ben_scared = "ben scaredd"
image image ben_relieved = "ben reliev"
image ben_sad = "ben sadd"
image ben_happy = "ben happ"
image ben_confused = "ben con"



image door_rain = "bg1.png"
image inside_house = "veronica house inside"
image room_night = "bed night"
image room_day = "bed morning"
image cafe = "caf"
iamage ballroom = "ball.jpg"

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
    "*as you drink the tea you start to feel sleepy*"
    y "The tea is warming me up, I feel so sleepy"
    hide veronica_casual 
    show veronica_slight
    v "I have a spare room you if you want to stay the night?"
    y "That would be great, thank you"
    jump bedroom

label refuse_tea:
    hide veronica_casual
    show veronica_slight
    v "Oh, are you sure?"
    y "Yes, sorry for making you go through the trouble of making it"
    v "Alright, if you're sure"
    hide veronica_slight with dissolve
    "*as veronica walks off you wonder if you were being rude*"
    y "\it's better not to accept anything to eat or drink from a stranger anyway\ you mumble to yourself"
    show veronica_slight
    v "So do you where you're going to stay tonight?"
    v "Do you have anyone to call?"
    y "No, sorry I don't know anyone here"
    y "I just remember waking up in the rain"
    v "Well, I have a spare room if you want to stay the night?"
    y "I might take you up on that offer, thank you"
    jump bedroom

label bedroom:
    scene room_night with fade
    "*you follow veronica to her spare room, it's small but cozy*"
    show veronica_casual
    v "Here you go, make yourself at home"
    v "If you need anything just let me know"
    v "There's a bathroom down the hall if you want to freshen up"
    y "Thank you, I really appreciate it"
    v "No problem, get some rest. Good night!"
    hide veronica_casual with dissolve
    "*you get ready for bed and lie down*"
    "*you lie down on the bed, it's surprisingly comfortable*"
    "*you wonder why a stranger would be so kind to you*"
    "*you feel your eyes getting heavy as you drift off to sleep*"
    scene room_day with fade
    "*you wake up the next morning feeling rested*"
    show veronica_casual
    v "Good morning! Did you sleep well?"
    y "Yes, thank you for letting me stay here"
    v "I'm glad to hear that. Do you want some breakfast?"
    y "Sure, that sounds great"
    v "Alright, get dressed let's go out!"
    hide veronica_casual
    show veronica_slight
    v "But umm, what's up with your clothes?"
    hide veronica_slight
    show veronica_casual
    v "We might need to get you some new ones especially since I have a suprise for you tonight!"
    y "Huh? A surprise?"
    v "You'll see, come on let's go!"
    jump outing

label outing:
    scene cafe with fade
    show veronica_casual_out with dissolve
    v "Here we are, this is my favorite cafe in town"
    y "It's nice, I've never been to a place like this before"
    v "Well, it's a good place to relax and have a nice meal"
    v "Plus, they have the best pastries!"
    y "Sounds great, I'm starving"
    v "Let's grab some food and find a table"
    hide veronica_casual_out with dissolve
    "*you and veronica enjoy a nice breakfast together, the food is delicious and the atmosphere is cozy*"
    y "So.. Veronica can I ask you something?"
    show veronica_slight_out
    v "Sure, what's on your mind?"
    y "What year is it? Everyone is dressed so differently from what I'm used to"
    hide veronica_slight_out
    show veronica_casual_out
    v "It's 1750, why do you ask?"
    y "HUH? I see..."
    y "I guess that explains why I don't recognize anything"
    hide veronica_casual_out
    show veronica_laugh_out
    v "Hahaha, I got you good didn't I?"
    v "Don't worry, it's 2025"
    hide veronica_laugh_out
    show veronica_casual_out
    v "This town is just really old fashioned"
    v "Anyway, I have a surprise for you later tonight"
    v "It kind of ties into the whole old fashoned thing"
    y "I can't wait to see what it is"
    hide veronica_casual_out 
    show veronica_slight_out
    v "You know, you might think it's really weird that I just let a stranger into my house last night"
    v "But i've been so loneley theese past few years and I just wanted to help someone in need"
    v "Plus, you seem like a nice person"
    v "While you're in town do you want to stay with me?"
    menu:
        "accept":
            jump accept_stay
        "decline":
            jump decline_stay

label decline_stay:
    y "I appreciate the offer but I think I should find my own place"
    y "Thank you for everything you've done for me"
    hide veronica_slight_out
    show veronica_casual_out
    v "I understand, if you change your mind the offer still stands"
    v "Enjoy the rest of your breakfast"
    "*you and veronica finish your breakfast and head back to her house*"
    "*you look forward to the surprise she has planned for you tonight*"
    show room_day with fade
    "*you arrive back at veronicas house and spend the day relaxing and getting to know each other*"
    show room_night with fade
    "*as night falls you wonder what the surprise could be*"
    jump ending1

label accept_stay: 
    y "That would be great, thank you"
    y "I've also really enjoyed spending time with you"
    hide veronica_slight_out 
    show veronica_casual_out
    v "I'm glad to hear that, I could use the company"
    v "Let's finish our breakfast and head back to my place"
    hide veronica_casual_out with dissolve
    "*you and veronica finish your breakfast and head back to her house*"
    "*you look forward to the surprise she has planned for you tonight*"
    show room_day with fade
    "*you arrive back at veronicas house and spend the day relaxing and getting to know each other*"
    show room_night with fade
    "*as night falls you wonder what the surprise could be*"
    jump ending2

label ending1:
    scene room_night with fade
    show veronica_casual with dissolve
    v "I wanted to do something special for you tonight."
    y "Special?"
    v "You’ve been through so much. I don’t want you to leave."
    v "Stay here. Stay with me. You won’t be cold or hungry again."
    "*her words are comforting, but you feel an odd heaviness in your chest*"
    y "If I stay… what happens to me?"
    hide veronica_casual
    show veronica_slight
    v "You’ll be safe. But the world outside — your memories, your name, your old life — you’ll have to let it go. You can’t have both."
    "*you realize she’s asking you to give up your freedom for her protection*"
    menu:
        "Sacrifice your freedom to stay":
            hide veronica_slight
            show veronica_casual
            y "Alright… I’ll stay. Even if it means losing who I was."
            v "Good… that’s all I wanted to hear."
            "*you feel your memories of the outside world begin to fade as Veronica smiles softly*"
            scene black with fade
            "*ENDING 1: You sacrificed your freedom to live safely at Veronica’s side.*"
            return

        "Refuse to give up your freedom":
            hide veronica_slight
            show veronica_angry
            v "Then go. Walk back into the storm. But you’ll have nothing and no one."
            y "I’d rather be free than live in a cage."
            "*you step out into the rain, cold but determined, the house fading behind you*"
            scene black with fade
            "*ENDING 1 (alternate): You sacrificed safety to keep your freedom — alone, but truly yourself.*"
            return


label ending2:
    backround room_night with fade
    show veronica_casual_ball with dissolve
    v "Surprise! I thought it would be fun to take you to a ball!"
    y "Wow, this is amazing! Thank you so much!"
    v "I'm glad you like it! Let's go have some fun!"
    background ballroom with fade
    "*you and veronica spend the night dancing and enjoying the ball*"
    "*you see someone staring at you from the corner of your eye*"
    y "Veronica don't freak out but that person over there has been staring at me the whole night"
    hide veronica_casual_ball
    show veronica_slight_ball 
    v "Oh no, let me handle this"
    hide veronica_slight_ball
    show veronica_angry_ball
    v "Hey! Can we help you with something?"
    show veronica_angry_ball left
    show ben_scared right
    u "I-I'm sorry, I didn't mean to stare. It's just..."
    y "OH MY! Ben? Is that you?"
    hide ben_scared
    show veronica_slight_ball
    show ben_relieved 
    b "Thank goodness you recognized me! I hope you didn't think I was a creep"
    y "No, not at all! It's just been a while since I've seen you"
    y "Ive.. missed you"
    b "Me too.."
    v "Do you know each other?"
    hide ben_relieved
    show ben_sad
    y "Yeah.. we used to be close"
    b "It was special"
    v "Hey can I talk to you for a moment in private?
    hide ben_sad
    hide veronica_slight_ball
    show veronica_casual_ball
    v "How do you know each other?"
    y "Well.. it's kinda hard to talk about"
    v "You can tell me, I won't judge"
    y "It's just.. we were in a relationship but it ended because we both weren't ready for something more commited"
    y "I still love him...
    v "well, if you love him maybe you should give it another chance"
    y "I don't know.."
    v "Well, the night is almost over, you should go talk to him"
    menu:
        "go talk to him":
            hide veronica_casual_ball
            show ben_happy
            b "You came to talk to me?"
            y "Yeah.. I think we need to talk about some things"
            b "I'd like that"
            hide ben_happy
            "*you and ben spend the rest of the night talking and catching up*"
            show ben_happy
            b "I'm really glad you came to talk to me"
            y "Me too"
            y "Come back to my place, we have a lot to talk about. We can figure things out together"
            b "I'd like that"
            hide ben_happy
            "*you and ben leave the ball together, hopeful for what the future holds*"
            jump house_end

        "stay with veronica":
            v "Well I think you should talk to him!"
            v "I'm going to invite him over to the house, you two need to sort things out!"
            y "uhhh.. okay"
            hide veronica_casual_ball
            "*veronica leaves to go invite ben over*"
            "*after a while the three of you go to the house together*"
            jump house_end
            
label house_end:
    backround inside_house with fade
    show veronica_slight_ball 
    v "Before ben comes here I need to tell you something"
    y "What is it?"
    hide veronica_slight_ball
    show veronica_vampire
    "*Veronica bites your neck, you feel a sharp pain followed by a wave of dizziness*"
    y "What.. what are you doing?!"
    v "I'm sorry, but I couldn't let you leave"
    v "I care about you too much to let you go"
    y "No.. please.. I don't want this.."
    v "It's for the best, you'll see"
    "*you feel yourself losing consciousness as the world around you fades to black*"
    background black with fade
    "*you wake up feeling different, stronger*"
    backround room_night with fade
    show veronica_vampire
    v "Welcome to your new life"
    v "I'm sorry you didn't ask for this but before you can fully gain your strength you need..."
    v "...to drink some blood of a beloved one"
    v "It's the only way to live after you've been turned"
    v "You need to sacrifice Ben"
    v "Afterwards then you can turn him too.."
    y "I-I can't believe this is happening"
    y "Why would you do this to me?"
    v "Because, I wanted you as a friend forever.."
    "*the door creaks open, Ben steps into the room*"
    show veronica_vampire left
    show ben_confused right
    b "Hey... what's going on in here? Are you okay?"
    y "Ben... run!"
    v "He can’t. You’re already feeling the hunger, aren’t you?"
    "*your throat burns, your vision sharpens, you feel Ben’s heartbeat*"
    menu:
        "Give in to the hunger":
            hide ben_confused
            show ben_scared
            "*you lunge at Ben, sinking your new fangs into his neck*"
            "*warm blood floods your mouth, the hunger quiets*"
            "*Ben’s eyes meet yours, shocked and betrayed, before going still*"
            hide ben_scared
            show veronica_vampire
            v "Good… now you’ll live. Sacrifice is the price of eternity."
            y "What have I done…?"
            v "You’ve survived. That’s all that matters now."
            "*you collapse, the room spinning, as Veronica embraces you in cold arms*"
            scene black with fade
            "*ENDING 2: The price of immortality is the sacrifice of love.*"
            return

        "Refuse to kill Ben":
            y "No… I won’t! I’d rather die than hurt him!"
            v "Then you’ll die, and so will he. I warned you."
            "*your body wracks with pain as the hunger eats you alive*"
            "*Veronica’s face hardens — she grabs Ben and drains him herself*"
            show veronica_vampire feeding
            "*you scream as the last of your strength fades, darkness swallowing you*"
            scene black with fade
            "*ENDING 2 (alternate): Refusal to sacrifice leads to the death of yours, and Ben’s.*"
            return


    return
