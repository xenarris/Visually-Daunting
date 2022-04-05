label lake_loop:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/backgrounds/bg lake_loop_transition0.png" with dissolve
    pause(.5)
    hide image "images/park/backgrounds/bg lake_loop_transition0.png"
    show image "images/park/backgrounds/bg lake_loop_transition1.png" with dissolve
    pause(.4)
    hide image "images/park/backgrounds/bg lake_loop_transition1.png"  with dissolve
    pause(.5)
    show image "images/park/backgrounds/bg lake_loop.png" with dissolve

    show donovan forward_smile_alt at five with dissolve
    pause(.1)
    show ethan forward_wave at three with dissolve
    pause(0.5)


    pause

return