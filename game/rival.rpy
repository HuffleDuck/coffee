
define Rival = Character("Shay", image= "rival",  who_color="#c8ffc8")
define Rival_side = Character("Shay", image= "rival_side",  who_color="#f85f22")

layeredimage rival:
    group base:
        attribute work default

image side rival_side =  LayeredImageProxy("rival", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))
