define o = Character("Odysseus")
define n = Character("Narrator")
define y = Character("You")
define c = Character("Crew member")



label start:

    scene boatwater

    n "Book 9: The Cyclops"
    n "Game made by Eddie, Matthew, & Krithik for Mr. Fleitas"

    o "Hi! We're on our way back to Ithaca after the war in Troy."
    o "Oh look! I can see land!"
    n "You arrived at the Island of the Cyclops."
    menu:
        o "Should we stop at the Island of the Cyclops??"
        "Go to the Island of the Cyclops":
            y "Let's go to the island. There ought to be good riches here."
        "Stay on the boat":
            y "Let's leave. This island looks worthless and isn't worth the danger."
            jump stay
    
    
    show boatland
    o "Wow what a nice island!"
    o "There's so much sheep!"
    o "I heard that this island has the Cyclops and that they have good items."
    o "Let us visit their cave."
    show caveoutside with fade
    c "There's so much cheese in this cave!"
    c "We should just take the cheese and the sheep outside and leave."
    menu:
        o "Hmm... What do you think traveler?"
        "Take the items and leave":
            y "We would be better off with these sheep and cheese. The Cyclops will probably kill us anyway."
            jump takei
        "Wait for the Cyclops to see if they have more things they can give us":
            y "Let's wait. The Cyclops will give us more treasures than what is offered now."
        "Set a trap for the Cyclops":
            y "How about we set a trap for the Cyclops to fall into?"
            y "Once the Cyclops is dead, we can take all of his belongings."
            jump trap
    
    
    o "Okay, we better wait then."
    define cyclops = Character("Cyclops")
    n "The cyclops enters the cave with his sheep."
    n "He closes the cave by rolling a massive boulder behind him."
    cyclops "(Surprised) What are you doing in my cave?"
    o "Do not worry. We have come in peace!"
    o "We are men of Agememnon!"
    o "We wish to recieve a gift from you as is customary! Otherwise you would be disrespecting the Gods!"
    cyclops "You foreigners are fools!"
    cyclops "We do not fear the Gods. We are more powerful than they are."
    cyclops "Anyways, where are you going with your ship?"
    o "We crashed into the coast! Poseiden wrecked our ship."
    cyclops "Unfortunately for you, I am a heartless creature!"
    cyclops "I will eat two of your men!"
    n "The Cyclops eats two men in a gruesome fasion."
    n "The night passes in fear as you and the rest of the crew huddle in a corner."
    cyclops "I will be leaving to herd the sheep. All of you must stay put."
    c "What should we do? We can't stay like this!"
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
    o "That's my style!"
    n "Odysseus and his crew prepare some wine and a large stick for later use."
    o "When the Cyclops returns, we shall offer him some wine."
    o "While he is distracted, we shall run!"
    n "The Cyclops returns hours later."
    o "Here is some wine!"
    cyclops "Huh?"
    n "The Cyclops drinks the wine"
    cyclops "What is this? This is very good!"
    n "The Cyclops drinks more wine."
    cyclops "Woah I'm getting drunk!"
    n "The Cyclops falls asleep."
    o "Hurry! Let us stick the stick in his eye!"
    n "Odysseus and his crew stick the stick into the Cyclops' eye."
    n "The Cyclops wakes up in the morning."
    cyclops "What happened?"
    cyclops "I can't see!"
    n "Odysseus and his crew don't respond."
    n "They are hiding beneath the sheep, waiting for the Cyclops to let his sheep out to graze."
    n "The Cyclops grunts as nobody responds."
    cyclops "Where are you guys?"
    n "The Cyclops runs around the cave, bumping into walls."
    n "In the end, he gives up."
    n "The Cyclops grunts as he opens the cave door."
    cyclops "You are free my sheep!"
    n "The sheep run out of the cave."
    odysseus "We made it!"
    n "Odysseus and his crew were able to escape the island."
    n "Odysseus and his crew climbed aboard the boat and sailed away."
    jump ending
    return


label violence:  #VIOLENCE
    y "Let's use violence. It's our only option now."
    o "Right O!"
    o "When the Cyclops gets back, we shall hold a sheep hostage!"
    n "The Cyclops returns hours later."
    o "Give us our freedom! Otherwise this sheep will become a thing of the past."
    cyclops "How dare you try to hold my sheep hostage!"
    n "The cyclops goes on to kill most of the crew members."
    o "Hurry! Grab that end of the rope so we can trip the cyclops!"
    n "The cyclops falls and Odysseus stabs him in the head."
    n "You are now free but only within the cave."
    n "The boulder still holds the crew inside."
    n "Odysseus' story is forgotten."
    return
label bribe:   #BRIBE
    y "We must bribe the Cyclops with riches! It's the only option worth giving a shot."
    o "Okay. When the Cyclops enters, we must shower it with treasures. While it is distracted, we run!"
    n "The Cyclops returns hours later."
    o "Here is some treasure!"
    c "We have more back here too!"
    cyclops "Huh?"
    cyclops "What are you talking about?"
    n "In his confused state, the Cyclops forgets to close the door behind him. He stumbles to the back of the cave where he finds nothing."
    cyclops "Theres nothing here?"
    n "The Cyclops turns around to be alone in a dark cave."
    n "Angry, the Cyclops runs out of the cave and catches up to the back half of Odysseus' crew."
    cyclops "How dare you try to escape!"
    n "The Cyclops kills the half."
    o "Oh no! The Cyclops is catching up!"
    menu:
        o "Where should we head to?"
        "The boat":
            jump boat
        "Into the trees":
            jump trees


label boat:
    o "Ok!"
    n "The first half of Odysseus' crew make it onto the boat."
    o "Hurry! We must get this boat out of here!"
    n "Unfortunately for you and the crew, you were unable to make it past the Cyclops' throwing range in time."
    n "He throws a boulder and everyone dies."
    n "Odysseus' story is forgotten."


label trees:
    o "Oh! Didn't think of that."
    n "The half that made it run into the dark forest."
    c "The Cyclops can't possibly find us here."
    o "I still don't want to risk it. I will lead us to the ship."
    o "Follow closely along. I do not want to lose more of you."
    cyclops "Rwahhh!!! I found you! You all are dead!"
    o "Run faster!"
    n "All survivors safely make it onto the ship."
    n "Without the Cyclops present, the boat swiftly escapes the island."
    n "{br}Good ending!{/br}"



label peace:    #PEACE
    y "Let's use peace. It's our only option now."
    o "Right O!"
    o "When the Cyclops gets back, we must all beg and try to make treaties."
    n "The Cyclops returns hours later."
    o "Please! we are begging you! Please let us go!"
    o "We won't ask for gifts!"
    cyclops "Do you really think I'm going to let you and your crew leave this cave?"
    cyclops "I earn nothing from letting you go! But if I keep you, I get all of the fresh human flesh!"
    n "The Cyclops eats Odysseus and then the rest of the crew."
    n "Odysseus' story is forgotten."
    return



label stay:
        n "You stayed on the boat and made your way safely back to Ithaca."
        n "All your crewmembers were safe and you didn't fall for any tricks on the way."
        n "Odysseus gets to meet Penelope again."
        n "Everything is happy again."
        return
label takei:
        n "You and the crew took the items and left the island."
        n "All your crewmembers were safe and you didn't fall for any tricks on the way."
        n "Odysseus gets to meet Penelope again."
        n "Everything is happy again."
        return
label trap:
        n "Your trap worked."
        n "Odysseus caught the Cyclops and killed him."
        n "The crew successfully returns to Ithaca with sheep and cheese."
        n "One problem though, the Gods are not happy with your actions."
        n "There will be consequences in the future."
        return


label escape:
    #implement random function to see if they taunt or not.

label ending:
    n "Looks like you made it to the end of the game."
    menu:
        n "Looks like you made it to the end of the game."
        "Play again":
            jump start
        "Quit":
            return