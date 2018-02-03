class header:
    def __init__(self, header):
        # Get type of command
        self.command = ''
        if header[0:3] == 'GET':
            self.command = 'GET'
        elif header[0:4] == 'POST':
            self.command = 'POST'

        header_bd = header.split('\r\n')
        self.cmdText = header_bd[0]
        self.headers = {}

        for s in header_bd[1:len(header_bd)-2]:
            t = s.split(": ")

            self.headers[t[0]] = t[1]

def create_headers(code, contentLen, contentType):
    header = ''
    # Code is int
    # First add the http thingy
    codeText = {200:'OK', 301:'Moved Permanently', 404:'Not Found', 418:"I'm a teapot", 500:'Internal Server Error'} [code]
    header = header + 'HTTP/1.1 '
    header = header + str(code) + ' ' + codeText
    header = header + '\r\n'
    header = header + 'Content-Length: ' + str(contentLen) + '\r\n'
    header = header + 'Content-Type: ' + contentType + '\r\n'
    header = header + '\r\n'
    return header