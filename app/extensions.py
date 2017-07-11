from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jsglue import JSGlue
from flask_marshmallow import Marshmallow
from flask_security import Security

io = SocketIO()
db = SQLAlchemy()
migrate = Migrate(db=db)
glue = JSGlue()
ma = Marshmallow()
security = Security()


def security_init_kwargs():
    from auth.models import user_datastore
    return dict(datastore=user_datastore)


def io_init_kwargs():
    return dict(logger=True, engineio_logger=True)
