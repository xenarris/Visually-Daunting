### TODO - PUT IN CHATS LATER ###

label park_billboard:
    $ seen_bulletin = True

    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/chat/billboard/bbchat1_donovan.png" at topright
    show image "images/park/backgrounds/bg billboard_transition0.png" with dissolve
    pause(.4)
    hide image "images/park/backgrounds/bg billboard_transition0.png"
    show image "images/park/backgrounds/bg billboard_transition1.png" with dissolve
    pause(.4)
    hide image "images/park/backgrounds/bg billboard_transition1.png"  with dissolve
    pause(.5)
    show image "images/park/backgrounds/bg billboard.png" with dissolve

    pause(1)
    donovan "Let's check this out."

    play sound "audio/park/voices/ethan/ethan_aww.mp3"
    hide image "images/park/chat/billboard/bbchat1_donovan.png"
    show image "images/park/chat/billboard/bbchat2_ethan.png" at topright
    ethan "Aww, there's a little missing dog.  Sad."

    #show image "images/park/chat/chat6.png" at topright

    donovan "Bro, this park was established 1915.  Woah!"

    donovan "Check out this map."

    hide image "images/park/chat/billboard/bbchat2_ethan.png"
    show image "images/park/chat/billboard/bbchat3_donovan.png" at topright
    donovan "The lake is to the North of here."

    donovan "Eagle Point is a little further up. Connected to this side trail here."

    hide image "images/park/chat/billboard/bbchat3_donovan.png"
    show image "images/park/chat/billboard/bbchat4_ethan.png" at topright
    ethan "There's also a little recreational space to the East.  With some benches and a stage."

    donovan "We should probably memorize this, so that we don't get lost."

    hide image "images/park/chat/billboard/bbchat4_ethan.png"
    show image "images/park/chat/billboard/bbchat5_ethan.png" at topright
    ethan "I've got you, I'll take a picture."

    pause(.3)
    play sound "audio/park/effects/camera.mp3"
    show image "images/park/backgrounds/bg billboard_snap.png"
    pause(1.1)
    hide image "images/park/backgrounds/bg billboard_snap.png" with dissolve
    show image "images/park/backgrounds/bg billboard.png" with dissolve

    pause(1)
    hide image "images/park/chat/billboard/bbchat5_ethan.png"
    show image "images/park/chat/billboard/bbchat6_ethan.png" at topright
    ethan "Got it!"
    donovan "Alright, let's go!"

    call screen continue_from_billboard
    pause
return