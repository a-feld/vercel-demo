def app(environ, start_response):
    start_response(
        "200 OK", (("Content-Type", "text/plain"), ("Cache-Control", "no-store"))
    )
    return (b"Hello World",)
