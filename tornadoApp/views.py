# Create your views here.
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World<br>")

        self.write("<a href='/story/1'>link to story 1</a><br>")
        # self.write()
        self.write("<a href='/index'>Index Page</a><br>")
        if not self.get_cookie("mycookie"):
            self.set_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set yet!!<br>")
        else:
            self.write("Your cookie was set!!<br>")


class StoryHandler(tornado.web.RequestHandler):

    def get(self, story_id):
        self.write('You have requested with id '+story_id)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        # self.get_template_path()
        self.render("index.html", title="My title", items=items)


# class WebSocketChatHandler(tornado.websocket.WebSocketHandler):
#
#     def open(self):
#         print "Connection Opened"
#         print("open", "WebSocketChatHandler")
#
#     def on_close(self):
#         print "Closed the connection"
#
#     def on_message(self, message):
#         print "Message: ", message

# Application object routes incoming request to handlers
# application = tornado.web.Application([
#     (r'/', MainHandler),
# ])
#
# if __name__ == "__main__":
#     application.listen(8080)
#     tornado.ioloop.IOLoop.instance().start()

# main() function to start the server


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/story/([0-9]+)', StoryHandler),
        (r'/index', IndexHandler),
    ], template_path=os.path.join(os.path.dirname(__file__),  '..', "templates"))
    # application = tornado.wsgi.WSGIAdapter(tornado_app)
    # return application


def main():
    app = make_app()
    app.listen(8080)
    # tornado.web.Application.settings = {
    #     template_path = os.path.join(os.path.dirname(__file__), '..', "templates")
    # }
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()