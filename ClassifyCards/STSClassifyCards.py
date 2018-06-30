# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 03:09:28 2018

@author: NingYu Zhang
"""

with open('cards.atlas', 'r') as f:
    lines = f.readlines()
    
    
#读出有用数据 并全部小写
cards = []
for line in lines:
    if line[:3]=='red' or line[:3]=='blu' or line[:3]=='gre' or line[:3]=='col' or line[:3]=='cur' or line[:3]=='sta':
        cards.append(line[:-1].lower())




red = []
blue = []
green = []
colorless = []
state = []
curse = []
for card in cards:
    if card[0]=='r':
        red.append(card)
    elif card[0]=='b':
        blue.append(card)
    elif card[0]=='g':
        green.append(card)
    elif card[0]=='s':
        state.append(card)
    elif card[:2]=='co':
        colorless.append(card)
    else:
        curse.append(card)
        
#所有卡牌的type和color
dict_cards = {}
for card in red:
    tmp = card.split('/')
    dict_cards[tmp[2]] = {'type': tmp[1], 'color': tmp[0]}
for card in blue:
    tmp = card.split('/')
    dict_cards[tmp[2]] = {'type': tmp[1], 'color': tmp[0]}
for card in green:
    tmp = card.split('/')
    dict_cards[tmp[2]] = {'type': tmp[1], 'color': tmp[0]}
for card in colorless:
    tmp = card.split('/')
    dict_cards[tmp[2]] = {'type': tmp[1], 'color': tmp[0]}
for card in state:
    tmp = card.split('/')
    dict_cards[tmp[1]] = {'type': tmp[0], 'color': tmp[0]}
for card in curse:
    tmp = card.split('/')
    dict_cards[tmp[1]] = {'type': tmp[0], 'color': tmp[0]}

import json
with open('sorted_cards.json', 'w') as f:
    json.dump(dict_cards, f, indent=2)
    

        
