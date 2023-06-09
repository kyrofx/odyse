﻿define o = Character("Odysseus")
define n = Character("Narrator")
define y = Character("You")
define c = Character("Crew member")
$ escapeByBoat = False
$ endingInt = 0
    # 0 = default
    # 1 = GOOD; on foot to boat
    # 2 = GOOD; How many tricks up your sleeve
    # 3 = BAD; Stuck in cave
    # 4 = BAD; Killed by Cyclops

label start:

    scene boatwater

    n "Book 9: The Cyclops"
    n "Game made by Eddie, Matthew, & Krithik for Mr. Fleitas"
    show odysseus
    o "Hi! We're on our way back to Ithaca after the war in Troy."
    o "Oh look! I can see land!"
    n "You arrived at the Island of the Cyclops."
    hide odysseus
    menu:
        o "Should we stop at the Island of the Cyclops??"
        "Go to the Island of the Cyclops":
            y "Let's go to the island. There ought to be good riches here."
        "Stay on the boat":
            y "Let's leave. This island looks worthless and isn't worth the danger."
            jump stay
    
    
    scene boatland with dissolve
    show odysseus
    o "Wow what a nice island!"
    o "There's so much sheep!"
    o "I heard that this island has the Cyclops and that they have good items."
    o "Let us visit their cave."
    scene caveoutside with fade
    show crew
    c "There's so much cheese in this cave!"
    c "We should just take the cheese and the sheep outside and leave."
    show odysseus
    menu:
        o "Hmm... What do you think traveler?"
        "Take the items and leave":
            y "We would be better off with these sheep and cheese. The Cyclops will probably kill us anyway."
            jump takei
        "Wait for the Cyclops to see if they have more things they can give us":
            scene caveinside with fade
            y "Let's wait. The Cyclops will give us more treasures than what is offered now."
        "Set a trap for the Cyclops":
            scene caveinside with fade
            y "How about we set a trap for the Cyclops to fall into?"
            y "Once the Cyclops is dead, we can take all of his belongings."
            jump trap
    
        #     This is the waiting scene.

    o "Okay, we better get comfortable then."
    define cyclops = Character("Cyclops")
    scene caveinsidecyclops with fade

    n "The cyclops enters the cave with his sheep."
    show cyclops
    n "He closes the cave by rolling a massive boulder behind him."
    cyclops "(Surprised) What are you doing in my cave?"
    show odysseus
    o "Do not worry. We have come in peace!"
    o "We are men of Agememnon!"
    o "We wish to recieve a gift from you as is customary! Otherwise you would be disrespecting the Gods!"
    show cyclops
    cyclops "You foreigners are fools!"
    cyclops "We do not fear the Gods. We are more powerful than they are."
    cyclops "Anyways, where are you going with your ship?"
    show odysseus
    o "We crashed into the coast! Poseiden wrecked our ship."
    show cyclops
    cyclops "Unfortunately for you, I am a heartless creature!"
    cyclops "I will eat two of your men!"

    scene cyclopskill
    n "The Cyclops eats two men in a gruesome fasion."
    n "The night passes in fear as you and the rest of the crew huddle in a corner."
    scene caveinsidecyclops
    show cyclops
    cyclops "I will be leaving to herd the sheep. All of you must stay put."
    scene caveinside
    show crew
    c "What should we do? We can't stay like this!"
    show odysseus
    o "Yes! We must plan."
    menu:
        o "What do you think we should do?"
        "Use trickery":
            jump tricks
        "Use violence":
            jump violence
        "Use bribery":
            jump bribe
        "Use peace":
            jump peace

    return

label tricks:    #TRICKS
    y "Let's use trickery! It's the smartest way out!"
    show odysseus
    o "That's my style!"
    n "Odysseus and his crew prepare some wine and a large stick for later use."
    o "When the Cyclops returns, we shall offer him some wine."
    o "While he is distracted, we shall run!"

    scene caveinsidecyclops with fade
    n "The Cyclops returns hours later."
    show odysseus
    o "Here is some wine!"
    show cyclops
    cyclops "Huh?"

    n "The Cyclops drinks the wine"
    cyclops "What is this? This is very good!"
    n "The Cyclops drinks more wine."
    cyclops "Woah I'm getting drunk!"
    n "The Cyclops falls asleep."
    show odysseus
    o "Hurry! Let us stick the stick in his eye!"
    hide odysseus
    scene cyclopsblind
    n "Odysseus and his crew stick the stick into the Cyclops' eye."
    scene caveinsidecyclops with fade
    n "The Cyclops wakes up in the morning."
    # add name function !!!!!
    show cyclops

    cyclops "What happened?"
    cyclops "I can't see!"
    n "Odysseus and his crew don't respond."
    n "They are hiding beneath the sheep, waiting for the Cyclops to let his sheep out to graze."
    n "The Cyclops grunts as nobody responds."
    cyclops "Where are you guys?"
    n "The Cyclops runs around the cave, bumping into walls."
    n "In the end, he gives up."
    n "The Cyclops grunts as he opens the cave door."
    hide cyclops
    scene outsidecavecyclopsoutside with fade

    cyclops "You are free my sheep!"
    n "The sheep run out of the cave."
    scene outsidecavecyclopsinside with dissolve
    show odysseus
    o "We made it!"
    hide odysseus
    scene black
    n "Odysseus and his crew climbed aboard the boat."
    $ escapeByBoat = True
    $ endingInt = 2
    jump escape
    jump ending
    return


label violence:  #VIOLENCE
    y "Let's use violence. It's our only option now."
    show odysseus
    o "Right O!"
    o "When the Cyclops gets back, we shall hold a sheep hostage!"
    scene caveinsidecyclops

    n "The Cyclops returns hours later."
    o "Give us our freedom! Otherwise this sheep will become a thing of the past."
    show cyclops
    cyclops "How dare you try to hold my sheep hostage!"
    scene cyclopskill
    hide cyclops
    n "The cyclops goes on to kill most of the crew members."
    show odysseus
    o "Hurry! Grab that end of the rope so we can trip the cyclops!"
    hide odysseus
    scene cyclopsblind
    n "The cyclops falls and Odysseus stabs him in the head."
    scene caveinside
    n "You are now free but only within the cave."
    n "The boulder still holds the crew inside."
    n "Odysseus' story is forgotten."
    $ endingInt = 3
    jump ending
    return


label bribe:   #BRIBE
    y "We must bribe the Cyclops with riches! It's the only option worth giving a shot."
    show odysseus
    o "Okay. When the Cyclops enters, we must shower it with treasures. While it is distracted, we run!"
    scene caveinsidecyclops
    n "The Cyclops returns hours later."
    show odysseus
    o "Here is some treasure!"
    show crew
    c "We have more back here too!"
    show cyclops
    cyclops "Huh?"
    cyclops "What are you talking about?"
    n "In his confused state, the Cyclops forgets to close the door behind him. He stumbles to the back of the cave where he finds nothing."
    cyclops "Theres nothing here?"
    hide cyclops
    n "The Cyclops turns around to be alone in a dark cave."
    scene outsidecavecyclopsoutside
    n "Angry, the Cyclops runs out of the cave and catches up to the back half of Odysseus' crew."
    show cyclops
    cyclops "How dare you try to escape!"
    n "The Cyclops kills the half."
    show odysseus
    o "Oh no! The Cyclops is catching up!"
    menu:
        o "Where should we head to?"
        "The boat":
            jump boat
        "Into the trees":
            jump trees


label boat:
    show odysseus
    o "Ok!"
    hide odysseus
    scene boatland with fade
    n "The first half of Odysseus' crew make it onto the boat."
    show odysseus
    o "Hurry! We must get this boat out of here!"
    scene cyclopsthrowingrock
    show cyclops
    cyclops "You all are so stupid!!"
    hide cyclops
    n "Unfortunately for you and the crew, you were unable to make it past the Cyclops' throwing range in time."
    n "He throws a boulder and everyone dies."
    n "Odysseus' story is forgotten."
    $ endingInt = 4
    jump ending
    return


label trees:
    scene boatland
    show odysseus
    o "Oh! Didn't think of that."
    hide odysseus
    n "The half that made it run into the dark forest."
    show crew
    c "The Cyclops can't possibly find us here."
    show odysseus
    o "I still don't want to risk it. I will lead us to the ship."
    o "Follow closely along. I do not want to lose more of you."
    show cyclops
    cyclops "Rwahhh!!! I found you! You all are dead!"
    show odysseus
    o "Run faster!"
    hide odysseus
    n "All survivors safely make it onto the ship."
    scene boatwater
    n "Without the Cyclops too close by, the boat swiftly escapes the island."
    $ endingInt = 9
    jump ending
    return



label peace:    #PEACE
    y "Let's use peace. It's our only option now."
    show odysseus
    o "Right O!"
    o "When the Cyclops gets back, we must all beg and try to make treaties."
    scene caveinsidecyclops
    n "The Cyclops returns hours later."
    o "Please! we are begging you! Please let us go!"
    o "We won't ask for gifts!"
    show cyclops
    cyclops "Do you really think I'm going to let you and your crew leave this cave?"
    cyclops "I earn nothing from letting you go! But if I keep you, I get all of the fresh human flesh!"
    hide cyclops
    scene cyclopskill

    n "The Cyclops eats Odysseus and then the rest of the crew."
    n "Odysseus' story is forgotten."
    $ endingInt = 4
    jump ending
    return



label stay:
        scene boatwater
        n "You stayed on the boat and made your way safely back to Ithaca."
        n "All your crewmembers were safe and you didn't fall for any tricks on the way."
        n "Odysseus gets to meet Penelope again."
        n "Everything is happy again."
        $ endingInt = 5
        jump ending
        return
label takei:
        scene boatwater
        n "You and the crew took the items and left the island."
        n "All your crewmembers were safe and you didn't fall for any tricks on the way."
        n "Odysseus gets to meet Penelope again."
        n "Everything is happy again."
        $ endingInt = 5
        jump ending
        return
label trap:
        scene cyclopsblind
        n "Your trap worked."
        n "Odysseus caught the Cyclops and killed him."
        n "The crew successfully returns to Ithaca with sheep and cheese."
        scene black
        n "One problem though, the Gods are not happy with your actions."
        n "There will be consequences in the future."
        $ endingInt = 6
        jump ending
        return


label escape:
    #implement random function to see if they taunt or not.
    $ taunt = renpy.random.randint(1, 2)
    if taunt == 1:
        #taunt
        scene cyclopsthrowingrock with fade
        show Odysseus
        o "Hey idiot!"
        o "The mortal that was able to beat you is Odysseus!"
        show cyclops
        cyclops "Curse you!"
        cyclops "You will never be able to return home! If it is fated that you do, you will do so with no honor!"
        hide cyclops
        if escapeByBoat == True:
            n "The Cyclops lifts a large boulder and throws it at the boat."
            n "The boat is destroyed and the crew is killed."
            n "Odysseus' story is forgotten."
            $ endingInt = 7
            jump ending
            return
        else:
            #no taunt, win
            scene boatwater with fade
            show odysseus
            o "We made it!"
            o "We escaped the Cyclops!"
            o "Let us celebrate. We are free again!"
            o "Turn the boat to Ithaca!"
            o "We're coming home Penelope!"
            hide odysseus
            $ endingInt = 7
            jump ending

        return
    else:
        #no taunt
        scene boatwater with fade
        show odysseus
        o "Phew that was close!"
        o "We are safe for now."
        o "Let us make our way towards Ithaca now."
        hide odysseus
        $ endingInt = 7
        jump ending
        return


label ending:
    if endingInt == 9:
           n "You successfully made it to the boat. Your achievement is {b}{i}Running to the boat!{/i}{/b}"
    elif endingInt == 2:
           n "You successfully made it to the boat. Your achievement is {b}{i}How many tricks do you have up your sleeve?{/i}{/b}"
    elif endingInt == 3:
             n "You were not successful in escaping. Your achievement is {b}{i}Stuck in a cave.{/i}{/b}"
    elif endingInt == 4:
                n "You were not successful in escaping. Your achievement is {b}{i}Struck down by a Cyclops.{/i}{/b}"
    elif endingInt == 5:
                n "You were successful in surviving. Your achievement is {b}{i}No problem to begin with!{/i}{/b}"
    elif endingInt == 6:
            n "You were successful in surviving. Your achievement is {b}{i}Who cares about what the Gods think?{/i}{/b}"
    elif endingInt == 7:
            $ intfd = 5


    scene odysseusending
    menu:

        n "This is the end of the game. Thank you for playing!"
        "Play again":
            jump start
        "Quit":
            n "Game coded by Eddie Gu. Script by Matthew Jung. Artwork by Krithik Sambathkumar & respective artists."
            n "This game should only appear for English 1 period 4 Mr. Fleitas' class."
            return
