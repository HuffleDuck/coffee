#COWORKER SPIRTES N STUFF FILES

# image CoWorker_base = im.Scale("Sprites/CoWorker/coworker_base.png", 720, 720)
# image CoWorker_head_angry = im.Scale("Sprites/CoWorker/coworker_head_angry.png", 720, 720)
# image CoWorker_head_neutral = im.Scale("Sprites/CoWorker/coworker_head_neutral.png", 720, 720)
# image CoWorker_head_happy = im.Scale("Sprites/CoWorker/coworker_head_happy.png", 720, 720)
# image CoWorker_head_sad = im.Scale("Sprites/CoWorker/coworker_head_sad.png", 720, 720)
#
# #side image
# image side CoWorker side_angry = im.Scale("Sprites/CoWorker/HEAD_ANGRY.png" , 720, 720)
# image side CoWorker side_neutral = im.Scale("Sprites/CoWorker/HEAD_NEUTRAL.png", 720, 720)
# image side CoWorker side_happy = im.Scale("Sprites/CoWorker/HEAD_HAPPY.png", 720, 720)
# image side CoWorker side_sad = im.Scale("Sprites/CoWorker/HEAD_SAD.png", 720, 720)
# #
# image side CoWorker side_sad = im.Scale("Sprites/CoWorker/LARM_DOWN.png", 720, 720)
# image side CoWorker side_sad = im.Scale("Sprites/CoWorker/LARM_HIPS.png", 720, 720)
# image side CoWorker side_sad = im.Scale("Sprites/CoWorker/RARM_DOWN.png", 720, 720)
# image side CoWorker side_sad = im.Scale("Sprites/CoWorker/RARM_HIPS.png", 720, 720)
# image side CoWorker side_sad = im.Scale("Sprites/CoWorker/RARM_UP.png", 720, 720)
define CoW = Character("Hugh Janus", image= "coworker")

layeredimage coworker:
    group base:
        attribute work default

    group head auto:
        attribute neutral default

    group left_arm auto:
        attribute down default

    group right_arm auto:
        attribute down default

layeredimage side coworker_side:
    group head auto:
        attribute neutral default
