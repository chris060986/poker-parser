from jsonpickle import Pickler
from poker.jsonencoding import JsonEncoder
from poker.room.pokerstars import PokerStarsHandHistory


class PokerstarsParser:

    def __init__(self):
        self.pickler = Pickler()
        self.json_encoder = JsonEncoder()

    @staticmethod
    def parse_hand_history(hand_history):
        hh = PokerStarsHandHistory(hand_text=hand_history)
        hh.parse()
        return hh

    @staticmethod
    def _clean_hand_history_str(raw_string):
        return str.replace(raw_string, "\r", "")

    def get_json_str(self, hand_history_str):
        hand_history = self.parse_hand_history(self._clean_hand_history_str(hand_history_str))
        return self.json_encoder.encode(hand_history)

    def get_json_doc(self, hand_history_str):
        hand_history = self.parse_hand_history(self._clean_hand_history_str(hand_history_str))
        return self.pickler.flatten(hand_history)