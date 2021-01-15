from clientRPC import clientRPC

HOST = '127.0.0.1'
PORT = 12346

rpc = clientRPC(HOST,PORT)
ans = rpc.add(2,3)
print("recvd ans ", ans)
mes = rpc.ConcatenateMessage("hello world")
print("concat msg ", mes)
ans = rpc.mult(4,5)
print(ans)

div = rpc.divide(2,4)
print(div)