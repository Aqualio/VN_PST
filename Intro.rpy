# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Mc = Character("You")
define Li = DynamicCharacter("li_name")

# The game starts here.
label start:

$li_name = "???"

transform slightright:
    xalign 0.75
    yalign 1.0

Li "Hey... Hello anyone here..."

Mc "Hum?!"

scene classroom
with wipeup
show eileen happy at slightright
with wipeup

Li "Finally! You're awake! Sleeping in the first lesson of college I see... Haha"

Mc "Huh... Yeah my bad..."

$li_name = "LOVEINTNAME"
Li "I'm LOVEINTNAME, nice to meet you! What's your name?" 

label nameDefine:

python:
    name = renpy.input("What's your name?")
    name = name.strip() or "John"

menu:

    Li "Are you sure?"
    
    "Yes":
        jump introEnd
    
    "No, try another one":
        jump nameDefine

label introEnd :
Li "So... It is [name], I see... Well see you later then! I hope we can become friend!"

Mc "Oh I hope it will be the case too..." 
