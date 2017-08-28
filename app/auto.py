import eventlet
eventlet.monkey_patch()

from empty import app_factory
from main import App
import config
import traceback
import logging

try:
    # SPA setup; template_folder ignored;
    app = app_factory(
        'app', config,
        template_folder=None,
        base_application=App)
except Exception as e:
    logging.error(traceback.format_exc())
    raise e
