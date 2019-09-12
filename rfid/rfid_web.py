from flask import Flask
import zmq
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/RFID/Read')
def rfid_read():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:6001')
    socket.setsockopt(zmq.SUBSCRIBE, b'card')
    topic = socket.recv()
    message = socket.recv()
    now = datetime.now()
    dt_tm_str = now.strftime('%Y-%m-%d %H:%M:%S')
    return json.dumps({'time':dt_tm_str, 'card_id':message.decode('utf-8')}) 
    
if __name__ == "__main__":
    app.run()
