import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="My title")

def make_app():
    settings = {'debug': True }
    handlers = [
		(r"/", MainHandler),
		(r"/index.html", MainHandler),
		(r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ]
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
