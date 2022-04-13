label rec_center:
    $ went_lakeside = False
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/backgrounds/bg recreation_transition0.png" with dissolve
    pause(.5)
    hide image "images/park/backgrounds/bg recreation_transition0.png"
    show image "images/park/backgrounds/bg recreation_transition1.png" with dissolve
    pause(.4)
    hide image "images/park/backgrounds/bg recreation_transition1.png"  with dissolve
    pause(.5)
    show image "images/park/backgrounds/bg rec_center.png" with dissolve

    # show donovan forward_smile at five with dissolve
    # pause(.1)
    # show ethan forward_wave at three with dissolve
    # pause(0.5)

    stop music fadeout 3
    play music "audio/park/park_intensifies.mp3" fadein 3

    # show donovan forward_smile_alt at flip with dissolve
    # pause(.1)
    # show ethan forward_smile_alt at eight with dissolve
    # pause(0.5)

    if seen_bulletin == True:

        show donovan upset at ten with dissolve
        show ethan concerned at five with dissolve

        ethan "Hey, we've got people...!"

        show donovan upset at three with dissolve
        show donovan upset at flip with dissolve

        show donna appears at fourteen with dissolve
        show wendy appears at ten with dissolve        

        show donovan big_smile at three with dissolve
        donovan "Hey!"

        show donovan upset with dissolve
        show wendy intrigued with dissolve
        show donna dubious with dissolve

        unknown "Hey."

        show ethan listening with dissolve
        show donovan listening with dissolve
        show wendy cry with dissolve
        show donna cry with dissolve

        donovan "What are you guys doing out here?"

        show ethan concerned with dissolve
        ethan "Looking real upset."

        show ethan listening with dissolve
        
        show donna cry with dissolve
        unknown "Uh, it's our dog.  We haven't been able to find him."

        show wendy cry with dissolve
        unknown "We've been looking..."

        show ethan big_smile with dissolve
        show donna smile with dissolve
        show wendy smile with dissolve
        ethan "Oh, hey! I think I saw your dog!"

        show ethan concerned with dissolve
        ethan "Ugh, no-no-no! Not like that. Sorry."
        ethan "I meant...on the flier. The one at the entrance."

        show ethan listening with dissolve
        show wendy listening with dissolve
        show donna dubious with dissolve

        unknown "Oh yeah, that's our baby. We put that up a week ago."
        show donna listening with dissolve

    else:
        
        donovan "Hey, I see something."

        donovan "Someone...?"

        unknown "Have you guys seen a dog?"

        ethan "A dog...?"

        donovan "No, we haven't seen one."

        unknown "We're looking for our dog, Chips.  We lost him."

    show donovan big_smile with dissolve
    donovan "If you guys need it, we can totally help you."

    show ethan big_smile with dissolve
    ethan "We've got you!"

    show wendy smile with dissolve
    unknown "Really?"

    show donna smile with dissolve
    unknown "We've been looking everywhere. You have no idea how much this means!"

    unknown "Oh, thank you."

    show donna surprised with dissolve
    show donovan smile with dissolve
    show ethan smile with dissolve
    donovan "No problem!  I'm Donovan by the way. He's Ethan."

    show donna smile with dissolve
    donna "I'm Donna"

    show donna smile with dissolve
    show wendy intrigued with dissolve
    wendy "Wendy."

    show wendy smile with dissolve
    show donovan big_smile with dissolve
    show ethan big_smile with dissolve
    donovan "Well, let's go find that pup!"

    show donovan smile with dissolve
    show wendy intrigued with dissolve
    wendy "The last time we saw him was around the lake."

    show donovan big_smile with dissolve
    donovan "Lead the way."

    call screen continue_from_rec
    pause
return