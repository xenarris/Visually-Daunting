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

    show donovan listening at five with dissolve
    pause(.1)
    show ethan listening at ten with dissolve
    pause(.6)

    stop music fadeout 3
    play music "audio/park/park_intensifies.mp3" fadein 3

    if seen_bulletin == True:

        show image "images/park/chat/chat_ethan_hey.png"

        ethan "Hey, we've got people...!"

        show donovan upset at three with dissolve

        show ethan concerned at six with dissolve

        show donna appears at fourteen with dissolve

        show wendy appears at eleven with dissolve

        show donna surprised with dissolve

        show wendy big_sad with dissolve

        hide image "images/park/chat/chat_ethan_hey.png"
        show image "images/park/chat/chat_dono_what.png"

        donovan "Hello?"

        show donna listening with dissolve

        show donovan upset with dissolve
        show wendy intrigued with dissolve
        show donna dubious with dissolve

        unknown "Hey."

        show donovan listening with dissolve

        donovan "What are you guys doing out here?"

        show ethan listening with dissolve

        ethan "Looking real upset."

        show wendy dubious with dissolve

        unknown "It's our dog.  We haven't been able to find him."

        show wendy big_sad with dissolve

        show donna ashamed with dissolve

        show wendy cry with dissolve
        unknown "We've been looking..."

        show ethan concerned with dissolve

        show donovan upset with dissolve

        show wendy intrigued with dissolve

        show donna dubious with dissolve

        ethan "Oh, hey! I think I saw your dog!"

        show ethan sorry with dissolve

        show wendy big_sad with dissolve

        show donna upset with dissolve

        ethan "Ugh, no-no-no! Not like that. Sorry."

        show donna listening with dissolve

        show wendy listening with dissolve

        ethan "I meant...on the flier. The one at the entrance."

        show wendy intrigued with dissolve

        show donna ashamed with dissolve

        show ethan concerned with dissolve

        unknown "Oh yeah, that's our baby. We put that up a week ago."
        show donna listening with dissolve

        show ethan listening with dissolve


    else:

        donovan "Hey, I see something."
        
        show donovan frown at six with dissolve

        show ethan concerned at three with dissolve

        show donna appears at eleven with dissolve

        show wendy appears at fourteen with dissolve

        donovan "Someone...?"

        show donna surprised at eleven with dissolve

        show wendy listening at fourteen with dissolve

        show donovan upset with dissolve

        unknown "Have you guys seen a dog?"

        show wendy dubious with dissolve
        show ethan concerned with dissolve
        ethan "A dog...?"

        show donovan listening with dissolve

        show wendy big_sad with dissolve

        donovan "No, we haven't seen one."

        show donna listening with dissolve

        show ethan listening with dissolve

        unknown "We're looking for our dog, Chips.  We lost him."
        
        show donna listening with dissolve

    show donovan smile with dissolve
    
    show donna surprised with dissolve

    show wendy confused with dissolve

    donovan "If you guys need it, we can totally help you."

    show ethan smile with dissolve

    ethan "We've got you!"

    show wendy listening with dissolve

    unknown "Really?"

    show donna smile with dissolve

    unknown "We've been looking everywhere. Thank you!"

    show wendy smile with dissolve

    unknown "Oh!"

    show wendy big_sad with dissolve

    show ethan concerned with dissolve

    show donna listening with dissolve

    donovan "No problem!  I'm Donovan by the way. He's Ethan."

    show ethan listening with dissolve

    show donna smile with dissolve

    donna "I'm Donna"

    show wendy listening with dissolve

    show ethan listening with dissolve

    wendy "Wendy."

    show ethan smile with dissolve
    pause(.3)
    show wendy smile with dissolve

    donovan "Well, let's go find that pup!"

    show donovan smile with dissolve
    show wendy intrigued with dissolve
    wendy "The last time we saw him was around the lake."

    show donna at flip with dissolve

    show wendy at flip with dissolve

    show donovan at eight with dissolve

    donovan "Lead the way."

    call screen continue_from_rec
    pause
return