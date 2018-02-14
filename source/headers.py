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
    codeText = {200:'OK', 201:'Created', 202:'Accepted', 203:'Non-Authoriative Information', 204:'No Content',
				205:'Reset Content', 206:'Partial Content', 207:'Multi Content', 208:'Already Reported', 226:'IM used',
				300:'Multiple Choices', 301:'Moved Permanently', 302:'Found', 303:'See Other', 304:'Not Modified',
				305:'Use Proxy', 306:'Switch Proxy', 307:'Temporary Redirect', 308:'Permanently Redirect',
				404:'Not Found', 418:"I'm a teapot", 500:'Internal Server Error'} [code]
    header = header + 'HTTP/1.1 '
    header = header + str(code) + ' ' + codeText
    header = header + '\r\n'
    header = header + 'Content-Length: ' + str(contentLen) + '\r\n'
    header = header + 'Content-Type: ' + contentType + '\r\n'
    header = header + '\r\n'
    return header
