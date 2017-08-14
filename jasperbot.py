from flask import Flask, request, Response, jsonify

app = Flask(__name__)
link = 'My bad!'


@app.route('/jasperbot', methods=['POST'])
def lumbergh():
    text = request.form.get('text', '')
    if 'jasper' in text.lower() and link not in text:
        return jsonify(text=link)
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
