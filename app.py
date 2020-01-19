from flask import Flask, request

import bot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'pyBot Beta v0.1'


'''
bot Request
{
    "Room": 'Room Name'
    "Sender": 'Sender Info'
    "Message": 'Message...'
}

bot Response
{
    "Result": "Response..."
}
'''


@app.route('/bot', methods=['POST'])
def pyKakaoBot():
    result = bot.listener(request.get_json())
    return result


@app.route('/posttest', methods=['POST'])
def posttest():
    data = request.get_json()
    return 'TestComplete ::::: %s' % data['test']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=37280)
