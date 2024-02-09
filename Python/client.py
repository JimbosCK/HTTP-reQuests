from http.client import HTTPConnection, HTTPResponse

def send_get_request(host, port) -> HTTPResponse:
    connection = HTTPConnection(host, port)
    headers = {'name': 'Jimbos'}
    path = '/'

    connection.request('GET', path, headers=headers)

    response = connection.getresponse()
    connection.close()
    return response




print(send_get_request(host='', port=3000).read().decode('utf-8'))