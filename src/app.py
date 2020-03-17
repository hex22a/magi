import json
import falcon


class EchoResource:
    def on_get(self, req, resp, field):
        resp.body = json.dumps({
            "magic": 500,
            "message": field
        })


def create_app():
    app = falcon.API()

    app.add_route("/{field}", EchoResource())

    return app
