from flask import Flask, render_template, request
from poker.room.pokerstars import PokerStarsHandHistory
from poker import jsonencoding

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        req_form = request.data
        hand = req_form["hand"]
        cleaned_hand = hand.replace("\r", " ")

        json_encoder = jsonencoding.JsonEncoder()

        hh = PokerStarsHandHistory(hand_text=cleaned_hand)
        hh.parse()
        jsondata = json_encoder.encode(hh)
        return render_template("index.html", result=jsondata)
    else:
        return render_template('index.html')

@app.route('/pokerstars', methods = ['POST'])
def pokerstars():
    data = request.json

    # hand = req_form["hand"]
    # cleaned_hand = hand.replace("\r", " ")
    print(data)
    return "200"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')