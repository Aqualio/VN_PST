##CHARACTER IMAGES
image John = "sylvie blue giggle.png"
image Suzanne = "sylvie green surprised.png"
##--------------------------------------------------------------------

##UI IMAGES
image CampusMap = im.Scale("Map.png", 400, 234) ##Image is bigger than what we need so we display it in another size.
image BoutonDeplacement = "BoutonDeplacement.png" #Doublon plus bas
image carnet = "images/carnet.png"
image carnet_hover = "carnet_hover.png"
image take_notes_button = "images/Take_Notes_button_idle.png"
image displacement = "BoutonDeplacement.png" #N'en garder qu'un

##---------------------------------------------------------------------
##BACKGROUND IMAGE
image Library = "bg club.jpg"
image Dormitory = "bg lecturehall.jpg" ##change image NASSIM
image Cafeteria = "bg club.jpg" ## changer d'image NASSIM
image LectureHall = "bg lecturehall.jpg"
##----------------------------------------------------------------------

init python:

    config.tag_layer['bg'] = 'background' # all images with the tag 'bg' are put on layer 'bg'

##Marine's Screens

screen Map():
    zorder 10 ## We add an order to the screen to indicate which one should be display in front or else
    add 'BoutonDeplacement' at displacement_btn_position

    imagemap:
        idle 'CampusMap' xpos 20 ypos 250

        imagebutton:
            focus_mask True
            idle "Dormitory_idle.png"
            hover "DormitoryHover.png"
            action Return("Dormitory")

        imagebutton:
            focus_mask True
            idle "LectureHall_idle.png"
            hover "LectureHallHover.png"
            action Return("LectureHall")

        imagebutton:
            focus_mask True
            idle "Cafeteria_idle.png"
            hover "CafeteriaHover.png"
            action Return("Cafeteria")

        imagebutton:
            focus_mask True
            idle "Map_idle_cross.png"
            hover "Map_red_cross.png"
            action Return("None")



screen Dormitory():
    ##layer "background"
    zorder 0
    window:
        style "gm_root"
        add 'Dormitory' xalign 0.0 yalign 0.0


screen Cafeteria():
    zorder 0
    window:
        style "gm_root"
        add 'Cafeteria' xalign 0.0 yalign 0.0

screen LectureHall():
    zorder 0
    window:
        style "gm_root"
        add 'LectureHall' xalign 0.0 yalign 0.0


##Nico's screens

transform carnet_position:
            align(1.01, 0.72)
transform take_note_button_position:
            align(0.94,0.73)
transform displacement_btn_position:
            align(0.05,0.73)

screen Menu(takeNotesClickable,displacementClickable):
        zorder 10
        $ print(name_of_label)

        #show carnet renpy.display.behavior.ImageButton("c")

        imagebutton:
                idle "carnet"
                hover "carnet_hover"
                at carnet_position
                focus_mask True
                action [Show("carnet_screen")]

        if takeNotesClickable == 1 :
            imagebutton:
                    idle "take_notes_button"
                    hover "take_notes_button_hover"
                    at take_note_button_position
                    focus_mask True
                    action [Function(notelist.add_notes,name_of_label), Function(renpy.invoke_in_new_context,renpy.say,centered,"new entry added to notebook",True)]
        if takeNotesClickable == 0 :
            add 'take_notes_button' at take_note_button_position

        if(displacementClickable ==1):
            imagebutton:
                    idle "displacement"
                    hover "BoutonDeplacement_hover.png"
                    at displacement_btn_position
                    focus_mask True
                    action [Function(renpy.call,"Map")]
        else:
            add 'displacement' at displacement_btn_position

init:
    $ imagelist = ImageList(0)
    $ imagelist.add("an_image")
    $ imagelist.add("an_image2")
    $ print(imagelist.indeximg)
    $ killscreen = 0
    $ notelist = NoteList()
    $ cluelist = ArrayClue()

    screen item_descriptions(item_ref=""):
        zorder 10
        tag item_descriptions
        modal False
        #here can make a list of object composed of each clues with each their description and according to param of the screen use the fct to look through the list and find the correct item available to player and display its information
        text "Place holder here ref=[item_ref]" size 16 xalign 0.8 yalign 0.2

    screen notebook_clues_screen:
        $x = 0.15
        $y = 0.2
        #look when after exceeding a certain value of x for which all new image displayed goes out of screen, we increment y
        zorder 10
        tag notebook_screen
        modal False
        #use frame when ui background will be made
        fixed:
            xalign 0.7
            yalign 0.040
            xfill 940
            yfill 660

            text "CLUES" color "#000" xalign 0.18 yalign 0.08

            #for clue in cluelist:
            #    imagebutton:
            #        idle clue.get_name + ".png"
            #        focus_mask True
            #        xalign x
            #        yalign y
            #        action [Show(clue.get_desc, item_ref=clue.get_name)]
            #    $x += 0.10
                #if(x > val):
                #    $x = 0.15
                #    $y += 0.1

            imagebutton:
                idle "TBD_icon.png"
                focus_mask True
                xalign 0.20
                yalign 0.15
                action [Show("item_descriptions", item_ref="KC_1")]

            imagebutton:
                idle "TBD_icon.png"
                focus_mask True
                xalign 0.30
                yalign 0.15
                action [Show("item_descriptions", item_ref="KC_angueury")]

    screen notebook_character_screen:
        zorder 10
        tag notebook_screen
        modal False

        fixed:
            xalign 0.7
            yalign 0.040
            xfill 940
            yfill 660

            text "CHARACTERS" color "#000" xalign 0.18 yalign 0.08

            imagebutton:
                idle "characters/Epstein_icon.png"
                focus_mask True
                xalign 0.18
                yalign 0.15

            imagebutton:
                idle "josh_icon.png"
                focus_mask True
                xalign 0.30
                yalign 0.15

            imagebutton:
                idle "juan_icon.png"
                focus_mask True
                xalign 0.40
                yalign 0.15
    screen notebook_notes_screen:
        zorder 10
        $d = {'menu_verif' : 'True'}
        tag notebook_screen
        modal False
        $i = 0
        $x = 0.30
        $y= 0.15
        $print(i)

        fixed:
            xalign 0.7
            yalign 0.040
            xfill 940
            yfill 660

            text "NOTES" color "#000" xalign 0.18 yalign 0.08

            for note in notelist.notes:
                textbutton note action [Function(renpy.call_replay,note)] xalign x yalign y
                $y += 0.05
                $i += 1

    screen carnet_screen:
        zorder 10
        tag carnet_screen
        modal True
        add "#0009"
        $ print(imagelist.indeximg)
        $ print(notelist.notes)
        $i = 0
        $print(i)
        fixed:
            xalign 0.7
            yalign 0.7
            xfill True
            yfill True
            #add imagelist.get_img() xalign 0.5 yalign 0.5
            #text "CARNET" color "#000" xalign 0.5 yalign 0.05
            add "notebook_menu_bg_final_final" xalign 0.42 yalign 0.45

            imagebutton:
                idle "exit_button_idle"
                hover "exit_button_hover"
                clicked "exit_button_clicked"
                xalign 0.999
                yalign 0.01
                focus_mask True
                action [Hide("carnet_screen"),Hide("notebook_screen"),Hide("item_descriptions")]

            imagebutton:
                idle "notes_taken_button_idle"
                hover "notes_taken_button_hover"
                xalign 0.070
                yalign 0.450
                focus_mask None
                action [Hide("item_descriptions"), Show("notebook_notes_screen")]

            imagebutton:
                idle "characters_menu_icon_idle"
                hover "characters_menu_icon_hover_resize"
                xalign 0.070
                yalign 0.067
                focus_mask True
                action [Hide("item_descriptions"), Show("notebook_character_screen")]

            imagebutton:
                idle "notebook_menu_icon_idle_resize"
                hover "notebook_menu_icon_hover_resize"
                xalign 0.070
                yalign 0.250
                focus_mask True
                action [Show("notebook_clues_screen"),Hide("notebook_character_screen")]

            #add "notebook_button_border" xalign 0.026 yalign 0.055
            #add "notebook_button_border" xalign 0.026 yalign 0.235
            #add "notebook_button_border" xalign 0.026 yalign 0.415
            #imagebutton:
            #    idle "arrow_left"
            #    hover "arrow_left_hover"
            #    xalign 0.05 yalign 0.5
            #    focus_mask True
            #    action [Function(imagelist.move_left),renpy.restart_interaction]
            #imagebutton:
            #    idle "arrow_right"
            #    hover "arrow_right_hover"
            #    xalign 0.95 yalign 0.5
            #    focus_mask True
            #    action [Function(imagelist.move_right), renpy.restart_interaction]

init -1 python:
    def label_callback(name, abnormal):
        store.current_label = name
    config.label_callback = label_callback

    def afct():
        renpy.hide_screen("oui")

    class ImageList(object):
        def __init__(self,arg):
            self.indeximg = arg
            self.images = []

        def add(self, name):
            self.images.append(name)

        def move_left(self):
            if self.indeximg == 0:
                self.indeximg = (len(self.images) - 1)
            else:
                self.indeximg -= 1

        def move_right(self):
            if self.indeximg == (len(self.images) - 1):
                self.indeximg = 0
            else:
                self.indeximg += 1

        def get_img(self):
            return self.images[self.indeximg]

    class NoteList(object):
        def __init__(self,arg = 0):
            self.indexnote = arg
            self.notes = []
        def add_notes(self,to_add):
            self.notes.append(to_add)
            return
        def remove_notes(self, num_memo):
            self.notes.pop(num_memo)
        def get_notes(self,i):
            return self.notes[i]

    class Clue(object):
        def __init__(self, name, state, desc):
            self.name = name
            self.state = state
            self.desc = desc
        def get_name(self):
            return self.name
        def get_state(self):
            return self.state
        def get_desc(self):
            return self.desc

    class ArrayClue(object):
        def __init__(self):
            self.inventory = []
        def add_clue(self, thisClue):
            self.inventory.append(Clue(thisClue.name, thisClue.state, thisClue.desc))


##Aure's screens

init python:

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("Quickstart"))

    Tutorial("tutorial_playing", _("Player Experience"))
    Tutorial("tutorial_create", _("Creating a New Game"))

    Section(_("In Depth"))

    Tutorial("text", _("Text Tags, Escapes, and Interpolation"))
    Tutorial("demo_character", _("Character Objects"))
    Tutorial("simple_displayables", _("Simple Displayables"), move=None)
    Tutorial("demo_transitions", _("Transition Gallery"))


screen buttons():
    zorder 5
    imagebutton:
                idle "boy a_casual_normal_idle.png"
                hover "boy a_casual_normal_hover.png"
                action Return("homme")
                xpos 30
                ypos 80
                xsize 280
                ysize 650

    imagebutton:
                idle "sprite female dark hair Neu02_idle.png"
                hover "sprite female dark hair Neu02_hover.png"
                action Return("femme")
                xpos 900
                ypos 80
                xsize 280
                ysize 650

    #$ result = ui.interact()


screen characters_interactions_screen(names,mode,labelname):
    $x = 10
    $y= 160
    zorder 5
    $characters = names.split(',')
    $print(characters)
    for _names in characters:
        if(mode == "normal_idle"):
            $print(_names)
            if(_names == "sadiq" or _names == "charles"):
                $y= 150
                $x -= 50
                imagebutton:
                    idle _names + " normal_idle"
                    action Return(labelname +"_"+_names)
                    focus_mask True
                    xpos x
                    ypos y
                    xsize 260
                    ysize 570
                $y= 160
            else:
                imagebutton:
                    idle _names + " normal_idle"
                    action Return(labelname +"_"+_names)
                    focus_mask True
                    xpos x
                    ypos y
                    xsize 280
                    ysize 650
            $x += 230
#TODO add other mode to manage other character face expression
