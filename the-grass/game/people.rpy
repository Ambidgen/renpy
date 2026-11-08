## people.rpy
##
## Every topic for every character.
##
## Topics are declared in PEOPLE (world.rpy) and the writing lives here, one
## label per topic: topic_<person>_<topic>. Talking costs a bell, which is
## why the conversation map is worth planning.

## A small helper so entrances look consistent.
init python:
    def enter(pid, pos="mid"):
        renpy.hide("sprite " + pid)
        renpy.show("sprite " + pid, at_list=[{"left": sprite_left,
                                             "right": sprite_right,
                                             "mid": sprite_mid}[pos], char_in])

    def leave(pid):
        renpy.hide("sprite " + pid)


## =============================================================== ELANDI ====
## Alexandria's mother. The political spine of the slice.

label topic_elandi_ledger:

    $ enter("elandi", "mid")
    a "The tally-board's got an empty column. The one marked for the Grass."

    ma "It has been empty since your father died. It used to be filled in every season: how much the Grass took, how much we spent making it not take more."

    ma "Nobody wanted to write the number down. A levy for the Grass is a levy for something that can't be fought and can't be farmed."

    ma "That is what a border is, Alexandria. Not a line. A column nobody wants to fill in."

    $ note("The Grass column on the moot's tally-board has been empty since Alexandria's father died.", "ledger")
    $ trust_hellers += 1

    hide sprite elandi with char_out
    return


label topic_elandi_father:

    $ enter("elandi", "mid")
    a "Do you still keep his things in the hall?"

    ma "I keep the chair. The chair is the moot's, not mine, and the moot has not seen fit to give it to anyone else."

    ma "Your father used to say a border village has three jobs: keep the road open, keep the school full, and keep the Grass out of the conversation at dinner."

    ma "He managed two of the three."

    a "Which two?"

    ma "The first two."

    $ note("The mayor — Alexandria's father — held that Hella has three jobs: the road, the school, and keeping the Grass out of dinner.", "father")
    $ trust_hellers += 1

    hide sprite elandi with char_out
    return


label topic_elandi_letters:

    $ enter("elandi", "mid")
    a "There are letters on your desk. Three sealed, one not."

    ma "The sealed ones are from the coast. The coast writes to Hella as though Hella were a person who could be told what to do."

    ma "The opened one is from the school board, and it is about whether the academy can keep its charter if the border is not safe this season."

    a "And if the caravan doesn't come?"

    ma "Then the board becomes a very different letter, and the school becomes a very different school, and Hella becomes a market town that nobody has a reason to walk to."

    $ note("Hella's economy is the school. Without the caravan and a safe border, the school board may pull the academy's charter.", "letters")
    $ trust_school += 1

    hide sprite elandi with char_out
    return


label topic_elandi_ravagers:

    $ enter("elandi", "mid")
    a "I met one of them. Vashk. She's a scout."

    ma "I know what she is. She has been standing at the edge of the weeds for three days, and Oren has been standing at the tower window for three days, and neither of them has done anything."

    a "She says the tribes aren't raiding this season."

    ma "Every person who has ever raided Hella has said that first."

    a "She says something else is out there."

    ma "Then she should tell the moot. In the hall. With the chart and the ledgers and the whole village watching, the way we do things."

    $ note("Elandi will hear Vashk out — but only at a formal moot session, in the hall.", "moot_promise")
    $ trust_grass += 1

    hide sprite elandi with char_out
    return


label topic_elandi_decision:

    if trust_hellers >= 3 and trust_grass >= 2:
        $ enter("elandi", "mid")
        a "The moot should hear from the Grass and from the village on the same day."

        ma "That is what I was hoping you would say. Not because it is wise. Because I could not have said it and been believed."

        a "Because you're the mayor's widow."

        ma "Because I am the mayor's widow, and every decision I make is a decision about whether my husband was right."

        ma "You are the mayor's daughter. You get to be wrong out loud. Use it."

        $ note("Elandi will call a moot session if Alexandria asks for one.", "council_ready")
        $ trust_hellers += 1
        $ trust_grass += 1

        hide sprite elandi with char_out
        return

    $ enter("elandi", "mid")
    a "What should Hella do?"

    ma "You are asking me the question I have been avoiding. Go and find out what is actually happening in the Grass and among the people, and come back with a thing to decide, not a feeling."

    $ note("Elandi wants a proposal, not a worry: talk to the village and to the Grass before asking her to call a moot.", "decision_hint")

    hide sprite elandi with char_out
    return


## ================================================================= MARTA ====

label topic_marta_orders:

    $ enter("marta", "mid")
    marta "Sit. No — stand, the benches are wet. There's a standing order from the caravan, every season, and it's chalked up behind the bar."

    marta "Two barrels of salt fish, a crate of lamp oil, four bales of sailcloth, and a letter. The letter is the important one and it's never been opened in this inn."

    a "Who's it for?"

    marta "Your mother. Every season. The caravan-master hands it to me, I hand it to Elandi, and I have never once asked what's in it."

    a "Why not?"

    marta "Because in a border village, the person who doesn't ask what's in the letter is the person who gets to keep running the inn."

    $ note("The caravan's standing order includes a sealed letter for Elandi, every season. Marta has never asked what is in it.", "orders")
    $ trust_hellers += 1

    hide sprite marta with char_out
    return


label topic_marta_storms:

    $ enter("marta", "mid")
    a "How long do the storms last?"

    marta "The stormy season runs six weeks. The Grass is only crossable in the first fortnight of it, if you're brave, and the last week, if you're lucky."

    marta "The caravaners who wait it out down at the coast, they sail back West. That's the rule. Wait, don't walk."

    a "And the ones who walk?"

    marta "Some say half of them get lost in the Grass."

    a "And the other half?"

    marta "Some say half is optimistic."

    $ note("The Grass is crossable in the first fortnight of the storm season and the last week. Caravaners usually wait the storms out and sail back West.", "storms")
    $ trust_grass += 1

    hide sprite marta with char_out
    return


label topic_marta_corin:

    $ enter("marta", "mid")
    a "Corin, off duty. What's he like?"

    marta "He's a good gateward and a bad liar. He's been counting the storms on that post since he was fifteen and he's never once been wrong, which on this border is worth more than a sword."

    marta "Also he's in love with my cook and the cook knows and the whole inn knows and Corin has not noticed."

    a "That's cruel."

    marta "It's Hella. We take our entertainment where we can."

    $ note("Corin's storm-count on the gatepost has never been wrong.", "corin_rumour")

    hide sprite marta with char_out
    return


label topic_marta_vashk:

    $ enter("marta", "mid")
    a "You've seen her. The one in the weeds."

    marta "Seen her, fed her, and been paid for it in coin I'd swear came off a Western ship."

    a "You fed a Ravager?"

    marta "I fed a customer. There's a difference in this village and I'd thank you not to lose it."

    $ note("Marta has fed Vashk. Vashk paid in Western coin.", "vashk_fed")
    $ trust_grass += 1

    hide sprite marta with char_out
    return


## =================================================================== IVO ====

label topic_ivo_school:

    $ enter("ivo", "mid")
    ivo "You are Elandi's girl. You have the look of someone who was told to go and listen."

    a "I've been told to go and listen."

    ivo "Good. Most people come here to be told things. The school exists because the coast believes weather can be taught, and Hella exists because the school does."

    ivo "Sixty girls, four mistresses, one courtyard, and a charter older than the palisade."

    $ note("Hella's school is the reason the village exists. Sixty students, four mistresses, an old charter.", "school")
    $ trust_school += 1

    hide sprite ivo with char_out
    return


label topic_ivo_sigils:

    $ enter("ivo", "mid")
    ivo "The sigils in the courtyard are wind-sigils. We do not do rain; rain is a sea problem and we are a mountain problem."

    a "What can you do with wind?"

    ivo "Read it. A wind that has crossed the Grass carries its dust, and the dust has a grain to it. A warden who knows the grain can tell you how far a thing has walked and how long it has been walking."

    ivo "In a bad season, that is the only warning a border gets."

    $ note("Sister Ivo can read wind and Grass-dust: it can tell how far and how long something has travelled.", "sigils")
    $ trust_school += 1
    $ trust_grass += 1

    hide sprite ivo with char_out
    return


label topic_ivo_tamsin:

    $ enter("ivo", "mid")
    a "Tamsin. Third-year."

    ivo "Third-year and better than she knows, which is a dangerous thing to be at nineteen."

    ivo "She has been going down to the edge of the weeds to read the dust on her own. I have not stopped her, because she is right, and I would rather she be right in a courtyard than alone in the Grass."

    a "She's been going out alone?"

    ivo "She has been going out. Whether she has been alone is a different question, and one I am not going to answer for her."

    $ note("Tamsin has been reading Grass-dust outside the palisade, with Sister Ivo's tacit approval.", "tamsin_rumour")
    $ trust_school += 1

    hide sprite ivo with char_out
    return


label topic_ivo_warding:

    $ enter("ivo", "mid")
    a "The Ravager colours. Can the school ward the palisade?"

    ivo "We can ward a gate against weather and a courtyard against wind. We cannot ward a village against people, and I would not do it if I could."

    ivo "A ward that turns people away turns the caravan away too. In a border village, the thing keeping you safe and the thing keeping you poor are the same spell."

    $ note("A ward could turn Ravagers away — but would also turn the caravan away.", "warding")
    $ trust_school += 1

    hide sprite ivo with char_out
    return


## ================================================================== OREN ====

label topic_oren_watch:

    $ enter("oren", "mid")
    oren "You have come up the tower stairs to look at an old man's chart."

    a "I've come up to look at the chart."

    oren "The watch is four people, one brazier, one bell, and one spyglass that the coast sent us in a year when they still remembered us."

    oren "Our job is not to fight. Our job is to know first."

    $ note("The border watch is four people. Its job is to know first, not to fight.", "watch")
    $ trust_hellers += 1

    hide sprite oren with char_out
    return


label topic_oren_pins:

    $ enter("oren", "mid")
    a "There are pins in the chart. Two of them are out in the middle of nothing."

    oren "Two pins, two nights ago, one at each edge of the hollow where the caravan camps."

    a "That's a scouts' pattern."

    oren "It is a scouts' pattern. It is also a shepherd's pattern, a poacher's pattern, and the pattern two of my own watchmen make when they walk a line they have been told to walk."

    oren "Knowing first is not the same as knowing. That is the whole difficulty of a border."

    $ note("Two pins appeared on the watch chart, one at each edge of the caravan's hollow — a scouts' pattern.", "pins")
    $ trust_grass += 1

    hide sprite oren with char_out
    return


label topic_oren_vashk:

    $ enter("oren", "mid")
    a "Vashk. The beastman scout. I spoke with her."

    oren "Then you have spoken to her more than I have, and I have been watching her for three days."

    a "She's not hiding."

    oren "No. She is standing exactly where she can be seen, which is either the most honest thing a scout has ever done or the most expensive."

    oren "If she wanted to raid us, she would have done it in the rain two nights ago. She didn't. I am not yet ready to say what that means."

    $ note("Oren has watched Vashk for three days. She has made no attempt to hide or to raid.", "oren_vashk")

    hide sprite oren with char_out
    return


label topic_oren_tribes:

    $ enter("oren", "mid")
    a "Tell me about the tribes."

    oren "Orkish and beastmen. They roam the Great Dead Grass in bands the coast calls Ravagers because the coast has never had to call them anything else."

    oren "They do not farm the Grass. Nobody farms the Grass. They move through it, and in a hard season they move through the borderlands, and the borderlands get thinner."

    oren "What they want, nobody in Hella has asked in forty years. We have been very good at knowing first and very bad at asking."

    $ note("The Ravager tribes do not farm the Grass; they move through it. Hella has never asked them what they want.", "tribes")
    $ trust_grass += 1

    hide sprite oren with char_out
    return


## ================================================================ TAMSIN ====

label topic_tamsin_academy:

    $ enter("tamsin", "mid")
    tamsin "You're the mayor's daughter. Everyone says you went to the coast to study."

    a "I went to the coast to study. It rained less."

    tamsin "Did you learn anything useful?"

    a "I learned how to be the only person from Hella in a room."

    tamsin "That's what the academy teaches too. They just call it rhetoric."

    $ note("Tamsin is a third-year at the academy. The school teaches the daughters of the coast to be sent back to the coast.", "tamsin_met")

    hide sprite tamsin with char_out
    return


label topic_tamsin_grass:

    $ enter("tamsin", "mid")
    tamsin "You want to know why I go down to the weeds."

    a "I want to know why you go down to the weeds."

    tamsin "Because the dust tells you things. Ivo taught us that, and then she stopped teaching us that, and I asked her why and she said 'because you will go and look'."

    a "And you went and looked."

    tamsin "Three times. The dust on the east side of the hollow is disturbed by carts and by ponies and by about eleven people. That's a caravan, sitting still, waiting."

    tamsin "But there's a fourth track. Something that walks on two legs in a line that has nothing to do with the road, coming down out of the north edge of the Grass, and it has been doing it for days."

    $ note("Tamsin read the Grass-dust: a caravan sitting still, and a two-legged track coming down out of the north for days.", "grass_reading")
    $ trust_grass += 1
    $ trust_school += 1

    hide sprite tamsin with char_out
    return


label topic_tamsin_ivo:

    $ enter("tamsin", "mid")
    a "What's Sister Ivo actually like?"

    tamsin "She is the only mistress here who has been past the milepost. The others teach from charts. She teaches from having been out there."

    tamsin "She is also the one who will tell the board to close the school rather than put sixty girls in a village that is about to be raided, and she will do it without asking any of us."

    a "And you'd want a say."

    tamsin "I'd want a say. I'm nineteen. It's the only thing I've got."

    $ note("Sister Ivo would close the school rather than risk a raid, and would not consult the students.", "ivo_rumour")

    hide sprite tamsin with char_out
    return


label topic_tamsin_offer:

    $ enter("tamsin", "mid")
    tamsin "If you're going into the Grass, I'm coming."

    a "The Grass isn't a field trip."

    tamsin "I've read the dust three times and you've read it none. I know the way to the hollow and back without a lantern. You'll get a hundred paces in and the track will stop being a track."

    a "Why?"

    tamsin "Because my whole education is a thing the coast sends here to be looked at, and out there it's the only thing I've ever done that was actually mine."

    menu:
        "Take her with you.":
            $ known.add("tamsin_companion")
            $ trust_school += 1
            $ trust_grass += 1
            a "All right. You walk in front and you tell me what you're reading as you read it."
            tamsin "Yes. Thank you."
            $ note("Tamsin will walk into the Grass with Alexandria.", "tamsin_companion")

        "Not yet. Let me look first.":
            a "Not yet. Let me go and look at the hollow first. If it's what you say it is, you're the first person I want next to me."
            tamsin "That's a very political way of saying no."
            a "I learned it on the coast."
            tamsin "Fine. But if you go out there without me and get lost, I'm going to be extremely smug about it at your funeral."

    hide sprite tamsin with char_out
    return


## ================================================================ HARROW ====

label topic_harrow_droving:

    $ enter("harrow", "mid")
    harrow "You're Elandi's. Good. Your mother pays on time."

    a "How does a drover get through the Grass?"

    harrow "You don't get through it. You get through it having made a decision about it, and the decision is different every time."

    harrow "Ponies can smell the difference between a storm coming and a storm already here. You learn to trust the ponies and to distrust the map, and you spend the whole crossing being corrected."

    $ note("Drovers cross the Grass by trusting ponies over maps, and by making a fresh decision each time.", "droving")
    $ trust_grass += 1

    hide sprite harrow with char_out
    return


label topic_harrow_half:

    $ enter("harrow", "mid")
    a "They say half of them get lost."

    harrow "They say half because they don't like the number."

    a "What's the number?"

    harrow "I've crossed nine times. Of the nine caravans I crossed with, I'm the only drover who's crossed all nine."

    harrow "That's not the Grass being hungry. That's the Grass being large, and being large in the storm season, and being the only road there is."

    $ note("Harrow has crossed the Grass nine times. He is the only drover of his nine caravans to have made all nine crossings.", "half")
    $ trust_grass += 1

    hide sprite harrow with char_out
    return


label topic_harrow_ork:

    $ enter("harrow", "mid")
    a "You're orkish. In Hella."

    harrow "I'm orkish and I'm a drover and I'm paid in Hella coin, and the three of those have never once been a problem in the same sentence."

    a "The tribes—"

    harrow "The tribes are not me any more than the coast is you. But I'll tell you the thing nobody in this village will tell you: they have not raided Hella in nine years."

    a "That's not what the moot says."

    harrow "The moot does not say anything. The moot is a set of stacked tables."

    $ note("Harrow says the Ravager tribes have not raided Hella in nine years.", "nine_years")
    $ trust_grass += 1

    hide sprite harrow with char_out
    return


label topic_harrow_caravan:

    $ enter("harrow", "mid")
    a "Where's the caravan?"

    harrow "Sitting. There's a hollow east of the milepost where the wagons wait out the worst of it. I saw the fire from the drovers' road three nights back."

    a "You saw a fire and told no one but the moot?"

    harrow "I told the moot, and the moot put it on the tally-board where it stayed. You're the first person in this village who's asked me a question with the word 'where' in it."

    $ note("The caravan is waiting in a hollow east of the milepost. Harrow saw its fire three nights ago.", "caravan_seen")
    $ trust_grass += 1

    hide sprite harrow with char_out
    return


## ================================================================= SEPPA ====
## Seppa only exists once the caravan has arrived.

label topic_seppa_goods:

    $ enter("seppa", "mid")
    seppa "Elandi's girl. Your mother's standing order is a very old piece of paper and I have honoured it for six seasons."

    a "What's in the crates?"

    seppa "Salt fish, lamp oil, sailcloth, four bales of western wool, and a barrel of something the school will not admit to ordering."

    a "And the letter?"

    seppa "The letter is not goods. The letter is a conversation between two people who have never met, and I am only the wagon it rides in."

    $ note("Seppa has carried the caravan's sealed letter to Elandi for six seasons without opening it.", "seppa_letters")

    hide sprite seppa with char_out
    return


label topic_seppa_route:

    $ enter("seppa", "mid")
    a "How did you get through?"

    seppa "Slowly. The Grass gives you about a mile a day in the storm season and takes back two if you're proud about it."

    seppa "We came in low, along the south edge, where the weeds thin out against the rocks. That way is longer and it is the only way I will take a wagon."

    a "Nobody uses the south edge."

    seppa "Nobody from Hella uses the south edge. From the west, it is the only edge that makes sense."

    $ note("Seppa crosses the Grass along the south edge, where it thins against the rocks — a route Hella does not use.", "south_edge")
    $ trust_grass += 1

    hide sprite seppa with char_out
    return


label topic_seppa_harrow:

    $ enter("seppa", "mid")
    a "Harrow. Your drover."

    seppa "Harrow is the reason this wagon is in one piece. There are drovers who read the Grass and drovers who fight it. He reads it."

    seppa "Also he does not talk during the crossing, which is worth more than a second pony."

    $ note("Seppa credits Harrow with the crossing.", "seppa_harrow")

    hide sprite seppa with char_out
    return


label topic_seppa_sign:

    $ enter("seppa", "mid")
    a "The sign your scouts saw."

    seppa "Two nights out of the hollow, my outriders found a camp that had been struck in a hurry. Cold fire, cut rope, a broken spear."

    a "Ravagers?"

    seppa "A broken spear is not a raid. A raid leaves broken spears in the village it raided. This was a camp that had been surprised."

    a "Surprised by what?"

    seppa "That is the question I have been carrying across the Grass for eleven days, and I am very tired of it."

    $ note("Seppa's outriders found a Ravager camp struck in a hurry — surprised by something, not raiding.", "ravager_camp")
    $ trust_grass += 1

    hide sprite seppa with char_out
    return


## ================================================================= VASHK ====

label topic_vashk_tribe:

    $ enter("vashk", "mid")

    n "She is standing in the weeds with her hands where you can see them, which is not a thing a raider does."

    vashk "You are the one who has been walking about asking questions. In the Grass we would call that a scout. In a village you call it a daughter."

    a "What are you doing here?"

    vashk "Standing where I can be seen. It is slower than hiding and it is the only way I have found to have a conversation with a wall."

    $ known.add("vashk_met")
    $ note("Vashk, a Ravager scout, is standing in plain sight to be seen rather than to hide.", "vashk_met")
    $ trust_grass += 1

    hide sprite vashk with char_out
    return


label topic_vashk_wants:

    $ enter("vashk", "mid")
    a "What do the tribes want?"

    vashk "To cross. That is all. The Grass is not a country, it is a road that takes a season, and this season it has taken too much."

    vashk "When the weeds do not hold, the bands move. When the bands move, the border gets thin. Your village calls that raiding. We call it a bad year."

    a "People have died in bad years."

    vashk "Yes. On both sides of a road neither of us built."

    $ note("The tribes want to cross the Grass during a hard season. They call it a bad year; Hella calls it raiding.", "vashk_wants")
    $ trust_grass += 2

    hide sprite vashk with char_out
    return


label topic_vashk_hellers:

    $ enter("vashk", "mid")
    a "What do you think of Hella?"

    vashk "It has a wall, a bell, and a school, and it smells of salt fish. In my language the word for a village is the word for a place that has decided to stay."

    a "That's not an answer."

    vashk "It is the answer I have. I have been standing at the edge of your staying for three days, and I have not decided what I think."

    $ note("Vashk has been at the edge of Hella for three days without deciding what to make of it.", "vashk_hellers")
    $ trust_grass += 1

    hide sprite vashk with char_out
    return


label topic_vashk_warning:

    $ enter("vashk", "mid")
    a "You have a warning. Say it."

    vashk "There is a band in the middle of the Grass that is not a band. It came down out of the north with no women, no children, no ponies and no loot."

    vashk "It struck a camp. It has been walking a straight line since."

    a "A straight line to where?"

    vashk "A straight line does not need a to. That is what a straight line is for."

    vashk "Your tower has pins in its chart. Your village has a bell. Use both, and tell the woman with the ledgers that I will stand at the moot if she lets me stand at the moot."

    $ note("A band came out of the north with no families and no ponies, struck a camp, and is walking a straight line. Vashk will speak at a moot if she is allowed.", "vashk_warning")
    $ known.add("council_ready")
    $ trust_grass += 2

    hide sprite vashk with char_out
    return


## ================================================================= CORIN ====

label topic_corin_gate:

    $ enter("corin", "mid")
    a "How is the gate kept?"

    corin "Two of us on it, daylight to last bell, and one on it after. The gate stays open until the storm-count on the post reaches six."

    a "Six being?"

    corin "Six being the number of storms in a season that a gate can be open in. Past six, the mud takes the hinges and the gate becomes a wall."

    $ note("Hella's gate stays open until the storm-count reaches six; after that the mud takes the hinges.", "gate_rule")
    $ trust_hellers += 1

    hide sprite corin with char_out
    return


label topic_corin_stormcount:

    $ enter("corin", "mid")
    a "The chalk on the post. Four."

    corin "Four storms so far this season, and the fifth is coming down the pass behind you. You came up it."

    corin "That's how it works. The storm-count is not a warning. It's a receipt."

    $ note("Four storms so far this season; the fifth came down the pass with Alexandria.", "stormcount")

    hide sprite corin with char_out
    return


label topic_corin_rumours:

    $ enter("corin", "mid")
    a "What have you heard?"

    corin "That there's something in the Grass that isn't Ravagers. That the caravan's sitting in the hollow. That the school board's writing letters."

    corin "And that the mayor's daughter has been walking about asking questions, which is the only rumour in this village I've seen with my own eyes."

    a "What do you think I should do?"

    corin "I think you should get everyone in one room before the fifth storm gets here. A border village that gets frightened in separate rooms stays frightened."

    $ note("Corin thinks the village needs one room and one conversation before the fifth storm.", "corin_advice")
    $ trust_hellers += 1

    hide sprite corin with char_out
    return
