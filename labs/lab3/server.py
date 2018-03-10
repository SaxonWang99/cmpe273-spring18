import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PULL)
sock.bind("tcp://127.0.0.1:5678")
sock2 = context.socket(zmq.PUB)
sock2.bind("tcp://127.0.0.1:5679")
# Run a simple "Echo" server
while True:
    message = sock.recv()
    #message = message.decode()
    #message = message[::-1]
    #sock.send_string("Echo: " + message)
    sock2.send( message)
    print("[Server] Echo: " + message.decode())