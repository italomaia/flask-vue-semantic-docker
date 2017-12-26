import os


def load_env(name):
    """
    Tries to load name from environment variables by name; if
    it is not set, appends "_FILE" to `name` and tries to load
    it from filesytem. This is quite useful for loading docker
    secrets.
    """
    value = os.getenv(name)
    if value is None:
        value = os.getenv('%s_FILE' % name)
        if value is not None and os.path.exists(value):
            with open(value) as fs:
                return fs.read()
    return value
