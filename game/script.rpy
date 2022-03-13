# The script of the game goes in this file.

#Initialize things here 
#(Ren'py reads everything as a giant file according to the internet)
init:

    ##### Global Game Assets #####
    image logo = "dirty_rotten.png"
    image warning = "explicit_content.png"
    image menu_pause = "gui/main_menu.png"
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

    show menu_pause with fade
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
    
    play music "audio/laptop_boot1.mp3" fadein 1.0
    scene bg laptop_twelve with fade
    pause(1.25)

    # Open Chat Alert
    play sound "audio/new_message.mp3"
    call screen chat_nav
    pause

return

