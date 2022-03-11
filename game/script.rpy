# The script of the game goes in this file.

#Initialize things here 
#(Ren'py reads everything as a giant file according to the internet)
init:

    ##### Game Assets #####
    image logo = "dirty_rotten.png"
    image warning = "explicit_content.png"
    image menu_pause = "gui/main_menu.png"

    ##### Flags #####
    #false = 0, true = 1
    $ seen_bulletin = 0
    $ went_lakeside = 0
    $ went_recreation_area = 0

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


    
########################### The game starts here. ###############################

##### Park ######
label start:

    # To add fade between menu & start of game
    scene black
    pause(1)

    scene bg laptop_twelve
    pause(1.5)

    show umbrae_intro_message
    pause

return

