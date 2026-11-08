################################################################################
## The Grass - visual identity
##
## A vertical (9:16) stage. Everything here is built for 720x1280.
################################################################################

init offset = -2

init python:
    gui.init(720, 1280)

define config.check_conflicting_properties = True


################################################################################
## Colours
##
## Ash, slate, wet wool, and the two accents Hella actually uses: the
## ochre of its banners and the blue-green of its witch-glass.

define gui.accent_color = "#c9b071"
define gui.idle_color = "#9a9486"
define gui.idle_small_color = "#bdb6a6"
define gui.hover_color = "#e8d9a8"
define gui.selected_color = "#f4ecd6"
define gui.insensitive_color = "#6b665c80"

define gui.muted_color = "#3b3629"
define gui.hover_muted_color = "#6b5d3a"

define gui.text_color = "#efe7d6"
define gui.interface_text_color = "#e6ddca"

## Story-specific colours, used by the notebook and the location header.
define grass_ink = "#0f1210"
define grass_panel = "#14181a"
define grass_edge = "#c9b071"
define grass_blue = "#7fb4bd"
define grass_dim = "#9a9486"


################################################################################
## Fonts
##

define gui.text_font = "fonts/Alegreya.ttf"
define gui.name_text_font = "fonts/Cinzel.ttf"
define gui.interface_text_font = "fonts/Alegreya.ttf"

## Used for location titles and the title screen.
define gui.title_font = "fonts/Cinzel.ttf"
define gui.title_text_size = gui.scale(58)

define gui.text_size = gui.scale(30)
define gui.name_text_size = gui.scale(30)
define gui.interface_text_size = gui.scale(26)
define gui.label_text_size = gui.scale(28)
define gui.notify_text_size = gui.scale(24)
define gui.title_text_size = gui.scale(58)


################################################################################
## Music and sound
##

define config.main_menu_music = None


################################################################################
## Transitions
##

define fade = Fade(0.35, 0.1, 0.45)
define dissolve = Dissolve(0.35)
define moveinright = MoveTransition(0.35)
define slowfade = Fade(1.0, 0.5, 1.4)

## A quiet horizontal drift used on the backgrounds, so still art breathes.
transform bg_drift:
    subpixel True
    zoom 1.04
    xalign 0.5
    yalign 0.5
    linear 22.0 xalign 0.56
    linear 22.0 xalign 0.44
    repeat

## The character sprite entrance.
transform char_in:
    alpha 0.0
    yoffset 22
    easein 0.35 alpha 1.0 yoffset 0

transform char_out:
    easeout 0.25 alpha 0.0 yoffset 14


################################################################################
## Dialogue
##

define gui.dialogue_xpos = gui.scale(96)
define gui.dialogue_ypos = gui.scale(56)
define gui.dialogue_width = gui.scale(720 - 192)
define gui.dialogue_text_xalign = 0.0

define gui.name_xpos = gui.scale(96)
define gui.name_ypos = gui.scale(0)
define gui.name_xalign = 0.0
define gui.name_text_xalign = 0.0

define gui.dialogue_line_spacing = gui.scale(6)

## The dialogue window sits over the lower third of the art but leaves the
## character sprites visible above it.
define gui.textbox_height = gui.scale(300)

## The choice menu, used for conversation topics.
define gui.choice_button_width = gui.scale(528)
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(gui.scale(20), gui.scale(14),
                                            gui.scale(20), gui.scale(14))
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.scale(26)
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = "#e6ddca"
define gui.choice_button_text_hover_color = "#f4ecd6"
define gui.choice_button_text_insensitive_color = "#6b665c"

define gui.choice_spacing = gui.scale(10)


################################################################################
## Buttons and frames used by screens.rpy
##

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(gui.scale(12), gui.scale(8), gui.scale(12), gui.scale(8))
define gui.button_tile = False

define gui.frame_borders = Borders(gui.scale(10), gui.scale(10), gui.scale(10), gui.scale(10))

define gui.slot_button_borders = Borders(gui.scale(6), gui.scale(6), gui.scale(6), gui.scale(6))

define gui.navigation_xpos = gui.scale(90)
define gui.skip_ypos = gui.scale(15)
define gui.notify_ypos = gui.scale(45)
define gui.choice_spacing = gui.scale(10)
define gui.navigation_spacing = gui.scale(6)
define gui.pref_spacing = gui.scale(15)
define gui.pref_button_spacing = gui.scale(4)
define gui.page_spacing = gui.scale(0)
define gui.slot_spacing = gui.scale(15)
define gui.main_menu_text_xalign = 0.5
