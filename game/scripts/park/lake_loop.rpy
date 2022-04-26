label lake_loop:
    $ went_lakeside = True
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

    show donovan forward_smile_alt at three with dissolve
    pause(.1)
    show ethan forward_smile_alt at eight with dissolve
    pause(0.5)

    donovan "Alright, you guys, let's talk some facts."

    show donovan forward_big_smile with dissolve
    show ethan forward_smile with dissolve

    donovan "Ethan, take it away!"

    show donovan forward_smile_alt with dissolve
    show ethan explains with dissolve

    ethan "Looking around, we can see a lot of younger trees. Some non-native species."
    
    ethan "We're looking for old-growth Alabama pines! That's where the Devil's Tooth grows."

    show ethan cheeky with dissolve

    ethan "And while maye look like we made a bad choice in parks, don't even worry."

    show donovan forward_big_smile_alt with dissolve

    if seen_bulletin == True:
        ethan "This park was established a long time ago."  
        ethan "Although its seen some revisions, I'm sure we'll find us some pines!"

    else:
        ethan "Most parks tend to keep some of their old trees around."

    show ethan forward_smile_alt with dissolve

    ethan "That's been an Ethan-minute."

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

    donovan "Woah!"

    ethan "Hello?"

    show donna dubious with dissolve
    show wendy big_sad with dissolve

    unknown "Hey, have you seen a dog?"

    show donovan listening with dissolve
    show ethan frustrated with dissolve

    ethan "What?"

    show wendy confused with dissolve
    show donna surprised with dissolve

    unknown "A dog. A King Cavalier. He's missing."

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

    donovan "How long has your..."

    show wendy big_sad with dissolve
    pause(.1)
    show ethan concerned with dissolve

    donovan "I'm sorry, what's your dog's name?"

    show wendy listening with dissolve
    show donna smile with dissolve
    show donovan smile with dissolve

    donna "I'm Donna, this is Wendy, our dog is Chips."

    show ethan smile with dissolve
    show wendy intrigued with dissolve

    ethan "I'm Ethan, he's Donovan."

    donovan "Right."

    show donna listening with dissolve
    show wendy listening with dissolve
    show ethan listening with dissolve
    show donovan listening with dissolve

    pause(1)

    show ethan concerned with dissolve

    ethan "So...how long has Chips been missing?"

    show wendy big_sad with dissolve

    wendy "It's not about how long he's been missing, it's about him being scared and hungry."
    
    show donovan smile at five with dissolve
    show ethan concerned at two with dissolve

    donovan "Let's find their dog."

    show ethan smile with dissolve
    show donovan big_smile with dissolve

    donovan "We can find anything! We can find Chips no problem."

    show wendy smile with dissolve
    show donna smile with dissolve

    wendy "Really? You would help us find him?"

    show ethan big_smile with dissolve

    ethan "It's our job, and we do it well."

    show ethan smile with dissolve
    show donovan smile with dissolve

    ethan "Take us to where you last saw him."

    show donna at flip with dissolve
    show wendy at flip with dissolve

    donna "It's right up here" 

    show donovan at eight with dissolve
    show ethan smile at four with dissolve

    ethan "Lead the way!"

    call screen continue_from_loop
    pause
return