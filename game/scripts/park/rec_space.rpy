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

    if seen_bulletin == True:

        ethan "Hey, we've got people...!"

        donovan "Hey!"

        unknown "Hey."

        donovan "What are you guys doing out here?"

        ethan "Looking real upset."

        unknown "Uh, it's our dog.  We haven't been able to find him."

        unknown "We've been looking..."

        ethan "Oh, hey! I think I saw your dog!"

        ethan "Ugh, no-no-no! Not like that. Sorry."

        ethan "I meant...on the flier. The one at the entrance."

        unknown "Oh yeah, that's our baby. We put that up a week ago."

    else:
        
        donovan "Hey, I see something."

        donovan "Someone...?"

        unknown "Have you guys seen a dog?"

        ethan "A dog...?"

        donovan "No, we haven't seen one."

        unknown "We're looking for our dog, Chips.  We lost him."

    donovan "If you guys need it, we can totally help you."

    ethan "We've got you!"

    unknown "Really?"

    unknown "We've been looking everywhere. You have no idea how much this means!"

    unknown "Oh, thank you."

    donovan "No problem!  I'm Donovan by the way. He's Ethan."

    donna "I'm Donna"

    wendy "Wendy."

    donovan "Well, let's go find that pup!"

    wendy "The last time we saw him was around the lake."

    donovan "Lead the way."

    call screen continue_from_rec
    pause
return