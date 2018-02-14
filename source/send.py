from source.headers import *

def sendFile(file, conn, contentType):
	try:
		file_text = ''
		with open('htdocs' + file, 'rb') as in_file:
			file_text = in_file.read()
			
		content = bytes(create_headers(200, len(file_text), contentType), 'utf-8')  + file_text

		conn.send(content)
	except FileNotFoundError:
		# Send 404 not found
		errorText = ''
		with open('error-files/404.html', 'rb') as in_file:
			errorText = bytes.decode(in_file.read())

			conn.send(bytes(create_headers(404, len(errorText), 'text/html') + errorText, 'utf-8'))
			print(addr[0] + ' - 404 error' + str(sys.exc_info()))
	except:
		# 500 error
		with open('error-files/500.html', 'rb') as in_file:
			errorText = bytes.decode(in_file.read())
			conn.send(bytes(create_headers(500, len(errorText), 'text/html') + errorText, 'utf-8'))
			print(addr[0] + ' - 500 error' + str(sys.exc_info()))

def sendText(text):
	pass
