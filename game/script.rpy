# The script of the game goes in this file.

#Initialize things here 
#(Ren'py reads everything as a giant file according to the internet)
init:

    ##### Game Assets #####
    image logo = "dirty_rotten.png"
    image warning = "explicit_content.png"
    image menu_pause = "gui/main_menu.png"

    ##### Flags #####
    $ seen_bulletin = False
    $ went_lakeside = False
    $ went_recreation_area = False

# TODO - Figure out splash screen fix
#### Splash Screen #####
label splashscreen:
    scene black
    with Pause(.25)

    show logo with fade
    with Pause(2)

    show warning
    with Pause(3)

    scene black with dissolve
    with Pause(.75)

    show menu_pause
    with Pause(.5)

    return

# Chat notation
#show image "park/chat/chat0.png" ypos -200 xpos 500
    
########################### The game starts here. ###############################

##### Park ######
label start:

    # Fade in
    stop music fadeout 1.0
    scene black
    pause(1)

    scene bg laptop_twelve with fade
    pause(1.25)

    # Open Chat Alert
    play sound "audio/new_message.ogg"
    call screen chat_nav



    # Pop open button
    # screen jump_to_first_chat:

    #     frame:
    #         xpadding 40
    #         ypadding 20
    #         xalign 0.5
    #         yalign 0.5
    #         textbutton "open chat" action [ToggleScreen("jump_to_first_chat"), Jump("first_chat")]

    # call screen jump_to_first_chat

    pause


            

return

