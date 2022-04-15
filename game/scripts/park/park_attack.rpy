label park_attack:
    scene green
    show image "images/park/assets/shamz_fwitch.png"

    donna "We lost Chips up this way..."

    donna "He had a lot of anxiety."

    wendy "We took him for training.  He was doing so much better."

    donna "He'd run."

    donovan "Is that why you lost him?"

    donna "We took him for a walk around the lake."

    donna "It's pretty quiet here during winter."

    wendy "You're not allowed to skateboard."

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
    show image "images/park/assets/shamz_fwitch.png"

    wendy "Ch-Chips...?"

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
    show image "images/park/assets/shamz_fwitch.png"

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



