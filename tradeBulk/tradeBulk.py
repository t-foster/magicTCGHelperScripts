#!/usr/bin/python3

import argparse
import csv
from collections import defaultdict



## parse the arguments
parser = argparse.ArgumentParser()

parser.add_argument('--giver', required=True) 
parser.add_argument('--receiver', required=True) 
parser.add_argument('--giver_threshold', type=int, default=4) 
parser.add_argument('--receiver_threshold', type=int, default=0) 
args = parser.parse_args()


giverCards = defaultdict(int)
receiverCards = defaultdict(int)


with open(args.giver, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    #print(len(list(reader)))
    for row in reader:
        giverCards[row['Name'] + " (" + row['Rarity'] + ")"] += int(row['Quantity'])

with open(args.receiver, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    #print(len(list(reader)))
    for row in reader:
        receiverCards[row['Name'] + " (" + row['Rarity'] + ")"] += int(row['Quantity'])

sorted_dict_desc = dict(sorted(giverCards.items(), key=lambda item: item[1], reverse=False))

for key, value in sorted_dict_desc.items():
    #print(f"consider: {value}: {key}")
    if value > args.giver_threshold and receiverCards[key] <= args.receiver_threshold:
        print(f"consider trading: {value}: {key}")