#!/usr/bin/python3

import argparse
import xml.etree.ElementTree as ET
import csv
from collections import defaultdict

comboList = set()
href = str("")



## recursive helper function for parsing an individual combo in an html scrape
def parseCommanderSpellbookCombo(theNode):
    retval = set()
    if theNode.tag == "span":
        retval.add(theNode.text)
    # print(child.tag, child.attrib)
    for child in theNode:
        retval.update(parseCommanderSpellbookCombo(child))
    ## using the raw span values gets extra stuff we dont care about
    retval.discard("Cards in combo:")
    retval.discard(None)
    return retval

## recursive helper function for going through html scrape and assembling the combos
def recurseCommanderSpellbookFiles(theNode, href):
    if "href" in theNode.attrib:
        href = str("https://commanderspellbook.com/" + theNode.attrib["href"])
    if "class" in theNode.attrib and "comboResultSection" in theNode.attrib["class"]:
        # print(href)
        thisCombo = parseCommanderSpellbookCombo(theNode)
        ## remove query from href
        thisCombo.add(href.split("?")[0])
        comboList.add(frozenset(thisCombo))
    for child in theNode:
        recurseCommanderSpellbookFiles(child, href)

## parse the arguments
parser = argparse.ArgumentParser()

parser.add_argument('--commanderSpellbookFiles', nargs='+') 
parser.add_argument('--manaboxCsvfile') 
parser.add_argument('--moxfieldTextfile') 
parser.add_argument('--threshold', type=int, default=0) 
args = parser.parse_args()

## iterate through the combo html files
for combofile in args.commanderSpellbookFiles:
    #print("filename = {}".format(combofile))

    tree = ET.parse(combofile)
    root = tree.getroot()

    recurseCommanderSpellbookFiles(root, href)


print("length of comboList = {}".format(len(comboList)))

myCards = set()

if args.manaboxCsvfile != None:
    ## iterate through manabox csv file
    with open(args.manaboxCsvfile, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        #print(len(list(reader)))
        for row in reader:
            # Access elements by column header name
            myCards.add(row['Name'])

if args.moxfieldTextfile != None:
    ## iterate through moxfield text file
    with open(args.moxfieldTextfile, mode='r', encoding='utf-8') as file:
        #print(len(list(reader)))
        for line in file:
            #print(line[2:-1])
            ## TODO might need finessing for foils and fancy formatting
            myCards.add(line[2:-1])

print("length of myCards = {}".format(len(myCards)))
cardCount = defaultdict(int)

## iterate through list of combos and see if I have all the cards in them
for combo in comboList:
    countOfCardsInCombo = 0
    for card in combo:
        if " other " in card or "commanderspellbook" in card or card in myCards:
            countOfCardsInCombo += 1

    #print("countOfCardsInCombo = {} , len(combo) = {}".format(countOfCardsInCombo, len(combo)))
    if (countOfCardsInCombo + args.threshold) >= len(combo):
        print("{} {}".format(len(combo),sorted(combo)))
        for card in combo:
            if " other " not in card and "commanderspellbook" not in card and card not in myCards:
                cardCount[card] += 1

if args.threshold != 0:
    # Sort by value in reverse
    sorted_dict_desc = dict(sorted(cardCount.items(), key=lambda item: item[1], reverse=False))

    for key, value in sorted_dict_desc.items():
        print(f"consider: {value}: {key}")



