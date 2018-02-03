import socket
import time
import sys
from source.headers import *
from source.get import *
from source.post import *


def server(HOST = '', PORT = 80):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.bind((HOST, PORT))
		sock.listen(3)
		# Server loop
		while True:
			# Send infomation
			conn, addr = sock.accept()
			out = conn.recv(4096)
			input = bytes.decode(out)

			# Parse header string
			headert = input.split('\r\n\r\n')

			head = header(headert[0])

			# First line is the request line
			if head.command == 'GET':
				# this is a get request, read until \r\n because http uses this.
				print(addr[0] + ' - "' + head.cmdText + '"')
				# Get file accessed
				argList = head.cmdText.split()

				file = argList[1]
				get(file, conn, addr)
			if head.command == "POST":
				print(addr[0] + ' - ' + head.cmdText)
				post(headert[1], conn, addr)
				argList = head.cmdText.split()
				file = argList[1]
				get(file, conn, addr)

			# Close connection
			conn.close()

