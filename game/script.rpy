# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return
label splashscreen:
    scene black
    with Pause(1)

    show text "Are you ready to identify some hostile design?" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    $ score = 0
    $ total = 5
    $ y = renpy.input("What is your name?", default = "Human Bean", length = 20)
    "Very well, [y]. Good luck!"


    scene bench_1
    "What's wrong here?"
    menu:
        "The benches":
            "Correct!"
            $ score += 1
        "The black pillars":
            "Not really"
    "The spikes on the bench prevent people from sleeping: from the homeless to the old and infirm"



    scene blue_room
    "What's wrong here?"
    menu:
        "The handles next to the commode":
            "They are actually helpful!"
        "The blue light":
            "Correct!"
            $ score += 1
    "The blue light is meant to make it difficult for drug users to locate a vein to inject themselves"



    scene boulder_sf
    "What's wrong here?"
    menu:
        "The boulders":
            "Correct!"
            $ score += 1
        "The walls":
            "Nope"
    "SF residents spent $2K to get these boulders to prevent the homeless from sleeping/camping"




    scene skate_stopper
    "What's wrong here?"
    menu:
        "The leaves":
            "Correct!"
            $ score += 1
        "The chair":
            "Nope - even tho it looks uncomfy"
    "These skate stoppers are meant to discourage sk8r boys from doing their thing"



    scene water_fountain
    "What's wrong here?"
    menu:
        "The fridge":
            "Incorrect"
        "The missing fountain":
            "Correct"
            $ score += 1
    "The water fountain has been removed to force people to pay to drink water"



    scene wtf_poop
    "What's wrong here?"
    menu:
        "Nothing":
            "Correct"
        "Absolutely nothing":
            "Absolutely correct"
    "You're good at this game, [y]"



    scene end_screen
    "Congratulations on making it to the end, [y]. Your total score is [score] / [total]"
return