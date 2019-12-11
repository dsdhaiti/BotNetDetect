# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:33:23 2019

@author: -
"""
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

followers = [
 "BakaryDembo2",
 "23Greyhound",
 "MrsDriscoll",
 "platedbullets",
 "worlddo17858792",
 "Srachelle3",
 "SandiLo71521482",
 "don_narp",
 "gracelover712",
 "leroylewis58",
 "phizog1",
 "DonnaJ183",
 "JustOne652",
 "USMCSDI",
 "Kristin1518",
 "TheyCallMeTomO1",
 "VexanFishing",
 "WendyKory3",
 "JordanElizabeth",
 "ariel_strength",
 "Freedom56810907",
 "theoxlox",
 "Chrisda58788186",
 "landiak2",
 "EvanAKilgore",
 "troblmakr4evr",
 "SteveHusker",
 "EricHartford6",
 "Dennisriordan4",
 "cjamwash",
 "SheldonKaufman",
 "Domer1976",
 "LadyDianeGuest",
 "TRUMPTRAINENGI1",
 "OfficialKindlyM",
 "an2stand",
 "LisaPurdue2",
 "Terry_BH",
 "PrabhuMteverest",
 "LeRoy4487",
 "LTyrney",
 "MrTwittttt",
 "CharlotteKayMo1",
 "neil32331615",
 "Davetheironman",
 "DandelionTuscan",
 "LawGorman",
 "Darrell03092157",
 "SusanHa58439616",
 "RWSalt",
 "mjgranger1",
 "deviceproblem",
 "RichardOBryan",
 "ruthtaka",
 "dmor55",
 "wildcatmom2013",
 "EsqRogowski",
 "OliviaDabson",
 "sue51684",
 "RealMattCouch"]


G.add_node('dannydeacon1970')

for x in followers:
    G.add_edge('dannydeacon1970',x)
plt.show()
nx.draw(G, with_labels=True)

plt.savefig("path.png")
#G.clear()