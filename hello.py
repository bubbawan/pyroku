def app(env, start_response):
    data = 'Hello WSGI'
    start_response('200 OK', [('Content-Type','text/plain'), ('Content-Length', str(len(data)))])
    return iter([data])

