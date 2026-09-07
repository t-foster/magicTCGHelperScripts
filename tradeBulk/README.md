# tradebulk.py

Script for comparing the contents of two different manabox collections (a giver and a recipient) to suggest cards that the giver has an excess of that the recipient has none (or optionally very few) of.

2. cd into the tradeBulk folder
3. Run the trade bulk script
    Example, this uses two different manabox collections, one from Scott and one from Troy: 
    `./tradeBulk.py --giver scotts.csv --receiver troy.csv`
    The results will looks like:
	```
	consider trading: 5: Electro's Bolt (common)
	consider trading: 5: Suburban Sanctuary (common)
	consider trading: 5: Beetle, Legacy Criminal (common)
	consider trading: 5: Jeskai Windscout (common)
	consider trading: 5: Landscape Painter // Vibrant Idea (common)
	consider trading: 5: Spider-Man No More (common)
	consider trading: 5: Spider Manifestation (common)
	consider trading: 5: Social Snub (uncommon)
	consider trading: 6: Spider-Man, Brooklyn Visionary (common)
	consider trading: 6: Visionary's Dance (common)
	consider trading: 6: Azog, Moria's Ruin (rare)
	consider trading: 7: Passenger Ferry (common)
	```
    The leading number is how many copies the giver has of the card, then the name ofthe card, then in parentheses the rarity of the card.
4. You can also change the giver and recipient threshold for how many copies of the card they each have.  The default is if the giver has more than 4 copies of the card and the recipient has 0 copies of the card.
    1. Example:
        `./tradeBulk.py --giver scotts.csv --receiver troy.csv --giver_threshold 5 --receiver_threshold 1`
    2. Which produces output like this:
	```
	consider trading: 6: Spider-Man, Brooklyn Visionary (common)
	consider trading: 6: Great Ugly-Looking Goblin // Clap! Snap! (uncommon)
	consider trading: 6: Common Crook (common)
	consider trading: 6: Pterafractyl (common)
	consider trading: 6: Visionary's Dance (common)
	consider trading: 6: News Helicopter (common)
	consider trading: 6: Azog, Moria's Ruin (rare)
	consider trading: 7: The Misty Mountains Cold (rare)
	consider trading: 7: Dwarven Mauler (uncommon)
	consider trading: 7: Colleen Wing, Street Samurai (uncommon)
	consider trading: 7: Daily Bugle Reporters (common)
	consider trading: 7: Mob Lookout (common)
	consider trading: 7: Passenger Ferry (common)
	consider trading: 8: Old Fat Spider (uncommon)
	consider trading: 10: Sound the Trumpets (uncommon)
	consider trading: 10: Stone by Sunlight (uncommon)
	```
    3. Which means that the giver has 10 copies of `Stone by Sunlight` and the recipient has only 1 copy of that card.
5. But what if I want to see what Try has that Scott does not?
    1. Switch the arguments `./tradeBulk.py --giver troy.csv --receiver scotts.csv`
    2. Which gives output like this
	```
	consider trading: 5: Action News Crew (common)
	consider trading: 5: Uneasy Alliance (common)
	consider trading: 5: Crustacean Commando (common)
	consider trading: 5: Insectoid Exterminator (common)]
	consider trading: 5: Power Sink (common)
	consider trading: 5: Quakestrider Ceratops (uncommon)
	. . .
	consider trading: 7: Safewright Cavalry (common)
	consider trading: 7: Summit Sentinel (common)
	consider trading: 9: Swiftwater Cliffs (common)
	consider trading: 11: Blossoming Sands (common)
	consider trading: 12: Llanowar Elves (common)
	```

## Happy trading!
