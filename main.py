from source.server import *

# Port number.
PORT = 80
HOST = ''

if __name__ == '__main__':
	print('Running server...')
	server(HOST, PORT)