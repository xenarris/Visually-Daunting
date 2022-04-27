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

    show donovan listening at flip  with dissolve
    pause(.1)
    show ethan concerned at twelve with dissolve
    pause(0.5)

    show ethan dubious at flip with dissolve

    show image "images/park/chat/junction/chat1_ethan.png" at topright

    ethan "I've got nothing."
    pause(.2)
    show donovan upset at flip_back with dissolve
    show ethan frustrated with dissolve

    hide image "images/park/chat/junction/chat1_ethan.png"
    show image "images/park/chat/junction/chat2_donovan.png" at topright

    donovan "I've got nothing, too."

    show ethan smile with dissolve
    show donovan smile with dissolve

    hide image "images/park/chat/junction/chat2_donovan.png"
    show image "images/park/chat/junction/chat3_ethan.png" at topright

    play sound "audio/park/voices/ethan/ethan_meh.mp3"
    ethan "Meh."
    
    show donovan with dissolve
    show ethan with dissolve
    show donovan forward_smile_alt with dissolve
    pause(.1)
    show ethan forward_smile with dissolve
    pause(.1)

    hide image "images/park/chat/junction/chat3_ethan.png"
    show image "images/park/chat/junction/chat4_ethan.png" at topright

    ethan "Well folks, this is not the spot."

    hide image "images/park/chat/junction/chat4_ethan.png"
    show image "images/park/chat/junction/chat5_donovan.png" at topright

    donovan "We've got to keep moving if we want to find our 'berries.'"

    hide image "images/park/chat/junction/chat5_donovan.png"
    show image "images/park/chat/junction/chat6_donovan.png" at topright

    donovan "So what will it be?"

    if seen_bulletin == True:
        show donovan forward_big_smile_alt with dissolve

        hide image "images/park/chat/junction/chat6_donovan.png"
        show image "images/park/chat/junction/chat7_donovan.png" at topright

        donovan "We could head North, towards the lake."

        show ethan forward_smile_alt with dissolve

        hide image "images/park/chat/junction/chat7_donovan.png"
        show image "images/park/chat/junction/chat8_ethan.png" at topright

        ethan "Or we could head East, towards the recreational center."

        hide image "images/park/chat/junction/chat8_ethan.png"
        show image "images/park/chat/junction/chat9_player.png" at topright

        call screen lake_or_rec
        pause

    else:
        show donovan forward_smile_alt with dissolve

        hide image "images/park/chat/junction/chat6_donovan.png"
        show image "images/park/chat/junction/chat7_nobill_donovan.png" at topright

        donovan "The low-road or high-road."

        show ethan forward_smile_alt with dissolve

        hide image "images/park/chat/junction/chat7_nobill_donovan.png"
        show image "images/park/chat/junction/chat8_nobill_ethan.png" at topright

        ethan "North or East? Flip a coin."

        hide image "images/park/chat/junction/chat8_nobill_ethan.png"
        show image "images/park/chat/junction/chat9_nobill_player.png" at topright

        call screen north_or_east
        pause

return