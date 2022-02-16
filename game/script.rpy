# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define dono = Character("Donovan")
define ethan = Character("Ethan")
define chat = Character("Chat")

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

    dono "We got a tip from user [[ricitioxy] on how local psychonauts survice such harsh climates."
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
    scene bg park_sw_switch
    "[[debug] sw_intersection start here"

    "{i}Nighttime{/i}"
    
    
    "[[debug] Will now restart/jump back to mushroom_hunting label"
    jump lb_mushroom_hunting
