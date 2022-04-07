label park_attack:
    scene bg park_blank

    show image "images/park/assets/shamz_fwitch.png"

    show donovan listening at flip with dissolve
    # pause(1)
    show ethan listening at two with dissolve
    # pause(1)

    show donna listening at fourteen with dissolve
    show wendy intrigued at ten with dissolve

    donna "We lost Chips up this way..."

    show donna listening at flip with dissolve
    show wendy intrigued at flip with dissolve

    show donovan listening at six with dissolve
    show ethan listening at three with dissolve

    donna "He had a lot of anxiety."

    show wendy smile with dissolve
    show ethan smile with dissolve
    show donovan smile with dissolve

    wendy "We took him for training.  He was doing so much better."

    show donna smile at flip with dissolve
    
    donna "He'd run."

    show donovan upset with dissolve

    donovan "Is that why you lost him?"

    show ethan listening with dissolve
    show donovan listening with dissolve
    show donna listening with dissolve

    donna "We took him for a walk around the lake."

    donna "It's pretty quiet here during winter."

    show wendy listening with dissolve

    wendy "You're not allowed to skateboard."

    show donna dubious with dissolve

    donna "Someone came up on us.  The noise from the wheels scared him."

    wendy "I was holding his leash, when he started to pull."

    donna "She fell forward, and I went to grab her.  That's when he ran."

    wendy "The leash flew from my hand, and we lost him!"

    donna "He took off into the woods.  We've been looking ever since."

    donna "It's been a week.  I can't even believe it."

    ethan "A week...we might be looking for a..."

    donovan "Look, I don't know what we'll find but let's set this right."

    jump chips_appears
    pause
return

label chips_appears:

    show wendy shocked at ten with dissolve

    wendy "Ch-Chips...?"

    hide donovan with dissolve
    hide ethan with dissolve
    hide wendy with dissolve
    hide donna with dissolve

    show bg chips_appears0 with dissolve
    
    chips "Rrrrrrrr..."

    donna "Wendy, I-I-I-I..."

    donna "I-I don't think Chips is alright."

    ethan "No, he's not!"

    wendy "Chips, baby. Come here. Come on. We've got you. Come!"

    wendy "Chips!"

    donovan "Woah...!"

    stop music fadeout 3
    play music "audio/park/park_attack.mp3" fadein 3
    jump chips_attacks
return

label chips_attacks:

    wendy "...ghhhk...ghkk..."

    donovan "Oh fuck, oh fuck!"

    ethan "Oh my god, we have to help!"

    wendy "Rrrraeeee!"

    ethan "Aughhhh! Oh-my-god, oh-my-god. What the fuck! Ughhh..."

    donovan "Dude, Ethan. Bro. What? Fuck!"

    donovan "Donna. Donna, come on. We've got to go. Donna. Get up. Fuck!"

    donovan "Fuck man. What the fuck!?"

    donovan "What do I do? What do I do?  Fuck."

    call screen park_ending
    pause
return



