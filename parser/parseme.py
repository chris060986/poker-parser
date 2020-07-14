from flask.json import tojson_filter
from poker.room.pokerstars import PokerStarsHandHistory, _Street
import jsonpickle
from jsonpickle.handlers import BaseHandler
from poker.card import Card

example="""
PokerStars Hand #212700439098:  Hold'em No Limit ($0.01/$0.02 USD) - 2020/04/25 13:29:31 ET
Table 'Heike II' 9-max Seat #8 is the button
Seat 2: christinaS85 ($2 in chips) 
Seat 3: oeggel ($2.05 in chips) 
Seat 4: 3_Socks420 ($0.96 in chips) 
Seat 5: Laandris09 ($3.55 in chips) 
Seat 6: Ammageddon ($3.48 in chips) 
Seat 7: BigSiddyB ($2.93 in chips) 
Seat 8: sindyeichelbaum ($0.63 in chips) 
Seat 9: masterhodge ($1.80 in chips) 
masterhodge: posts small blind $0.01
KyJIaKoB: is sitting out 
christinaS85: posts big blind $0.02
*** HOLE CARDS ***
Dealt to christinaS85 [Th 5s]
KyJIaKoB leaves the table
oeggel: folds 
3_Socks420: folds 
Laandris09: folds 
Ammageddon: folds 
BigSiddyB: raises $0.02 to $0.04
sindyeichelbaum: raises $0.59 to $0.63 and is all-in
masterhodge: folds 
christinaS85: folds 
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
Seat 2: christinaS85 (big blind) folded before Flop
Seat 3: oeggel folded before Flop (didn't bet)
Seat 4: 3_Socks420 folded before Flop (didn't bet)
Seat 5: Laandris09 folded before Flop (didn't bet)
Seat 6: Ammageddon folded before Flop (didn't bet)
Seat 7: BigSiddyB showed [Qh As] and won ($0.62) with three of a kind, Threes
Seat 8: sindyeichelbaum (button) showed [Ad 9h] and won ($0.62) with three of a kind, Threes
Seat 9: masterhodge (small blind) folded before Flop
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

hh = PokerStarsHandHistory(hand_text=example)
hh.parse()
jsonpickle.handlers.register(StreetHandler)
jsonpickle.handlers.register(CardHandler)

jsondata = jsonpickle.encode(hh.turn)
print(jsondata)

jsondata = jsonpickle.encode(hh.flop)
print(jsondata)
