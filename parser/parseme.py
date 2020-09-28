from flask.json import tojson_filter
from poker.room.pokerstars import PokerStarsHandHistory, _Street
import jsonpickle
from jsonpickle.handlers import BaseHandler
from poker.card import Card

example="""
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

@jsonpickle.handlers.register(Card, base=True)
class CardHandler(BaseHandler):

    def flatten(self, obj, data):
        print(obj.__getattribute__('suit'))
        data = {}
        data['rank'] = obj.rank.val
        data['suit'] = obj.suit.name
        return data

    def restore(self, obj):
        raise NotImplementedError

CardHandler.handles(Card)

@jsonpickle.handlers.register(_Street, base=True)
class StreetHandler(BaseHandler):

    def flatten(self, obj, data):
        data = {}
        data['street'] = list(obj.__getattribute__('cards'))
        return data

    def restore(self, obj):
        raise NotImplementedError

hh = PokerStarsHandHistory(hand_text=HAND13)
hh.parse()
jsonpickle.handlers.register(StreetHandler)
jsonpickle.handlers.register(CardHandler)

jsondata = jsonpickle.encode(hh.turn)
print(jsondata)

jsondata = jsonpickle.encode(hh.flop)
print(jsondata)
