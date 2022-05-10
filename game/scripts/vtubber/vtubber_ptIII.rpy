label vtubber_silent:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    morrigu "Silence is not an option."

    # Head over to "trapped" ending

    pause
return

label vtubber_no:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    # Put a lot of angry chatter here
    pause(1)
    # more angry chats
    pause(1)
    # more here...
    pause(1)

    # all chats from here on out will just say Fiant tenebrae!

    morrigu "Silence! Such chatter. That's better!"

    morrigu "You say 'no,' yet you are already cursed."

    morrigu "Once cursed, never removed."

    morrigu "If you'll not join us, you will feed us!"

    # Scoot to cursed ending

    pause
return

label vtubber_join:
    scene bg park_blank
    show image "images/park/assets/shamz_fwitch.png"

    morrigu "How wonderful!"

    morrigu "Go show your conviction. Make it bloody."

    morrigu "We're watching!"

    # Scoot to join ending

    pause
return