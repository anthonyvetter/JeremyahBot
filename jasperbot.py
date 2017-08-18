from flask import Flask, request, Response, jsonify
from random import randint

app = Flask(__name__)
phrase_list = ['my bad', 
'10-4', 
'damn dewd', 
'hooray', 
'is that a "no"?', 
'#deepThoughts', 
'/inspireme', 
'mm i want steak now', 
'love it', 
'tinman-pxe is dead. long live tinman-pxe',
'test passed :wink:', 
':smile:', 
':thumbsupparrot:', 
'neg', 
'hah true', 
':poke ball:', 
'usually the sun makes things hotter? I dunno', 
'that\'s cool tech, although it sounds backwards :slightly_smiling_face:', 
'ok now the next thing breaks', 
'yeah that ain\'t ever gonna work', 
'yeah looks like their regex is wrong :disappointed:', 
'still not working :disappointed:', 
'you\'d call me and i\'d read you out a 14 character mess', 
'ahh that\'s in master', 
'i\'m manually adding it to see if it will help', 
'the smoke tests are failing due to a known issue :wink:', 
'been there', 
'#almostDeep', 
'such parrot, much deploy', 
'so random', 
'LMAO']


@app.route('/jasperbot', methods=['POST'])
def jasperbot():
    text = request.form.get('text', '')
    if 'jasper' in text.lower():
        return jsonify(text=phrase_list[randint(0, 30)])
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
