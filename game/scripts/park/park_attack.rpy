label park_attack:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/chat/chat_find_chips.png" at topright

    if went_lakeside == True:
        show image "images/park/backgrounds/bg lake_loop_transition2.png" with dissolve
        pause(.4)
        hide image "images/park/backgrounds/bg lake_loop_transition2.png"
        show image "images/park/backgrounds/bg lake_loop_transition3.png" with dissolve
        pause(.4)
        hide image "images/park/backgrounds/bg lake_loop_transition3.png"  with dissolve
        pause(.5)

    else:
        show image "images/park/backgrounds/bg rec_center_transition0.png" with dissolve
        pause(.4)
        hide image "images/park/backgrounds/bg rec_center_transition0.png"
        show image "images/park/backgrounds/bg rec_center_transition1.png" with dissolve
        pause(.4)
        hide image "images/park/backgrounds/bg rec_center_transition1.png"  with dissolve
        pause(.5)

    show image "images/park/backgrounds/bg lake_event.png" with dissolve

    pause(1)

    hide image "images/park/chat/chat_find_chips.png" 

    show image "images/park/assets/shamz_fwitch.png"

    show donna listening at thirteen with dissolve

    show wendy listening at ten with dissolve

    show donovan listening at three with dissolve

    show ethan listening at six with dissolve

    show image "images/park/chat/park_attack/pa_chat1.png" at topright
    donna "We lost Chips up this way..."

    show donna sad with dissolve

    donna "He had a lot of anxiety."

    show wendy big_sad with dissolve

    show ethan sorry with dissolve

    hide image "images/park/chat/park_attack/pa_chat1.png"
    show image "images/park/chat/park_attack/pa_chat2.png" at topright
    play sound "audio/park/voices/wendy/wendy_specialist.mp3"
    wendy "We got him help! He was doing so much better."

    show donna ashamed with dissolve

    hide image "images/park/chat/park_attack/pa_chat2.png"
    show image "images/park/chat/park_attack/pa_chat3.png" at topright
    donna "He'd run."

    show donovan question with dissolve

    donovan "Is that why you lost him?"

    show donna listening with dissolve

    hide image "images/park/chat/park_attack/pa_chat3.png"
    show image "images/park/chat/park_attack/pa_chat4.png" at topright
    show donovan listening with dissolve

    donna "We took him for a walk around the lake."

    show donna sad with dissolve

    donna "It's pretty quiet here during winter."

    show wendy cry with dissolve

    hide image "images/park/chat/park_attack/pa_chat4.png"
    show image "images/park/chat/park_attack/pa_chat5.png" at topright
    wendy "You're not allowed to skateboard."

    show donna upset with dissolve

    play sound "audio/park/voices/donna/donna_scared.mp3"
    donna "Someone came up on us.  The noise from the wheels scared him."

    show wendy big_cry with dissolve

    hide image "images/park/chat/park_attack/pa_chat5.png"
    show image "images/park/chat/park_attack/pa_chat6.png" at topright
    wendy "I was holding his leash, when he started to pull."

    show donna ashamed_cry with dissolve

    donna "She fell forward, and I went to grab her.  That's when he ran."

    show wendy big_big_cry with dissolve

    hide image "images/park/chat/park_attack/pa_chat6.png"
    show image "images/park/chat/park_attack/pa_chat7.png" at topright
    show donna cry with dissolve

    play sound "audio/park/voices/wendy/wendy_stop.mp3"
    wendy "The leash flew from my hand, and we lost him!"

    show donna big_cry with dissolve

    play sound "audio/park/voices/donna/donna_looked.mp3"
    donna "He took off into the woods.  We've been looking ever since."

    show donna big_big_cry with dissolve

    hide image "images/park/chat/park_attack/pa_chat7.png"
    show image "images/park/chat/park_attack/pa_chat8.png" at topright
    donna "It's been a week.  I can't even believe it."

    show ethan dubious with dissolve

    play sound "audio/park/voices/ethan/ethan_sass.mp3"
    ethan "A week!? We might be looking for a uhhh...!"

    show donovan smile with dissolve

    show wendy cry with dissolve

    show donna cry with dissolve

    hide image "images/park/chat/park_attack/pa_chat8.png"
    show image "images/park/chat/park_attack/pa_chat9.png" at topright
    donovan "Look, E.  Let's make this right. We can find him."

    play sound "audio/park/effects/twigs.mp3"

    show ethan concerned with dissolve

    show donovan question with dissolve

    show donna at flip with dissolve

    show wendy at flip with dissolve

    show wendy confused with dissolve

    show donna surprised with dissolve

    show donovan confused with dissolve

    hide image "images/park/chat/park_attack/pa_chat9.png"
    show image "images/park/chat/park_attack/pa_chat10.png" at topright
    ethan "What was that?"

    hide ethan

    hide donovan

    hide donna

    hide wendy

    jump chips_appears
    pause
return

label chips_appears:
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/backgrounds/bg chips_appears0.png"
    pause (.2)

    show image "images/park/backgrounds/bg chips_appears1.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears0.png"
    pause (.2)

    hide image "images/park/chat/park_attack/pa_chat10.png"
    show image "images/park/chat/park_attack/pa_chat11.png" at topright
    show image "images/park/backgrounds/bg chips_appears2.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears1.png"
    pause(1.1)

    hide image "images/park/chat/park_attack/pa_chat11.png"
    show image "images/park/chat/park_attack/pa_chat12.png" at topright
    show image "images/park/backgrounds/bg chips_appears3.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears2.png"
    pause(2)
    play sound "audio/park/voices/chips/chips_growl.mp3"
    show image "images/park/backgrounds/bg chips_appears4.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears3.png"
    pause(3.4)

    hide image "images/park/chat/park_attack/pa_chat12.png"
    show image "images/park/chat/park_attack/pa_chat13.png" at topright
    hide image "images/park/backgrounds/bg chips_appears4.png" with dissolve

    show wendy shocked at ten

    show donna big_upset at thirteen

    show ethan scared at six with dissolve
    
    show donovan scared at three with dissolve

    
    play sound "audio/park/voices/wendy/wendy_chips.mp3"
    wendy "Ch-Chips...?"

    hide image "images/park/chat/park_attack/pa_chat13.png"
    show image "images/park/chat/park_attack/pa_chat14.png" at topright
    show donovan at four with dissolve

    show ethan at one with dissolve    

    play sound "audio/park/voices/chips/chips_angry.mp3"
    chips "Rrrrrrrr..."

    show wendy at six with dissolve

    hide image "images/park/chat/park_attack/pa_chat14.png"
    show image "images/park/chat/park_attack/pa_chat15.png" at topright
    show donna glower at nine with dissolve

    donna "Honey, back up. I...don't think Chips is okay."

    show ethan big_scared with dissolve

    ethan "No, he's not!"

    hide image "images/park/chat/park_attack/pa_chat15.png"
    show image "images/park/chat/park_attack/pa_chat16.png" at topright
    show wendy happy_cry at eleven with dissolve

    show wendy at eleven with dissolve

    show donna disbelief with dissolve

    play sound "audio/park/voices/wendy/wendy_come.mp3"
    wendy "There's my baby! Chips, come on. Let's go home!"
    hide image "images/park/chat/park_attack/pa_chat16.png"
    show image "images/park/chat/park_attack/pa_chat17.png" at topright

    show wendy happy_big_cry at fifteen with dissolve

    play sound "audio/park/voices/wendy/wendy_calls.mp3"
    wendy "Chips!"

    show donna at ten with dissolve

    show donovan scared_mad at six with dissolve

    hide image "images/park/chat/park_attack/pa_chat17.png"
    show image "images/park/chat/park_attack/pa_chat18.png" at topright
    show ethan at two with dissolve

    play sound "audio/park/voices/donovan/donovan_woah.mp3"
    donovan "Woah...!"

    hide ethan

    hide donovan

    hide donna

    hide wendy

    stop music fadeout 3
    play music "audio/park/park_attack.mp3" fadein 3
    jump chips_attacks
return

label chips_attacks:
    show image "images/park/assets/shamz_fwitch.png"

    hide image "images/park/chat/park_attack/pa_chat18.png"
    show image "images/park/chat/park_attack/pa_chat19.png" at topright
    play sound "audio/park/voices/chips/chips_lunges.mp3"
    show image "images/park/backgrounds/bg chips_attacks0.png"
    pause(2)

    show image "images/park/backgrounds/bg chips_attacks1.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks0.png"
    pause(1.4)

    hide image "images/park/chat/park_attack/pa_chat19.png"
    show image "images/park/chat/park_attack/pa_chat20.png" at topright
    play sound "audio/park/voices/chips/chips_before_spew.mp3"
    show image "images/park/backgrounds/bg chips_attacks2.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks1.png"
    pause(1.3)


    play sound "audio/park/voices/chips/chips_spews.mp3"
    show image "images/park/backgrounds/bg chips_attacks3.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks2.png"
    pause(3)
    
    play sound "audio/park/voices/chips/chips_breathes.mp3"
    show image "images/park/backgrounds/bg chips_attacks4.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks3.png"
    pause(3)

    hide image "images/park/backgrounds/bg chips_attacks4.png" with dissolve
    pause(1)

    show donna shocked at ten with dissolve

    show donovan shocked at six with dissolve
    hide image "images/park/chat/park_attack/pa_chat20.png"
    show image "images/park/chat/park_attack/pa_chat21.png" at topright

    show ethan shocked at two with dissolve

    play sound "audio/park/voices/wendy/wendy_suffers.mp3"
    wendy "...ghhhk...ghkk..."

    play sound "audio/park/voices/donovan/donovan_freaks.mp3"
    donovan "Oh fuck, oh fuck!"

    hide image "images/park/chat/park_attack/pa_chat21.png"
    show image "images/park/chat/park_attack/pa_chat22.png" at topright
    play sound "audio/park/voices/ethan/ethan_shocked.mp3"
    ethan "Oh my god, we have to help!"


    hide ethan with dissolve
    pause(1)

    hide donna

    hide donovan


    show image "images/park/backgrounds/bg wendy_dies0.png"
    pause(3)

    hide image "images/park/chat/park_attack/pa_chat22.png"
    show image "images/park/chat/park_attack/pa_chat23.png" at topright
    show image "images/park/backgrounds/bg wendy_dies1.png" with dissolve
    hide image "images/park/backgrounds/bg wendy_dies0.png"
    pause(1)

    play sound "audio/park/voices/wendy/wendy_chokes.mp3" 
    show image "images/park/backgrounds/bg wendy_dies2.png" with dissolve
    hide image "images/park/backgrounds/bg wendy_dies1.png"
    pause(2)
    hide image "images/park/chat/park_attack/pa_chat23.png"
    show image "images/park/chat/park_attack/pa_chat24.png" at topright


    play sound "audio/park/voices/ethan/ethan_attacked.mp3" 
    show image "images/park/backgrounds/bg ethan_attack0.png" with dissolve
    hide image "images/park/backgrounds/bg wendy_dies2.png"
    pause(3)

    show image "images/park/backgrounds/bg ethan_attack1.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_attack0.png"
    pause(3)

    hide image "images/park/backgrounds/bg ethan_attack1.png" with dissolve

    show ethan after_attack at thirteen with dissolve

    show donovan shocked_big_ups at six with dissolve

    show donna in_shock at ten with dissolve

    show donovan shocked_big at six with dissolve
    pause(.3)

    hide image "images/park/chat/park_attack/pa_chat24.png"
    show image "images/park/chat/park_attack/pa_chat25.png" at topright
    show donovan shocked_big_ups at six with dissolve

   
    play sound "audio/park/voices/donovan/donovan_disbelief.mp3" 
    donovan "Dude, Ethan. Bro. What the fuck!?"

    ethan "Aughhhh! Oh-my-god, oh-my-god. Ughhh...!"

    hide ethan

    hide donovan

    hide donna

    show image "images/park/backgrounds/bg ethan_dies0.png"
    pause(1)

    show image "images/park/backgrounds/bg ethan_dies1.png" with dissolve
    hide image "images/park/chat/park_attack/pa_chat25.png"
    show image "images/park/chat/park_attack/pa_chat26.png" at topright
    hide image "images/park/backgrounds/bg ethan_dies0.png"
    pause(1)

    play sound "audio/park/voices/ethan/ethan_dies.mp3" 
    
    show image "images/park/backgrounds/bg ethan_dies2.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_dies1.png"
    pause(3)

    play sound "audio/park/effects/hits_ground.mp3"
    hide image "images/park/chat/park_attack/pa_chat26.png"
    show image "images/park/chat/park_attack/pa_chat27.png" at topright 
    show image "images/park/backgrounds/bg ethan_dies3.png"
    hide image "images/park/backgrounds/bg ethan_dies2.png"
    pause(1)

    play sound "audio/park/voices/wendy/wendy_eats.mp3"
    show image "images/park/backgrounds/bg ethan_dies4.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_dies3.png"
    pause(3)

    hide image "images/park/backgrounds/bg ethan_dies4.png" with dissolve

    show donovan shocked_big_ups at six with dissolve

    show donna in_shock at ten with dissolve

    show donovan shocked_big at six with dissolve

    hide image "images/park/chat/park_attack/pa_chat27.png"
    show image "images/park/chat/park_attack/pa_chat28.png" at topright 
    play sound "audio/park/voices/donovan/donovan_come_on.mp3" 
    donovan "Donna. Donna, come on. We've got to go. Donna. Get up. Fuck!"

    show donovan shocked_big_ups at six with dissolve

    donovan "Fuck man. What the fuck!?"

    show donovan shocked_big_ups at flip with dissolve

    pause(.2)

    hide image "images/park/chat/park_attack/pa_chat28.png"
    show image "images/park/chat/park_attack/pa_chat29.png" at topright 
    show donovan shocked_big at flip_back with dissolve

    pause(.1)

    show donovan shocked_big_ups with dissolve

    play sound "audio/park/voices/donovan/donovan_upset.mp3" 
    donovan "What do I do? What do I do?  Fuck."
    hide image "images/park/chat/park_attack/pa_chat29.png"
    show image "images/park/chat/park_attack/pa_chat30.png" at topright 
    
    show donovan shocked_big at flip_back with dissolve

    call screen park_ending
    pause
return



