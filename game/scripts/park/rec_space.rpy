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

    show donovan listening at ten with dissolve
    pause(.1)
    show ethan listening at five with dissolve
    pause(.6)

    stop music fadeout 3
    play music "audio/park/park_intensifies.mp3" fadein 3

    if seen_bulletin == True:

        show image "images/park/chat/Rec_center/Billboard/chat1_ethan.png" at topright

        show ethan frustrated at two with dissolve

        show donovan frown at five with dissolve

        pause(1)

        show donna appears at fourteen with dissolve

        show wendy appears at eleven with dissolve

        ethan "Hey, we've got people...!"

        show ethan concerned with dissolve

        show donovan upset with dissolve

        show donna surprised with dissolve

        show wendy big_sad with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat1_ethan.png"
        show image "images/park/chat/Rec_center/Billboard/chat2_donovan.png" at topright

        play sound "audio/park/voices/ethan/ethan_unknown_hello.mp3"
        ethan "Hello?"

        show donna listening with dissolve
        
        hide image "images/park/chat/Rec_center/Billboard/chat2_donovan.png"
        show image "images/park/chat/Rec_center/Billboard/chat3_wendy.png" at topright

        unknown "Hey."

        show donovan listening with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat3_wendy.png"
        show image "images/park/chat/Rec_center/Billboard/chat4_donovan.png" at topright

        donovan "What are you guys doing out here?"

        show ethan listening with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat4_donovan.png"
        show image "images/park/chat/Rec_center/Billboard/chat5_ethan.png" at topright

        ethan "Looking real upset."

        show wendy dubious with dissolve
        
        hide image "images/park/chat/Rec_center/Billboard/chat5_ethan.png"
        show image "images/park/chat/Rec_center/Billboard/chat6_wendy.png" at topright

        unknown "It's our dog.  We haven't been able to find him."

        show wendy big_sad with dissolve

        show donna ashamed with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat6_wendy.png"
        show image "images/park/chat/Rec_center/Billboard/chat7_donna.png" at topright

        unknown "We've been looking..."

        show ethan concerned with dissolve

        show donovan upset with dissolve

        show wendy intrigued with dissolve

        show donna dubious with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat7_donna.png"
        show image "images/park/chat/Rec_center/Billboard/chat8_ethan.png" at topright

        ethan "Oh, hey! I think I saw your dog!"

        show ethan sorry with dissolve

        show wendy big_sad with dissolve

        show donna upset with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat8_ethan.png"
        show image "images/park/chat/Rec_center/Billboard/chat9_ethan.png" at topright

        ethan "Ugh, no-no-no! Not like that. Sorry."

        show donna listening with dissolve

        show wendy listening with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat9_ethan.png"
        show image "images/park/chat/Rec_center/Billboard/chat10_ethan.png" at topright

        ethan "I meant...on the flier. The one at the entrance."

        show wendy intrigued with dissolve

        show donna ashamed with dissolve

        show ethan concerned with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat10_ethan.png"
        show image "images/park/chat/Rec_center/Billboard/chat11_donna.png" at topright

        unknown "Oh yeah, that's our baby. TYeah,hat's Chips!"

        show ethan listening with dissolve

        hide image "images/park/chat/Rec_center/Billboard/chat11_donna.png"

    else:
        
        show image "images/park/chat/Rec_center/No Billboard/chat1_nobill_donovan.png" at topright

        donovan "Hey, I see something."

        show ethan concerned at two with dissolve

        show donovan frown at five with dissolve

        show donna appears at eleven with dissolve

        show wendy appears at fourteen with dissolve

        hide image "images/park/chat/Rec_center/No Billboard/chat1_nobill_donovan.png"
        show image "images/park/chat/Rec_center/No Billboard/chat2_nobill_donovan.png" at topright

        donovan "Someone...?"

        show donna surprised at eleven with dissolve

        show wendy listening at fourteen with dissolve

        show donovan upset with dissolve

        hide image "images/park/chat/Rec_center/No Billboard/chat2_nobill_donovan.png"
        show image "images/park/chat/Rec_center/No Billboard/chat3_nobill_donna.png" at topright

        unknown "Have you guys seen a dog?"

        hide image "images/park/chat/Rec_center/No Billboard/chat3_nobill_donna.png"
        show image "images/park/chat/Rec_center/No Billboard/chat4_nobill_ethan.png" at topright

        ethan "A dog...?"

        show donovan listening with dissolve

        show wendy big_sad with dissolve

        hide image "images/park/chat/Rec_center/No Billboard/chat4_nobill_ethan.png"
        show image "images/park/chat/Rec_center/No Billboard/chat5_nobill_donovan.png" at topright

        donovan "No, we haven't seen one."

        show donna listening with dissolve

        show ethan listening with dissolve

        hide image "images/park/chat/Rec_center/No Billboard/chat5_nobill_donovan.png"
        show image "images/park/chat/Rec_center/No Billboard/chat6_nobill_wendy.png" at topright

        unknown "We're looking for our dog, Chips.  We lost him."

        hide image "images/park/chat/Rec_center/No Billboard/chat6_nobill_wendy.png"

    show donovan smile with dissolve
    
    show donna surprised with dissolve

    show wendy confused with dissolve

    show image "images/park/chat/Rec_center/chat12_donovan.png" at topright

    donovan "If you guys need it, we can totally help you."

    show ethan smile with dissolve

    hide image "images/park/chat/Rec_center/chat12_donovan.png"
    show image "images/park/chat/Rec_center/chat13_ethan.png" at topright

    ethan "We've got you!"

    show wendy listening with dissolve

    hide image "images/park/chat/Rec_center/chat13_ethan.png"
    show image "images/park/chat/Rec_center/chat14_wendy.png" at topright

    unknown "Really?"

    show donna smile with dissolve

    hide image "images/park/chat/Rec_center/chat14_wendy.png"
    show image "images/park/chat/Rec_center/chat15_donna.png" at topright

    unknown "We've been looking everywhere. Thank you!"

    show wendy smile with dissolve

    hide image "images/park/chat/Rec_center/chat15_donna.png"
    show image "images/park/chat/Rec_center/chat16_wendy.png" at topright

    unknown "Oh!"

    show wendy big_sad with dissolve

    show ethan concerned with dissolve

    show donna listening with dissolve

    hide image "images/park/chat/Rec_center/chat16_wendy.png"
    show image "images/park/chat/Rec_center/chat17_donovan.png" at topright

    donovan "No problem!  I'm Donovan by the way. He's Ethan."

    show ethan listening with dissolve

    show donna smile with dissolve

    hide image "images/park/chat/Rec_center/chat17_donovan.png"
    show image "images/park/chat/Rec_center/chat18_donna.png" at topright

    donna "I'm Donna"

    show wendy listening with dissolve

    show ethan listening with dissolve

    hide image "images/park/chat/Rec_center/chat18_donna.png"
    show image "images/park/chat/Rec_center/chat19_wendy.png" at topright

    wendy "Wendy."

    show ethan smile with dissolve
    pause(.3)
    show wendy smile with dissolve

    hide image "images/park/chat/Rec_center/chat19_wendy.png"
    show image "images/park/chat/Rec_center/chat20_donovan.png" at topright

    donovan "Well, let's go find that pup!"

    hide image "images/park/chat/Rec_center/chat20_donovan.png"
    show image "images/park/chat/Rec_center/chat21_wendy.png" at topright

    wendy "The last time we saw him was around the lake."

    show donna at flip with dissolve

    show wendy at flip with dissolve

    show donovan at eight with dissolve

    show ethan at five with dissolve

    hide image "images/park/chat/Rec_center/chat21_wendy.png"
    show image "images/park/chat/Rec_center/chat22_donovan.png" at topright

    donovan "Lead the way."
    
    hide donna with dissolve

    hide wendy with dissolve

    hide donovan with dissolve
    
    hide ethan with dissolve

    call screen continue_from_rec
    pause
return