import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options

import os.path
from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("source/index.html", title="My title")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        self.write_message("Your message was: " + message)

    def on_close(self):
        pass

def make_app():
    settings = {'debug': True }
    handlers = [
        (r"/", MainHandler), (r"/websocket", WebSocketHandler),
        (r"/index.html", MainHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ]
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
