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
