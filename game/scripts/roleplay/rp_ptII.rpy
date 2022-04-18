label roleplay_intro:
    scene green

    terry "Welcome to Shiverbrows!"

    terry "The channel where we play weekly campaigns of Gerblins & Ghouls."

    terry "A homebrew RPG with simplified mechanics and fast travel."

    terry "I'm Terry, your Story Weaver (SW) for this evening."

    lenn "I'm Lenn otherwise known as Ryden, Lionborn Paladin!"

    skye "Hey, I'm Skye! A.k.a. Tiefling Assassin Iiria!"

    johnny "Johnny, a Human Fire Mage named Alvie!"

    marlon "Human name, Marlon. Goblin name, Gilbert."

    marlon "Tinkerer with a heart of gold and pocket full of boom!"

    terry "Thanks everyone for the introductions."

    terry "Let's get to it."

    # TODO - Make this into a chat screen w/ multiple options

    jump innkeeper
return

label innkeeper:
    # TODO - Start singular cult chant

    terry "The last we saw our adventurers, they had a close call with some Myconid."

    terry "Poisonous spores caused jagged frills to burst from their bodies."

    terry "Yet knowing of their weakness to light, Gilbert cast his Lantern of Xin."

    terry "Smashing it on the ground, and releasing the spirit within."

    terry "Light filled the cavern. Stunning the fungus, and allowing for escape."

    # TODO - Chat Ooos & Ahs - another strange chant

    terry "Since, they have come across the small town of Faradale."

    terry "As the group recuperates in a dingy tavern, they are approached."

    terry "(???) 'How do, travelers? I see you are weary from battle.'"

    terry "(Kada) 'I am Kada, owner of this tattered establishment.'"

    lenn "(Ryden) 'How do, Kada! Cheerier walls, we've seen. Yet rest comes well!'"

    terry "(Kada) 'Kind words. Of mine I shall not mince! I've come with a request.'"

    terry "(Kada) 'Our village is under attack. Locals lost to unseen captives.'"

    terry "(Kada) 'The forest is alight at night. We have written for help.’”

    terry “(Kada) 'Yet receive none, and are fewer as days pass. Please, help us!'"

    marlon "(Gilbert) 'What's in it for us?'"

    johnny "(Alvie) 'We are weary, we need rest.'"

    skye "(Iiria) 'And supplies, if this is to be a journey!'"

    lenn "(Ryden) 'We will not cheat these people of their meager things.'"

    lenn "(Ryden) 'We shall do it for room and board.'"

    terry "(Kada) 'It is settled, Arkund bring spindleweed ale and spiced pears!'"

    marlon "Ooph! Here we go again."

    terry "Ahem!"

    terry "(Kada) 'Any questions, kind travelers? Before your feast!'"

    # TODO - Multi-split into single question can ask
    pause
return

label tell_light:

    terry "They want the light."
    
    johnny "(Alvie) 'Could you tell us more about the light?'"

    marlon "(Gilbert) 'Do you know if it's containable by nature?'"

    terry "(Kada) 'There is very little we can figure of it.'"

    terry "(Kada) 'It appears sometimes a soft glow, other times a flash!'"

    terry "(Kada) 'Its arrival began with loss of others.'"

    marlon "(Gilbert) 'So, it's containable?'"

    jump start_journey
    pause
return

label tell_missing:

    terry "They want to explore missing people!"

    skye "(Iiria) 'Could you tell, of the ones missing?'"

    skye "(Iiria) 'Perhaps there is a link?'"

    terry "(Kada) 'We did not notice at first.'"

    terry "(Kada) 'Our numbers dwindled, and we became alarmed.'"

    terry "(Kada) 'Last night they took Vruma's daughter as she slept.'"

    terry "(Kada) 'We fear the worse, yet of no link can we form.'"

    jump start_journey
    pause
return

label tell_contacted:

    terry "They want to know who was contacted for help."

    lenn "(Ryden) 'Who turned their backs on such holy a quest?'"

    terry "(Kada) 'Westra Stonar, a Tiefling Ranger and local legend.'"

    terry "(Kada) 'Kethend the Great, a Lizardfolk Wizard who has...'"

    lenn "(Ryden) 'Let the people of this town down.'"

    lenn "(Ryden) 'Let's drink to our soon glory!'"

    jump start_journey
    pause
return

label start_journey:

    terry "(Kada) 'Please, eat well and rest soon.'"

    terry "(Kada) 'We will need you gone before sunset.'"

    marlon "(Gilbert) 'Before sunset? Why so soon?'"

    terry "(Kada) 'We fear another will be taken, if haste is not used.'"

    skye "(Iiria) 'We should rest soon.'"

    johnny "(Alvie) 'I've got some elk jerky if anyone wants some!'"

    marlon "(Gilbert) 'Murph!'"

    lenn "Alright, let's figure this out!"

    #TODO - Strange chant enters again
    # TODO - Split into next scene
    pause
return