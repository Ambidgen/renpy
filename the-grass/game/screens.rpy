## screens.rpy
##
## The Grass - custom vertical UI for a 720x1280 stage.
##
## The look: grey weather, wet wool, ochre banners, witch-blue glass.
## The layout: a slim status bar at the top, the story stage filling the
## middle, and a matte bar of actions along the bottom.

init python:

    def clock_text():
        return "%s  ·  day %d" % (store.hour_name(bell), storm_day)

    def topic_ok(t):
        cond = t[2]
        if cond is None:
            return True
        try:
            return bool(eval(cond))
        except Exception:
            return False

    def available_topics(pid):
        p = person(pid)
        out = []
        for t in p.topics:
            if (pid, t[0]) in talked:
                continue
            if topic_ok(t):
                out.append(t)
        return out

    def seen_topics(pid):
        p = person(pid)
        return [t for t in p.topics if (pid, t[0]) in talked]


################################################################################
## Styles
################################################################################

style default:
    font gui.text_font
    size gui.text_size
    color gui.text_color

style grass_label is text:
    font gui.name_text_font
    size 21
    color grass_edge
    kerning 2

style grass_dim is text:
    size 21
    color grass_dim

style grass_button is button:
    background Frame(Solid("#141819e8"), 6, 6)
    hover_background Frame(Solid("#2b3334e8"), 6, 6)
    padding (14, 10)

style grass_button_text is text:
    size 24
    color "#ddd4c0"
    hover_color "#f7f0dd"

style grass_panel:
    background Frame(Solid("#0e1214f2"), 6, 6)
    padding (18, 16)


################################################################################
## The location HUD
##
## Shown with `call screen`, so every button returns a value to the script.
################################################################################

screen location_hud():
    zorder 30

    ## status bar -------------------------------------------------------
    frame:
        background Solid("#060809e6")
        xfill True
        ysize 74
        xpos 0
        padding (76, 0, 20, 0)

        hbox:
            yalign 0.5
            spacing 10

            text loc(location).name:
                font gui.name_text_font
                size 25
                color "#f0e8d4"
                yalign 0.5

            text "·":
                size 24
                color "#4d5a58"
                yalign 0.5

            text clock_text() style "grass_dim" yalign 0.5

            null width 1

            if caravan_state != "overdue":
                text "caravan" size 18 color grass_blue yalign 0.5

    ## who is around ----------------------------------------------------
    $ here_people = people_here(location)

    vbox:
        xpos 24
        ypos 96
        spacing 8

        for p in here_people:
            button:
                style "grass_button"
                xsize 250
                action Return(("talk", p.id))
                hbox:
                    spacing 10
                    add ("images/portrait/%s.png" % p.id) zoom 0.22 yalign 0.5
                    vbox:
                        yalign 0.5
                        text p.name size 21 font gui.name_text_font color p.color
                        text p.title size 15 color grass_dim

    ## action bar -------------------------------------------------------
    hbox:
        xalign 0.5
        ypos 1166
        spacing 8

        button:
            style "grass_button"
            xsize 164
            ysize 58
            action Return("map")
            text "Map" size 23 align (0.5, 0.5)

        button:
            style "grass_button"
            xsize 164
            ysize 58
            action Return("look")
            text "Look" size 23 align (0.5, 0.5)

        button:
            style "grass_button"
            xsize 164
            ysize 58
            action Return("notes")
            text "Notes" size 23 align (0.5, 0.5)

        button:
            style "grass_button"
            xsize 164
            ysize 58
            action Return("wait")
            text "Wait" size 23 align (0.5, 0.5)


################################################################################
## The map of the ten locations
################################################################################

screen map_screen():
    modal True
    zorder 60

    add Solid("#070a0bf5")

    text "THE BORDERLANDS OF HELLA":
        style "grass_label"
        xpos 40
        ypos 36

    text "Travel":
        font gui.name_text_font
        size 40
        color "#f2ead2"
        xpos 40
        ypos 62

    frame:
        background Solid("#101617f5")
        xpos 30
        ypos 132
        xsize 660
        ysize 900
        padding (0, 0)

        fixed:
            xsize 660
            ysize 900

            ## links, drawn as dotted lines under the markers
            for l in LOCATIONS:
                for other in l.links:
                    $ p1 = l.map_pos
                    $ p2 = loc(other).map_pos
                    for i in range(1, 12):
                        $ t = i / 12.0
                        $ mx = p1[0] + (p2[0] - p1[0]) * t
                        $ my = p1[1] + (p2[1] - p1[1]) * t
                        add Solid("#3d4c47", xsize=5, ysize=5):
                            xpos int(40 + mx * 580) - 2
                            ypos int(30 + my * 840) - 2

            ## markers
            for l in LOCATIONS:
                $ here = (l.id == location)
                $ been = l.id in visited
                button:
                    xsize 200
                    ysize 62
                    xpos int(40 + l.map_pos[0] * 580) - 100
                    ypos int(30 + l.map_pos[1] * 840) - 31
                    background Frame(Solid("#c9b071" if here else ("#232b2b" if been else "#161b1c")), 6, 6)
                    hover_background Frame(Solid("#e2cb8b"), 6, 6)
                    sensitive not here
                    action Return(("go", l.id))

                    vbox:
                        align (0.5, 0.5)
                        spacing -2
                        text l.name:
                            size 19
                            font gui.name_text_font
                            xalign 0.5
                            color ("#15120e" if here else ("#e6ddca" if been else "#7d7a70"))
                        if here:
                            text "you are here" size 12 color "#3a3529" xalign 0.5

    textbutton "Close":
        style "grass_button"
        xsize 150
        ysize 56
        xpos 540
        ypos 1160
        action Return(None)


################################################################################
## Talking: a topic list for one person
################################################################################

screen topics_screen(pid):
    modal True
    zorder 60

    $ p = person(pid)
    $ topics = available_topics(pid)
    $ old = seen_topics(pid)

    add Solid("#070a0bfa")

    vbox:
        xpos 40
        ypos 50
        spacing 4
        text p.title style "grass_label"
        text p.name font gui.name_text_font size 52 color p.color

    add ("images/portrait/%s.png" % pid):
        xalign 0.95
        ypos 24
        zoom 0.55

    vbox:
        xpos 40
        ypos 300
        spacing 12
        xsize 640

        if not topics:
            text "Nothing more to say about that, for now." style "grass_dim"

        for t in topics:
            button:
                style "grass_button"
                xsize 640
                ysize 76
                action Return(("topic", t[0]))
                text t[1] size 25 yalign 0.5 xpos 6

        if old:
            null height 8
            text "ALREADY HEARD" style "grass_label"
            for t in old:
                text "· " + t[1] size 19 color "#6f6c63"

    textbutton "Step away":
        style "grass_button"
        xsize 200
        ysize 56
        xpos 40
        ypos 1166
        action Return(None)


################################################################################
## Notebook
################################################################################

screen notebook():
    modal True
    zorder 70

    add Solid("#070a0bfa")

    text "ALEXANDRIA'S NOTEBOOK" style "grass_label" xpos 40 ypos 50
    text "What she has been told":
        font gui.name_text_font
        size 34
        color "#f2ead2"
        xpos 40
        ypos 78

    frame:
        background Solid("#101617f5")
        xpos 30
        ypos 160
        xsize 660
        ysize 940
        padding (24, 20)

        vbox:
            xsize 600
            spacing 14
            if not notebook:
                text "Nothing yet. Go and be told things." style "grass_dim"
            for entry in notebook:
                text "— " + entry size 22 color "#d9d0bb" xsize 590

    textbutton "World":
        style "grass_button"
        xsize 160
        ysize 56
        xpos 40
        ypos 1166
        text_size 22
        text_xalign 0.5
        action Show("lore")

    textbutton "Close":
        style "grass_button"
        xsize 150
        ysize 56
        xpos 540
        ypos 1166
        text_size 22
        text_xalign 0.5
        action Hide("notebook")


################################################################################
## Dialogue
################################################################################

screen say(who, what):
    window:
        id "window"
        background Solid("#050708e0")
        xfill True
        ysize 340
        yalign 1.0
        padding (44, 28)

        vbox:
            spacing 10
            if who is not None:
                text who id "who":
                    font gui.name_text_font
                    size 29
                    color gui.accent_color
            text what id "what":
                size 28
                color "#f0e8d7"
                line_spacing 8

style say_label is text:
    font gui.name_text_font
    size 29
    color gui.accent_color

style say_dialogue is text:
    size 28
    color "#f0e8d7"
    line_spacing 8


################################################################################
## The stage
################################################################################

transform bg_drift:
    subpixel True
    zoom 1.05
    xalign 0.5
    yalign 0.5
    linear 26.0 xalign 0.58
    linear 26.0 xalign 0.42
    repeat

transform char_in:
    alpha 0.0
    yoffset 20
    easein 0.30 alpha 1.0 yoffset 0

transform char_out:
    easeout 0.22 alpha 0.0


################################################################################
## Choices
################################################################################

screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.55
        spacing 12

        for i in items:
            textbutton i.caption action i.action:
                xsize 600
                padding (26, 18)
                background Frame(Solid("#101516ee"), 6, 6)
                hover_background Frame(Solid("#2a3436ee"), 6, 6)
                text_size 26
                text_color "#e6ddca"
                text_hover_color "#f7f0dd"


################################################################################
## Main menu
################################################################################

screen main_menu():
    tag menu

    add "images/bg/bg_grass.jpg"
    add Solid("#070a0b70")

    vbox:
        xalign 0.5
        ypos 210
        spacing 12
        text "THE GRASS":
            font gui.name_text_font
            size 78
            color "#f4ecd6"
            xalign 0.5
            kerning 8
        text "a sandbox visual novel of Faeblue" size 24 color "#c9b071" xalign 0.5
        add Solid("#c9b07166", xsize=260, ysize=1) xalign 0.5

    vbox:
        xalign 0.5
        ypos 620
        spacing 8

        textbutton "Begin the storm" action Start():
            xsize 420 padding (18, 16) text_xalign 0.5 xfill True
            background Frame(Solid("#12181999"), 6, 6) hover_background Frame(Solid("#283233cc"), 6, 6)
            text_size 26 text_font gui.name_text_font text_color "#e8dfc9" text_hover_color "#fff8e4"
        textbutton "Load" action ShowMenu("load"):
            xsize 420 padding (18, 16) text_xalign 0.5 xfill True
            background Frame(Solid("#12181999"), 6, 6) hover_background Frame(Solid("#283233cc"), 6, 6)
            text_size 26 text_font gui.name_text_font text_color "#e8dfc9" text_hover_color "#fff8e4"
        textbutton "Options" action ShowMenu("preferences"):
            xsize 420 padding (18, 16) text_xalign 0.5 xfill True
            background Frame(Solid("#12181999"), 6, 6) hover_background Frame(Solid("#283233cc"), 6, 6)
            text_size 26 text_font gui.name_text_font text_color "#e8dfc9" text_hover_color "#fff8e4"
        textbutton "Credits" action ShowMenu("about"):
            xsize 420 padding (18, 16) text_xalign 0.5 xfill True
            background Frame(Solid("#12181999"), 6, 6) hover_background Frame(Solid("#283233cc"), 6, 6)
            text_size 26 text_font gui.name_text_font text_color "#e8dfc9" text_hover_color "#fff8e4"

    text "vertical slice  ·  prototype  ·  v[config.version]":
        xalign 0.5
        ypos 1214
        size 17
        color "#8d897e"


################################################################################
## Game menus (save / load / options / about)
################################################################################

screen navigation():
    pass

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu

    add Solid("#070a0bf7")

    text title:
        style "grass_label"
        xpos 84
        ypos 34

    frame:
        background Solid("#101617f5")
        xpos 30
        ypos 90
        xsize 660
        ysize 1010
        padding (22, 20)

        if scroll == "viewport":
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                yinitial yinitial
                vbox:
                    transclude
        else:
            transclude

    textbutton "Back":
        style "grass_button"
        xsize 150
        ysize 56
        xpos 540
        ypos 1166
        action Return()

screen about():
    tag menu
    use game_menu("ABOUT"):
        vbox:
            spacing 16
            add "images/bg/bg_gate.jpg" xsize 600 ysize 320
            text "[config.name!t]" size 32 font gui.name_text_font color gui.accent_color
            text "[config.version]" size 20 color grass_dim
            text "[gui.about!t]" size 22 color "#ddd4c0"

screen save():
    tag menu
    use game_menu("SAVE"):
        vpgrid:
            cols 2
            spacing 12
            ysize 960
            scrollbars "vertical"
            mousewheel True

            for i in range(1, 7):
                button:
                    style "grass_button"
                    action FileAction(i)
                    xsize 296
                    ysize 132
                    vbox:
                        spacing 2
                        text ("%d" % i) size 30 font gui.name_text_font color gui.accent_color
                        text "[FileTime(i, format='%Y-%m-%d %H:%M')]" size 16 color grass_dim
                        text "[FileSaveName(i)]" size 18

screen load():
    tag menu
    use game_menu("LOAD"):
        vpgrid:
            cols 2
            spacing 12
            ysize 960
            scrollbars "vertical"
            mousewheel True

            for i in range(1, 7):
                button:
                    style "grass_button"
                    action FileAction(i)
                    xsize 296
                    ysize 132
                    vbox:
                        spacing 2
                        text ("%d" % i) size 30 font gui.name_text_font color gui.accent_color
                        text "[FileTime(i, format='%Y-%m-%d %H:%M')]" size 16 color grass_dim
                        text "[FileSaveName(i)]" size 18

screen preferences():
    tag menu
    use game_menu("OPTIONS"):

        vbox:
            spacing 18
            xsize 600

            text "Text speed" style "grass_label"
            bar value Preference("text speed") xsize 580 ysize 22:
                left_bar Solid("#c9b071")
                right_bar Solid("#252c2d")
                thumb None

            text "Auto-forward delay" style "grass_label"
            bar value Preference("auto-forward time") xsize 580 ysize 22:
                left_bar Solid("#c9b071")
                right_bar Solid("#252c2d")
                thumb None

            text "Music volume" style "grass_label"
            bar value Preference("music volume") xsize 580 ysize 22:
                left_bar Solid("#c9b071")
                right_bar Solid("#252c2d")
                thumb None

            text "Sound volume" style "grass_label"
            bar value Preference("sound volume") xsize 580 ysize 22:
                left_bar Solid("#c9b071")
                right_bar Solid("#252c2d")
                thumb None

            null height 10

            text "Display" style "grass_label"
            hbox:
                spacing 12
                textbutton "Window":
                    style "grass_button"
                    action Preference("display", "window")
                    text_size 22
                textbutton "Fullscreen":
                    style "grass_button"
                    action Preference("display", "fullscreen")
                    text_size 22

            null height 10

            text "Accessibility" style "grass_label"
            textbutton "Self-voicing":
                style "grass_button"
                action Preference("self voicing", "toggle")
                text_size 22

            null height 10

            text "Progress" style "grass_label"
            text "Places visited: [len(visited)] / 10" size 21 color "#d9d0bb"
            text "Notebook entries: [len(notebook)]" size 21 color "#d9d0bb"


style pref_bar is bar:
    left_gutter 0
    right_gutter 0
    thumb None
    thumb_shadow None

style pref_bar:
    xsize 580
    ysize 24

################################################################################
## Small screens Ren'Py expects
################################################################################

screen notify(message):
    zorder 100
    frame at notify_appear:
        background Solid("#0e1214f2")
        xalign 0.5
        ypos 160
        padding (20, 12)
        text "[message!tq]" size 21 color gui.accent_color
    timer 2.5 action Hide("notify")

transform notify_appear:
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        linear 0.4 alpha 0.0

screen nvl(dialogue, items=None):
    pass

screen skip_indicator():
    zorder 100
    text "skipping" size 18 color grass_dim xpos 24 ypos 40
