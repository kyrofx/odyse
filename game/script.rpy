define o = Character("Odysseus")
define n = Character("Narrator")
define y = Character("You")
define c = Character("Crew member")



label start:

    scene bgboat

    n "Chapter 1... The journey"
    n "Game made by Eddie, Matthew, & Krithik for Mr. Fleitas"

    o "Hi! We're on our way back to Ithaca after the war in Troy."
    o "Oh look! I can see land!"
    n "You arrived at the Island of the Cyclops."
    scene fromboat
    menu:
        o "Should we stop at the Island of the Cyclops??"
        "Go to the Island of the Cyclops":
            y "Let's go to the island. There ought to be good riches here."
        "Stay on the boat":
            y "Let's leave. This island looks worthless and isn't worth the danger."
            jump stay
    
    
    show island
    o "Wow what a nice island!"
    o "There's so much sheep!"
    o "I heard that this island has the Cyclops and that they have good items."
    o "Let us visit their cave."
    show cave
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

return 
n "test"
    default f = renpy.random.randint(1,5)
    if f == 1:
        n "odyseus died."
        return
    if f == 2:
        n "odyseus is alive"
        return
    else:
        n "yayysyrs"
    return