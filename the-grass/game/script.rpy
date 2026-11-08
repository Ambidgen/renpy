## script.rpy
##
## The prologue, and the end of the slice.
##
## The tutorial is wrapped around a real story: Alexandria comes home for
## the storm season, the caravan is overdue, and something is moving in the
## Great Dead Grass. Everything after the prologue is sandbox.

define n = Character(None, what_color="#cdc5b2", what_italic=True)

## One character object per speaker. The name colours match the portrait
## panels in the HUD so the cast reads consistently.
define a = Character("Alexandria", color="#e8dcb4")
define ma = Character("Elandi", color="#d9b0a0")
define corin = Character("Corin", color="#d8c890")
define marta = Character("Marta", color="#e2c184")
define ivo = Character("Sister Ivo", color="#a8c8e8")
define oren = Character("Master Oren", color="#c8b8e8")
define tamsin = Character("Tamsin", color="#a8d8b0")
define harrow = Character("Harrow", color="#b8c890")
define seppa = Character("Seppa", color="#d8a8a0")
define vashk = Character("Vashk", color="#c0b0a0")

## Sprites -----------------------------------------------------------------

image side alexandria = "images/portrait/alexandria.png"

## The stage is 720x1280 and the dialogue box occupies the bottom 340px,
## so sprites stand on a floor line at y=960 with their feet on it.
## Sprites stand on a floor line above the dialogue box.
define SPRITE_FLOOR = 1010
define SPRITE_ZOOM = 1.75

transform sprite_left:
    subpixel True
    xalign 0.24
    ypos SPRITE_FLOOR
    yanchor 1.0
    zoom SPRITE_ZOOM

transform sprite_right:
    subpixel True
    xalign 0.76
    ypos SPRITE_FLOOR
    yanchor 1.0
    zoom SPRITE_ZOOM

transform sprite_mid:
    subpixel True
    xalign 0.5
    ypos SPRITE_FLOOR
    yanchor 1.0
    zoom SPRITE_ZOOM

image sprite alexandria = "images/char/alexandria.png"
image sprite elandi = "images/char/elandi.png"
image sprite marta = "images/char/marta.png"
image sprite ivo = "images/char/sister_ivo.png"
image sprite oren = "images/char/master_oren.png"
image sprite tamsin = "images/char/tamsin.png"
image sprite harrow = "images/char/harrow.png"
image sprite seppa = "images/char/seppa.png"
image sprite vashk = "images/char/vashk.png"
image sprite corin = "images/char/corin.png"

## The stage background follows store.location, so travel is a single
## variable change and the loop always shows the right art.
init python:
    def _stage_image(st, at):
        path = "images/" + loc(store.location).bg
        return Transform(path, zoom=1.05, xalign=0.5, yalign=0.5), None

image stage = DynamicDisplayable(_stage_image)

## The backgrounds are also individually available, e.g. `scene bg gate`.
image bg gate = "images/bg/bg_gate.jpg"
image bg market = "images/bg/bg_market.jpg"
image bg moot = "images/bg/bg_moot.jpg"
image bg inn = "images/bg/bg_inn.jpg"
image bg school = "images/bg/bg_school.jpg"
image bg house = "images/bg/bg_house.jpg"
image bg pass = "images/bg/bg_pass.jpg"
image bg watchtower = "images/bg/bg_watchtower.jpg"
image bg grass = "images/bg/bg_grass.jpg"
image bg camp = "images/bg/bg_camp.jpg"


label start:

    $ quick_menu = False

    scene expression "images/bg/bg_grass.jpg" with slowfade


    n "The Grass does not look like a border. It looks like weather that has been left out too long."

    n "From the pass road, in the last of the light, it goes on west until it is only a colour. Grey under grey. A whole sea of it, and no far shore anyone has agreed on."

    n "Behind you, the mountains. Below you, in the fold of the valley, the palisade and the lights of Hella, where you were born and where you have not been for four years."

    scene expression "images/bg/bg_gate.jpg" with slowfade

    n "The gate is open, because in Hella the gate is always open until the storm-count reaches six."

    show sprite corin at sprite_mid, char_in
    corin "That'll be the mayor's daughter, then. Four years, and you come back in this."

    a "Hello, Corin. You've grown a beard."

    corin "It's a storm beard. You grow one so you've got something to talk about."

    corin "Your mother's in the moot hall. She's been in the moot hall since the last bell, and the last bell was a while ago."

    a "Is she all right?"

    corin "She's the mayor's widow running a village with a school in it and no mayor. She's exactly as all right as that."

    $ note("Corin keeps the East Gate. In a storm, the gate stays open until the storm-count reaches six.", "corin_met")
    $ known.add("corin_met")
    $ visited.add("gate")

    hide sprite corin with dissolve
    scene expression "images/bg/bg_moot.jpg" with fade

    n "The moot hall smells of wet wool and cold ash. Your mother is at the long table with the ledgers, and she does not stand up when she sees you, which is how you know she is glad."

    show sprite elandi at sprite_mid, char_in
    ma "You came up the pass in the rain."

    a "I came up the pass in the rain."

    ma "Good. It's the only road. Sit down, Alexandria. I need you to hear a number."

    ma "Eleven days ago the caravan left the Western coasts. A fortnight is usual, in the storms. Nine days is what it takes if the Grass is kind, and the Grass is not kind."

    ma "It's overdue. And this morning Harrow came in from the drovers' road with a story about lights out past the milepost, and Vashk — you don't know Vashk — has been seen at the edge of the weeds with her people's colours on."

    a "Ravagers."

    ma "Orkish and beastmen, in the dead grass, in the storm season. That is the sentence I have been failing to say to the moot for two days."

    $ note("The caravan from the Western coasts is overdue. A fortnight is usual; it has been eleven days.", "caravan_rumour")
    $ note("Ravager colours have been seen at the edge of the Great Dead Grass.", "ravager_sign")

    ma "I am not asking you to be mayor. Hella has a moot and a school and a watch, and it will get on with the business of being frightened without a mayor's daughter to help it."

    ma "I am asking you to go and be in the village. Talk to people. Look at things. You were always good at the part nobody tells you about, which is listening."

    ma "The caravan will wait out the storms or it won't. But we have a fortnight of storm season and a village full of people who need to decide whether to be afraid, and I would rather you decided with them than at me."

    a "That's not a task. That's a whole village."

    ma "Yes."

    hide sprite elandi with dissolve

    scene expression "images/bg/bg_gate.jpg" with fade

    n "There are ten places in Hella worth being, and the storm season is not long. Somewhere out in the grey, a caravan is deciding whether to exist."

    n "Go and be in the village."

    $ renpy.notify("The sandbox is open. Use Map to travel, and the names on the left to talk.")

    jump explore


## -------------------------------------------------------------- the ending

label ending_wrap:

    $ renpy.hide_screen("location_hud")

    scene black with slowfade
    $ renpy.show("stage", at_list=[bg_drift])
    with dissolve

    n "The fifth storm comes down the pass before you are ready for it. They come in fives in Hella, and the fifth is the one that changes the season."

    if caravan_state == "arrived":
        n "The caravan is drawn up in the inn yard with its canvas tied down and its ponies in the stable, which means that for the first time in a fortnight, Hella has more in it than it started with."
    else:
        n "The caravan is still out in the Grass, or it is not, and there is no way from Hella to tell which."

    if has("vashk_warning"):
        n "Out past the milepost, the thing that walked in a straight line has stopped walking. Vashk was right about the direction and wrong about the speed, which is the most anyone at a border can be."

    if has("council_ready") and trust_hellers >= 3 and trust_grass >= 3:
        scene expression "images/bg/bg_moot.jpg" with slowfade

        n "The moot hall is full. The tables are along the walls and the chair on the dais is still draped in the old colours, and your mother is standing beside it rather than in it."

        n "Vashk stands at the door with her hands where everyone can see them. Corin stands behind her, because he is a gateward and that is what a gateward does."

        if has("tamsin_companion"):
            n "Tamsin stands at the chart with her finger on a hollow she has read at three different times of day, and she does not once look at the coast for permission."
        else:
            n "Tamsin stands at the chart anyway, because nobody has told her not to."

        n "The tally-board goes up on its hooks. The Grass column is still empty. It will not be empty by the end of the session, and everyone in the hall knows it."

        n "Hella does not decide to be brave. It decides to write the number down, which is the same thing in a border village, done slowly."

    elif trust_grass > trust_hellers:
        n "You spend the fifth storm out past the milepost with the people who read the dust, and Hella spends it in its own rooms, and the two of you will have to argue about that later."

    else:
        n "You spend the fifth storm in the inn, with Marta, and the fire, and twenty people who are all talking at once. It is not a decision. It is what a village is before it makes one."

    scene expression "images/bg/bg_gate.jpg" with slowfade

    n "The storm season turns. Whether the caravan sails, and what Hella decides it is, is the rest of the game — but the slice ends here."

    n "You have been to [len(visited)] of the ten places, and written [len(notebook)] things in the notebook."

    if len(visited) < 5:
        n "Hella is bigger than that. It will keep."

    n "The Grass is still grey, and still moving, and still the only road there is."

    $ renpy.notify("End of the slice. Thank you for playing.")

    return
