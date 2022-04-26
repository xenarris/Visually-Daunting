label start_the_stream: 
    scene bg park_front
    show image "images/park/assets/shamz_fwitch.png"
    show image "images/park/chat/chat5_start_stream.png" at topright
    queue music "audio/park/stream_background.mp3" fadein 1.5
    show donovan forward_smile at ten with dissolve
    pause(.1)
    show ethan forward_wave at five with dissolve
    pause(0.5)

    hide image "images/park/chat/chat5_start_stream.png"
    show image "images/park/chat/chat6.png" at topright

    #play sound "audio/park/snippets/donovan_hello.mp3"
    ethan "Hello, happy viewers!"

    hide image "images/park/chat/chat6.png"
    show image "images/park/chat/chat7.png" at topright

    #play sound "audio/park/snippets/ethan_treat.mp3"
    donovan "Good morning, or evening!  Where ever you are."

    show ethan forward_smile with dissolve
    show donovan forward_big_smile with dissolve
    
    hide image "images/park/chat/chat7.png"
    show image "images/park/chat/chat9.png" at topright

    ethan "We're coming to you guys live from Eureka Springs, Arkansas."

    show donovan forward_smile_alt with dissolve

    hide image "images/park/chat/chat9.png"
    show image "images/park/chat/chat10.png" at topright

    donovan "Not a location we typically visit."

    show donovan forward_upset_alt with dissolve
    show ethan forward_sad with dissolve

    donovan "Especially considering that mushrooms are a controlled substance here."

    hide image "images/park/chat/chat10.png"
    show image "images/park/chat/chat12.png" at topright

    show ethan thinking with dissolve

    ethan "A Class C felony, even for harvesting."

    show donovan forward_big_smile_alt with dissolve
    donovan "Don't worry you guys, we're not after anything illegal here."

    hide image "images/park/chat/chat12.png"
    show image "images/park/chat/chat14.png" at topright

    show ethan cheeky with dissolve
    show donovan forward_smile_alt with dissolve

    ethan "We found a loophole!"


    hide image "images/park/chat/chat14.png"
    show image "images/park/chat/chat15.png" at topright

    ##### TODO - Streamline this #####
    ##### Dondation animation #####
    show image "images/park/assets/rainbow_donation3.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation3.png"
    show image "images/park/assets/rainbow_donation4.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation4.png"
    show image "images/park/assets/rainbow_donation5.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation5.png"
    show image "images/park/assets/rainbow_donation4.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation4.png"
    show image "images/park/assets/rainbow_donation3.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation3.png"
    show image "images/park/assets/rainbow_donation3.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation3.png"
    show image "images/park/assets/rainbow_donation4.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation4.png"
    show image "images/park/assets/rainbow_donation5.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation5.png"
    show image "images/park/assets/rainbow_donation4.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation4.png"
    show image "images/park/assets/rainbow_donation3.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation3.png"
    show image "images/park/assets/rainbow_donation3.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation3.png"
    show image "images/park/assets/rainbow_donation4.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation4.png"
    show image "images/park/assets/rainbow_donation5.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation5.png"
    show image "images/park/assets/rainbow_donation4.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation4.png"
    show image "images/park/assets/rainbow_donation3.png"
    pause(.1)

    hide image "images/park/assets/rainbow_donation3.png"

    #### Donation image ends #####

    show ethan forward_smile with dissolve
    show donovan forward_big_smile_alt with dissolve

    ethan "Knew you would like that."



    hide image "images/park/chat/chat15.png"
    show image "images/park/chat/chat16_ricitoxy.png" at topright

    donovan "We got a tip from user ricitioxy on how local psychonauts survive such harsh climates."

    
    ##### TODO - add more chats here ####

    show ethan explains with dissolve
    show donovan forward_big_smile with dissolve

    ethan "For those who don't grow, there's some wild foraging at hand."
    ethan "Arkansas' mild winters lead to excellent fruiting."

    hide image "images/park/chat/chat16_ricitoxy.png"
    show image "images/park/chat/chat13.png" at topright


    show ethan forward_smile with dissolve
    show donovan forward_smile_alt with dissolve

    ethan "And while harvesting mushrooms is illegal, harvesting what comes out isn't."

    hide image "images/park/chat/chat13.png"
    show image "images/park/chat/chat11.png" at topright

    
    hide image "images/park/chat/chat11.png"
    show image "images/park/chat/chat8.png" at topright

    show ethan explains with dissolve
    show donovan forward_big_smile_alt with dissolve

    #play sound "audio/park/snippets/ethan_devils_tooth.mp3"
    ethan "Tonight we're searching for Hydnellum Peckii, a.k.a. the 'Devil's Tooth.'"

    show ethan forward_smile with dissolve
    show donovan forward_smile_alt with dissolve

    donovan "A cream colored mushroom with a short body and a wide cap, that's flat on top."
    donovan "A cap peppered with a series of red dots."

    hide image "images/park/chat/chat8.png"
    show image "images/park/chat/chat17.png" at topright

    ethan "And those dots are why we're here tonight! We've come to harvest the 'Devil's Berry!'"

    show donovan forward_big_smile_alt with dissolve

    donovan "So, should we start?"

    hide image "images/park/chat/chat17.png"
    show image "images/park/chat/chat18_choose0.png" at topright

    ethan "So...into the park, or check out that billboard?"

    call screen park_or_billboard
    pause
return

label park_junction_choice:
    $ seen_bulletin = False

    show donovan forward_big_smile with dissolve
    donovan "Alright folks...let's do this!"
    show ethan explains with dissolve
    ethan "Lets!"

    hide donovan with dissolve
    hide ethan with dissolve

    pause (1)
    jump park_junction
return

label park_billboard_choice:
    show donovan forward_smile_alt with dissolve
    donovan "You guys want us to check the billboard?"
    show ethan explains with dissolve
    show donovan forward_big_smile_alt with dissolve
    donovan "Done!"

    hide ethan with dissolve
    pause(.3)
    hide donovan with dissolve

    pause(.5)

    jump park_billboard
return
