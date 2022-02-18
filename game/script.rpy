# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define dono = Character("Donovan")
define ethan = Character("Ethan")
define wendy = Character("Wendy")
define donna = Character("Donna")
define chat = Character("Chat")
define unknown = Character("???")

#Initialize things here 
#(Ren'py reads everything as a giant file according to the internet)
init:
    # Image Resizing
    image bg laptop_full = im.Scale("bg laptop_full.png", 1920, 1080)
    image bg laptop_full_chat = im.Scale("bg laptop_full_chat.png", 1920, 1080)
    image bg laptop_overlay = im.Scale("bg laptop_overlay.png", 1920, 1080)
    image bg park_entrance = im.Scale("bg park_entrance.png", 1920, 1080)
    image bg park_bulletin = im.Scale("bg park_bulletin.png", 1920, 1080)
    image bg park_sw_switch = im.Scale("bg park_south_switch.png", 1920, 1080)
    image bg white = im.Scale("bg white.jpg", 1920, 1080)

    #choice flags here
    #false = 0, true = 1
    $ seen_bulletin = 0
    $ went_lakeside = 0
    $ went_recreation_area = 0

    #counters here
    
# The game starts here.

label start:

    jump lb_laptop_introduction

    #everything in this label past this is unused
    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label lb_laptop_introduction:

    #initial bg
    scene bg laptop_full
    
    "Start of Laptop Intro"
    "[[Streamer scene - Mushroom Hunting]\nIF 12:25 [[MISS STREAM\] - ELSE -\nJump in @time-stamp"
    ""
    "The stream will start soon..."

    scene bg laptop_full_chat

    "{i}Fwitch nonsense here x10{/i}"

    "{i}Tutorial scenes here (probably not needed though){/i}"

    "Oh, the stream is finally starting! Let's see what we have here tonight..."

    jump lb_mushroom_hunting



label lb_mushroom_hunting:
    #Off Stream intoduction
    scene bg park_bulletin

    "Two young friends, Donovan and Ethan, stand in front of a park billboard."

    show donovan happy at left
    "One hosts a clean cut, preppy like look."

    show ethan happy at right
    "The other has ventured into the soft gothic territory."

    "Their stream PsyShmanz pulls a lot of viewers."
    "They travel around the globe, looking for different psychedelics to take."
    "Everyone thinks they're brothers, but they're not."

    hide donovan happy
    hide ethan happy


    #Stream's park entrance
    scene bg laptop_overlay as overlay
    show bg park_entrance behind overlay
    "{b}Ext. Park Entrance - Night{/b}"

    show donovan happy at left behind overlay
    "{i}A smiling figure holding the camera appears on stream{/i}"

    dono "Hello, happy viewers!"
    dono "Good morning, or evening! Where ever you are."

    "{i}CHAT goes wild{/i}"

    show ethan happy at right behind overlay
    ethan "We're coming to you guys live from Eureka Springs, Arkansas."

    "{i}CHAT goes wild once more!{/i}"

    dono "Not a location we typically visit. "
    dono "Especially considering that mushrooms are a controlled substance here."

    "[[reponse surrounding psychedelics]"

    show ethan sad at right behind overlay
    show donovan sad at left behind overlay
    ethan "A Class C felony, even for harvesting."

    "{i}[[Chat Pop-up here]{/i}: [[user] donated $my spleen"
    "{i}Chat filled with rage/defensive comments{/i}"

    show donovan happy at left behind overlay
    dono "Don't worry you guys, we're not after anything illegal here."

    show ethan happy at right behind overlay
    ethan "We found a loophole!"

    "{i}Chat blows up excited over this{/i}"
    "{i}[[A pop up here happens]{/i}"

    ethan "Knew you would like that."

    "{i}[[Chat likes that meme]{/i}"

    dono "We got a tip from user [[ricitioxy] on how local psychonauts service such harsh climates."
    "{i}[[Donovan closed eyes, open mouth]{/i}"
    dono "For those who don't grow, there's some wild foraging at hand."
    dono "Arkansas' mild winters lead to excellent fruiting. And while harvesting mushrooms is illegal..."
    dono "harvesting what comes out isn't."

    "{i}Chat loves Donovan some more{/i}"

    ethan "Tonight we're searching for Hydnellum Peckii, a.k.a. the 'Devil's Tooth.'"

    dono "A cream colored mushroom with a short body and a wide cap, that's flat on top."
    dono "A cap peppered with a series of red dots."

    "{i}Chat has been diagnosed with excitement emoji syndrome{/i}"

    dono "And those dots are why we're here tonight! We've come to harvest the 'Devil's Berry!'"

    "{i}Chat blows up{/i}"

    ethan "These 'berries' contain a hallucinogenic compound called myristicin. Known for it's euphoric effects."

    "{i}Chat psychedelic emojis{/i}"

    dono "So, should we start?"
    ethan "Lets..."

    "{i}Chat goes wild, psy boy love{/i}"
    
    #first choices
    #we can set boolean values after this
    menu :
        "[[Awaiting user input]"
        "Check the post!":
            $ seen_bulletin = 1
            jump lb_mushroom_hunting_opt1
        "Get going!":
            jump lb_mushroom_hunting_opt2
        "[[debug] Continue to repeat from laptop intro":
            "Will now restart/jump back to laptop intro label"
            jump lb_laptop_introduction
        "[[debug] Continue to repeat from mushroom_hunting label":
            "Will now restart/jump back to mushroom_hunting label"
            jump lb_mushroom_hunting

    jump lb_mushroom_hunting


label lb_mushroom_hunting_opt1:
    "[[debug] Option 1 start here"

    "{i}[[Chat talks about billboard]{/i}"

    #Surpised Donovan here
    "{i}Donovan looks surprised{/i}"
    dono "You guys want us to check the billboard?"

    #smile donovan here
    dono "Done!"
    
    #Go to billboard moments later
    scene bg laptop_overlay as overlay
    show bg park_bulletin behind overlay

    #zoom to billboard for five seconds before beginning to talk

    #Donovan and Ethan should be off screen at this point

    ethan "Aww, there's a little missing dog."

    "{i}[[Chat is being sympathetic to Ethan]{/i}"

    dono "Bell Lake, Established 1915. Huh!"
    dono "Check out this map."

    "{i}[[Chat is shocked emoji]{/i}"

    dono "Bell Lake is to the North. Eagle Point is a little further up. It's connected to this side trail here."
    dono "There's also a little recreational space to the East. With some benches and a stage."
    dono "We should probably memorize this, so that we don't get lost."

    "{i}[[Chat chants don't get lost]{/i}"

    ethan "I've got you, I'll take a picture"

    "{i}[[Chat blows up at the idea of picture taking]{/i}"

    #emulate a flash
    window hide dissolve
    pause 1.0
    show bg white as white_bg behind overlay with dissolve
    pause 1.0
    show bg park_entrance behind white_bg
    hide white_bg with dissolve
    pause 1.0
    window show dissolve

    #Park entrance takeoff
    show ethan happy at right
    ethan "Got it!"

    show donovan happy at left
    dono "Let's go!"

    "{i}[[Chat blows up let's do this!]{/i}"
    

    jump lb_mushroom_hunting_sw_intersection


label lb_mushroom_hunting_opt2:
    "[[debug] Option 2 start here"

    "{i}[[Chat blows up let's do this!]{/i}"

    dono "Alright folks...let's do this!"

    ethan "Lets!"

    jump lb_mushroom_hunting_sw_intersection

label lb_mushroom_hunting_sw_intersection:

    scene bg laptop_overlay as overlay
    show bg park_sw_switch behind overlay
    "[[debug] sw_intersection start here"

    "{i}Nighttime{/i}"
    
    "Ethan and Donovan seem to be bent over looking"

    "{i}Rustling{/i}"

    show ethan sad at right behind overlay
    ethan "I've got nothing."

    show donovan sad at left behind overlay
    dono "Ah, I've got nothing."

    #chat is sending emoji's here too
    "{i}Chat seems visibly upset{/i}"

    show donovan happy at left
    dono "Alright folks, it looks like the proverbial 'high-road/low-road' situation."
    dono "So, should we head further North? Or Flip East? Up to you guys."

    #Choice North (Lake side) or East (Recreation area)
    menu:
        dono "So, should we head further North? Or Flip East? Up to you guys."
        "North!!":
            $ went_lakeside = 1
            jump lb_mushroom_hunting_lakeside
        "East, east, east, eastast!!!":
            $ went_recreation_area = 1
            jump lb_mushroom_hunting_recreation

    
    "[[debug] Will now restart/jump back to mushroom_hunting label"
    jump lb_mushroom_hunting

label lb_mushroom_hunting_lakeside:

    scene bg laptop_overlay as overlay
    show bg park_lakeside behind overlay
    "[[Debug] went lakeside"

    show donovan happy at left behind overlay
    dono "Alright, you guys, let's talk some facts."
    
    #Donovan points at ethan here
    dono "Ethan, take it away!"

    "{i}Chat sends ethan love{/i}"

    #Scholarly Ethan mode here
    show ethan happy at right behind overlay
    ethan "Looking around, we can see a lot of younger trees and a lot of non-native species."

    "{i}Chat sending mixed emojis of trees{/i}"

    ethan "What we're truly looking for though, are some of those old-growth Alabama pines! As the Devil's Tooth loves to grow on them."  
    
    "{i}Chat is mind blown and memeing{/i}"

    #donovan does a smile at the camera here
    show donovan happy at left behind overlay

    "{i}Chat is sending pines, hearts, mind-blown emojis{/i}"

    #typo? maye TODO
    ethan "And while maye look like we made a bad choice in parks, don't even worry."

    if seen_bulletin == 1:
        ethan "This park was established a long time ago. Although its seen some revisions, I'm sure we'll find us some pines!"
    else:
        ethan "Most parks, even the newer ones, tend to keep some of their old trees around."

    "{i}Chat goes wild over the boys, loves their travels{/i}"

    ethan "That's been an Ethan-minute."

    dono "Thanks E, for putting us in the know."

    #Light approaches in the background, Ethan moves
    #over to Donovan and makes room for Donna & Wendy to enter

    #TODO Move dono and ethan left properly
    show donovan shocked at left behind overlay
    dono "Woah!"

    show ethan confused at left behind overlay
    ethan "Hello?"

    #Meeting wendy and donna the first time
    #unknown person at first
    show donna worried at right behind overlay
    unknown "Hey, have you seen a dog?"

    #Confused ethan
    ethan "What?"

    unknown "A dog. A Cavalier King. He's a Cavalier King. He's missing."

    #Worried donovan
    show donovan worried at left behind overlay

    if seen_bulletin == 1:
        dono "We saw your poster earlier. The one at the entrance. That's your dog right?"
    else:
        "Woah, folks. It looks like we've got a missing dog."

    dono "How long has your..."
    dono "I'm sorry, what's your dog's name?"

    #donna frustated here
    show donna frustrated at right behind overlay
    donna "I'm Donna, this is Wendy, our dog is Chips."

    #Frustrated ethan
    show ethan frustated at left behind overlay
    ethan "I'm Ethan, he's Donovan."
    
    #frustrated donovan
    show donovan frustated at left behind overlay
    dono "Right."

    show donovan concerned at left behind overlay
    dono "So, how long has Chips been missing?"

    #sad wendy
    show wendy sad at right behind overlay
    wendy "It's not about how long he's been missing, it's about him being scared and hungry."

    #straight faced ethan
    show ethan smile at left behind overlay
    ethan "Hmmph, Donovan let's find their dog."

    #smiling donovan
    show donovan smile at left behind overlay
    dono "We can find anything, we can find Chips no problem."

    #worried wendy
    show wendy worried at right behind overlay
    wendy "Really? You would help us find him?"

    #smile ethan
    ethan "It's our job, and we do it well. Take us to where you last saw him."

    #neutral donna
    show donna neutral at right behind overlay
    donna "It's right up here"

    #still smiling here
    ethan "So, you guys ready?"

    #player must agree to progress
    menu:
        ethan "So, you guys ready?"

        "I'm ready":
            "{i}Chat agrees{/i}"

    "[[debug] Will now restart/jump back to mushroom_hunting label"
    jump lb_mushroom_hunting

label lb_mushroom_hunting_recreation:
    "[[Debug] went lakeside"    
    
    "[[debug] Will now restart/jump back to mushroom_hunting label"
    jump lb_mushroom_hunting
