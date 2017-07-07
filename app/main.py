from empty import Empty


class App(Empty):
    def configure_error_handlers(self):
        """SPA"""
        pass


if __name__ == '__main__':
    from auto import app
    from extensions import io

    io.run(app)
