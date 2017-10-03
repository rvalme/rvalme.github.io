import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="My title")

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
        (r"/", MainHandler),
        (r"/websocket", WebSocketHandler),
        (r"/index.html", MainHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ]
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
