label fight_wendy:
    scene blue
    show image "images/park/assets/shamz_fwitch.png"

    donovan "I've got a knife, I'm going to fight."

    donovan "Donna, it'll be okay."

    donovan "Fuck."

    donovan "Fuck you! Fuck you! Fuck you! FUCK!"

    donovan "I got it! I did it! We're okay!"

    donovan "Donna...!"

    donovan "Woah, Ethan...bro."

    donovan "BRO, NO!"

    #Ethan kills Donovan here

    jump mods_shut_down_park

return

label help_donna:
    scene green
    show image "images/park/assets/shamz_fwitch.png"

    donovan "Donna. We need to go.  Come on!"

    donovan "Please, get up!"

    donovan "Donna..."

    #Chips sneaks up and kills donovan camera falls and shows his demise
    
    jump mods_shut_down_park
return


label run_away:
    scene white
    show image "images/park/assets/shamz_fwitch.png"

    donovan "Fuck this, I'm gone!"

    donovan "Ethan, fuck!"

    donovan "Keys."

    #As messing with keys shadow appears in background
    
    jump mods_shut_down_park
return

label mods_shut_down_park:
    scene purple
    show image "images/park/assets/shamz_fwitch.png"

    "This channel is currently under review.\nAll content is temporarily removed."

    # pauses and then - Umbrae messages again

    pause
return
