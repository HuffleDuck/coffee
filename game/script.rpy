# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Coworker = Character("Eileen")
image CoWorker = im.Scale("coworker_default.png", 323, 628)
image bg_shop = im.Scale("bg room.jpeg", 1280, 720)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_shop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show CoWorker

    # These display lines of dialogue.

    "<Insert Generic COFFEE HOUSE NAME Here>"

    Coworker "HELLO WELCOME TO COFFEE SHOP?"

    # This ends the game.

    return
