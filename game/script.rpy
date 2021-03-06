﻿##CHARACTERS NAME
define e = Character("Eileen")
define m = Character("Marine")
define h = Character("Jeune Homme")
define f = Character("Jeune Femme")

define mc = Character("You")
define li = DynamicCharacter("li_name")
define epstein = Character("Epstein")
define josh = Character("Josh")
define john = Character("John")
define juan = Character("Juan")
define brice = Character("Brice")
define sadiq = Character("Sadiq")
define charles = Character("Charles")
define mc_meuf = Character("Alex")

##EFFECTS

define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

##--------------------------------------

##VARIABLE
define sequence_number = 0
define location = ""
define storyDevelopment = "intro"
##---------------------------------------
##CHARACTER AND BACKGROUND LAYOUT
init python:

    ##CHARACTER OBJECT DEFINITION
    C_Epstein = CharacterObj('Epstein','characters/Epstein','TRIVIA','TRIVIA','TRIVIA',0)
    C_Josh = CharacterObj('Josh','josh','TRIVIA','TRIVIA','TRIVIA',1)
    C_John = CharacterObj('John','john','TRIVIA','TRIVIA','TRIVIA',2)
    C_Juan = CharacterObj('Juan','juan','TRIVIA','TRIVIA','TRIVIA',3)
    C_Brice = CharacterObj('Brice','brice','TRIVIA','TRIVIA','TRIVIA',4)
    C_Sadiq = CharacterObj('Sadiq','sadiq','TRIVIA','TRIVIA','TRIVIA',5)
    C_Charles = CharacterObj('Charles','charles','TRIVIA','TRIVIA','TRIVIA',6)

    config.tag_layer['charac josh normal_idle'] = 'screens'

    config.tag_layer['charac'] = 'screens' # all images with the tag 'bg' are put on layer 'bg'

    vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=1.275)#0.275 de base
    opunch = Move((0, 5), (0, -5), .10, bounce=True, repeat=True, delay=.5)
    hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

##----------------------------------------


label start:
        jump preintro
        #jump Dormitory


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


label preintro:

    $li_name = "???"

    transform slightright:
        xalign 0.75
        yalign 1.0

    li "Hey... Hello anyone here..."

    mc "Hum?!"

    scene classroom
    with fade
    show charac alex normal_idle at slightright
    with fade

    li "Finally! You're awake! Sleeping in the first lesson of college I see... Haha"

    mc "Huh... Yeah my bad..."

    $li_name = "Alex"
    li "I'm Alex, nice to meet you! What's your name?"

label nameDefine:

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "John"

    menu:
        li "Really?"

        "Yes":
            jump introEnd

        "No, try another one":
            jump nameDefine

label introEnd :
    li "So... It is [name], I see... Well see you later then! I hope we can become great friends!"

    mc "Oh yeah, I hope so too..."
    
    hide charac alex normal_idle 
    with fade

    show pblack_screen
    with dissolve

    "1 Year later..."

label intro:
    $config.label_callback
    $name_of_label = current_label
    $talk_count = 0

    #EXAMPLE TO ADD AN OBJECT
    #$clue1 = Clue("test",0,"test")
    #$cluelist.add_clue(clue1)

    scene school front with fade
    play music "audio/BGM/BGM1_(Tiny_Little_Adiantum_Instrumental).mp3" fadein 1.0 fadeout 1.0
    show screen Menu(0,0)
    mc "There it is, Lord Gril’s University, it sure feels good to be back."
    mc "This second year here began really well and first semester sure was a blast, I sure hope the second can be just as good! School life, here I come!"
    mc "Now, I gotta find which room i’m in… lemme see… ah! The board’s over there."

    #need info board bg
    scene placeholder with fade

    mc "Engineering majors… hmmmm"
    mc "Ah! Room A5, let’s go then."

    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}The tutorial on how to use the map starts now{/outlinecolor}{/color}{/size}"
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}Please click on the shoe icon to display the map and click on a location !{/outlinecolor}{/color}{/size}"
    hide screen Menu
    show screen Menu(0,1)
    
    while 1:
        $renpy.pause(hard=True)


label intro_LectureHall:
    $location = "LectureHall"
    hide placeholder

    scene amphitheater
    mc "Everyone’s already here, the teacher isn’t though, perfect time to chat and catch up with the bois."
    hide screen Menu
    show charac josh normal_idle
    josh ""
    hide charac josh normal_idle
    show charac john normal_idle
    john ""
    hide charac john normal_idle
    show charac juan normal_idle
    juan ""
    hide charac juan normal_idle
    show charac brice normal_idle
    brice ""
    hide charac brice normal_idle
    show charac sadiq normal_idle
    sadiq ""
    hide charac sadiq normal_idle
    show charac charles normal_idle
    charles ""
    hide charac charles normal_idle

    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}The tutorial for character interaction will now start{/outlinecolor}{/color}{/size}"
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}Please click on the character you want to interact with{/outlinecolor}{/color}{/size}"

    while talk_count < 3:
        call screen characters_interactions_screen('josh,john,juan,brice,sadiq,charles','normal_idle',name_of_label)
        $ val = _return
        $talk_count += 1
        $renpy.call(val)
    show screen Menu(0,0)
    play sound "audio/Effects/Door_opening_old.ogg"

    show charac epstein normal_idle
    epstein "Ok everyone, to your seats, we’re gonna start the course. And don’t even hope we’re gonna talk about the holidays, you’ve got a lot to learn before the end of the year, so let’s get into it right now."
    hide charac epstein normal_idle

    hide screen LectureHall
    with dissolve
    
    jump prologue
    while 1:
        $renpy.pause(hard=True)
#zaeaz

label intro_Cafeteria:
    show screen Menu(0,1)
    $location = "Cafeteria"
    m "mmmh... I need to go to the lecture hall..."
    while 1:
        $renpy.pause(hard=True)

label intro_Dormitory:
    show screen Menu(0,1)
    $location = "Dormitory"
    m "mmmh... I need to go to the lecture hall..."
    while 1:
        $renpy.pause(hard=True)

label intro_josh:
    show charac josh normal_idle
    show screen Menu(0,0)
    josh "It would seem this encounter has granted me new and unforeseen powers…"
    mc "Hi Josh, how are you doing?"
    josh "DON’T COME NEAR ME, CLUELESS MORTAL!"
    mc "What!? I see Josh hasn’t changed over the holidays, he’s as … quirky as usual."
    josh "I have acquired new and dangerous powers while I was away from you mortals. But I can’t control them fully yet, come near me and you might get hurt. YOU’VE BEEN WARNED!"
    mc "Yeah sure enough buddy…"
    menu:
        "Play along":
            mc "Josh, I’ve noticed you were different the moment I entered the room. If I might ask, what are these new powers?"
            josh "Oooooh, so you’ve noticed uh? Maybe you aren’t such a useless mortal after all, I might even make you my disciple. These new powers came at quite the symbolic moment you see."
            mc "Oh, and when is that?"
            josh "New year’s eve, the moment we switched years to be precise. At this moment where time changed for the mortal realm, the spiritual one granted me new time-related powers!"
            mc "Interesting, really interesting, and what do they do?"
            josh "They allow me to look into the future you see."
            mc "And what do you foresee?"
            josh "A great catastrophe, something bad is coming [MC], I can assure you. You aren’t as bad as the other mortals here, so I’ll ask you to please be careful around here."
            hide charac josh normal_idle
            mc "Well, this sure was entertaining, Josh is a cool guy, he’s just really… passionate."

        "I’m tired of his shenanigans":
            mc "Well, guess I better get away then, see you around Josh."
            josh "The cataclysm is coming and they can’t see it. このばああかあああ"
            mc "I know Josh isn’t a bad dude, but I really don’t understand why he acts this way."
            hide charac josh normal_idle

    mc "Now who to talk to?"
    hide screen Menu

    $characterlist.add_character(C_Josh)

    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}New entry added for Josh{/outlinecolor}{/color}{/size}"

    return 0

label intro_john:
    show charac john normal_idle
    show screen Menu(0,0)
    john "Yo [MC], long time no see! How are you doing?"
    mc "Hey John, i’m fine, and you? The holidays were nice and all, but i’m still happy coming back and seeing you all."
    john "Yup, I’m happy too. How were your holidays? Did you have fun?"
    mc "Yeah, that was fine. I had the occasion to see members of my family I haven’t seen for a long time. And you, how was it?"
    john "Oh, that’s nice. Personally, I used this occasion to do some sport, and relax a bit. I could also study a bit, so that’s all good."
    mc "Oh yeah, of course!"
    mc "Oh right, I almost forgot he’s a guy who lives for sports, yet ended up in a computer science university. So yeah, obviously he has difficulties, but he works hard to overcome it."
    mc "But well, in general he’s a nice guy, so that’s fine.."
    mc "Soo, you’re gonna be alright with the second semester?"
    john "Yeah, that should be okay."
    mc "Anyway, if you have any problems, don’t hesitate to ask me.."
    john "Got it, thanks. Same goes for you."
    mc "Okay, thanks. See you later."
    john "See ya."
    hide charac john normal_idle
    hide screen Menu

    $characterlist.add_character(C_John)
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}New entry added for John{/outlinecolor}{/color}{/size}"

    return 0

label intro_juan:
    show charac juan normal_idle
    show screen Menu(0,0)
    mc "Here’s Juan, he looks baked as usual, no harm talking to him though. Hey man, how’re you doing."
    juan "Yooooooo ma man, doin’ greaaaat and you?"
    mc "I’m doing fine myself thank you."
    juan "Maaaan, that’s hella good, i’m feelin’ some real chill vibes from you right now, you been doin’ good haven’t ya?"
    mc "well, yeah, I just told you"
    juan "It’s cooool man, real cool. I mean, what do we have left in this world if not for unfucked vibes you know what I mean man?"
    mc "Uuuuh… yes?"
    juan "That’s real good man, real good, always knew you were the type of dude to get what  i’m putting down here man. Always knew you were real good at just you know, vibin’"
    mc "….. thank you?"
    juan "No need for thanks my man, we be connected you know, no need for talk between us my guy."
    mc "Okay…. well i’ll be going then."
    juan "Alright my guy, keep doin’ whatever you do out there and watch out for yourself ok?"
    mc "yeah sure, see you. Yep, sure enough, first day of class and he’s already high as a kite, some things never change eh?"
    hide charac juan normal_idle
    hide screen Menu

    $characterlist.add_character(C_Juan)
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}New entry added for Juan{/outlinecolor}{/color}{/size}"

    return 0

label intro_brice:
    show charac brice normal_idle
    show screen Menu(0,0)
    brice "Oh Hi [MC]! I sure am glaaaaaad to see you here!"
    mc "And here is Brice, your local big-mouthed annoying dude who has yet to understand that this isn’t high school anymore and bullying people won’t get you a fan club."
    mc "Honestly, I hate how he just can’t get himself to just chill and enjoy uni life without being a bother. But hey, he was my practical works partner for the first semester and he did his part, so let’s at least try to be nice."
    mc "Hi Brice, how was your christmas ?"
    brice "I don’t remember asking you anything [MC]. Where’d you get the idea you could just come and talk to me like that."
    mc "Well you were the one to call to me."
    brice "I didn’t, I just commented on you being here, I didn’t want any talking back from you."
    mc "Yeah, sure, you know what, do whatever you want ok?"
    brice "I’m already doing that. HA!"
    mc "I really can’t fucking stand him."
    hide charac brice normal_idle
    hide screen Menu

    $characterlist.add_character(C_Brice)
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}New entry added for Brice{/outlinecolor}{/color}{/size}"

    return 0

label intro_sadiq:
    show charac sadiq normal_idle
    show screen Menu(0,0)
    mc "Hi Sadiq, how was your winter?"
    sadiq "It was great man, and yours?"
    mc "Nice, nice, ready for the second round?"
    sadiq "As ready as one can be bro! I’m definitely enjoying this more than my previous studies."
    mc "Glad to hear it. You were in medicine weren’t you?"
    sadiq "Yeah, sure was, I mean it wasn’t all bad you know, nothing ever is. But it sure was more of a hassle than this."
    mc "You mean this is easier?"
    sadiq "In a sense yeah, I mean the technical difficulty is about the same, but this is more about practical stuff and less about mindless learning by heart, which in the end makes it easier for me you know."
    mc "Yeah, I totally get that man."
    sadiq "You were partnered with Brice for first semester weren’t you?"
    mc "Yeah… I was."
    sadiq "Must’ve sucked."
    mc "Sure did."
    sadiq "Good thing is it can’t happen again right? I hope we can get partnered together."
    mc "That would be very nice indeed."
    sadiq "I’ll pray for it to happen man. Oh and by the way, this new teacher we have this smester, mr epstein right?"
    mc "yeah, what about him?"
    sadiq "I heard he’s quite severe and also, he does surprise tests every 2 weeks"
    mc "Oh, better remember that! Thanks for the heads up man!"
    hide screen Menu

    centered "{size=+10}{outlinecolor=#ffffff}{color=#000000}As your classmate just said, it is important to take notes{/color}{/outlinecolor}{/size}"
    centered "{size=+10}{outlinecolor=#ffffff}{color=#000000}Use the '{b}Take Notes{/b}' button to write down the curent discution in your notebook{/color}{/outlinecolor}{/size}"
    centered "{size=+10}{outlinecolor=#ffffff}{color=#000000}You will be able to read it again whenever and wherever you want{/color}{/outlinecolor}{/size}"
    centered "{size=+10}{outlinecolor=#ffffff}{color=#000000}But be careful! You only have {color=#f00}10{/color} entries available{/color}{/outlinecolor}{/size}"
    show screen Menu(1,0)
    sadiq "You’re welcome man, alright i’ll be going now, see you soon."
    mc "Yeah, see you man. Sadiq really is a chill guy, I truly hope i can get to know him more."
    hide screen Menu
    hide charac sadiq normal_idle

    $characterlist.add_character(C_Sadiq)
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}New entry added for Sadiq{/outlinecolor}{/color}{/size}"

    return 0

label intro_charles:
    show charac charles normal_idle
    show screen Menu(0,0)
    mc "Hey Charles, how you doing mate?"
    charles "Good Morning [MC]. I’m fine, thank you. And you, how are you ? How were your holidays ?"
    mc "Well, nothing special, I just-"
    charles "Han, personally, I went skiing in one of those prestigious french ski stations."
    mc "...Yup, as always, all that matters to him is to brag and feel superior. Well, I got no choice but to listen to him now…"
    charles "It was soooo good. The only problem i had were those peasants that do not know they have to let the place to those who know what they’re doing. They were so frustrating! But wait, I haven’t told you about what I got there! I could buy so many souvenirs! First there was…"
    mc "I’d better try to escape before he keeps me here for half an hour…"
    mc "Yeah, yeah, I think I get it, those guys must be pretty annoying. Anyway, i’m gonna say hello to the others before Mr. Epstein comes. See you later."
    charles "Hmph, alright. Not that I wanted to tell you that anyway, peasant…"
    mc "… Let’s ignore that last sentence, he’s like that with everyone…"
    mc "Now who to talk to?"
    hide charac charles normal_idle
    hide screen Menu

    $characterlist.add_character(C_Charles)
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}New entry added for Charles{/outlinecolor}{/color}{/size}"

    return 0

label prologue:
    $storyDevelopment = "prologue"
    pause 1
    scene school hallway morning with fade # need
    pause 1
    $stylo = Clue("Stylo",0,"a pen I found in the hallway")
    $cluelist.add_clue(stylo)

    mc "And here I am, wandering about in the university’s hallways while the sun is bright out and other students are enjoying their day. Even I’m wondering why i’m here."
    
    with opunch
    mc "Oh! what is this ?"
    centered "{size=+10}{color=#000000}{outlinecolor=#ffffff}An item has been added to your inventory. Go check it out !{/outlinecolor}{/color}{/size}"
    
    mc "Why is it that I end up spending my afternoon going to my math teacher’s office to ask him for help with his own course."
    mc "While it is true that maths never really were my strong suit, this semester’s been the absolute worse so far."
    mc "Mr Epstein really is what the rumors depicted him as, and more."
    mc "So anyway I’m lost. My airhead brain can’t remember where Epstein’s bloody office is."
    mc "Let’s think this through, right now i’m in B7, i’m quite sure his office was somewhere around here."
    mc "Ok so now if I turn right, the math department should be here right?"
    mc "Aaaaand it’s not, DAMMIT!"
    
    stop music 
    play sound "audio/Effects/girl_shouting.ogg" 
    "AAAAAAAAAAAAHH" with vpunch
    


    mc "What the hell was that!? A scream ?!"
    mc "As I turn around, I see the sign above the opposite hallway: mathematics department."
    mc "Well, here it is then! But what the heck was that noise? It came from there."
    
    play music "audio/BGM/BGM1_(Tiny_Little_Adiantum_Instrumental).mp3" fadein 1.0 fadeout 1.0
    
    mc "As I reach the mid-section of the hallway, I see a notice board on the door to my left: Mr Epstein, Aggregate Teacher"
    mc "Well finally! Here it is!"
    mc "I’m pretty sure the scream came from here though… Maybe he fell and broke a shelf or something, he must be quite hurt in here from the sound of it. Should I maybe come back later?"
    mc "Eh? Whatever, i’m already wasting my afternoon being here, better at least help him out, maybe i’ll get something out of it who knows."
    mc "I slowly push the door open…"
    pause 1 

    play sound "audio/Effects/Creeky-Interior-Door.mp3"

    scene pblack_screen
    with dissolve
    play music "audio/BGM/epstein_dead.ogg" fadein 1.0 fadeout 1.0

    mc "He’s not alone ! He is with a girl ? What are they doing together ? What !?"
    mc "It’s Alex ! What are they doing on the ground so close to each other ? Did he hurt her ?! That bastard ! I repress my surging anger and ask"
    mc "What’s happening here ?"
    
    show charac alex sad_idle
    
    mc_meuf "I...I..tried to st...stop him. He was to fast."
    mc "What are you talking about, what happened ?"
    mc "As I look around I see that Epstein is still on the ground. He’s not moving. Is he …?"
    mc_meuf "He tri..tried to kill himself and I..I wanted to stop but he was to fast !"
    mc_meuf "I don’t know what to do now.."
    mc "Oh my god, oh my god, I can’t believe it"
    mc "It feels surreal, I can’t believe it’s happening right now, I’m having a hard time breathing, my palms are sweaty, knees getting weak, arms are heavy"
    mc "I’m gonna vomit on my sweater already"
    mc_meuf "We can’t stay here, we have to get out.. Maybe we should call someone"
    mc "I hear her mumbling something and helping me move in the hall before I lose consciousness."
    
    stop music 
    return
    while 1:
        $renpy.pause(hard=True)

label prologue_Dormitory:
    show screen Menu(0,1)
    $location = "Dormitory"
    m "mmmh...nothing to do in the dormitory yet..."
    while 1:
        $renpy.pause(hard=True)

label prologue_LectureHall:
    show screen Menu(0,1)
    $location = "LectureHall"
    m "mmmh...nothing to do in the LectureHall yet..."
    while 1:
        $renpy.pause(hard=True)

label prologue_Cafeteria:
    show screen Menu(0,1)
    $location = "Cafeteria"
    m "mmmh...nothing to do in the cafeteria yet..."
    while 1:
        $renpy.pause(hard=True)
