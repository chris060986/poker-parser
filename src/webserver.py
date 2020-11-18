from flask import Flask, render_template, request
from config import config

from poker_parser.database.couch_db import CouchDBAccess
from poker_parser.parser.pokerstars_parser import PokerstarsParser


app = Flask(__name__)
app.config.from_object(config.PokerParserConfig)
if app.config["DEBUG"]:
    print(app.config)
parser = PokerstarsParser()
couch_db = CouchDBAccess(app.config)


@app.route('/web', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        req_form = request.form
        hand = req_form["hand"]
        cleaned_hand = hand.replace("\r", " ")

        hh_json_str = parser.get_json_str(cleaned_hand)
        hh_doc = parser.get_json_doc(cleaned_hand)

        print(hh_json_str)
        couch_db.save_poker_hand('pokerhero', hh_doc)

        return render_template("index.html", result=hh_json_str)
    else:
        return render_template('index.html')


@app.route('/pokerstars/<hero>', methods=['POST'])
def pokerstars(hero):
    data = request.json

    hh_doc = parser.get_json_doc(data['hand'])
    couch_db.save_poker_hand(hero, hh_doc)
    print(data)
    return "200"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
