## events.rpy
##
## Story events that happen to the sandbox, rather than because Alexandria
## asked for them. These are what make the loop feel like a place instead
## of a menu: the storm advances, a caravan comes in, and somewhere out in
## the grey, the thing that is walking keeps walking.

## --------------------------------------------------------------------------
## The caravan
## --------------------------------------------------------------------------

label caravan_arrives:

    $ caravan_state = "arrived"
    $ location = "gate"
    $ visited.add("gate")

    scene bg gate with slowfade
    $ renpy.show("bg gate", at_list=[bg_drift])

    n "Mid-morning, with the rain coming in sideways, the gateward's bell rings twice. Twice is not the alarm. Twice is the noise Hella makes when something has arrived."

    n "A wagon comes up out of the Grass and into the road: high, patched, leaning, and drawn by two ponies that look like they have opinions about this."

    show sprite seppa at sprite_mid, char_in
    seppa "Salt fish. Lamp oil. Sailcloth. A barrel of something the school will deny."

    seppa "And a letter for Elandi, which has ridden eleven days in a dry box and is, I am pleased to report, still dry."

    a "You made it."

    seppa "I made it. The Grass made its point on the way. We are not sailing back West. Not this season. The route we came by is not there any more."

    $ note("The caravan has arrived from the Western coasts. It cannot sail back West — the route is gone.", "caravan_here")
    $ known.add("caravan_here")

    hide sprite seppa with char_out

    n "The wagon is drawn up in the yard of the Salt & Lantern, and Hella does the thing Hella does: it queues."

    $ renpy.notify("The Western caravan has made it in.")

    return


## --------------------------------------------------------------------------
## The fifth storm
## --------------------------------------------------------------------------

label fifth_storm:

    ## A set piece for the end of the slice. Triggered when the player has
    ## done enough of the village, or when the clock runs out.
    scene bg gate with slowfade
    n "The fifth storm comes down the pass like something with a purpose."

    return


## --------------------------------------------------------------------------
## Triggers, checked every time Alexandria travels or waits
## --------------------------------------------------------------------------

label check_story:

    ## The caravan is late, then it is not.
    if caravan_state == "overdue" and storm_day >= 3:
        call caravan_arrives from _event_caravan
        return

    ## The slice has a soft ending: enough of the village heard, or out of days.
    if has("council_ready") and trust_hellers >= 3 and trust_grass >= 3 and storm_day >= 4:
        jump ending_wrap

    if storm_day >= 6:
        jump ending_wrap

    return
