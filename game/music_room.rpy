init python:
    mr_rows = 3
    mr_cols = 2

    mr_cells = mr_rows * mr_cols
    mr = MusicRoom(fadeout=1.0)

    for track in music_room.tracks:
        mr.add(track["file"])

screen music_room:
    tag menu
    default mr_page = 0
    default is_playing = None

    use game_menu(_("Music Room")):
        $ current_num = mr_page + 1

        fixed:
            xpos -170

            vbox:
                ypos 55
                xalign 0.5
                if (len(music_room.tracks) > mr_cells):
                    text "Page {}".format(current_num):
                        xalign 0.5
                        style "page_label_text"
                text "Currently Playing: {}".format(is_playing):
                    xalign 0.5

                if is_playing:
                    imagebutton:
                        top_margin 20
                        auto "gui/gallery/pause_%s.png"
                        xalign 0.5
                        action [mr.Stop(), SetScreenVariable("is_playing", None)]
                        foreground Text(_("STOP"), style="mr_btn", size=24) 
                        hover_foreground Text(_("STOP"), style="mr_btn_hover", size=24)
                        insensitive_foreground Text(_("STOP"), style="mr_btn_insensitive", size=24)
                        hovered [ Play("sound", "audio/click.mp3") ]
                        
            
            frame:
                background None
                top_margin 50
                xalign 0.5
                yalign 0.5

                grid mr_rows mr_cols:
                    xalign 0.5
                    yalign 0.5
                    spacing gui.slot_spacing

                    $ i = 0
                    $ next_mr_page = mr_page + 1
                    $ prev_mr_page = mr_page - 1

                    if next_mr_page > int (len(music_room.tracks)/mr_cells):
                        $ next_mr_page = 0
                    
                    elif prev_mr_page == -1:
                        $ prev_mr_page = 0

                    for track in music_room.tracks:
                        $ i += 1
                        if i <= (mr_page+1)*mr_cells and i>mr_page*mr_cells:
                            if mr.is_unlocked(track["file"]):

                                imagebutton:
                                    auto "gui/gallery/slot_%s.png"

                                    foreground Text(_(track["name"]), style="mr_btn") 
                                    hover_foreground Text(_(track["name"]), style="mr_btn_hover")
                                    insensitive_foreground Text(_(track["name"]), style="mr_btn_insensitive")

                                    action [mr.Play(track["file"]), SetScreenVariable("is_playing", track["name"])]


                                    sensitive not is_playing == track["name"]
                                    hovered [ Play("sound", "audio/click.mp3") ]
                            
                            else:
                                add "gui/gallery/locked.png"

                    for j in range(i, (mr_page+1)*mr_cells): #we need this to fully fill the grid
                        null

                if (len(music_room.tracks)>mr_cells):
                    $ pages = ((len(music_room.tracks)) / mr_cells) + 1

                    hbox:
                        style_prefix "page"

                        xalign 0.5
                        yalign 0.96

                        spacing gui.page_spacing

                        imagebutton:
                            auto "gui/gallery/page_number_%s.png"
                            foreground Text(_("<"),style="pg_num_idle")
                            hover_foreground Text(_("<"),style="pg_num_hover") 
                            insensitive_foreground Text(_("<"),style="pg_num_insensitive")
                            action [SetScreenVariable('mr_page', prev_mr_page)]
                            sensitive mr_page != 0
                            hovered [ Play("sound", "audio/click.mp3") ]

                        for num in range(pages):
                            $display_num = num + 1
                            imagebutton:
                                auto "gui/gallery/page_number_%s.png"
                                foreground Text(_("{}".format(display_num)), style="pg_num_idle")
                                hover_foreground Text(_("{}".format(display_num)), style="pg_num_hover")
                                action [SetScreenVariable('mr_page', num)]
                                hovered [ Play("sound", "audio/click.mp3") ]

                        imagebutton:
                            auto "gui/gallery/page_number_%s.png"
                            foreground Text(_(">"),style="pg_num_idle")
                            hover_foreground Text(_(">"),style="pg_num_hover")
                            insensitive_foreground Text(_(">"),style="pg_num_insensitive")
                            action [SetScreenVariable('mr_page', next_mr_page)]
                            sensitive mr_page != pages-1
                            hovered [ Play("sound", "audio/click.mp3") ]

    if config.main_menu_music:
        on "replaced" action Play("music", config.main_menu_music, if_changed=True)
    
    else:
        on "replaced" action mr.Stop()

style mr_btn:
    xalign 0.5
    yalign 0.5
    size 46
    
style mr_btn_hover:
    xalign 0.5
    yalign 0.5
    size 46
    color gui.hover_color

style mr_btn_insensitive:
    xalign 0.5
    yalign 0.5
    size 46
    color "#ddd"



    


                        


