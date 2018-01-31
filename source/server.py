import socket
import time

def server(HOST = '', PORT = 80):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.bind((HOST, PORT))
		sock.listen(3)
		# Server loop
		while True:
			# Send infomation
			conn, addr = sock.accept()
			out = conn.recv(2048)
			input = bytes.decode(out)
			
			# Parse header string
			# First line is the request line
			if input[0:3] == 'GET':
				# this is a get request, read until \r\n because http uses this.
				nl = input.find('\r\n')
				print(addr[0] + ' - "' + input[0:nl] + '"')
				# Get file accessed
				argList = input.split()
				
				file = argList[1]
				if file.endswith('/'):
					file = file + 'index.html'
				try:
					file_text = ''
					with open('htdocs' + file, 'rb') as in_file:
						file_text = in_file.read()
						
					contentType = ''
					if file.endswith('.html'):
						contentType = 'text/html'
					elif file.endswith('.css'):
						contentType = 'text/css'
					elif file.endswith('.jpeg') | file.endswith('.jpg'):
						contentType = 'image/jpeg'
					else:
						contentType = 'text/plain'
						
					content = bytes(create_headers(200, len(file_text), contentType), 'utf-8') + file_text
					
					conn.send(content)
				except FileNotFoundError:
					# Send 404 not found
					errorText = ''
					with open('error-files/404.html', 'rb') as in_file:
						errorText = bytes.decode(in_file.read())
						
					conn.send(bytes(create_headers(404, len(errorText), 'text/html') + errorText, 'utf-8'))
					print(addr[0] + ' - 404 error')
				except:
					# 500 error
					with open('error-files/500.html', 'rb') as in_file:
						errorText = bytes.decode(in_file.read())
					conn.send(bytes(create_headers(500, len(errorText), 'text/html') + errorText, 'utf-8'))
					print(addr[0] + ' - 500 error')
					
					
				conn.close()	
				continue
				
					
				
def create_headers(code, contentLen, contentType):
	header = ''
	# Code is int
	# First add the http thingy
	header = header + 'HTTP/1.1 '
	header = header + str(code)
	header = header + '\r\n'
	header = header + 'Content-Length: ' + str(contentLen) + '\r\n'
	header = header + 'Content-Type: ' + contentType + '\r\n'
	header = header + '\r\n'
	return header