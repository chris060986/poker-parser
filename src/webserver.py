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
        try:
            req_form = request.form
            hand = req_form["hand"]

            hh_json_str = parser.get_json_str(hand)
            hh_doc = parser.get_json_doc(hand)

            print(hh_json_str)
            couch_db.save_poker_hand(hh_doc['hero'], hh_doc)
        except Exception:
            hh_json_str = "exception while handling input of request: " + str(request.form)
        return render_template("index.html", result=hh_json_str)
    else:
        return render_template('index.html')


@app.route('/pokerstars/<hero>', methods=['POST'])
def pokerstars(hero):
    try:
        data = request.json
        # should be logging
        print("Data received, try to parse: " + str(data))
        hh_doc = parser.get_json_doc(data['hand'])
        couch_db.save_poker_hand(hero, hh_doc)
    except Exception as e:
        print(e)
        return "500"
    return "200"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
