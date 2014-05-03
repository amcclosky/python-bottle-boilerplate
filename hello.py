import os
import sys
import logging

import bottle

DEBUG = os.environ.get('BOTTLE_DEBUG', True)
RELOAD = os.environ.get('BOTTLE_RELOAD', True)
PORT = os.environ.get('BOTTLE_PORT', '8080')
HOST = os.environ.get('BOTTLE_HOST', '0.0.0.0')

logging_level = logging.INFO
if DEBUG:
    logging_level = logging.DEBUG

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

app = bottle.Bottle()


def get_message(name):
    return "Hello {name}!".format(name=name)


@app.route('/')
@app.route('/hello')
def hello():
    return {'message': get_message("World")}


@app.route('/hello/:name')
def hello_name(name):
    return {'message': get_message(name)}


def main():
    bottle.debug(DEBUG)

    bottle.run(app, server='wsgiref', port=PORT, host=HOST, reloader=RELOAD)

if __name__ == "__main__":
    sys.exit(main())