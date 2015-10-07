import SocketServer
import json
import time
import sys




class LedServer(SocketServer.ThreadingTCPServer):
		allow_reuse_address = True
		server = None
		def __init__(self, server_address, handler,main):
				SocketServer.ThreadingTCPServer.__init__(self, server_address,handler)
				LedServer.main = main
	
class LedServerHandler(SocketServer.BaseRequestHandler):

            

    def handle(self):
        while True:
            receivedData = self.request.recv(4)
            if not receivedData: break
            try:
                test = json.loads( self.request.recv(int(receivedData)))
                callbackID = test["id"]
                data = test["command"]

                i = test["pid"]
                if isinstance(data,dict):
                    packet = LedServer.main.proccessRequest(i, data)
                else:
                    packet = LedServer.main.proccessRequest(i,bytearray(data, "UTF-8"))
                re = {};
                re["id"] = callbackID
                if isinstance(packet.returnString(), str):
                    re["returnString"] = str(packet.returnString())
                else:
                    re["returnString"] = packet.returnString()
                self.request.sendall(json.dumps(re) + " ")
            except Exception, e:
                print "Exception wile processing P1: ", e
                print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
