#!/usr/bin/python
#import signal
#import datetime
import tornado.httpserver
import tornado.websocket
import tornado.ioloop

#def signal_handler(signum, frame):
#    tornado.ioloop.IOLoop.instance().stop()

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        print 'New connection'
        #self.write_message("Hello user")
        WSHandler.clients.append(self)

    def on_message(self, message):
        #print 'Message received: %s' % message
        WSHandler.write_to_clients(message)

    def on_close(self):
        print 'Connection closed'
        WSHandler.clients.remove(self)

    @classmethod
    def write_to_clients(cls, message):
        #print "Writing message to all clients"
        for client in cls.clients:
            client.write_message(message)


application = tornado.web.Application([
  (r'/', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9999)
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=10), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()
    #signal.signal(signal.SIGINT, signal_handler)
