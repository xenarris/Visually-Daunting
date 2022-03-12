label first_chat:

    # Fade in
    stop music fadeout 1.0
    scene black
    pause(1)

    #First round of messages
    scene bg wizcord
    show image "park/dms/umbrae0.png"
    pause(.5)
    play sound "audio/message_short.mp3"
    hide image "park/dms/umbrae0.png"
    show image "park/dms/umbrae1.png"
    pause(1.75)
    call screen chat_choice01
    pause

return

label gaming:

    #user
    pause(1)
    hide image "park/dms/umbrae1.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae2.png"
    pause(1.5)
    hide image "park/dms/umbrae2.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae3.png"
    pause(1.5)
    hide image "park/dms/umbrae3.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae4.png"
    pause(2.5)

    #umbrae
    hide image "park/dms/umbrae4.png"
    play sound "audio/message_short.mp3"
    show image "park/dms/umbrae5.png"
    pause(1.5)
    hide image "park/dms/umbrae5.png"
    play sound "audio/message_short.mp3"
    show image "park/dms/umbrae6.png"
    pause(2.5)
    
    #user
    hide image "park/dms/umbrae6.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae7.png"
    pause(1.5)
    hide image "park/dms/umbrae7.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae8.png"
    pause(1.75)
    hide image "park/dms/umbrae8.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae9.png"
    pause(1.5)

    #umbrae
    hide image "park/dms/umbrae9.png"
    play sound "audio/message_short.mp3"
    show image "park/dms/umbrae10.png"
    pause(1.5)
    hide image "park/dms/umbrae10.png"
    play sound "audio/message_short.mp3"
    show image "park/dms/umbrae11.png"
    pause(2.5)

    #user
    hide image "park/dms/umbrae11.png"
    play sound "audio/message_sent.mp3"
    show image "park/dms/umbrae12.png"
    pause(1.5)

    pause
return

label sleeping:
    play sound "audio/message_sent.mp3"
    pause(.5)
    pause(.5)
    pause(.5)
    pause
return

label working:
    play sound "audio/message_sent.mp3"
    pause(.5)
    pause(.5)
    pause(.5)
    pause
return