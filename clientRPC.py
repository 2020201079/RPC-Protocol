import socket 
import json
import sys

HOST = '127.0.0.1'
PORT = 12346

class callableFunc:
    def __init__(self,name,numberOfArgs):
        self.name = name
        self.numberOfArgs = numberOfArgs
    def __call__(self,*args):
        if len(args) != self.numberOfArgs :
            print("incorrect args in " + self.name)
            exit()

class clientRPC:
    functionDetails = []
    def __init__(sef,HOST,PORT):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((HOST,PORT))
        s.sendall(b'getFunctions')
        data = s.recv(1024).decode('utf-8')
        data = data.split('$')
        for d in data:
            funcDetails = json.loads(d)
            print(funcDetails['args'])
            print("number of args : ",len(funcDetails['args']))
            newFunc = callableFunc(funcDetails['name'],len(funcDetails['args']))
            setattr(clientRPC,funcDetails['name'],newFunc)

def main():
    rpc = clientRPC(HOST,PORT)

    rpc.add(2,3)
    rpc.ConcatenateMessage("hello","its me")

if __name__ == "__main__":
    main()