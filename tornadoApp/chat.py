__author__ = 'Heta'
# Create your views here.
import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
        self.write("<a href='/story/1'>link to story 1</a>")


class WebSocketChatHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print "Connection Opened"
        print("open", "WebSocketChatHandler")

    def on_close(self):
        print "Closed the connection"

    def on_message(self, message):
        print "Message: ", message





class StoryHandler(tornado.web.RequestHandler):

    def get(self, story_id):
        self.write('You have requested with id '+story_id)



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
    ])


def main():
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()