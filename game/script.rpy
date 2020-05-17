##CHARACTERS NAME 
define e = Character("Eileen")
define m = Character("Marine")
define h = Character("Jeune Homme")
define f = Character("Jeune Femme")
##--------------------------------------

##VARIABLE 
define sequence_number = 0
define location = "Dormitory"
##---------------------------------------
##CHARACTER AND BACKGROUND LAYOUT 
init python:

    config.tag_layer['boy'] = 'screens' # all images with the tag 'bg' are put on layer 'bg'
    config.tag_layer['female'] = 'screens' # all images with the tag 'bg' are put on layer 'bg'

##----------------------------------------


label start:
        jump Dormitory


default tutorials_adjustment = ui.adjustment()
# The game starts here.

label DiscussionType:
        
    call screen buttons()
    
    $ test = _return
    
    # "test value is [test]"
    
    if test == "homme":
        jump homme_clicked
    if test == "femme":
        jump femme_clicked
        
    hide screen buttons


        
label homme_clicked: 
    $config.label_callback
    $name_of_label = current_label
    $menu_verif = True

    
    if _in_replay:
        $menu_verif = False

    if menu_verif == True:
        show screen Menu(1)

    show boy a_casual_sad #happy #n'existe pas dans le folder image donc normal qu'il s'affiche pas A CHANGER
    h "Yosh! Ca fait plaisir de te voir ici!"
    hide boy a_casual_sad
        
    $renpy.end_replay()
    
    if menu_verif == True:
        jump Library
    
    
label femme_clicked:
    ##PREREQUIS
    $config.label_callback
    $name_of_label = current_label
    $menu_verif = True


    if _in_replay:
        $menu_verif = False

    if menu_verif == True:
        show screen Menu(1)
    
    show female a_casual_smile
    f "Hey, ça va? Tu fais quoi de beau aujourd'hui?"
    hide female a_casual_smile 
    
    $renpy.end_replay() ## TO END the replay
    if menu_verif == True:
        jump Library

    

