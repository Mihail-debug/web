def app(environ, start_response):
    status = '200 OK'
    data = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    header = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, header)
    return data
