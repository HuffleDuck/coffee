# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg_shop = "backgrounds/coffee_shop.png"

define Boss = Character("Manager", image="Boss")
image Boss = im.Scale("sprites/Boss/manager.png",323,628)
image BossSmile = im.Scale("Sprites/Boss/sidesmile.png",323,628)

define Rival = Character("RIVAL", who_color="#c8ffc8")


image bg_cobedroom = im.Scale("backgrounds/bed-bedroom-room-furniture(oil2).jpg", 1920, 1080)
image bg_fallsidewalk = im.Scale("backgrounds/fallsidewalk.png", 1920, 1080)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
$snooze = 0
scene bg_shop
show coworker
pause
CoW angry "angry"
pause
CoW sad "sad"
pause
CoW neutral "null"
pause
CoW happy "hap"

label alarm:
    scene black
    pause 2.4

    play sound "music/sfx/Loud_Alarm_Clock_Buzzer.wav"

    #    $subtitle="[[alarm clock is going off]"
    #scene bg_shop

    menu:
      "hit snooze":
        stop sound
        CoW "..."
        "..."
        $snooze += 1
        if snooze >= 3:
            play sound "music/sfx/Loud_Alarm_Clock_Buzzer.wav"
            "8:34 AM"
            with hpunch
            CoW angry "FUCK"
        else:
            jump alarm
      "get up":
        CoW "hrgfhgfnn"
        "Hugh anus sits up and looks at the time or some shit like that"
        CoW side_happy "7:15, naisu"
    stop sound
    scene bg_cobedroom
    if snooze >= 3:
        with vpunch
    else:
        with fade

    pause
    #show CoWorker
    #pause

    if snooze == 0:
        "nice teeth brushing"
        "empty fridge"
        "what a loser"
    elif snooze >= 1:
        "rush thru morning"
    else:
        "fUCK"
    play sound "music/sfx/Doorbell-SoundBible.com-516741062.mp3"
    "RIVAL??? SHOWS UP"
    show coworker # at right

    if snooze == 0:
        Rival "YO, YOU're up ALREADY??"
    else:
        Rival "you look awful lol"

    scene bg_fallsidewalk
    with fade
    "they walk outside"
    "some cute friendship talk shit? idk"
    "some mean friendship talk shit? idk"
    "some funny friendship talk shit? idk"
    show Boss # at right
    show BossSmile # at right
    CoW side happy "hi"
    Rival "lol ur face"
    CoW side angry "wtf why r u always so mean 2 me"




    pause

    scene bg_shop
    "she made it to the coffee shop wow"
    pause
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show CoWorker

    # These display lines of dialogue.

    #"<Insert Generic COFFEE HOUSE NAME Here>"

    #CoWorker "HELLO WELCOME TO COFFEE SHOP?"

    # This ends the game.

    return
