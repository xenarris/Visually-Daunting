label park_attack:
    scene bg lake_event
    show image "images/park/assets/shamz_fwitch.png"

    show donna listening at thirteen with dissolve

    show wendy listening at ten with dissolve

    show donovan listening at flip with dissolve

    show ethan listening at six with dissolve

    donna "We lost Chips up this way..."

    show donna sad with dissolve

    donna "He had a lot of anxiety."

    show wendy big_sad with dissolve

    show ethan sorry with dissolve

    wendy "We got him help! He was doing so much better."

    show donna ashamed with dissolve

    show donna smile at flip with dissolve
    
    donna "He'd run."

    show donovan question with dissolve

    donovan "Is that why you lost him?"

    show donna listening with dissolve

    show donovan listening with dissolve

    donna "We took him for a walk around the lake."

    show donna sad with dissolve

    donna "It's pretty quiet here during winter."

    show wendy cry with dissolve

    wendy "You're not allowed to skateboard."

    show donna upset with dissolve

    donna "Someone came up on us.  The noise from the wheels scared him."

    show wendy big_cry with dissolve

    wendy "I was holding his leash, when he started to pull."

    show donna ashamed_cry with dissolve

    donna "She fell forward, and I went to grab her.  That's when he ran."

    show wendy big_big_cry with dissolve

    show donna cry with dissolve

    wendy "The leash flew from my hand, and we lost him!"

    show donna big_cry with dissolve

    donna "He took off into the woods.  We've been looking ever since."

    show donna big_big_cry with dissolve

    donna "It's been a week.  I can't even believe it."

    show ethan dubious with dissolve

    ethan "A week!? We might be looking for a..."

    show donovan smile with dissolve

    show wendy cry with dissolve

    show donna cry with dissolve

    donovan "Look, E.  Let's make this right. We can find him."

    play sound "audio/park/effects/twigs.mp3"

    show ethan concerned with dissolve

    show donovan question with dissolve

    show donna at flip with dissolve

    show wendy at flip with dissolve

    show wendy confused with dissolve

    show donna surprised with dissolve

    show donovan confused at flip with dissolve

    ethan "What as that?"

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
    show image "images/park/backgrounds/bg chips_appears2.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears1.png"
    pause(1.1)
    show image "images/park/backgrounds/bg chips_appears3.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears2.png"
    pause(2)
    show image "images/park/backgrounds/bg chips_appears4.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears3.png"
    pause(3.4)

    show image "images/park/backgrounds/bg chips_appears1.png" with dissolve
    hide image "images/park/backgrounds/bg chips_appears4.png"
    pause(1)
    hide image "images/park/backgrounds/bg chips_appears1.png"

    show wendy shocked at ten

    show donna big_upset at thirteen

    show donovan scared at three with dissolve

    show ethan scared at six with dissolve

    show wendy shocked at ten with dissolve

    wendy "Ch-Chips...?"

    show donovan at four with dissolve

    show ethan at one with dissolve    

    chips "Rrrrrrrr..."

    show wendy at six with dissolve

    show donna glower at nine with dissolve

    donna "Honey, back up. I...don't think Chips is okay."

    show ethan big_scared with dissolve

    ethan "No, he's not!"

    show wendy happy_cry at eleven with dissolve

    show wendy at eleven with dissolve

    show donna disbelief with dissolve

    wendy "There's my baby! Chips, come on. Let's go home!"

    show wendy happy_big_cry at fifteen with dissolve

    wendy "Chips!"

    show donna at ten with dissolve

    show donovan scared_mad at six with dissolve

    show ethan at two with dissolve

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

    show image "images/park/backgrounds/bg chips_attacks0.png"

    show image "images/park/backgrounds/bg chips_attacks1.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks0.png"
    pause(.2)

    show image "images/park/backgrounds/bg chips_attacks2.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks1.png"
    pause(.2)
    show image "images/park/backgrounds/bg chips_pukes0.png" with dissolve
    hide image "images/park/backgrounds/bg chips_attacks2.png"
    pause(.2)
    
    show image "images/park/backgrounds/bg chips_pukes1.png" with dissolve
    hide image "images/park/backgrounds/bg chips_pukes0.png"
    pause(.2)

    show image "images/park/backgrounds/bg chips_pukes1.png" with dissolve
    hide image "images/park/backgrounds/bg chips_pukes0.png"
    pause(.2)

    show image "images/park/backgrounds/bg chips_pukes2.png" with dissolve
    hide image "images/park/backgrounds/bg chips_pukes1.png"
    pause(.2)

    show image "images/park/backgrounds/bg chips_pukes3.png" with dissolve
    hide image "images/park/backgrounds/bg chips_pukes2.png"
    pause(.2)

    hide image "images/park/backgrounds/bg chips_pukes3.png" with dissolve

    show donna shocked at ten with dissolve

    show donovan shocked at six with dissolve

    show ethan shocked at two with dissolve

    wendy "...ghhhk...ghkk..."

    donovan "Oh fuck, oh fuck!"

    ethan "Oh my god, we have to help!"

    hide ethan

    hide donovan

    hide donna

    show image "images/park/backgrounds/bg wendy_dies0.png"

    show image "images/park/backgrounds/bg wendy_dies1.png" with dissolve
    hide image "images/park/backgrounds/bg wendy_dies0.png"
    pause(.2)

    show image "images/park/backgrounds/bg wendy_dies2.png" with dissolve
    hide image "images/park/backgrounds/bg wendy_dies1.png"
    pause(.2)

    show image "images/park/backgrounds/bg ethan_attack0.png" with dissolve
    hide image "images/park/backgrounds/bg wendy_dies2.png"
    pause(.2)

    show image "images/park/backgrounds/bg ethan_attack1.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_attack0.png"
    pause(.2)

    hide image "images/park/backgrounds/bg ethan_attack1.png" with dissolve

    show ethan after_attack at fourteen with dissolve

    show donovan shocked_big_ups at six with dissolve

    show donna in_shock at ten with dissolve

    show donovan shocked_big at six with dissolve
    pause(.3)

    show donovan shocked_big_ups at six with dissolve

    donovan "Dude, Ethan. Bro. What the fuck!?"

    ethan "Aughhhh! Oh-my-god, oh-my-god. Ughhh...!"

    hide ethan

    hide donovan

    hide donna

    show image "images/park/backgrounds/bg ethan_dies0.png"
    pause(.4)

    show image "images/park/backgrounds/bg ethan_dies1.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_dies0.png"
    pause(1)

    show image "images/park/backgrounds/bg ethan_dies2.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_dies1.png"
    pause(2.5)

    show image "images/park/backgrounds/bg ethan_dies3.png" with dissolve
    hide image "images/park/backgrounds/bg ethan_dies2.png"
    pause(3.5)

    hide image "images/park/backgrounds/bg ethan_dies3.png" with dissolve

    show donovan shocked_big_ups at six with dissolve

    show donna in_shock at ten with dissolve

    show donovan shocked_big at six with dissolve

    donovan "Donna. Donna, come on. We've got to go. Donna. Get up. Fuck!"

    show donovan shocked_big_ups at six with dissolve

    donovan "Fuck man. What the fuck!?"

    show donovan shocked_big_ups at flip with dissolve

    pause(.2)

    show donovan shocked_big at flip_back with dissolve

    pause(.1)

    show donovan shocked_big_ups with dissolve

    donovan "What do I do? What do I do?  Fuck."
    
    show donovan shocked_big at flip_back with dissolve

    call screen park_ending
    pause
return



