from flask import Flask, request, Response, jsonify
from random import randint

app = Flask(__name__)
phrase_list = ['oh, but the breadsticks'
              ]

@app.route('/jasperbot', methods=['POST'])
def jeremyahbot():
    text = request.form.get('text', '')
    if 'jeremyah' in text.lower():
        return jsonify(text=phrase_list[randint(0, len(phrase_list-1))])
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
