import zmq
import threading
import sys
import time

# ZeroMQ Context
context = zmq.Context()
username = sys.argv[1]
# Define the socket using the "Context"
chat_sock = context.socket(zmq.PUSH)
chat_sock.connect("tcp://127.0.0.1:5678")

print("User [%s] Connected to the chat server." %(username))

def start_main_loop():
    sub_sock = context.socket(zmq.SUB)
    sub_sock.connect("tcp://127.0.0.1:5679")
    sub_sock.setsockopt_string(zmq.SUBSCRIBE, "")

    while True:
        time.sleep(1)
        #print("Thread is running.")
        replyMsg = sub_sock.recv().decode()
        if replyMsg:
            print(replyMsg)

def run():
    thread = threading.Thread(target=start_main_loop)
     # make sure this background thread is daemonized
     # so that when user sends interrupt, whole program stops
    thread.start()


#print("[Client]:"+msg)
# Send a "message" using the socket
run()
while True:
    msg = input("[{0}] > ".format(username))
    msg = "[%s]:  %s" % (username, msg)
    chat_sock.send(msg.encode())