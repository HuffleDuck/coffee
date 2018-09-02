# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg_shop = "backgrounds/coffee_shop.png"

image bg_cobedroom = im.Scale("backgrounds/bed-bedroom-room-furniture(oil2).jpg", 1920, 1080)
image bg_fallsidewalk = im.Scale("backgrounds/fallsidewalk.png", 1920, 1080)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
$snooze = 0

#scene bg_shop
# show coworker
# pause
# CW angry hips "angry"
# #CoW_side sad down "sad"
# #CoW_side neutral "null"
# CW happy "hap"
# CW upset "upset"
#show coworker_side
#CW_side "7:15, naisu"
pause

label alarm:
    scene black
    pause 2.4

    play sound "music/sfx/Loud_Alarm_Clock_Buzzer.wav"

    #    $subtitle="[[alarm clock is going off]"
    #scene bg_shop

    menu:
      "hit snooze":
        stop sound
        CW "..."
        "..."
        $snooze += 1
        if snooze >= 3:
            play sound "music/sfx/Loud_Alarm_Clock_Buzzer.wav"
            "Blake rolls over and blinks at her clock"
            "8:34 AM"
            with hpunch
            CW_side angry "FUCK"
        else:
            jump alarm
      "get up":
        CW_side "hrgfhgfnn!"
        "Blake sits up and looks at her clock"
        CW_side happy "7:15, naisu"
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
    elif snooze > 0 and snooze < 3:
        "rush thru morning"
    else:
        "fUCK!!"
        show rival
        play sound "music/sfx/Doorbell-SoundBible.com-516741062.mp3"
        Rival "Hey, you awake in there?"
    if snooze == 0:
        show rival
        Rival "Yo, you’re up bright and early."
        Rival ""
        CW ""
    elif snooze > 0 and snooze < 3:
        show rival
        Rival "Ypu take a big dump this morning or somthing?"
        CW "Hey, I wasn't that late!"
        Rival "You ready to head out?"
        CW "Yeah Shay, whenever you are."
    else:
        show rival
        Rival "Ayyy!! What’s taking so long?"
        Rival "You fall in or something??!!"
        CW_side angry "NO SHUP!!!"
        with hpunch
        "Blake is frantically tying on her apron."
        Rival "What the fuck is \"shup\" supposed to mean??"
        CW_side "SHUT UP I’M COMING OUT!!"
        with hpunch
        Rival "You don’t need to tell me again, we had this talk years ago…"
        CW_side "SHAY YOU ASSHOLE, YOU KNOW WHAT I MEAN!"

    scene bg_fallsidewalk
    with fade
    "they walk outside"

    CW_side happy "hi"
    Rival "C'mon sleepy, let's get going."
    CW_side angry "wtf why r u always so mean 2 me"

    pause

    Rival "See you after work!"
    CW "Bye!"
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
