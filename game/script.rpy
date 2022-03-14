# The script of the game goes in this file.

#Initialize things here 
#(Ren'py reads everything as a giant file according to the internet)
init:

    ##### Positions #####
    $ zero = Position(xpos=0.0, xanchor='center')
    $ one = Position(xpos=0.1, xanchor='center')
    $ two = Position(xpos=0.2, xanchor='center')
    $ three = Position(xpos=0.3, xanchor='center')
    $ four = Position(xpos=0.4, xanchor='center')
    $ five = Position(xpos=0.5, xanchor='center')
    $ six = Position(xpos=0.6, xanchor='center')
    $ seven = Position(xpos=0.7, xanchor='center')
    $ eight = Position(xpos=0.8, xanchor='center')
    $ nine = Position(xpos=0.9, xanchor='center')
    $ ten = Position(xpos=1.0, xanchor='center')
                    
    ##### Global Game Assets #####
    image logo = "dirty_rotten.png"
    image warning = "explicit_content.png"
    image menu_fade = "gui/menu_fade.png"
    image menu_clear = "gui/menu_clear.png"
    image menu_appear = "gui/main_menu.png"
    image bg wizcord = "bg wizcord.png"
    image bg wizcord_choice = "bg wizcord_choice.png"
    image bg wizcord_stream_ease = "bg wizcord_stream_ease.png"

    ##### Flags #####
    $ seen_bulletin = False
    $ went_lakeside = False
    $ went_recreation_area = False

#### Splash Screen #####
label splashscreen:
    scene black with fade
    with Pause(.25)

    show logo with dissolve
    with Pause(3.5)

    scene black with fade
    show warning with fade
    with Pause(7.5)

    scene black with dissolve
    with Pause(.75)

    show menu_fade with fade
    with Pause(.2)
    
    play sound "audio/visually_daunting.mp3"

    show menu_clear with dissolve
    with Pause(.3)
    
    show menu_appear with dissolve
    with Pause(1)

    return
    
########################### The game starts here. ###############################

##### Park ######
label start:

    # Fade in
    stop music fadeout 1.0
    
    pause(2)
    scene black
    show image "images/park/assets/actI.png" with dissolve
    pause(5)
    scene black with dissolve
    
    play music "audio/boot_seance.mp3" fadein 1.0
    scene bg laptop_twelve with fade
    pause(1.25)

    # Open Chat Alert
    play sound "audio/new_message.mp3"
    call screen chat_nav
    pause

return

