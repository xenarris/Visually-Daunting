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

    show donovan forward_smile_alt at flip with dissolve
    pause(.1)
    show ethan forward_smile_alt at three with dissolve
    pause(0.5)

    donovan "Alright, you guys, let's talk some facts."

    donovan "Ethan, take it away!"

    ethan "Looking around, we can see a lot of younger trees and a lot of non-native species."

    ethan "What we're truly looking for though, are some of those old-growth Alabama pines! As the Devil's Tooth loves to grow on them."

    ethan "And while maye look like we made a bad choice in parks, don't even worry."

    if seen_bulletin == True:
        ethan "This park was established a long time ago.  Although its seen some revisions, I'm sure we'll find us some pines!"

    else:
        ethan "Most parks, even the newer ones, tend to keep some of their old trees around."

    ethan "That's been an Ethan-minute."

    donovan "Thanks E, for putting us in the know."

    stop music fadeout 3

    jump lake_loop_appears
return

label lake_loop_appears:
    play music "audio/park/park_intensifies.mp3" fadein 3

    donovan "Woah!"

    ethan "Hello?"

    unknown "Hey, have you seen a dog?"

    ethan "What?"

    unknown "A dog. A King Cavalier. He's missing."

    if seen_bulletin == True:
        donovan "We saw your poster earlier. The one at the entrance. That's your dog right?"

    else:

        donovan "Woah, folks. It looks like we've got a missing dog."

    donovan "How long has your..."

    donovan "I'm sorry, what's your dog's name?"

    donna "I'm Donna, this is Wendy, our dog is Chips."

    ethan "I'm Ethan, he's Donovan."

    donovan "Right."

    donovan "So, how long has Chips been missing?"

    wendy "It's not about how long he's been missing, it's about him being scared and hungry."
    
    ethan "Hmmph, Donovan let's find their dog."

    donovan "We can find anything, we can find Chips no problem."

    wendy "Really? You would help us find him?"

    ethan "It's our job, and we do it well. Take us to where you last saw him."

    donna "It's right up here" 

    ethan "So, you guys ready?"

    call screen continue_from_loop
    pause
return