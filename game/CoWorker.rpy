#COWORKER SPIRTES N STUFF FILES
init python:
    class Picker(object):
        def __init__(self, options):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

            return rv

#Blake Riley

define CW = Character("Blake", image= "coworker",  who_color="#f85f22")
define CW_side = Character("Blake", image= "coworker_side",  who_color="#f85f22")

layeredimage coworker:
    group combos:
        attribute upset null

    attribute_function Picker([
    "upset coworker_left_arm_hip coworker_right_arm_up coworker_head_sad"
    ])

    group base:
        attribute work default
    group left_arm auto:
        attribute down default
    group right_arm auto:
        attribute down default
    group head auto:
        attribute neutral default

image side coworker_side =  LayeredImageProxy("coworker", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=40, yoffset=-200))
