from source.headers import *
from source.send import *
import sys

def get(file, conn, addr):
	contentType = ''
	if file.endswith('/'):
		file = file + 'index.html'	
	if file.endswith('.html'):
		contentType = 'text/html'
	elif file.endswith('.css'):
		contentType = 'text/css'
	elif file.endswith('.jpeg') | file.endswith('.jpg'):
		contentType = 'image/jpeg'
	else:
		contentType = 'text/plain'
	sendFile(file, conn, contentType)
