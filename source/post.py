from source.headers import *

def post(postText, conn, addr):
	# Parse post text
	postTextTemp = postText.split('&')

	#iterate through post text
	postText = {}
	for i in postTextTemp:
		splitter = i.split('=')
		postText[splitter[0]] = splitter[1]

	print(postText)

	fullName = postText["fname"] + " " + postText["lname"]
	print(fullName)

	return '''<p>'''+ fullName +'''</p>'''
