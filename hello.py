bind = "0.0.0.0:8080"

def app(environ, start_response):
    data = [(pair + '\n').encode('utf-8') for pair in environ['QUERY_STRING'].split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    return data