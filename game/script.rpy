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

    m "sequence_number [sequence_number]"
    
    if sequence_number == 0:
        show boy a_casual_sad zorder 20 #happy #n'existe pas dans le folder image donc normal qu'il s'affiche pas A CHANGER
        h "Yosh! Ca fait plaisir de te voir ici!"
        $ sequence_number =1
        
        hide boy a_casual_sad
        $renpy.end_replay()
        if menu_verif == True:
            jump Library
    else:
        show boy a_casual_sad zorder 1
        h "Tu viens me voir qu'en deuxième... Nan, c'est pas grave, ça me dérange pas.. haha"
        
        hide boy a_casual_sad
        $renpy.end_replay()
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
    
    ##FIN prérequis 
    m "sequence_number [sequence_number]"
    
    if sequence_number == 0:
        show female a_casual_smile zorder 1
        f "Hey, ça va? Tu fais quoi de beau aujourd'hui?"
        $ sequence_number = 1
        
        hide female a_casual_smile 
        $renpy.end_replay() ## TO END the replay
        if menu_verif == True:
            jump Library
    else:
        show female a_casual_annoyed zorder 1
        f "Tu viens me voir qu'en deuxième..? Je pensait que tu m'appréciais plus que ça, mais ok..."
        
        hide female a_casual_annoyed
        $renpy.end_replay() ## TO END the replay
        jump Library
    

