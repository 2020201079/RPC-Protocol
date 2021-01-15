from clientRPC import clientRPC

HOST = '127.0.0.1'
PORT = 12346

rpc = clientRPC(HOST,PORT)
ans = rpc.add(HOST,PORT)
