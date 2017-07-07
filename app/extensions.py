from flask_socketio import SocketIO

io = SocketIO()


def io_init_kwargs():
    return dict(logger=True, engineio_logger=True)
