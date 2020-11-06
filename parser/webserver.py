from flask import Flask, render_template, request
from poker.room.pokerstars import PokerStarsHandHistory
from poker import jsonencoding

webserver = Flask(__name__)


@webserver.route('/web', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        req_form = request.form
        hand = req_form["hand"]
        cleaned_hand = hand.replace("\r", " ")

        json_encoder = jsonencoding.JsonEncoder()

        hh = PokerStarsHandHistory(hand_text=cleaned_hand)
        hh.parse()
        jsondata = json_encoder.encode(hh)
        print(jsondata)
        return render_template("index.html", result=jsondata)
    else:
        return render_template('index.html')


@webserver.route('/pokerstars', methods=['POST'])
def pokerstars():
    data = request.json

    # hand = req_form["hand"]
    # cleaned_hand = hand.replace("\r", " ")
    print(data)
    return "200"


if __name__ == '__main__':
    webserver.run(debug=True, host='0.0.0.0')
