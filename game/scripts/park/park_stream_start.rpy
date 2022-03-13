# Beginning of the Act I Stream
# This is a tutorial to demo
label park_stream:
    stop music fadeout 1.0
    scene black
    show image "images/park/assets/fwitch_tutorial_overlay_explanation.png" with dissolve
    pause(5)
    scene black with dissolve


    scene bg stream_fade with fade
    play music "audio/park/stream_upbeat_loading.mp3" fadein 1.0
    scene bg stream_starting
    show image "images/park/assets/shamz_fwitch_choice.png"
    show image "images/park/chat/chat0.png" at topright



    call screen tutorial_0
    pause
return

# Tutorial 1
label tutorial_go_choice:
    hide image "images/park/chat/chat0.png"
    show image "images/park/chat/chat1.png" at topright
    show image "images/park/chat/user/user0.png" at topright

    call screen tutorial_1
    pause
return

label tutorial_hey_choice:
    hide image "images/park/chat/chat0.png"
    show image "images/park/chat/chat1.png" at topright
    show image "images/park/chat/user/user1.png" at topright

    call screen tutorial_1
    pause
return

label tutorial_kekw_choice:
    hide image "images/park/chat/chat0.png"
    show image "images/park/chat/chat1.png" at topright
    show image "images/park/chat/user/user2.png" at topright

    call screen tutorial_1
    pause
return

# Tutorial 2
label tutorial_ooo_choice:
    hide image "images/park/chat/chat1.png"
    hide image "images/park/chat/user/user0.png"
    hide image "images/park/chat/user/user1.png"
    hide image "images/park/chat/user/user2.png"

    show image "images/park/chat/chat2.png" at topright
    show image "images/park/chat/user/user3.png" at topright
    
    call screen tutorial_2
    pause
return

label tutorial_yay_choice:
    hide image "images/park/chat/chat1.png"
    hide image "images/park/chat/user/user0.png"
    hide image "images/park/chat/user/user1.png"
    hide image "images/park/chat/user/user2.png"

    show image "images/park/chat/chat2.png" at topright
    show image "images/park/chat/user/user4.png" at topright

    
    call screen tutorial_2
    pause
return

label tutorial_lets_go_choice:
    hide image "images/park/chat/chat1.png"
    hide image "images/park/chat/user/user0.png"
    hide image "images/park/chat/user/user1.png"
    hide image "images/park/chat/user/user2.png"

    show image "images/park/chat/chat2.png" at topright
    show image "images/park/chat/user/user5.png" at topright

    call screen tutorial_2
    pause
return

# Tutorial 3
label tutorial_woo_choice:
    hide image "images/park/chat/chat2.png"
    hide image "images/park/chat/user/user3.png"
    hide image "images/park/chat/user/user4.png"
    hide image "images/park/chat/user/user5.png"

    show image "images/park/chat/chat3.png" at topright
    show image "images/park/chat/user/user6.png" at topright

    call screen tutorial_3
    pause
return

label tutorial_smile_choice:
    hide image "images/park/chat/chat2.png"
    hide image "images/park/chat/user/user3.png"
    hide image "images/park/chat/user/user4.png"
    hide image "images/park/chat/user/user5.png"

    show image "images/park/chat/chat3.png" at topright
    show image "images/park/chat/user/user7.png" at topright

    call screen tutorial_3
    pause
return

label tutorial_lets_woah_choice:
    hide image "images/park/chat/chat2.png"
    hide image "images/park/chat/user/user3.png"
    hide image "images/park/chat/user/user4.png"
    hide image "images/park/chat/user/user5.png"

    show image "images/park/chat/chat3.png" at topright
    show image "images/park/chat/user/user8.png" at topright

    call screen tutorial_3
    pause
return

# Final Tutorial
label tutorial_keysmash_choice:
    hide image "images/park/chat/chat3.png"
    hide image "images/park/chat/user/user6.png"
    hide image "images/park/chat/user/user7.png"
    hide image "images/park/chat/user/user8.png"

    hide image "images/park/assets/shamz_fwitch_choice.png"
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/chat/chat4.png" at topright
    show image "images/park/chat/user/user9.png" at topright
    
    scene bg fade_out with dissolve
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/chat/chat4.png" at topright
    show image "images/park/chat/user/user9.png" at topright
    pause(3)
    jump tutorial_end
return

label tutorial_zzz_choice:
    hide image "images/park/chat/chat3.png"
    hide image "images/park/chat/user/user6.png"
    hide image "images/park/chat/user/user7.png"
    hide image "images/park/chat/user/user8.png"

    hide image "images/park/assets/shamz_fwitch_choice.png"
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/chat/chat4.png" at topright
    show image "images/park/chat/user/user10.png" at topright
    
    scene bg fade_out with dissolve
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/chat/chat4.png" at topright
    show image "images/park/chat/user/user10.png" at topright
    pause(3)
    jump tutorial_end
return

label tutorial_lul_choice:
    hide image "images/park/chat/chat3.png"
    hide image "images/park/chat/user/user6.png"
    hide image "images/park/chat/user/user7.png"
    hide image "images/park/chat/user/user8.png"

    hide image "images/park/assets/shamz_fwitch_choice.png"
    show image "images/park/assets/shamz_fwitch.png"

    show image "images/park/chat/chat4.png" at topright
    show image "images/park/chat/user/user11.png" at topright

    scene bg fade_out with irisout
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/chat/chat4.png" at topright
    show image "images/park/chat/user/user11.png" at topright
    pause(2)
    jump tutorial_end
return

label tutorial_end:
    stop music fadeout 1.0
    scene bg stream_switch
    scene bg park_front
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/chat/chat5_start_stream.png" at topright
    pause
return