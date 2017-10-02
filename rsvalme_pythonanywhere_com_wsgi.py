import tornado.ioloop
import tornado.wsgi
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="My title")

def make_app():
    settings = {'debug': False }
    handlers = [
		(r"/", MainHandler),
		(r"/index.html", MainHandler),
		(r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ]
    return tornado.wsgi.WSGIApplication(handlers, **settings)

application = make_app()
