from poker import jsonencoding
from poker.room.pokerstars import PokerStarsHandHistory

# TODO: Remove file.

example = """
PokerStars Hand #212700439098:  Hold'em No Limit ($0.01/$0.02 USD) - 2020/04/25 13:29:31 ET
Table 'Heike II' 9-max Seat #8 is the button
Seat 2: pokerhero ($2 in chips) 
Seat 3: oeggel ($2.05 in chips) 
Seat 4: 3_Socks420 ($0.96 in chips) 
Seat 5: Laandris09 ($3.55 in chips) 
Seat 6: Ammageddon ($3.48 in chips) 
Seat 7: BigSiddyB ($2.93 in chips) 
Seat 8: sindyeichelbaum ($0.63 in chips) 
Seat 9: masterhodge ($1.80 in chips) 
masterhodge: posts small blind $0.01
KyJIaKoB: is sitting out 
pokerhero: posts big blind $0.02
*** HOLE CARDS ***
Dealt to pokerhero [Th 5s]
KyJIaKoB leaves the table
oeggel: folds 
3_Socks420: folds 
Laandris09: folds 
Ammageddon: folds 
BigSiddyB: raises $0.02 to $0.04
sindyeichelbaum: raises $0.59 to $0.63 and is all-in
masterhodge: folds 
pokerhero: folds 
BigSiddyB: calls $0.59
*** FLOP *** [3c 3h 3s]
*** TURN *** [3c 3h 3s] [7c]
*** RIVER *** [3c 3h 3s 7c] [Ks]
*** SHOW DOWN ***
BigSiddyB: shows [Qh As] (three of a kind, Threes)
sindyeichelbaum: shows [Ad 9h] (three of a kind, Threes)
BigSiddyB collected $0.62 from pot
sindyeichelbaum collected $0.62 from pot
*** SUMMARY ***
Total pot $1.29 | Rake $0.05 
Board [3c 3h 3s 7c Ks]
Seat 2: pokerhero (big blind) folded before Flop
Seat 3: oeggel folded before Flop (didn't bet)
Seat 4: 3_Socks420 folded before Flop (didn't bet)
Seat 5: Laandris09 folded before Flop (didn't bet)
Seat 6: Ammageddon folded before Flop (didn't bet)
Seat 7: BigSiddyB showed [Qh As] and won ($0.62) with three of a kind, Threes
Seat 8: sindyeichelbaum (button) showed [Ad 9h] and won ($0.62) with three of a kind, Threes
Seat 9: masterhodge (small blind) folded before Flop
"""

HAND13 = """PokerStars Hand #218853792406:  Hold'em No Limit ($0.02/$0.05 USD) - 2020/09/27 14:37:04 ET
Table 'Jiangxi IV' 9-max Seat #2 is the button
Seat 1: Mauor4ik ($6.96 in chips)
Seat 2: pulman23 ($4 in chips)
Seat 3: pokerhero ($5.06 in chips)
Seat 4: ROMPAL76 ($5 in chips)
Seat 5: BluffOnTable ($6.68 in chips)
Seat 6: LPSkillz ($5.14 in chips)
Seat 7: heureka3 ($2.80 in chips)
Seat 8: pasha-s-1983 ($2.42 in chips)
Seat 9: ErkZme ($5 in chips)
pokerhero: posts small blind $0.02
ROMPAL76: posts big blind $0.05
*** HOLE CARDS ***
Dealt to pokerhero [Ah 4c]
BluffOnTable: folds
LPSkillz: folds
heureka3: calls $0.05
pasha-s-1983: folds
ErkZme: folds
Mauor4ik: folds
pulman23: folds
pokerhero: calls $0.03
ROMPAL76: checks
*** FLOP *** [8s 5h Jh]
pokerhero: checks
ROMPAL76: bets $0.07
heureka3: calls $0.07
pokerhero: folds
*** TURN *** [8s 5h Jh] [2h]
ROMPAL76: checks
heureka3: checks
*** RIVER *** [8s 5h Jh 2h] [2c]
ROMPAL76: bets $0.10
heureka3: calls $0.10
*** SHOW DOWN ***
ROMPAL76: shows [Kh Jd] (two pair, Jacks and Deuces)
heureka3: mucks hand
ROMPAL76 collected $0.47 from pot
*** SUMMARY ***
Total pot $0.49 | Rake $0.02
Board [8s 5h Jh 2h 2c]
Seat 1: Mauor4ik folded before Flop (didn't bet)
Seat 2: pulman23 (button) folded before Flop (didn't bet)
Seat 3: pokerhero (small blind) folded on the Flop
Seat 4: ROMPAL76 (big blind) showed [Kh Jd] and won ($0.47) with two pair, Jacks and Deuces
Seat 5: BluffOnTable folded before Flop (didn't bet)
Seat 6: LPSkillz folded before Flop (didn't bet)
Seat 7: heureka3 mucked [As Qc]
Seat 8: pasha-s-1983 folded before Flop (didn't bet)
Seat 9: ErkZme folded before Flop (didn't bet)
"""

HAND14 = """PokerStars Hand #219345967221:  Hold'em No Limit ($0.02/$0.05 USD) - 2020/10/13 12:23:58 ET
Table 'Alauda II' 9-max Seat #9 is the button
Seat 1: MikeVulcan ($9.24 in chips) 
Seat 2: Chrissi986 ($5 in chips) 
Seat 3: shinga999 ($3.73 in chips) 
Seat 4: *#300427#* ($4.19 in chips) 
Seat 5: klugkk ($11.24 in chips) 
Seat 6: WingsForMyV ($5 in chips) 
Seat 7: georgio951 ($3.88 in chips) 
Seat 9: MKDunmore858 ($7.94 in chips) 
MikeVulcan: posts small blind $0.02
Chrissi986: posts big blind $0.05
*** HOLE CARDS ***
Dealt to Chrissi986 [Td 6c]
shinga999: folds 
*#300427#*: folds 
klugkk: folds 
WingsForMyV: folds 
georgio951: folds 
MKDunmore858: folds 
MikeVulcan: folds 
Uncalled bet ($0.03) returned to Chrissi986
Chrissi986 collected $0.04 from pot
Chrissi986: doesn't show hand 
*** SUMMARY ***
Total pot $0.04 | Rake $0 
Seat 1: MikeVulcan (small blind) folded before Flop
Seat 2: Chrissi986 (big blind) collected ($0.04)
Seat 3: shinga999 folded before Flop (didn't bet)
Seat 4: *#300427#* folded before Flop (didn't bet)
Seat 5: klugkk folded before Flop (didn't bet)
Seat 6: WingsForMyV folded before Flop (didn't bet)
Seat 7: georgio951 folded before Flop (didn't bet)
Seat 9: MKDunmore858 (button) folded before Flop (didn't bet)"""

# def get_json():
json_encoder = jsonencoding.JsonEncoder()

hh = PokerStarsHandHistory(hand_text=HAND14)
hh.parse()
jsondata = json_encoder.encode(hh)
print(jsondata)

hh2 = PokerStarsHandHistory(hand_text=example)
hh2.parse()
jsondata2 = json_encoder.encode(hh2)
print(jsondata2)
    # return jsondata


# def get_dict():
#     hh = PokerStarsHandHistory(hand_text=HAND14)
#     hh.parse()
#
#     pickler = Pickler()
#     return pickler.flatten(hh)