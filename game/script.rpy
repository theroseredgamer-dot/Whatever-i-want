# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
label Characters:
    define Renji = Character("Renji", color="#b460bd")
    define You = Character("You", color="#525152")
    define teacher = Character("teacher", color="#01474a")

label sprites:
    image renjibunny = "images/renjibunny.png"

    label backgrounds:
        image bgroom = "images/bgroom.png"

    label audio:
        define audio.clock = "audio/clock.wav"

# The game starts here.

label start:
    "You hear a voice..."
    "It's calling your name..."
    "...What is your name?"
    "teacher" "Wake up!!"
    scene bgroom
    with fade 
    play sound clock
    show renjibunny
    "Renji" "H-hi! I'm your new deskmate!"
