## explore.rpy
##
## The sandbox loop.
##
## Alexandria stands somewhere in Hella. The HUD offers Map, Look, Notes,
## Wait, and every person present. Choosing one runs a piece of story and
## then drops her back here, so the ten locations are freely navigable and
## nothing has to be done in a fixed order.

default _seen = set()
default _dest = ""
default _who = ""
default _arrive = ""

default _looked = set()


label explore:

    while True:

        ## Keep the scene in sync with wherever she is.
        if not renpy.showing("stage"):
            scene black
            $ renpy.show("stage", at_list=[bg_drift])

        $ renpy.show_screen("location_hud")
        $ _result = renpy.call_screen("location_hud")
        $ renpy.hide_screen("location_hud")

        if _result is None:
            pass

        elif _result[0] == "go":
            $ _dest = _result[1]
            call travel from _explore_travel

        elif _result[0] == "talk":
            $ _who = _result[1]
            call talk_to from _explore_talk

        elif _result == "look":
            call look_around from _explore_look

        elif _result == "notes":
            $ renpy.call_screen("notebook")

        elif _result == "wait":
            call wait_here from _explore_wait

        elif _result == "map":
            $ _map = renpy.call_screen("map_screen")
            if _map and _map[0] == "go":
                $ _dest = _map[1]
                call travel from _explore_travel_map

    return


## ---------------------------------------------------------------- travelling

label travel:

    $ change_location(_dest)
    $ bell += 1
    $ renpy.transition(fade)
    $ renpy.notify(loc(_dest).name)

    call arrival_beat from _travel_beat
    call check_story from _travel_story

    return


label arrival_beat:

    if _dest not in _seen:
        $ _seen.add(_dest)
        $ note("Arrived at %s." % loc(_dest).name)
        $ renpy.say(None, describe_arrival(_dest))

    return

init python:

    def describe_arrival(lid):
        """One-line, time-aware description of where Alexandria stands."""
        l = loc(lid)
        if bell >= 10:
            tail = " The light is going; the lamps are coming on one at a time."
        elif bell >= 7:
            tail = " The day has settled into a wet, even grey."
        else:
            tail = ""
        return l.blurb + tail


## ------------------------------------------------------------------ looking

label look_around:

    $ renpy.say(None, look_text(location))

    if location not in _looked:
        $ _looked.add(location)
        $ note("Looked closely at %s." % loc(location).name)

    $ bell += 1
    call check_story from _look_story

    return

init python:

    def look_text(lid):
        """A deeper look at the place, coloured by what is actually there."""
        l = loc(lid)
        extra = {
            "gate": "Corin has chalked the day's storm-count on the gatepost: four. Harrow's drover cart is drawn up inside the palisade, and the mud around it is the only mud in Hella that has been arranged.",
            "market": "Two of the stalls are packed down to their frames. That is what a market does when it expects a caravan, and what it does when it does not.",
            "moot": "The tally-board by the door has the season's levies on it, and a column for the Grass that nobody has filled in since the last mayor died.",
            "inn": "Marta keeps a slate behind the bar with the caravan's standing order chalked on it. It has been half-rubbed-out and rewritten for three weeks.",
            "school": "The courtyard sigils are for wind, not for rain. Someone has been teaching the students to read the Grass.",
            "house": "The desk has three letters on it your mother has not opened, and one she has opened four times.",
            "pass": "Fresh ruts in the road: a heavy cart, coming down, in the last day or so. Nobody has come through the gate.",
            "watchtower": "The chart on the table has pins in it. Two pins are out in the Grass, in places the chart marks as nothing at all.",
            "grass": "The track bends around a hollow and stops. Beyond it, something has flattened a long, straight line through the weeds.",
            "camp": "The wagon's canvas is patched with sailcloth. The patches are from three different ships.",
        }
        return l.blurb + "\n\n" + extra.get(lid, "")


## ------------------------------------------------------------------- waiting

label wait_here:

    $ bell += 1
    if bell > 12:
        $ bell = 1
        $ storm_day += 1
        $ renpy.notify("The night passes. Day %d of the storm." % storm_day)
    else:
        $ renpy.notify(clock_text())

    $ renpy.say(None, wait_text(location))
    call check_story from _wait_story

    return

init python:

    def wait_text(lid):
        if loc(lid).indoor:
            return "You sit with it a while. The rain finds a new part of the roof to come through."
        return "You stand in the weather a while, because the weather in Hella is the closest thing it has to a town crier."


## ------------------------------------------------------------------ talking

label talk_to:

    $ p = person(_who)
    $ renpy.say(None, "You find %s." % p.name)

    while True:

        $ _t = renpy.call_screen("topics_screen", pid=_who)

        if _t is None:
            return

        $ _tid = _t[1]
        $ talked.add((_who, _tid))
        $ bell += 1

        call expression ("topic_" + _who + "_" + _tid) from _talk_topic
        call check_story from _talk_story

    return
