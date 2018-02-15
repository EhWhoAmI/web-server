class parser:
	def __init__(self， text):
		# Remove all whitespace that is not between double or single brackets/
		# Iterate thru string
		parse = list(text)
		content = []
		quotes = False
		for i in parse:
			if (i == ' ' or i == '\n' or i == '\t') and quotes == False:
				pass
			else:
				content.append(i)
			