label first_chat:

    # Fade in
    scene black
    pause(1)

    #First round of messages
    scene bg wizcord
    show image "park/dms/umbrae0.png"
    pause(.5)
    play sound "audio/new_message.mp3"
    hide image "park/dms/umbrae0.png"
    show image "park/dms/umbrae1.png"
    pause(1.75)
    call screen chat_choice0
    pause

return

label gaming:

    #user
    pause(1)
    hide image "park/dms/umbrae1.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae2.png"
    pause(1.5)
    hide image "park/dms/umbrae2.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae3.png"
    pause(1.5)
    hide image "park/dms/umbrae3.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae4.png"
    pause(2.5)

    #umbrae
    hide image "park/dms/umbrae4.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae5.png"
    pause(1.5)
    hide image "park/dms/umbrae5.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae6.png"
    pause(2.5)
    
    #user
    hide image "park/dms/umbrae6.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae7.png"
    pause(1.5)
    hide image "park/dms/umbrae7.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae8.png"
    pause(1.75)
    hide image "park/dms/umbrae8.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae9.png"
    pause(1.5)

    #umbrae
    hide image "park/dms/umbrae9.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae10.png"
    pause(1.5)
    hide image "park/dms/umbrae10.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae11.png"
    pause(2.5)

    #user
    hide image "park/dms/umbrae11.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae12.png"
    jump join_park_stream
return

label sleeping:

    #user
    pause(1)
    hide image "park/dms/umbrae1.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae13.png"
    pause(1.5)
    hide image "park/dms/umbrae13.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae14.png"
    pause(2)

    #umbrae
    hide image "park/dms/umbrae14.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae15.png"
    pause(1.5)
    hide image "park/dms/umbrae15.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae16.png"
    pause(1.5)
    hide image "park/dms/umbrae16.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae17.png"
    pause(2.5)
    
    #user
    hide image "park/dms/umbrae17.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae18.png"
    pause(1.5)
    hide image "park/dms/umbrae18.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae19.png"
    jump join_park_stream
return

label working:
    #user
    pause(1)
    hide image "park/dms/umbrae1.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae20.png"
    pause(1.5)
    hide image "park/dms/umbrae20.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae21.png"
    pause(1.5)
    hide image "park/dms/umbrae21.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae22.png"
    pause(2)

    #umbrae
    hide image "park/dms/umbrae22.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae23.png"
    pause(2.5)
    
    #user
    hide image "park/dms/umbrae23.png"
    play sound "audio/ur_message.mp3"
    show image "park/dms/umbrae24.png"
    jump join_park_stream
return

# All roads lead here
label join_park_stream:
    pause(3)

    #First round of messages
    hide image "park/dms/umbrae12.png"
    hide image "park/dms/umbrae19.png"
    hide image "park/dms/umbrae24.png"

    scene bg wizcord_stream_ease
    pause(.4)

    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae25.png"
    show image "watch_idle.png"
    pause(1.1)
    hide image "park/dms/umbrae25.png"
    play sound "audio/new_message.mp3"
    show image "park/dms/umbrae26.png"
    call screen stream_join0
    pause

return