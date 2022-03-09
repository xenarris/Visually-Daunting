# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define dono = Character("Donovan:")
define ethan = Character("Ethan:")
define wendy = Character("Wendy:")
define donna = Character("Donna:")
define chat = Character("Chat:")
define unknown = Character("???:")
define chips = Character("Chips:")

#Initialize things here 
#(Ren'py reads everything as a giant file according to the internet)
init:
    # Image Resizing
    image bg laptop_full = im.Scale("bg laptop_full.png", 1920, 1080)
    image bg laptop_full_chat = im.Scale("bg laptop_full_chat.png", 1920, 1080)
    image bg laptop_overlay = im.Scale("bg laptop_overlay.png", 1920, 1080)
    image bg park_entrance = im.Scale("bg park_entrance.png", 1920, 1080)
    image bg park_bulletin = im.Scale("bg park_bulletin.png", 1920, 1080)
    image bg park_sw_switch = im.Scale("bg park_south_switch.png", 1920, 1080)
    image bg white = im.Scale("bg white.jpg", 1920, 1080)

    #choice flags here
    #false = 0, true = 1
    $ seen_bulletin = 0
    $ went_lakeside = 0
    $ went_recreation_area = 0

    #counters here
    
# The game starts here.

label start:

    jump lb_laptop_introduction

    # 12:05
    #everything in this label past this is unused
    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label lb_laptop_introduction:

    #initial bg
    scene bg laptop_full
    
    "Start of Laptop Intro"
    "[[Streamer scene - Mushroom Hunting]\nIF 12:25 [[MISS STREAM\] - ELSE -\nJump in @time-stamp"
    ""
    "The stream will start soon..."

    scene bg laptop_full_chat

    "{i}Fwitch nonsense here x10{/i}"

    "{i}Tutorial scenes here (probably not needed though){/i}"

    "Oh, the stream is finally starting! Let's see what we have here tonight..."

    jump lb_mushroom_hunting



label lb_mushroom_hunting:
    #Off Stream intoduction
    #12:06
    scene bg park_bulletin

    "Two young friends, Donovan and Ethan, stand in front of a park billboard."

    show donovan happy at left
    "One hosts a clean cut, preppy like look."

    show ethan happy at right
    "The other has ventured into the soft gothic territory."

    "Their stream PsyShmanz pulls a lot of viewers."
    "They travel around the globe, looking for different psychedelics to take."
    "Everyone thinks they're brothers, but they're not."

    hide donovan happy
    hide ethan happy


    #Stream's park entrance
    scene bg laptop_overlay as overlay
    show bg park_entrance behind overlay
    "{b}Ext. Park Entrance - Night{/b}"

    show donovan happy at left behind overlay
    "{i}A smiling figure holding the camera appears on stream{/i}"

    dono "Hello, happy viewers!"
    dono "Good morning, or evening! Where ever you are."

    "{i}CHAT goes wild{/i}"

    show ethan happy at right behind overlay
    ethan "We're coming to you guys live from Eureka Springs, Arkansas."

    "{i}CHAT goes wild once more!{/i}"

    dono "Not a location we typically visit. "
    dono "Especially considering that mushrooms are a controlled substance here."

    "[[reponse surrounding psychedelics]"

    show ethan sad at right behind overlay
    show donovan sad at left behind overlay
    ethan "A Class C felony, even for harvesting."

    "{i}[[Chat Pop-up here]{/i}: [[user] donated $my spleen"
    "{i}Chat filled with rage/defensive comments{/i}"

    show donovan happy at left behind overlay
    dono "Don't worry you guys, we're not after anything illegal here."

    show ethan happy at right behind overlay
    ethan "We found a loophole!"

    "{i}Chat blows up excited over this{/i}"
    "{i}[[A pop up here happens]{/i}"

    ethan "Knew you would like that."

    "{i}[[Chat likes that meme]{/i}"

    dono "We got a tip from user [[ricitioxy] on how local psychonauts service such harsh climates."
    "{i}[[Donovan closed eyes, open mouth]{/i}"
    dono "For those who don't grow, there's some wild foraging at hand."
    dono "Arkansas' mild winters lead to excellent fruiting. And while harvesting mushrooms is illegal..."
    dono "harvesting what comes out isn't."

    "{i}Chat loves Donovan some more{/i}"

    #12:08
    ethan "Tonight we're searching for Hydnellum Peckii, a.k.a. the 'Devil's Tooth.'"

    dono "A cream colored mushroom with a short body and a wide cap, that's flat on top."
    dono "A cap peppered with a series of red dots."

    "{i}Chat has been diagnosed with excitement emoji syndrome{/i}"

    dono "And those dots are why we're here tonight! We've come to harvest the 'Devil's Berry!'"

    "{i}Chat blows up{/i}"

    ethan "These 'berries' contain a hallucinogenic compound called myristicin. Known for it's euphoric effects."

    "{i}Chat psychedelic emojis{/i}"

    #12:09
    dono "So, should we start?"
    ethan "Lets..."

    "{i}Chat goes wild, psy boy love{/i}"
    
    #first choices
    #we can set boolean values after this
    menu :
        "[[Awaiting user input]"
        "Check the post!":
            $ seen_bulletin = 1
            jump lb_mushroom_hunting_opt1
        "Get going!":
            jump lb_mushroom_hunting_opt2
        "[[debug] Continue to repeat from laptop intro":
            "Will now restart/jump back to laptop intro label"
            jump lb_laptop_introduction
        "[[debug] Continue to repeat from mushroom_hunting label":
            "Will now restart/jump back to mushroom_hunting label"
            jump lb_mushroom_hunting

    jump lb_mushroom_hunting


label lb_mushroom_hunting_opt1:
    "[[debug] Option 1 start here"

    "{i}[[Chat talks about billboard]{/i}"

    #Surpised Donovan here
    "{i}Donovan looks surprised{/i}"
    dono "You guys want us to check the billboard?"

    #smile donovan here
    dono "Done!"
    
    #Go to billboard moments later
    scene bg laptop_overlay as overlay
    show bg park_bulletin behind overlay

    #zoom to billboard for five seconds before beginning to talk

    #Donovan and Ethan should be off screen at this point

    ethan "Aww, there's a little missing dog."

    "{i}[[Chat is being sympathetic to Ethan]{/i}"

    dono "Bell Lake, Established 1915. Huh!"
    dono "Check out this map."

    "{i}[[Chat is shocked emoji]{/i}"

    dono "Bell Lake is to the North. Eagle Point is a little further up. It's connected to this side trail here."
    dono "There's also a little recreational space to the East. With some benches and a stage."
    dono "We should probably memorize this, so that we don't get lost."

    "{i}[[Chat chants don't get lost]{/i}"

    ethan "I've got you, I'll take a picture"

    "{i}[[Chat blows up at the idea of picture taking]{/i}"

    #emulate a flash
    window hide dissolve
    pause 1.0
    show bg white as white_bg behind overlay with dissolve
    pause 1.0
    show bg park_entrance behind white_bg
    hide white_bg with dissolve
    pause 1.0
    window show dissolve

    #Park entrance takeoff
    show ethan happy at right
    ethan "Got it!"

    show donovan happy at left
    dono "Let's go!"

    "{i}[[Chat blows up let's do this!]{/i}"
    

    jump lb_mushroom_hunting_sw_intersection


label lb_mushroom_hunting_opt2:
    "[[debug] Option 2 start here"

    "{i}[[Chat blows up let's do this!]{/i}"

    dono "Alright folks...let's do this!"

    ethan "Lets!"

    jump lb_mushroom_hunting_sw_intersection

label lb_mushroom_hunting_sw_intersection:

    scene bg laptop_overlay as overlay
    show bg park_sw_switch behind overlay
    "[[debug] sw_intersection start here"
    #12:10

    "{i}Nighttime{/i}"
    
    "Ethan and Donovan seem to be bent over looking"

    "{i}Rustling{/i}"

    show ethan sad at right behind overlay
    ethan "I've got nothing."

    show donovan sad at left behind overlay
    dono "Ah, I've got nothing."

    #chat is sending emoji's here too
    "{i}Chat seems visibly upset{/i}"

    show donovan happy at left
    dono "Alright folks, it looks like the proverbial 'high-road/low-road' situation."
    dono "So, should we head further North? Or Flip East? Up to you guys."

    #Choice North (Lake side) or East (Recreation area)
    menu:
        dono "So, should we head further North? Or Flip East? Up to you guys."
        "North!!":
            $ went_lakeside = 1
            jump lb_mushroom_hunting_lakeside
        "East, east, east, eastast!!!":
            $ went_recreation_area = 1
            jump lb_mushroom_hunting_recreation

label lb_mushroom_hunting_lakeside:

    scene bg laptop_overlay as overlay
    show bg park_lakeside behind overlay
    "[[Debug] went lakeside"
    #12:11

    show donovan happy at left behind overlay
    dono "Alright, you guys, let's talk some facts."
    
    #Donovan points at ethan here
    dono "Ethan, take it away!"

    "{i}Chat sends ethan love{/i}"

    #Scholarly Ethan mode here
    show ethan happy at right behind overlay
    ethan "Looking around, we can see a lot of younger trees and a lot of non-native species."

    "{i}Chat sending mixed emojis of trees{/i}"

    ethan "What we're truly looking for though, are some of those old-growth Alabama pines! As the Devil's Tooth loves to grow on them."  
    
    "{i}Chat is mind blown and memeing{/i}"

    #donovan does a smile at the camera here
    show donovan happy at left behind overlay

    "{i}Chat is sending pines, hearts, mind-blown emojis{/i}"

    #typo? maye TODO
    ethan "And while maye look like we made a bad choice in parks, don't even worry."

    if seen_bulletin == 1:
        ethan "This park was established a long time ago. Although its seen some revisions, I'm sure we'll find us some pines!"
    else:
        ethan "Most parks, even the newer ones, tend to keep some of their old trees around."

    #12:12

    "{i}Chat goes wild over the boys, loves their travels{/i}"

    ethan "That's been an Ethan-minute."

    dono "Thanks E, for putting us in the know."

    #Light approaches in the background, Ethan moves
    #over to Donovan and makes room for Donna & Wendy to enter

    #TODO Move dono and ethan left properly
    show donovan shocked at left behind overlay
    dono "Woah!"

    show ethan confused at left behind overlay
    ethan "Hello?"

    #Meeting wendy and donna the first time
    #unknown person at first
    show donna worried at right behind overlay
    unknown "Hey, have you seen a dog?"

    #Confused ethan
    ethan "What?"

    unknown "A dog. A Cavalier King. He's a Cavalier King. He's missing."

    #Worried donovan
    show donovan worried at left behind overlay

    if seen_bulletin == 1:
        dono "We saw your poster earlier. The one at the entrance. That's your dog right?"
    else:
        "Woah, folks. It looks like we've got a missing dog."

    dono "How long has your..."
    dono "I'm sorry, what's your dog's name?"

    #donna frustated here
    show donna frustrated at right behind overlay
    donna "I'm Donna, this is Wendy, our dog is Chips."

    #Frustrated ethan
    show ethan frustated at left behind overlay
    ethan "I'm Ethan, he's Donovan."
    
    #frustrated donovan
    show donovan frustated at left behind overlay
    dono "Right."

    show donovan concerned at left behind overlay
    dono "So, how long has Chips been missing?"

    #sad wendy
    show wendy sad at right behind overlay
    wendy "It's not about how long he's been missing, it's about him being scared and hungry."

    #straight faced ethan
    show ethan smile at left behind overlay
    ethan "Hmmph, Donovan let's find their dog."

    #smiling donovan
    show donovan smile at left behind overlay
    dono "We can find anything, we can find Chips no problem."

    #worried wendy
    show wendy worried at right behind overlay
    wendy "Really? You would help us find him?"

    #smile ethan
    ethan "It's our job, and we do it well. Take us to where you last saw him."

    #neutral donna
    show donna neutral at right behind overlay
    donna "It's right up here"

    #still smiling here
    ethan "So, you guys ready?"

    #player must agree to progress
    menu:
        ethan "So, you guys ready?"

        "I'm ready":
            "{i}Chat agrees{/i}"

    #12:13
    #jump to next part

    jump lb_mushroom_hunting_lake_act1_ending_scene

label lb_mushroom_hunting_recreation:

    scene bg laptop_overlay as overlay
    show bg park_recreation behind overlay

    #Seen Bulletin board

    "[[Debug] went east]"


    #12:11
    #ETHAN
    #[Looking to side, inquisitive]
    show ethan inquisitive_side at left behind overlay
    ethan "Hey, we've got people...!"
    #(Show "dark frames" in the distance)

    #CHAT [Ponders, jokes about serial killers - gets scared - oh no!]

    # DONOVAN [Hand up, waving]
    show donovan waving at left behind overlay
    dono "Hey!"
    #(Move Donovan over, have dark shadows "Move" forward and then
    #transform into same figures but visibly women)

    #CHAT [responds to mystery]

    #WOMEN [Standing close together - single illustration, visibly gloomy]
    unknown "Hey."


    show donovan inquisitive at left behind overlay
    #[Looking inquisitive] 
    dono "What are you guys doing out here?"
    
    show ethan inquisitive at left behind overlay
    #[Also inquisitive]
    ethan "Looking real upset."
    
    #WOMEN [Standing close] 
    unknown "Uh, it's our dog. We haven't been able to find him."

    unknown "We've been looking..."
    

    #[Looks surprised]
    show ethan surprised at left behind overlay
    ethan "Oh, hey! I think I saw your dog!"

    #(non-verbal)[Looks at Ethan confused]
    #WOMEN(non-verbal) [Look up, lively even]

    #[Looks ashamed]
    show ethan ashamed at left behind overlay
    ethan "Ugh, no-no-no! Not like that. Sorry."

    #WOMEN(non-verbal)[Looking extra gloomy, hopeless]
    #CHAT[crying, sad]
    
    #ETHAN [Still ashamed]
    ethan "I meant...on the flier. The one at the entrance."

    #DONOVAN (non-verbal) [Frowns]

    #WOMEN [demure] 
    unknown "Oh yeah, that's our baby. We put that up a week ago."

    #ETHAN [Looks at women concerned]

    #DONOVAN [Looks at women concerned]
    
    #CHAT [RIP, dog emojis, sad, crying]

    #ETHAN [Shocked]
    ethan "Wait, a week? Like seven days. Seven."
    
    ethan "I just need to clarify so I know we're on the same page."

    #CHAT [shock emojis]

    #DONOVAN [Unhappy]
    dono "Bruh,seriously!"
    dono "Hey, don't worry."
    dono "He's just concerned. You know?"
    
    #ETHAN [Frustrated]
    ethan "That's a long time for a dog to be lost!"

    #12:12

    #DONOVAN [Frustrated back]
    dono "Bruh, stop."
    
    #WOMEN [one begins crying while other comforts]
    unknown "..."
    unknown "We...we already know that. You're not telling us something new."
    unknown "It's just, our baby is out here and we just want to find him."
    unknown "However that is..."

    #CHAT [cry emojis sad]
    #ETHAN (non-verbal)[sad]
    #DONOVAN (non-verbal)[sad]

    #DONOVAN (CONT'D) [Snaps to smile]
    dono "Hey, it's cool. We've got you."
    
    #[CHAT] [Happy emojis]

    #WOMEN [Look up, original gloom]
    unknown "What...?"
    
    #DONOVAN [Smiles at women]
    dono "It's cool, really! Trust me. We got you. We find stuff, that's our job."
    dono "We're practically experts."

    #ETHAN [smiles as well]
    ethan "We can find your dog, don't even sweat it!"
    
    #CHAT [dog emojis & psy love]
    
    #WOMEN [look a little happier]
    unknown "Really?"
    
    #ETHAN [Big smile]
    ethan "A hundred percent!"
    
    #DONOVAN(non-verbal)[big smiles]

    #DONNA [Smiling but looking gloomy still]
    donna "I'm Donna."

    #DONOVAN [smiling] 
    dono "Donovan."

    #WENDY [looking a bit less gloomy]
    wendy "Wendy..."
    
    #ETHAN [smiling]
    ethan "Ethan!"
    ethan "And we're looking for...?"

    #DONNA[A little optimistic]
    donna "Chips."
    
    #DONOVAN [Smiling]
    dono "Well let's go find the pup!"

    #CHAT [Blows up about dog, fired up] (Only advances afteradding a response.)
    # 12:13
    
    jump lb_mushroom_hunting_lake_act1_ending_scene

label lb_mushroom_hunting_recreation_no_bulletin:

    scene bg laptop_overlay as overlay
    show bg park_recreation behind overlay
    
    #12:11
    #DONOVAN [looking inquisitive]
    dono "Hey, I see something."

    #[Focusing hard]
    dono "Someone...?"

    #CHAT
    # chat "sends alien, werewolf, zombie emojis"
    
    #??? [Come forward into the light]
    unknown "Have you guys seen a dog?"

    # DONOVAN (non-verbal) [confused]

    # ETHAN [confused]
    ethan "A dog...?"
    
    # chat "Shocked faces"
    
    # DONOVAN [still confused]
    dono "No, we haven't seen one."
    
    # ETHAN [inquisitive]
    ethan "Is that why you guys are here?"
    
    #??? [gloomy looking]
    unknown "We're looking for Chips, our dog. We lost him. Did you guys see the posters?"

    unknown "The ones at the front. That's us. That's Chips."

    # ETHAN [more confused]
    ethan "We didn't see those either. Sorry."

    chat "dog emojis"

    # ??? [gloomy one other speaks up]
    unknown "We put them up, so that people would see."

    # ETHAN [matter of factly]

    ethan "We didn't."

    # ??? [frustrated]
    
    unknown "Mmmph."
    
    # DONOVAN [concerned]
    dono "Is there any way we can help?"

    chat "Psy love"
    
    # ETHAN [Shoots Donovan a confused glance]
    
    # ??? [gloomy]
    unknown "We'd appreciate if you guys looked for him. Maybe...help us find him?"  
    unknown "We've been trying for the past week and..."
    
    # ETHAN [matter of factly]
    
    ethan "Woah, woah, woah, woah, woah!"
    ethan "A week? That's a long time to have not seen your dog. Are you sure he's not..."

    # 12:12
    # DONOVAN [Frustrated looking at Ethan]
    dono "Ethan! Bruh."
    
    # [Sympathetic look]
    dono "I'm sorry about him, he clearly has no filter."

    CHAT "blows up, some mad some not"
    
    # ETHAN (non-verbal) [looks a bit disgruntle]
    
    # DONOVAN [Ignores Ethan, smiles]
    dono "If you guys need help, we can totally help you."
    
    # [big toothy smile]
    dono "We've got you!"

    # CHAT [Swoons over Donovan]

    # ETHAN (non-verbal) [face straightens out]

    # ??? [relief]
    unknown "Really?"
    unknown "We've been looking everywhere. You have no idea how much this means!"
    unknown "Oh, thank you."

    #DONOVAN[Smiles]
    
    dono "No problem! I'm Donovan by the way. He's Ethan."
    
    chat "psy love"

    # DONNA [Smiles back but still looks weathered]
    
    donna "I'm Donna, she's Wendy. You already know Chips."

    # DONOVAN [smiling]
    
    dono "Well, let's go find him. Let's go find Chips!"

    # ETHAN [exhasperated]
    
    ethan "Then we can get back to our buisness..."
    
    chat "some love ethan's cattiness"

    # WENDY [a little optimistic but more guarded]
    
    wendy "The last time we saw him was around the lake."

    # DONOVAN [smiles]
    
    dono "Cool."
    dono "Where's that at?"

    chat "lake & lochness monster"

    # DONNA [a little optimistic as well]
    donna "It's back that way, and a little to the North. We'll show you."

    # ETHAN [little flustered]
    ethan "Lead the way..."
    
    chat "blows up for adventure, finding dog, gogogo]"
    # 12:13

    jump lb_mushroom_hunting_lake_act1_ending_scene

label lb_mushroom_hunting_lake_act1_ending_scene:
    # EXT. OUTTER LAKE NE JUNCTION - NIGHT - [HAVE MET D&W]
    
    # This scene joins all extensions, leading to the attack from Chips the missing dog.  It breaks up into three parts (before the attack chatter) (the attack) and (the decision path).  From there, it breaks up into another three parts, all of which lead to doom but in differing ways.  Afterwards you stay and fight or you run a) People choose to help and get attacked.  Camera falls and shows cowering Donna as the blood pools.  b) You tell the character to run c) (stretch) tell them to help Donna
    # ======
    # 12:13
    
    # DONNA [Frowning] 
    donna "Chips ran off on us up here..."
    donna "You know, I know what you're thinking, but we're good moms.  We never expected he'd would run off like this."
    # (Non-verbal)[Back to frowning]

    # WENDY [Frowning] 
    wendy "When we first got him, Chips was afraid of his own shadow."

    # CHAT [Sends dog emojis]
    # DONNA [Smiling] 
    donna "Hell, I once farted and he took off running."
    # (non-verbal)[Back to frowning]

    # WENDY [Sad] 
    wendy "We trained him, took him to a specialist.  Bought him this harness.  Was supposed to be good for anxious dogs."
        
    # DONNA [Looking @Wendy] 
    donna "You know dogs, you never know what's going to trigger them."
        
    # DONOVAN [Concern]
    dono "How did he got lost?"

    # ETHAN [Flustered]
    ethan "Yes, how did you guys lose Chips?"
        
    # CHAT [Detective emoji stuffs - whatever]

    # DONNA [Frowning still] 
    donna "We took him here, because it's a lot calmer than most places."

    # WENDY [Sad] 
    wendy "With the training and everything, his behavior had changed drastically. We just wanted to be safe."
        
    # DONNA [Frowning] 
    donna "One of the things you can't do here is skateboard."
        
    # ETHAN [Straight faced] 
    ethan "Another thing you can't do is be in this park after dark. And we're all breaking that rule."
        
    # DONNA [Frowining] 
    donna "Exactly, people break the rules. I don't know why we thought otherwise. We fucked up."
        
    # 12:14
        
    # CHAT [Chat freaks out - shocked/sad]
        
    # DONOVAN (non-verbal) [Sad]
        
    # ETHAN (non-verbal) [Sad]
        
    # DONNA (non-verbal) [Sad]

    # WENDY [Sad] 
    wendy "There was a skateboarder. He got scared."
        
    # DONNA [Frustrated] 
    donna "The wheels must have freaked him out or something.  I don't know."

    # WENDY [Crying] 
    wendy "I was holding him that day.  I had the leash."
    wendy"He got scared and started to pull.  He kept pulling, and I wasn't strong enough to fight him. I fell."

    # DONNA [Sad] 
    donna "I'm trying to save her, and while I'm doing that he's already bolted."

    # WENDY [Crying] 
    wendy "The leash fell out of my hand. He got so scared he just ran. He went to hide in the woods."

    # DONNA [Frustrated] 
    donna "We looked for him. We couldn't stop."
    donna "They had to kick us out. We waited in the car until there was nobody left, and went right back out."
        
    # WENDY [sad] 
    wendy "We keep coming back, every day. We hung those posters too. In the hopes someone had seen Chips. That they could maybe bring him home."
        
    # CHAT [Crying sad wah, wah messages]
        
    # ETHAN [Sympathetic] 
    ethan "Who even skateboards in the middle of winter? What is wrong with people?"
        
    # DONOVAN [Frustrated] 
    dono "I don't know bro, but let's set this right."

    # 12:15
    # ****
        
    # (Sudden ruffle in the bushes. Everyone turns to look.)

    # [We're getting PEAK zombie dog here]

    # (Camera cuts to bushes)
    # (Rustling continues - Bushes cut to shadow)

    # (Shadow cuts to zombie Chips appearing. Looking all mangled and nasty.)

    # *****
        
    # ETHAN (non-verbal) [disgusted]
    # DONOVAN (non-verbal) [confused]
    # DONNA (non-verbal) [disgusted]
    # CHAT [freaking out, puking, grossed out]
    # WENDY [Shocked] 
    wendy "Ch-Chips...?"

    # ****
    # (Not sure if Chips is off-screen or everyone has moved to one side w/ Chips on the other - pushed as far as they can go and very close together.)
    # ******

    # CHIPS [Zombie stare] 
    chips "Rrrrrrrr..."

    # DONNA [Scared] 
    donna "Wendy, I-I-I-I..."
    donna "I-I don't think Chips is alright."
        
    # ETHAN [Scared] 
    ethan "That dog is not okay!"
        
    # WENDY [Happy face] 
    wendy "Chips, baby. Come here. Come on. We've got you. Come!"
    wendy "Chips!"
        
    # DONOVAN [Scared] 
    dono "Woah...!"
        
    # ****
    # (Chips suddenly attacks Wendy who has crept closer and closer to the zombie dog. Jumping up, knocking her down again (with his weight) and biting on to her neck as she falls. Blood splurts everywhere, everyone instantly is shocked)

    # (Dog stands on top of Wendy and vomits black substance from mouth all over her face. In an instant the dog runs back off into the woods.)
    # *******
        
    # 12:16
        
    # CHAT [some shocked, some laughing, some calling it fake, some saying call the cops]
        
    # WENDY [In shock] 
    wendy "...ghhhk...ghkk..."
        
    # DONOVAN [Freaked out] 
    dono "Oh fuck, oh fuck!"
        
    # ETHAN [Freaking out] 
    ethan "Holy shit, oh-my-god!"
    
    # ****
    # (Ethan starts clawing the gunk off her face.)

    # (Donna has shut down, she collapses to the ground in total non-responsive shock.)

    # (Within seconds, Wendy changes hands on Ethans head, biting off a portion of his cheek.)
    # *******
        
    # WENDY [Enraged] 
    wendy "Rrrraeeee!"
    
    # ETHAN [Shocked] 
    ethan "Aughhhh! Oh-my-god, oh-my-god. What the fuck! Ughhh..."
    
    # ****
    # (As Ethan attempts to get up and run Wendy takes this moment to grab on to his shoulders and bite into his neck. His eyes go wide, as he breathes his last breath.)
    # ******
        
    # DONOVAN [Insanely terrified] 
    dono "Dude, Ethan. Bro. What? Fuck!"
    dono "Donna. Donna, come on. We've got to go. Donna. Get up. Fuck!"
        
    # ****
    # (Donovan tries to pull Donna up but she doesn't respond. Wendy stands up.)
    # ******
        
    # 12:17
        
    # DONOVAN [Crying scared] 
    dono "Fuck man, what do I do? Fuck. Please...!"
        
    # USER
    # [Option 1] FIGHT!111!!!1!!!
    # [Option 2] HELP DONNA!!!
    # [Option 3] GET OUT OF THERE
    # ****
    # (At this point depending on what the user chooses it sets up three different endings.)
    # *****
    # ****
        
    menu :
        dono ""
        "FIGHT!111!!!1!!!":
            # Option 1
            jump lb_mushroom_hunting_act1_end1
        "HELP DONNA!!!":
            # Option 2
            jump lb_mushroom_hunting_act1_end2
        "GET OUT OF THERE":
            # Option 3
            jump lb_mushroom_hunting_act1_end3

label lb_mushroom_hunting_act1_end1:
    # [Option 1] 
    # (Donovan's skull gets crushed)
        
    # DONOVAN [Scared but more aware] 
    dono "Fight...! Yeah. I should do that.  What the fuck. Okay."

    # [Scared] 
    dono "I've got my knife. I'm going to fuck her up."

    # [Angry] 
    dono "Yargh! Fuck you, fuck you! Fuck!"

    # ****
    # (Donovan kicks Wendy back with his boot and stabs her in her head. Wendy collapses.)
    # ******
    
    # DONOVAN [Aggressive, Happy & Blood Covered] 
    dono "Yeah, fuck! Fuck you. Fuck!"

    # [Sad holding back tears]
    dono "Man, Ethan, man. Fuck!"
    
    # *****
    # (At this moment Chips appears out of nowhere again, lunging high and opening his jaw biting on to Donovan's entire head.)
    # ******
    
    # [Confused]
    dono "Uuh. Wuhh...wooo?"
    
    # ****
    # (Ethan collapses. The camera focusing on the dog's backside. Black begins to cover the lens (the goo). Chat is blowing up. Give it 4 seconds - and shut it down automatically on the 5th.)
    # 12:18

label lb_mushroom_hunting_act1_end2:
    # [Option 2] (Donovan is going to get murdercycled here)
    
    # DONOVAN
    # [Upset] 
    dono "Donna, Donna. Come on! We need to go, please! Get up!"
    dono "Donna, please! Fuck! What the fuck, man! Fuck."
    
    # ****
    # (Ethan sits up with Wendy standing. They both start walking towards them.)
    # ******
    # DONOVAN
    # [Freaking out] 
    dono "Ethan, bro. The fuck!? What the fuck, what the fuck!"

    dono "Fuck, man. Donna! Please! We gotta go...! Fuck!"
    
    # ****

    # (Shows Donovan trying to drag comatose Donna as he suddenly gets charged by the two. The camera falls and just shows Donna lit up and empty. Black goo slides on the ground. Mods cut in, and feed ends.)
    
    # 12:18


label lb_mushroom_hunting_act1_end3:  
    # [Option 3 - Uncertain ending - Run]
    
    # ****
    # (If the player tells Ethan to run all we hear is him screaming "Fuck!" as he runs, he'll make it to the car, jingle the keys, open the door and the feed will cut out b/c mods.)
    # *****
    
    # DONOVAN [Scared] 
    dono "Fuck this, I'm fucking gone!"
    
    # ****
    # (Starts running, camera keeps flying in and out of his scared face as if being swayed up and down.)
    # ******
    
    # DONOVAN [Scared] 
    dono "Fuck man, Ethan, man! Fuck!"
    
    # ****
    # (Keeps running and hits the car)
    # *****
    
    # DONOVAN [Scared] 
    dono "Fucking keys. Fuck. Fuck!"
    
    # *****
    # (Shows door then smashes keys in. Turn door opens. Donovan gets in, at the same moment the feed cuts out. Mods shut it down.)
    # ****
    
    # 12:18