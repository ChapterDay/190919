from flask import Flask, Response
from flask_cors import CORS
from time import sleep
import zmq

app = Flask(__name__)

@app.route('/LCD/Write/<message>')
def lcd_write(message):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:6002')
    sleep(1)
    print('sending message...')
    socket.send_string('text', zmq.SNDMORE)
    socket.send_string(message)
    return 'OK' 

    
if __name__ == "__main__":
    CORS(app)
    app.run(host='0.0.0.0', port=5002)
