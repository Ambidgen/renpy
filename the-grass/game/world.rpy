## world.rpy
##
## Faeblue, Hella, and the ten places the slice is made of.
##
## Everything about the sandbox that is *data* lives here: the locations,
## the cast, who is present and when, and the small story flags. The
## writing that uses that data lives in story.rpy and people.rpy.

init -10 python:

    class Location(object):
        """A navigable place in the slice."""

        def __init__(self, id, name, bg, blurb, links=(), people=(),
                     map_pos=(0.5, 0.5), indoor=False, sub=""):
            self.id = id
            self.name = name
            self.bg = bg
            self.blurb = blurb
            self.links = list(links)
            self.people = list(people)
            self.map_pos = map_pos
            self.indoor = indoor
            self.sub = sub

        def __repr__(self):
            return "<Location %s>" % self.id

    class Person(object):
        """Someone Alexandria can talk to."""

        def __init__(self, id, name, color, title, topics=()):
            self.id = id
            self.name = name
            self.color = color
            self.title = title
            self.topics = list(topics)

        def __repr__(self):
            return "<Person %s>" % self.id


## The ten locations of the slice. map_pos is in map-sheet space: x and y
## run 0..1 from left to right and from the bottom of the valley (the
## palisade) to the top (the Grass and the caravan camp).

define LOCATIONS = [
    Location(
        "gate", "The East Gate", "bg/bg_gate.jpg",
        "The timbers are wet and the road out is a river of mud. Beyond the palisade the weather is already the Grass's weather.",
        links=["market", "pass", "watchtower"],
        people=["corin", "harrow"],
        map_pos=(0.50, 0.84),
        sub="Hella"),
    Location(
        "market", "Market Row", "bg/bg_market.jpg",
        "Canvas awnings, wet cobbles, and turnips that have been rained on twice. The whole of Hella is buying and selling at once.",
        links=["gate", "inn", "moot", "school"],
        people=["marta", "seppa"],
        map_pos=(0.36, 0.66),
        sub="Hella"),
    Location(
        "moot", "The Moot Hall", "bg/bg_moot.jpg",
        "The long tables are stacked against the walls, which means the moot is not sitting. The chair on the dais is still draped in the old colours.",
        links=["market", "house"],
        people=["elandi"],
        map_pos=(0.24, 0.52),
        indoor=True,
        sub="Hella"),
    Location(
        "inn", "The Salt & Lantern", "bg/bg_inn.jpg",
        "A fire, a cauldron, and twenty years of smoke in the beams. The only room in Hella that is ever properly warm.",
        links=["market"],
        people=["marta", "corin"],
        map_pos=(0.60, 0.60),
        indoor=True,
        sub="Hella"),
    Location(
        "school", "The Witches' School", "bg/bg_school.jpg",
        "Pale stone, storm-sigils re-chalked on the flags, and blue glass charms knocking together in the wind.",
        links=["market", "house"],
        people=["ivo", "tamsin"],
        map_pos=(0.74, 0.48),
        sub="Hella Academy"),
    Location(
        "house", "The Mayor's House", "bg/bg_house.jpg",
        "Your mother's house. Your house. The fire is lit, the desk is not hers any more, and nobody has said so out loud.",
        links=["moot", "school", "pass"],
        people=["elandi"],
        map_pos=(0.46, 0.40),
        indoor=True,
        sub="Hella"),
    Location(
        "pass", "The Long Pass", "bg/bg_pass.jpg",
        "The road goes down between the mountains toward the sea, thin as a thread. The waystones wear blue ribbons older than you are.",
        links=["gate", "house", "grass"],
        people=["tamsin", "harrow"],
        map_pos=(0.22, 0.30),
        sub="The coastal pass"),
    Location(
        "watchtower", "The Watchtower", "bg/bg_watchtower.jpg",
        "The brazier is banked and the chart is out, and the stone is cold in the way stone is cold when nobody has been stationed here for a while.",
        links=["gate", "grass"],
        people=["oren", "seppa"],
        map_pos=(0.78, 0.30),
        sub="The border watch"),
    Location(
        "grass", "The Great Dead Grass", "bg/bg_grass.jpg",
        "Grey, silver, and moving. The weeds are over your knees, and they are not so much growing out of soil as out of the idea of soil.",
        links=["pass", "watchtower", "camp"],
        people=["vashk"],
        map_pos=(0.52, 0.16),
        sub="The borderlands"),
    Location(
        "camp", "The Caravan Camp", "bg/bg_camp.jpg",
        "A patched wagon, a banked fire, and a hollow in the Grass used by other caravans on other nights for a very long time.",
        links=["grass"],
        people=["vashk", "seppa"],
        map_pos=(0.30, 0.06),
        sub="The Western caravan"),
]


define PEOPLE = {
    "alexandria": Person("alexandria", "Alexandria", "#e8dcb4", "the mayor's daughter"),
    "elandi": Person("elandi", "Elandi", "#d9b0a0", "the late mayor's wife",
        topics=[
            ("ledger", "The tally-board and the Grass column", None),
            ("father", "About your father", None),
            ("letters", "The letters on the desk", "has('caravan_rumour')"),
            ("ravagers", "What the Ravagers actually want", "has('vashk_met')"),
            ("decision", "What Hella should do", "has('council_ready')"),
        ]),
    "marta": Person("marta", "Marta", "#e2c184", "innkeeper of the Salt & Lantern",
        topics=[
            ("orders", "The caravan's standing order", None),
            ("storms", "How long the storms last", None),
            ("corin", "What Corin is like off duty", "has('corin_met')"),
            ("vashk", "The beastman in the Grass", "has('vashk_met')"),
        ]),
    "ivo": Person("ivo", "Sister Ivo", "#a8c8e8", "storm-warden of the school",
        topics=[
            ("school", "What the school teaches", None),
            ("sigils", "Reading the Grass", None),
            ("tamsin", "About Tamsin", "has('tamsin_met')"),
            ("warding", "Warding the palisade", "has('ravager_sign')"),
        ]),
    "oren": Person("oren", "Master Oren", "#c8b8e8", "master of the border watch",
        topics=[
            ("watch", "What the watch is for", None),
            ("pins", "The pins in the chart", None),
            ("vashk", "The scout you met", "has('vashk_met')"),
            ("tribes", "The Ravager tribes", "has('ravager_sign')"),
        ]),
    "tamsin": Person("tamsin", "Tamsin", "#a8d8b0", "third-year of Hella Academy",
        topics=[
            ("academy", "Life at the academy", None),
            ("grass", "Why she reads the Grass", None),
            ("ivo", "What Sister Ivo is really like", "has('ivo_met')"),
            ("offer", "Her offer to walk out with you", "has('ravager_sign')"),
        ]),
    "harrow": Person("harrow", "Harrow", "#b8c890", "drover, out of the West",
        topics=[
            ("droving", "How a drover gets through", None),
            ("half", "The half that get lost", None),
            ("ork", "Being orkish in Hella", None),
            ("caravan", "Where the caravan is", "has('caravan_rumour')"),
        ]),
    "seppa": Person("seppa", "Seppa", "#d8a8a0", "caravan trader, orkish",
        topics=[
            ("goods", "What she brought through", None),
            ("route", "The route through the Grass", None),
            ("harrow", "Harrow, her drover", "has('harrow_met')"),
            ("sign", "The sign her scouts saw", "has('ravager_sign')"),
        ]),
    "vashk": Person("vashk", "Vashk", "#c0b0a0", "of the Ravager tribes",
        topics=[
            ("tribe", "What she is doing here", None),
            ("wants", "What the tribes want", None),
            ("hellers", "What she thinks of Hella", None),
            ("warning", "The warning she carries", "has('ravager_sign')"),
        ]),
    "corin": Person("corin", "Corin", "#d8c890", "gateward of Hella",
        topics=[
            ("gate", "How the gate is kept", None),
            ("stormcount", "The storm-count chalked on the post", None),
            ("rumours", "What he has heard about the Grass", "has('ravager_sign')"),
        ]),
}


init python:

    def loc(lid):
        for l in LOCATIONS:
            if l.id == lid:
                return l
        raise Exception("No such location: %r" % lid)

    def person(pid):
        if pid not in PEOPLE:
            raise Exception("No such person: %r" % pid)
        return PEOPLE[pid]

    def present(pid):
        """
        Who is around right now.

        Small readable rules rather than a scheduler: the orkish caravan
        only exists once it has arrived, Tamsin's school day ends at the
        ninth bell, and Vashk is only found out in the Grass.
        """
        if pid in ("elandi", "corin", "marta", "ivo", "oren", "harrow"):
            return True
        if pid == "seppa":
            return caravan_state != "overdue"
        if pid == "tamsin":
            return bell < 9
        if pid == "vashk":
            return has("vashk_met") or location in ("grass", "camp")
        return True

    def people_here(lid):
        return [person(pid) for pid in loc(lid).people if present(pid)]

    def hour_name(b):
        names = ["last bell", "third bell", "fourth bell", "fifth bell",
                 "sixth bell", "seventh bell", "eighth bell", "ninth bell",
                 "tenth bell", "eleventh bell", "noon bell",
                 "evening bell", "last bell"]
        b = max(0, min(12, b))
        return names[b] if b else "last bell"

    def note(text, flag=None):
        """Alexandria writes something down. This is the tutorial's memory."""
        if text not in notebook:
            notebook.append(text)
        if flag:
            known.add(flag)

    def has(flag):
        return flag in known

    def change_location(lid):
        store.location = lid
        visited.add(lid)


## ------------------------------------------------------------ story state

default location = "gate"
default visited = set()
default notebook = []
default known = set()
default talked = set()

default bell = 2
default storm_day = 1
default caravan_state = "overdue"

## small reputations, shown in the notebook screen as the slice's progress
default trust_hellers = 0
default trust_school = 0
default trust_grass = 0
