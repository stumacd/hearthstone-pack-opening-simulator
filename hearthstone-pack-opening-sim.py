#! /usr/bin/env python
import pprint
from random import randint
#import matplotlib.pyplot as plt

class Rarity:
    Common = 0
    Rare = 1
    Epic = 2
    Legendary = 3

class Expansion:
    Expert = [94,81,37,33]
    GvG = [40,37,26,20]
    TGT = [49,36,27,20]

class Dust:
    Enc = [40, 100, 400, 1600]
    Dis = [ 5,  20, 100,  400]

#[75,20, 4, 1]
class Probability:
    Drop = [77,95, 99, 100]
    Gold = [ 2, 6, 5, 8]

# Add a card to the collection
def add_card(rarity):
    if randint(1,100) <= Probability.Gold[rarity]:
        return Dust.Enc[rarity]
    else:
        num = randint(1,exp[rarity])-1
    if collection[rarity][num] is 0:
        return Dust.Dis[rarity]
    else:
        collection[rarity][num] -= 1
        return 0

# Opan a pack
def get_pack():
    dust_back = 0
    all_com = True

    for i in xrange(0,5):
        card = 0
        num = randint(1,100)
        if num > Probability.Drop[Rarity.Common] :
            all_com = False
        for j in xrange(Rarity.Common,Rarity.Legendary+1):

            if num <= Probability.Drop[j]:
                if i is 4 and j is Rarity.Common and all_com:
                    dust_back += add_card(Rarity.Rare) 
                else :
                    dust_back += add_card(j) 
                break
    return dust_back

# See what remains to be made to complate the collection
# TODO make add card subtract from an initial dust required value.
def dust_reqd(collection):
    dust_total = 0
    for j in xrange(Rarity.Common,Rarity.Legendary+1):
        dust_total += sum(collection[j]) * Dust.Enc[j]
    return dust_total

# Dict to store results
d = {}
# Choose Expansion
exp = Expansion.GvG

if __name__ == "__main__":
    samples = 1000
    print "Simulating %d player experiences - opening packs!" % samples
    tot = 0
    for z in xrange(0,samples):
        packs = 0
        mydust = 0
        collection = [[2]*exp[Rarity.Common] , [2]*exp[Rarity.Rare],  [2]*exp[Rarity.Epic], [1]*exp[Rarity.Legendary] ]
        while 1:
            packs += 1
            mydust += get_pack()
            if (mydust > dust_reqd(collection)):
                if packs in d:
                    d[packs] += 1
                else:
                    d[packs] = 1
                break
    
    for k,v in d.items():
        tot+=k*v
    tot /= samples
    print "On average you will need to open %d packs to have a complate (non-golden) collection." % tot

    #plt.bar(d.keys(), d.values(), align='center', width=1)
    #plt.show()