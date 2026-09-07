# comboFinder


2. cd into the comboFinder directory
3. Run the curl scripts.
    1. curlJson.sh will download and unzip a single large json file from https://commanderspellbook.com/
4. Run the comboParser.py script.  
    Example:
    `./comboParser.py --jsonfile json/variants.json --manaboxCsvfile ManaBox_Collection.csv`
    The results will look like:
	```
	timestamp = 2026-09-05T15:08:45.512846+00:00
	length of comboList = 108918
	length of myCards = 5210
	2 ['Goldspan Dragon', 'Whip Silk', 'https://commanderspellbook.com/combo/3809-4124', 'identity=RG']
	2 ['Rite of Replication', 'Scourge of Valkas', 'https://commanderspellbook.com/combo/1744-2676', 'identity=UR']
	3 ['Barbarian Class', 'Breath of Fury', 'Royal Talon Fighter Jet', 'https://commanderspellbook.com/combo/3259-7297-7759', 'identity=RW']
	2 ['Metallic Mimic', 'Spawning Pit', 'https://commanderspellbook.com/combo/345-3899--5', 'identity=C']
	2 ['Kami of Whispered Hopes', 'Ringing Strike Mastery', 'https://commanderspellbook.com/combo/81-7500', 'identity=GU']
	3 ['Joo Dee, One of Many', 'Lavaleaper', 'Pitiless Plunderer', 'https://commanderspellbook.com/combo/4871-7072-7175', 'identity=BR']
	2 ['Blowfly Infestation', 'Flourishing Defenses', 'https://commanderspellbook.com/combo/1084-4994', 'identity=BG']
	. . .
	```
    The leading number is how many pieces are in the combination, then there is a list of pieces of the combination, then a link to the webpage for it, then the color identity of the combination
6. Use script to find cards that might be good for your current card combinations through the threshold argument.  It prints the number of times each card you do not have shows up in the list of your combinations.
    1. Example
        1. `./comboParser.py --jsonfile json/variants.json --manaboxCsvfile ManaBox_Collection.csv --threshold 1 | tail`
    2. Which produces output like this:
	```
	consider: 18: Bartolomé del Presidio
	consider: 18: Viscera Seer
	consider: 18: Altar of Dementia
	consider: 18: Carrion Feeder
	consider: 18: Yahenni, Undying Partisan
	consider: 19: Goblin Bombardment
	consider: 20: Basking Broodscale
	consider: 26: Phyrexian Altar
	consider: 28: Ashnod's Altar
	consider: 60: Kodama of the East Tree
	```
    3. Which means there are 60 potential combinations in my card collection that Kodama could fit into.
    4. A better way of viewing it is to look at those combinations
       1. `./comboParser.py --jsonfile json/variants.json --manaboxCsvfile ManaBox_Collection.csv --threshold 1 | grep Kodama | sort`
    5. That produces output like this:
	```
	4 ['Azorius Chancery', 'Dancing from Dark to Dawn', 'Kodama of the East Tree', 'https://commanderspellbook.com//combo/1479-3147-7889/']
	4 ['Azorius Chancery', 'Kodama of the East Tree', 'Mole Man, Moloid Master', 'https://commanderspellbook.com//combo/1479-3147-7705/']
	4 ['Azorius Chancery', 'Kodama of the East Tree', 'Quantum Misalignment', 'https://commanderspellbook.com//combo/1479-3147-5362/']
	4 ['Azorius Chancery', 'Kodama of the East Tree', 'Thranduil, Sindarin Liege // Silvan Rally', 'https://commanderspellbook.com//combo/1479-3147-7893/']
	4 ['Dancing from Dark to Dawn', 'Golgari Rot Farm', 'Kodama of the East Tree', 'https://commanderspellbook.com//combo/280-1479-7889/']
	. . .
	```
7. Use the script to find combinations that work in a certain color identity.
    1. Example
        1. `./comboParser.py --jsonfile json/variants.json --manaboxCsvfile ManaBox_Collection.csv --colorIdentity WB`
    2. Which produces output like this:
	```
	timestamp = 2026-09-05T15:08:45.512846+00:00
	length of comboList = 108918
	length of myCards = 5210
	3 ['Hammerhead, Maggia Boss', 'Pitiless Plunderer', 'Stridehangar Automaton', 'https://commanderspellbook.com/combo/4871-6291-8095', 'identity=B']
	3 ['Fiend Hunter', 'Spawning Pit', 'Sun Titan', 'https://commanderspellbook.com/combo/1734-3175-3899', 'identity=W']
	3 ['Invisible Woman, Sue Storm', 'Soul Warden', 'Spider-Man, Peter Parker', 'https://commanderspellbook.com/combo/360-6824-7690', 'identity=W']
	3 ['Aethergeode Miner', 'Decoction Module', 'Panharmonicon', 'https://commanderspellbook.com/combo/2397-3484-4374', 'identity=W']
	3 ['Haliya, Guided by Light', 'Invisible Woman, Sue Storm', 'Spider-Man, Peter Parker', 'https://commanderspellbook.com/combo/6752-6824-7690', 'identity=W']
	2 ['Bloodthirsty Conqueror', 'Epicure of Blood', 'https://commanderspellbook.com/combo/4912-6191', 'identity=B']
	. . .
	appearances: 8: Spider-Man, Peter Parker
	appearances: 8: Light of Promise
	appearances: 9: Plague of Vermin
	appearances: 13: Spawning Pit
	appearances: 14: Hammerhead, Maggia Boss
	appearances: 15: Invisible Woman, Sue Storm
	```




