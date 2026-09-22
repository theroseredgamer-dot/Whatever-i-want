# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
label Characters:
    define Renji = Character("Renji", color="#b460bd")
    define You = Character("[player_name]", color="#525152")
    default player_name = "Player"
    define teacher = Character("teacher", color="#01474a")

label sprites:
    image renjibunny = "images/renjibunny.png"

    label backgrounds:
        image bgroom = "images/bgroom.png"

    label audio:
        define audio.clock = "audio/clock.wav"

# The game starts here.

label start:
    """
    {cps=10}You hear a voice...{/cps}

    {cps=10}It's calling your name...{/cps}
    """
    $ player_name = renpy.input("...What is your name?", length=13)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Player"
    
    teacher """
    Wake up [player_name]!!
    """
    scene bgroom
    with fade 
    play sound clock
    show renjibunny
    Renji """
    H-hi! I'm your new deskmate!

    I'm the transfer student.  

    We used to be neighbors, but I moved away a long time ago.
    """
    # walk home together
    # set up appartment
    # get kidnapped lol