# To call umbrae chat button
screen chat_nav():
    add "images/park/assets/umbrae_intro_message.png"

    imagebutton auto "message_%s.png":
        focus_mask True
        action Jump("first_chat")
        hovered [ Play("sound", "audio/click.mp3") ]

# Umbrae first chat Screens
screen chat_choice0():

    imagebutton auto "park/dms/gaming_%s.png":
        focus_mask True
        action Jump("gaming")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/dms/sleeping_%s.png":
        focus_mask True
        action Jump("sleeping")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/dms/working_%s.png":
        focus_mask True
        action Jump("working")
        hovered [ Play("sound", "audio/click.mp3") ]

# To join first stream
screen stream_join0():
    imagebutton auto "watch_%s.png":
        focus_mask True
        action Jump("park_stream")
        hovered [ Play("sound", "audio/click.mp3") ]

######################### TUTORIAL ##############################

# Tutorial trial buttons
screen tutorial_0():
    imagebutton auto "park/choices/tutorial/tutorial0_%s.png":
        focus_mask True
        action Jump("tutorial_go_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial1_%s.png":
        focus_mask True
        action Jump("tutorial_hey_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial2_%s.png":
        focus_mask True
        action Jump("tutorial_kekw_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

screen tutorial_1():
    imagebutton auto "park/choices/tutorial/tutorial3_%s.png":
        focus_mask True
        action Jump("tutorial_ooo_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial4_%s.png":
        focus_mask True
        action Jump("tutorial_yay_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial5_%s.png":
        focus_mask True
        action Jump("tutorial_lets_go_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

screen tutorial_2():
    imagebutton auto "park/choices/tutorial/tutorial6_%s.png":
        focus_mask True
        action Jump("tutorial_woo_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial7_%s.png":
        focus_mask True
        action Jump("tutorial_smile_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial8_%s.png":
        focus_mask True
        action Jump("tutorial_lets_woah_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

screen tutorial_3():
    imagebutton auto "park/choices/tutorial/tutorial9_%s.png":
        focus_mask True
        action Jump("tutorial_keysmash_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial10_%s.png":
        focus_mask True
        action Jump("tutorial_zzz_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/tutorial/tutorial11_%s.png":
        focus_mask True
        action Jump("tutorial_lul_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

######################## PARK ################################

screen park_or_billboard():
    imagebutton auto "park/choices/choice0_%s.png":
        focus_mask True
        action Jump("park_junction_choice")
        hovered [ Play("sound", "audio/click.mp3") ]

    imagebutton auto "park/choices/choice1_%s.png":
        focus_mask True
        action Jump("park_billboard_choice")
        hovered [ Play("sound", "audio/click.mp3") ]
