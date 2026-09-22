# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
label Characters:
    define Renji = Character("Renji", color="#b460bd")
    define You = Character("[player_name]", color="#525152")
    default player_name = "Player"
    define teacher = Character("teacher", color="#01474a")

label sprites:
    image renB = "images/Renji/renjibunny.png"
    image rensad = "images/Renji/renjisad.png"
    image rensmile = "images/Renji/renjismile.png"

    label backgrounds:
        image class = "images/backgrounds/bgclass.png"

    label sound:
        define audio.clock = "audio/clock.wav"

    label music:
        define lostM = "audio/lost memory.mp3"

    label audio:
        define lull = "audio/The princess's lullaby.mp3"

    label music:
        define walking = "audio/walking.mp3"

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
    scene class
    with fade 
    play sound clock
    show renB with moveinright
    play music lostM

    
    Renji """
    H-hi! I'm your new deskmate!

    I'm the transfer student.  

    We used to be neighbors, but I moved away a long time ago.

    Do you remember me, [player_name]?
    """
    
    """
    You smile. Of course you remember Renji! 
    
    You two were best friends when you were younger. 
    
    You two used to play together all the time, and you even had sleepovers at each other's houses.

    You still remember how you two met. 

    He really hasn't changed at all. He's still just as cute as back then.
    """

    You """
    Renji! It's been so long!

    I missed you.
    """
    
    hide renB with dissolve
    stop music fadeout 1.0

    """
    Before you could say more, the teacher calls everyone's attention back to class.

    ...
    """

    play audio lull

    """
    After class ends, Renji approaches you again.
    """

    show renB with moveinright

    Renji """
    [player_name]! 

    Can we- or maybe you want to- walk home together?
    """

    menu :

        "I'd love to!":
            # walk home together
            jump walk_home
        "I want to walk alone...":
            # game end: you don't walk home with Renji
            jump game_end

label walk_home: 
        hide renB with dissolve
        show rensmile
        Renji 
        """
        Really? I'm so happy!
        """:
            jump continue_story

label game_end:
        hide renB with dissolve
        show rensad
        Renji
        """
        Oh... I see. I understand.
        """
        
        """ 
        game end: you don't walk home with Renji
        """
        return

label continue_story:

        hide renB with dissolve
        hide class with fade
        play music walking

        """
        You and Renji walk to his apartment together.

        When you arrive, you see there are still boxes all over the floor.
        """



    # walk home together
    # set up appartment
    # get kidnapped lol