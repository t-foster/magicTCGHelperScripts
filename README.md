# magicTCGHelperScripts

Collection of scripts for helping find stuff in your Magic card bulk

1. Go through and inventory your magic cards with manabox and export the CSV file from your phone to your computer

There is 1 subdirectory (currently), one for finding potential infinite combinations in your bulk(, and more to come eventually)

2. cd into the comboFinder directory
3. Run the curl scripts.
  1. curlMostPopular.sh will download a bunch of the most popular combinations
  2. curlMostRecent.sh will download a bunch of the most recently submitted combinations, very useful when a new release occurs and fresh combinations are recognized.
  3. curlSpecificCardCombos.sh when passed in a card that you want to use, will download up to 20 pages of combinations for that name.  The script will stop if it gets a page without any combinations.
  Note: commanders spellbook does sometimes throttle usage, just wait a few hours.
4. Run the comboParser.py script.  
    Example:
    `./comboParser.py --commanderSpellbookFiles specific/* recent/* comboFiles/* --manaboxCsvfile ManaBox_Collection.csv`
    The results will look like:
    ```
length of comboList = 28397
length of myCards = 3374
4 ['Kykar, Zephyr Awakener', 'Temporal Manipulation', 'Zealous Lorecaster', 'https://commanderspellbook.com//combo/2104-7370-7487/']
5 ['+1 other prerequisite', 'Dazzling Angel', 'Invisible Woman, Sue Storm', 'Spider-Man, Peter Parker', 'https://commanderspellbook.com//combo/6719-6824-7690/']
6 ['+1 other prerequisite', 'Aetherstorm Roc', 'Aurelia, the Warleader', "Gonti's Aether Heart", 'Saheeli, Radiant Creator', 'https://commanderspellbook.com//combo/3487-4364-4636-6320/']
6 ['+1 other card', '+1 other prerequisite', 'Essence Warden', 'Heroic Feast', 'Invisible Woman, Sue Storm', 'https://commanderspellbook.com//combo/2741-7690-7743--165/']
. . .
    ```
    The leading number is how many pieces are in the combination, then there is a list of pieces of the combination, then a link to the webpage for it.
5. Use script to check the infinte combinations in a Moxfield deck list.
    1. Go to Moxfield, find the deck of interest, click to download link, then "Download for MTGO", save the text file somewhere.
    2. run the script with the moxfieldTextfile argument.
    3. Example:
    `./comboParser.py --commanderSpellbookFiles specific/* recent/* comboFiles/* --moxfieldTextfile cabal-a-faster-krrik-storm--cedh-w-primer-20260808-031552.txt`
    4. which produces output like this:
    ```
./comboParser.py --commanderSpellbookFiles specific/* recent/* comboFiles/* --moxfieldTextfile cabal-a-faster-krrik-storm--cedh-w-primer-20260808-031552.txt --threshold=0
length of comboList = 28411
length of myCards = 87
4 ['Asmodeus the Archfiend', 'Necrotic Ooze', 'Skirge Familiar', 'https://commanderspellbook.com//combo/970-1656-1742/']
    ```
6. Use script to find cards that might be good for your current card combinations through the threshold argument.  It prints the 
    1. Example
    `./comboParser.py --commanderSpellbookFiles specific/* recent/* comboFiles/* --manaboxCsvfile ManaBox_Collection.csv --threshold 1 | tail`
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
    `./comboParser.py --commanderSpellbookFiles specific/* recent/* comboFiles/* --manaboxCsvfile ManaBox_Collection.csv --threshold 1 | grep Kodama | sort`
    5. That produces output like this:
    ```
4 ['Azorius Chancery', 'Dancing from Dark to Dawn', 'Kodama of the East Tree', 'https://commanderspellbook.com//combo/1479-3147-7889/']
4 ['Azorius Chancery', 'Kodama of the East Tree', 'Mole Man, Moloid Master', 'https://commanderspellbook.com//combo/1479-3147-7705/']
4 ['Azorius Chancery', 'Kodama of the East Tree', 'Quantum Misalignment', 'https://commanderspellbook.com//combo/1479-3147-5362/']
4 ['Azorius Chancery', 'Kodama of the East Tree', 'Thranduil, Sindarin Liege // Silvan Rally', 'https://commanderspellbook.com//combo/1479-3147-7893/']
4 ['Dancing from Dark to Dawn', 'Golgari Rot Farm', 'Kodama of the East Tree', 'https://commanderspellbook.com//combo/280-1479-7889/']
. . .
    ```