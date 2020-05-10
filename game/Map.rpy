##########      SEPARATE FILE FOR MAP FUNCTIONALITY     #################

label Map :
    call screen Map #Use call as it returns a value

    m "Current location [location]"
    #m "Selected [_return]"

    if _return != location and _return != "None": ##Check that the value return by the map screen isn't null and the same location as the current one 
        
        $renpy.hide_screen("".join([location])) #We hide the background of the current location 
        with dissolve
        
        $location = _return ## We save our next current location 
        ##m "Moving to [location]"
        $renpy.show_screen("".join([location])) #We display the background of the new current location 
        with fade

    elif _return == "None" : ## Check if the value return by map screen is null 
        ##m "No location chosen"
        $renpy.jump("".join([location])) ## We go back to the location label 

    else :      ## If the location = return_ 
        m "I'm already here..."

    hide screen Menu ## We had the screen menu
    $renpy.jump("".join([_return]))## We jump to the return_ label 

    $renpy.pause(hard=True) # Just to be sure we won't go further than the previous command


############### GAME LOCATIONS ###################

label Dormitory:
    ###PREREQUIS
    $name_of_label = current_label
    show screen Menu(0) ## Put 0 as we don't want the "take notes" button to be clickable 
    ##End Prerequis
        
    m "Dormitory Babyyyy"

    $renpy.pause(hard=True)
    

label Library:
    ###PREREQUIS 
    $name_of_label = current_label
    show screen Menu(0) ## Put 0 as we don't want the "take notes" button to be clickable 
    ##End Prerequis
    
    
    jump DiscussionType

    $renpy.pause(hard=True)