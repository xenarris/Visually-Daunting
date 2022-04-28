label fight_wendy:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/backgrounds/bg lake_event.png"
    show donovan shocked_big_ups at six with dissolve

    show donna in_shock at ten with dissolve
    donovan "I've got a knife, I'm going to fight."

    donovan "Donna, it'll be okay."

    hide donna with dissolve
    show wendy zombie at fourteen with dissolve
    show donovan scared_mad with dissolve

    donovan "Fuck."

    show donovan knife at eight with dissolve

    donovan "Fuck you! Fuck you! Fuck you! FUCK!"

    hide donovan

    hide wendy

    play sound "audio/park/voices/donovan/donovan_attacks.mp3"
    show image "images/park/backgrounds/bg donovan_knife0.png" with dissolve
    pause(3)

    hide image "images/park/backgrounds/bg donovan_knife0.png" with dissolve

    show donovan scared_mad at six with dissolve

    show donna in_shock at ten with dissolve

    donovan "I got it! I did it! We're okay!"

    donovan "Donna...!"

    hide donna with dissolve
    show ethan zombie at fourteen with dissolve

    donovan "Woah, Ethan...bro."
    pause(1)

    show ethan zombie at flip with dissolve

    play sound "audio/park/voices/ethan/ethan_zombie.mp3"
    donovan "BRO, NO!"

    show ethan zombie at ten with dissolve
    pause(.3)

    hide donovan
    hide ethan

    play sound "audio/park/voices/donovan/donovan_bit.mp3"
    show image "images/park/backgrounds/bg donovan_knife1.png" with dissolve
    pause(5)

    jump mods_shut_down_park

return

label help_donna:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    pause(1.4)
    show image "images/park/backgrounds/bg donovan_attack0.png" with dissolve

    show image "images/park/chat/park_endings/parkend_helpDonna1.png" at topright
    donovan "Donna. We need to go.  Come on!"

    show image "images/park/backgrounds/bg donovan_attack1.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_attack0.png"
    pause(1.4)

    hide image "images/park/chat/park_endings/parkend_helpDonna1.png"
    show image "images/park/chat/park_endings/parkend_helpDonna2.png" at topright    
    donovan "Please, get up!"

    show image "images/park/backgrounds/bg donovan_attack2.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_attack1.png"
    pause(1.4)
    hide image "images/park/chat/park_endings/parkend_helpDonna2.png"
    show image "images/park/chat/park_endings/parkend_helpDonna3.png" at topright  
    donovan "Donna..."
    hide image "images/park/backgrounds/bg donovan_attack2.png" with dissolve
    pause(1.5)

    play sound "audio/park/voices/chips/chips_creeps.mp3"
    show image "images/park/backgrounds/bg donovan_attack3.png" with dissolve
    hide image "images/park/chat/park_endings/parkend_helpDonna3.png"
    show image "images/park/chat/park_endings/parkend_helpDonna4.png" at topright  
    pause(3.2)

    hide image "images/park/backgrounds/bg donovan_attack3.png" with dissolve
    pause(1.5)

    show image "images/park/backgrounds/bg donovan_attack4.png" with dissolve
    hide image "images/park/chat/park_endings/parkend_helpDonna4.png"
    show image "images/park/chat/park_endings/parkend_helpDonna5.png" at topright  
    pause(.3)

    show image "images/park/backgrounds/bg donovan_attack5.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_attack4.png"
    pause(.3)

    show image "images/park/backgrounds/bg donovan_attack6.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_attack5.png"
    pause(.3)

    hide image "images/park/chat/park_endings/parkend_helpDonna5.png"
    show image "images/park/chat/park_endings/parkend_helpDonna6.png" at topright 
    show image "images/park/backgrounds/bg donovan_attack7.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_attack6.png"
    pause(.3)

    hide image "images/park/backgrounds/bg donovan_attack7.png" with dissolve
    pause(1.5) 

    play sound "audio/park/voices/donovan/donovan_dies.mp3"
    show image "images/park/backgrounds/bg donovan_attack8.png" with dissolve
    pause(5)
    hide image "images/park/chat/park_endings/parkend_helpDonna6.png"

    
    jump mods_shut_down_park
return


label run_away:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/backgrounds/bg lake_event.png"

    show donovan scared_mad at six with dissolve

    show donna in_shock at ten with dissolve

    donovan "Fuck this, I'm gone!"

    hide donovan
    
    hide donna

    show image "images/park/backgrounds/bg donovan_runs0.png" with dissolve
    pause(1)

    show image "images/park/backgrounds/bg donovan_runs1.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_runs0.png"
    pause(.4)

    show image "images/park/backgrounds/bg donovan_runs2.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_runs1.png"
    pause(.4)

    show image "images/park/backgrounds/bg donovan_runs3.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_runs2.png"
    pause(.4)



    show image "images/park/backgrounds/bg donovan_runs4.png" with dissolve
    pause(.1)
    donovan "Keys."
    hide image "images/park/backgrounds/bg donovan_runs3.png"
    pause(1)

    play sound "audio/park/effects/keys.mp3"

    pause(3)
    show image "images/park/backgrounds/bg donovan_runs5.png" with dissolve
    hide image "images/park/backgrounds/bg donovan_runs4.png"
    pause(2.1)
    
    jump mods_shut_down_park
return

label mods_shut_down_park:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    pause (4)
    show image "images/park/backgrounds/bg stream_offline.png" with dissolve

    "This channel is currently under review.\nAll content is temporarily removed."

    # pauses and then - Umbrae messages again

    pause
return
