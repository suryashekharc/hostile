label splashscreen:
    scene two_cats
    with Pause(1)

    show text "{outlinecolor=#00ff00}{color=#0000ffff}Are you ready to identify some hostile design?{/color}{/outlinecolor}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    $ score = 0
    $ total = 8
    $ y = renpy.input("What is your name?", default = "Human Bean", length = 20)
    "Very well, [y]. Try to identify the hostile design in the game without looking at the options first. Good luck!"


    scene bench_1
    "What's the hostile design here?"
    menu:
        "The benches":
            "Correct!"
            $ score += 1
        "The black pillars":
            "Not really"
    "The spikes on the bench prevent people from sleeping: from the homeless to the old and infirm"



    scene blue_room
    "What hostile design do you notice in this nightclub washroom?"
    menu:
        "The handles next to the commode":
            "They are actually helpful!"
        "The blue light":
            "Correct!"
            $ score += 1
    "The blue light is meant to make it difficult for drug users to locate a vein to inject themselves"



    scene boulder_sf
    "What is the anti-homeless hostile design here?"
    menu:
        "The boulders":
            "Correct!"
            $ score += 1
        "The walls":
            "Nope"
    "SF residents spent $2K to get these boulders to prevent the homeless from sleeping/camping"


    scene skate_stopper
    "What hostile design is in play here?"
    menu:
        "The leaves":
            "Correct!"
            $ score += 1
        "The chair":
            "Nope - even tho it looks uncomfy"
    "These skate stoppers are meant to discourage sk8r boys from doing their thing"



    scene water_fountain
    "This one is hard. Can you guess what went on here?"
    menu:
        "The fridge":
            "Incorrect"
        "The missing fountain":
            "Correct"
            $ score += 1
    "The water fountain has been removed to force people to pay to drink water"


    scene awning
    "What apparent design flaw is hiding in this picture?"
    menu:
        "The roof awning":
            "Correct"
            $ score += 1
        "The cycle stands":
            "Not really"
    "The awning has a gap to let rainwater drip to the floor preventing the homeless from seeking shelter there during rainy weather"


    scene grate
    "What is the grate design trying to prevent?"
    menu:
        "Loitering":
            "Yep"
            $ score += 1
        "Littering":
            "Not really"
    "Homeless people often rest on or gather around grates for the warmth they get from them in cold weather"


    scene plant
    "What is the hostile design element here? It's a toughie."
    menu:
        "The potted plants":
            "Correct"
            $ score += 1
        "The tile design":
            "Not exactly"
    "The plant walls guide the pedestrians to stick to the sidewalk, making it hard for the homeless to sleep there"


    scene wtf_poop
    "What's wrong here?"
    menu:
        "Nothing":
            "Correct"
        "Absolutely nothing":
            "Absolutely correct"
    "You're good at this game, [y]"



    scene end_screen
    "Congratulations on making it to the end, [y]. Your total score is [score] / [total]. "
    "The problem with hostile design is that it tries to solve the problem by not acknowledging it in the first place. Homelessness is not solved by pushing the homeless out of sight."
    "Thank you for playing this game - hope you learnt a thing or three. I sure did!"
return