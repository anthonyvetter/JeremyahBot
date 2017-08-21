from flask import Flask, request, Response, jsonify
from random import randint

app = Flask(__name__)
phrase_list = ['oh, but the breadsticks',
               'Lock them in a closet with some cheerios',
               'Blink twice if you\'re being kept in a closet against your will.',
               'If that were the case at least I\'d have a wicked cool beard and be able to come out of a dark closet covered in magnetic ribbons',
               'I\'m pretty sure it\'s my kids fault.',
               'Kids are disease machines',
               'and it exploded',
               'Fantasic',
               'no',
               'I applaud your wishful thinking, optimism is good among those who are about to die',
               'I dunno',
               'puttin the fun in disfunctional',
               'Little known fact about horses: They keep excellent records of ip addresses.',
               'In fact, you control the pizza. So you can summon it at will.',
               'so much suppression',
               'I totally deleted that meeting by mistake',
               ':jeremyah:',
               'yay',
               'woohoo',
               'Rule #1: A small number times a big number, is a big number.',
               'Rule #2: Query not list',
               'Rule #3: Consistency is King',
               'Rule #4: The goal is not to be only as good today as yesterday.',
               'Rule #5: Memory and Context are the enemy of the automated process. ',
               'Rule #6: Best way to encourage DR planning is to burn down the building next door.',
               'Rule #7: If you\’re parsing text you\’ve already lost.',
               'Rule #8: Don\’t wait, evaluate.',
               'Rule #9: Failure over time is 100%',
               'Rule #10: Don\’t move anything you don\’t absolutely have to move.',
               'Rule #11: Don\’t transform anything you don\’t absolutely have to transform.',
               'Rule #12: Remembering things is for computers, patterns are for humans.',
               'Rule #13: Do The Right Thing isn\’t a plan.',
              ]

@app.route('/jeremyahbot', methods=['POST'])
def jeremyahbot():
    text = request.form.get('text', '')
    if 'jeremyah' in text.lower():
        return jsonify(text=phrase_list[randint(0, len(phrase_list-1))])
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
