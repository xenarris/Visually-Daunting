# TODO - Replace repeated image with movement through trees - when drawn

label park_junction:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/backgrounds/bg billboard_transition0.png" with dissolve
    pause(.5)
    hide image "images/park/backgrounds/bg billboard_transition0.png"
    show image "images/park/backgrounds/bg junction_transition0.png" with dissolve
    pause(.4)
    hide image "images/park/backgrounds/bg junction_transition0.png"  with dissolve
    pause(.5)
    show image "images/park/backgrounds/bg park_junction.png" with dissolve

    show donovan listening at two with dissolve
    pause(.1)
    show ethan concerned at six with dissolve
    pause(0.5)

    show ethan dubious at flip with dissolve

    ethan "I've got nothing."
    pause(.2)
    show donovan upset at flip with dissolve
    pause(.1)
    show ethan frustrated with dissolve
    pause(.1)
    donovan "I've got nothing, too."

    show ethan smile with dissolve
    pause(.2)
    show donovan smile with dissolve
    ethan "Meh."

    show donovan at three with dissolve
    show ethan at five with dissolve
    show donovan forward_smile_alt with dissolve
    pause(.1)
    show ethan forward_smile with dissolve
    pause(.1)

    ethan "Well folks, this is not the one."

    donovan "We've got to keep moving if we want to find our 'berries.'"

    donovan "So what will it be?"

    if seen_bulletin == True:
        show donovan forward_big_smile_alt with dissolve
        donovan "We could head North, towards the lake."

        show ethan forward_smile_alt with dissolve
        pause(.1)
        ethan "Or we could head East, towards the recreational center."

        pause

    else:
        show donovan forward_smile_alt with dissolve
        pause(.1)
        donovan "It's the low-road or high-road situation."

        show ethan forward_smile_alt with dissolve
        pause(.1)
        ethan "Should we head North or take this path East?\"\n\"Flip a coin."
        pause

    # TODO - Make some screen buttons & paths

    pause
return