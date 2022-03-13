# To call umbrae chat button
screen chat_nav():
    add "images/park/assets/umbrae_intro_message.png"

    imagebutton auto "message_%s.png":
        focus_mask True
        action Jump("first_chat")

# Umbrae first chat Screens
screen chat_choice0():

    imagebutton auto "park/dms/gaming_%s.png":
        focus_mask True
        action Jump("gaming")

    imagebutton auto "park/dms/sleeping_%s.png":
        focus_mask True
        action Jump("sleeping")

    imagebutton auto "park/dms/working_%s.png":
        focus_mask True
        action Jump("working")

# To join first stream
screen stream_join0():
    imagebutton auto "watch_%s.png":
        focus_mask True
        action Jump("park_stream")

# Tutorial trial buttons
screen tutorial_0():
    imagebutton auto "park/tutorial/tutorial0_%s.png":
        focus_mask True
        action Jump("tutorial_go_choice")

    imagebutton auto "park/tutorial/tutorial1_%s.png":
        focus_mask True
        action Jump("tutorial_hey_choice")

    imagebutton auto "park/tutorial/tutorial2_%s.png":
        focus_mask True
        action Jump("tutorial_kekw_choice")

screen tutorial_1():
    imagebutton auto "park/tutorial/tutorial3_%s.png":
        focus_mask True
        action Jump("tutorial_ooo_choice")

    imagebutton auto "park/tutorial/tutorial4_%s.png":
        focus_mask True
        action Jump("tutorial_yay_choice")

    imagebutton auto "park/tutorial/tutorial5_%s.png":
        focus_mask True
        action Jump("tutorial_lets_go_choice")

screen tutorial_2():
    imagebutton auto "park/tutorial/tutorial6_%s.png":
        focus_mask True
        action Jump("tutorial_woo_choice")

    imagebutton auto "park/tutorial/tutorial7_%s.png":
        focus_mask True
        action Jump("tutorial_smile_choice")

    imagebutton auto "park/tutorial/tutorial8_%s.png":
        focus_mask True
        action Jump("tutorial_lets_woah_choice")

screen tutorial_3():
    imagebutton auto "park/tutorial/tutorial9_%s.png":
        focus_mask True
        action Jump("tutorial_keysmash_choice")

    imagebutton auto "park/tutorial/tutorial10_%s.png":
        focus_mask True
        action Jump("tutorial_zzz_choice")

    imagebutton auto "park/tutorial/tutorial11_%s.png":
        focus_mask True
        action Jump("tutorial_lul_choice")
