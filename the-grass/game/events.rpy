## events.rpy
##
## Story events that happen to the sandbox rather than because Alexandria
## asked for them. These are what make the loop feel like a place instead
## of a menu.

## --------------------------------------------------------------------------
## The caravan
## --------------------------------------------------------------------------

label caravan_arrives:

    $ caravan_state = "arrived"
    $ location = "gate"
    $ visited.add("gate")
    $ _seen.add("gate")

    scene black with fade
    $ renpy.show("stage", at_list=[bg_drift])
    with dissolve

    n "Mid-morning, with the rain coming in sideways, the gateward's bell rings twice. Twice is not the alarm. Twice is the noise Hella makes when something has arrived."

    n "A wagon comes up out of the Grass and into the road: high, patched, leaning, and drawn by two ponies that look like they have opinions about this."

    show sprite seppa at sprite_mid, char_in
    seppa "Salt fish. Lamp oil. Sailcloth. A barrel of something the school will deny."

    seppa "And a letter for Elandi, which has ridden eleven days in a dry box and is, I am pleased to report, still dry."

    a "You made it."

    seppa "I made it. The Grass made its point on the way. We are not sailing back West. Not this season. The route we came by is not there any more."

    a "Then how do you get home?"

    seppa "By waiting. By the last week of the storms, or by the coast road, which is three weeks and a mountain. I have not decided which of those is the less cheerful."

    $ note("The caravan has arrived from the Western coasts. It cannot sail back West — the southern route is gone for the season.", "caravan_here")
    $ known.add("caravan_here")

    hide sprite seppa with dissolve

    n "The wagon is drawn up in the yard of the Salt & Lantern, and Hella does the thing Hella does: it queues."

    $ renpy.notify("The Western caravan has made it in.")

    return


## --------------------------------------------------------------------------
## Triggers, checked after every action that spends a bell
## --------------------------------------------------------------------------

default ending_pending = False

label check_story:

    ## The caravan is late, then it is not.
    if caravan_state == "overdue" and storm_day >= 2:
        call caravan_arrives from _event_caravan
        return

    ## Enough of the village has been heard: the slice has a shape.
    if has("council_ready") and trust_hellers >= 3 and trust_grass >= 3:
        $ ending_pending = True
        return

    ## Or the storm season simply runs its course.
    if storm_day >= 4:
        $ ending_pending = True
        return

    return
