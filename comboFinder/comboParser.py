#!/usr/bin/python3

import argparse
import json
import csv
from collections import defaultdict

comboList = set()


## parse the arguments
parser = argparse.ArgumentParser()

parser.add_argument('--jsonfile', required=True) 
parser.add_argument('--manaboxCsvfile', required=True) 
parser.add_argument('--threshold', type=int, default=0) 
parser.add_argument('--colorIdentity', type=str, default="WUBRGC") 
args = parser.parse_args()

## open json file


# Open and parse the JSON file
with open(args.jsonfile, 'r', encoding='utf-8') as file:
    data = json.load(file)

    print("timestamp = {}".format(data["timestamp"]))
    for variant in data["variants"]:
        #print(variant["id"])
        variantInfo=set()
        variantInfo.add("https://commanderspellbook.com/combo/" + variant["id"])
        for use in variant["uses"]:
            variantInfo.add(use["card"]["name"])
        variantInfo.add("identity=" + variant["identity"])
        comboList.add(frozenset(variantInfo))


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


print("length of myCards = {}".format(len(myCards)))
cardCount = defaultdict(int)

## iterate through list of combos and see if I have all the cards in them
for combo in comboList:
    countOfCardsInCombo = 0
    hasColorIdentity = True
    for card in combo:
        if "identity=" in card or "commanderspellbook" in card or card in myCards:
            countOfCardsInCombo += 1
        if "identity=" in card:
            for color in card[9:]:
                if color not in args.colorIdentity:
                    hasColorIdentity = False

    #print("countOfCardsInCombo = {} , len(combo) = {}".format(countOfCardsInCombo, len(combo)))
    if (countOfCardsInCombo + args.threshold) >= len(combo) and hasColorIdentity:
        print("{} {}".format(len(combo)-2,sorted(combo)))
        for card in combo:
            if "identity=" not in card and "commanderspellbook" not in card:
                cardCount[card] += 1

if args.threshold != 0 or args.colorIdentity != "WUBRGC":
    # Sort by value in reverse
    sorted_dict_desc = dict(sorted(cardCount.items(), key=lambda item: item[1], reverse=False))

    for key, value in sorted_dict_desc.items():
        print(f"consider: {value}: {key}")



