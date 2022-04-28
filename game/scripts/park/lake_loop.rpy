label lake_loop:
    $ went_lakeside = True
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/chat/chat_lake_loop_transition.png" at topright

    show image "images/park/backgrounds/bg lake_loop_transition0.png" with dissolve
    pause(.5)
    hide image "images/park/backgrounds/bg lake_loop_transition0.png"
    show image "images/park/backgrounds/bg lake_loop_transition1.png" with dissolve
    pause(.4)
    hide image "images/park/backgrounds/bg lake_loop_transition1.png"  with dissolve
    pause(.5)
    show image "images/park/backgrounds/bg lake_loop.png" with dissolve

    show donovan forward_smile_alt at three with dissolve
    pause(.1)
    show ethan forward_smile_alt at eight with dissolve
    pause(0.5)

    hide image "images/park/chat/chat_lake_loop_transition.png"
    show image "images/park/chat/lake_loop/chat1_donovan.png" at topright

    donovan "Alright, you guys, let's talk some facts."

    show donovan forward_big_smile with dissolve
    show ethan forward_smile with dissolve

    hide image "images/park/chat/lake_loop/chat1_donovan.png"
    show image "images/park/chat/lake_loop/chat2_donovan.png" at topright

    donovan "Ethan, take it away!"

    show donovan forward_smile_alt with dissolve
    show ethan explains with dissolve

    hide image "images/park/chat/lake_loop/chat2_donovan.png"
    show image "images/park/chat/lake_loop/chat3_ethan.png" at topright

    ethan "Looking around, we can see a lot of younger trees. Some non-native species."

    hide image "images/park/chat/lake_loop/chat3_ethan.png"
    show image "images/park/chat/lake_loop/chat4_ethan.png" at topright
    
    ethan "We're looking for old-growth Alabama pines! That's where the Devil's Tooth grows."

    show ethan cheeky with dissolve

    hide image "images/park/chat/lake_loop/chat4_ethan.png"
    show image "images/park/chat/lake_loop/chat5_ethan.png" at topright

    ethan "And while it may look like we made a bad choice in parks, don't even worry."

    show donovan forward_big_smile_alt with dissolve

    hide image "images/park/chat/lake_loop/chat5_ethan.png"
    show image "images/park/chat/lake_loop/chat6_ethan.png" at topright

    if seen_bulletin == True:
        ethan "This park was established a long time ago."  

        hide image "images/park/chat/lake_loop/chat6_ethan.png"
        show image "images/park/chat/lake_loop/chat7_ethan.png" at topright

        ethan "Although its seen some revisions, I'm sure we'll find us some pines!"

        hide image "images/park/chat/lake_loop/chat7_ethan.png"

    else:
        ethan "Most parks tend to keep some of their old trees around."

        hide image "images/park/chat/lake_loop/chat6_ethan.png"

    show image "images/park/chat/lake_loop/chat8_ethan.png" at topright
    show ethan forward_smile_alt with dissolve

    ethan "That's been an Ethan-minute."

    hide image "images/park/chat/lake_loop/chat8_ethan.png"
    show image "images/park/chat/lake_loop/chat9_donovan.png" at topright

    donovan "Thanks E, for putting us in the know."

    stop music fadeout 3

    jump lake_loop_appears
return

label lake_loop_appears:
    play music "audio/park/park_intensifies.mp3" fadein 3

    show donna appears at fourteen with dissolve
    show wendy appears at ten with dissolve
    show donovan upset at two with dissolve
    show ethan concerned at five with dissolve

    hide image "images/park/chat/lake_loop/chat9_donovan.png"
    show image "images/park/chat/lake_loop/chat10_donovan_intro_gals.png" at topright

    donovan "Woah!"

    hide image "images/park/chat/lake_loop/chat10_donovan_intro_gals.png"
    show image "images/park/chat/lake_loop/chat11_ethan.png" at topright

    ethan "Hello?"

    show donna dubious with dissolve
    show wendy big_sad with dissolve

    hide image "images/park/chat/lake_loop/chat11_ethan.png"
    show image "images/park/chat/lake_loop/chat12_donna.png" at topright

    unknown "Hey, have you seen a dog?"

    show donovan listening with dissolve
    show ethan frustrated with dissolve

    hide image "images/park/chat/lake_loop/chat12_donna.png"
    show image "images/park/chat/lake_loop/chat13_ethan.png" at topright

    ethan "What?"

    show wendy confused with dissolve
    show donna surprised with dissolve

    hide image "images/park/chat/lake_loop/chat13_ethan.png"
    show image "images/park/chat/lake_loop/chat14_wendy.png" at topright

    unknown "A dog. A King Cavalier. He's missing."

    hide image "images/park/chat/lake_loop/chat14_wendy.png"
    show image "images/park/chat/lake_loop/chat15_donovan.png" at topright

    if seen_bulletin == True:
        show ethan  concerned with dissolve
        show donna listening with dissolve
        donovan "We saw your poster earlier. The one at the entrance. That's your dog right?"

    else:
        show donovan upset with dissolve
        show ethan concerned with dissolve
        donovan "A missing dog?"

    show donovan listening with dissolve
    show ethan listening with dissolve

    hide image "images/park/chat/lake_loop/chat15_donovan.png"
    show image "images/park/chat/lake_loop/chat16_donovan.png" at topright

    donovan "How long has your..."

    show wendy big_sad with dissolve
    pause(.1)
    show ethan concerned with dissolve

    hide image "images/park/chat/lake_loop/chat16_donovan.png"
    show image "images/park/chat/lake_loop/chat17_donovan.png" at topright

    donovan "I'm sorry, what's your dog's name?"

    show wendy listening with dissolve
    show donna smile with dissolve
    show donovan smile with dissolve

    hide image "images/park/chat/lake_loop/chat17_donovan.png"
    show image "images/park/chat/lake_loop/chat18_donna.png" at topright

    donna "I'm Donna, this is Wendy, our dog is Chips."

    show ethan smile with dissolve
    show wendy intrigued with dissolve

    hide image "images/park/chat/lake_loop/chat18_donna.png"
    show image "images/park/chat/lake_loop/chat19_ethan.png" at topright

    ethan "I'm Ethan, he's Donovan."

    hide image "images/park/chat/lake_loop/chat19_ethan.png"
    show image "images/park/chat/lake_loop/chat20_donovan.png" at topright

    donovan "Right."

    show donna listening with dissolve
    show wendy listening with dissolve
    show ethan listening with dissolve
    show donovan listening with dissolve

    pause(1)

    show ethan concerned with dissolve

    hide image "images/park/chat/lake_loop/chat20_donovan.png"
    show image "images/park/chat/lake_loop/chat21_ethan.png" at topright

    ethan "So...how long has Chips been missing?"

    show wendy big_sad with dissolve

    hide image "images/park/chat/lake_loop/chat21_ethan.png"
    show image "images/park/chat/lake_loop/chat22_wendy.png" at topright

    wendy "It's not about how long he's been missing, it's about him being scared and hungry."
    
    show donovan smile at five with dissolve
    show ethan concerned at two with dissolve

    hide image "images/park/chat/lake_loop/chat22_wendy.png"
    show image "images/park/chat/lake_loop/chat23_donovan.png" at topright

    donovan "Let's find their dog."

    show ethan smile with dissolve
    show donovan big_smile with dissolve

    hide image "images/park/chat/lake_loop/chat23_donovan.png"
    show image "images/park/chat/lake_loop/chat24_donovan.png" at topright

    donovan "We can find anything! We can find Chips no problem."

    show wendy smile with dissolve
    show donna smile with dissolve

    hide image "images/park/chat/lake_loop/chat24_donovan.png"
    show image "images/park/chat/lake_loop/chat25_wendy.png" at topright

    wendy "Really? You would help us find him?"

    show ethan big_smile with dissolve

    hide image "images/park/chat/lake_loop/chat25_wendy.png"
    show image "images/park/chat/lake_loop/chat26_ethan.png" at topright

    ethan "It's our job, and we do it well."

    show ethan smile with dissolve
    show donovan smile with dissolve

    hide image "images/park/chat/lake_loop/chat26_ethan.png"
    show image "images/park/chat/lake_loop/chat27_ethan.png" at topright

    ethan "Take us to where you last saw him."

    show donna at flip with dissolve
    show wendy at flip with dissolve

    hide image "images/park/chat/lake_loop/chat27_ethan.png"
    show image "images/park/chat/lake_loop/chat28_donna.png" at topright

    donna "It's right up here." 

    show donovan at eight with dissolve
    show ethan smile at four with dissolve

    hide image "images/park/chat/lake_loop/chat28_donna.png"
    show image "images/park/chat/lake_loop/chat29_ethan.png" at topright

    ethan "Lead the way!"

    hide donna with dissolve

    hide wendy with dissolve

    hide donovan with dissolve

    hide ethan with dissolve

    call screen continue_from_loop
    pause
return