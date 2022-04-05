# To call umbrae chat button
screen chat_nav():
    add "images/park/assets/umbrae_intro_message.png"

    imagebutton auto "message_%s.png":
        focus_mask True
        action Jump("first_chat")
        activate_sound "audio/click.mp3"

# Umbrae first chat Screens
screen chat_choice0():

    imagebutton auto "park/dms/gaming_%s.png":
        focus_mask True
        action Jump("gaming")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/dms/sleeping_%s.png":
        focus_mask True
        action Jump("sleeping")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/dms/working_%s.png":
        focus_mask True
        action Jump("working")
        activate_sound "audio/click.mp3"

# To join first stream
screen stream_join0():
    imagebutton auto "watch_%s.png":
        focus_mask True
        action Jump("park_stream")
        activate_sound "audio/click.mp3"

######################### TUTORIAL ##############################

# Tutorial trial buttons
screen tutorial_0():
    imagebutton auto "park/choices/tutorial/tutorial0_%s.png":
        focus_mask True
        action Jump("tutorial_go_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial1_%s.png":
        focus_mask True
        action Jump("tutorial_hey_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial2_%s.png":
        focus_mask True
        action Jump("tutorial_kekw_choice")
        activate_sound "audio/click.mp3"

screen tutorial_1():
    imagebutton auto "park/choices/tutorial/tutorial3_%s.png":
        focus_mask True
        action Jump("tutorial_ooo_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial4_%s.png":
        focus_mask True
        action Jump("tutorial_yay_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial5_%s.png":
        focus_mask True
        action Jump("tutorial_lets_go_choice")
        activate_sound "audio/click.mp3"

screen tutorial_2():
    imagebutton auto "park/choices/tutorial/tutorial6_%s.png":
        focus_mask True
        action Jump("tutorial_woo_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial7_%s.png":
        focus_mask True
        action Jump("tutorial_smile_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial8_%s.png":
        focus_mask True
        action Jump("tutorial_lets_woah_choice")
        activate_sound "audio/click.mp3"

screen tutorial_3():
    imagebutton auto "park/choices/tutorial/tutorial9_%s.png":
        focus_mask True
        action Jump("tutorial_keysmash_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial10_%s.png":
        focus_mask True
        action Jump("tutorial_zzz_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/tutorial/tutorial11_%s.png":
        focus_mask True
        action Jump("tutorial_lul_choice")
        activate_sound "audio/click.mp3"

######################## PARK ################################

screen park_or_billboard():
    imagebutton auto "park/choices/choice0_%s.png":
        focus_mask True
        action Jump("park_junction_choice")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/choice1_%s.png":
        focus_mask True
        action Jump("park_billboard_choice")
        activate_sound "audio/click.mp3"

screen continue_from_billboard():
    imagebutton auto "park/choices/choice0_%s.png":
        focus_mask True
        action Jump("park_junction")
        activate_sound "audio/click.mp3"

screen lake_or_rec():
    imagebutton auto "park/choices/choice2_%s.png":
        focus_mask True
        action Jump("lake_loop")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/choice3_%s.png":
        focus_mask True
        action Jump("rec_center")
        activate_sound "audio/click.mp3"

screen north_or_east():
    imagebutton auto "park/choices/choice4_%s.png":
        focus_mask True
        action Jump("lake_loop")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/choice5_%s.png":
        focus_mask True
        action Jump("rec_center")
        activate_sound "audio/click.mp3"

screen continue_from_loop():
    imagebutton auto "park/choices/choice0_%s.png":
        focus_mask True
        action Jump("park_attack")
        activate_sound "audio/click.mp3"

screen continue_from_rec():
    imagebutton auto "park/choices/choice0_%s.png":
        focus_mask True
        action Jump("park_attack")
        activate_sound "audio/click.mp3"

screen park_ending():
    imagebutton auto "park/choices/choice6_%s.png":
        focus_mask True
        action Jump("fight_wendy")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/choice7_%s.png":
        focus_mask True
        action Jump("help_donna")
        activate_sound "audio/click.mp3"

    imagebutton auto "park/choices/choice8_%s.png":
        focus_mask True
        action Jump("run_away")
        activate_sound "audio/click.mp3"