import zmq
import msgpack
import time

class ZMQClient(object):
	
	def __init__(self):
		self.context = zmq.Context()
		self.sock = self.context.socket(zmq.PUB)
		self.sock.bind("tcp://*:5555")
		time.sleep(.5)

	def send(self, feature):
	    msg = msgpack.packb(feature)
	    self.sock.send(msg)
	    message = self.sock.recv()
