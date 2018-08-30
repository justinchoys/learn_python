
# class Lexicon(object):
	
d = {'direction' : ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
	 'verb' : ['go', 'stop', 'kill', 'eat'],
	 'stop' : ['the', 'in', 'of', 'from', 'at', 'it'],
	 'noun' : ['door', 'bear', 'princess', 'cabinet']
	 }

def scan(s):
	result = []

	for word in s.split():
		found = False
		for key in d.keys():
			if word in d[key]:
				result.append((key, word))
				found = True

		if not found:
			result.append(convert_number(word))
	return result


def convert_number(word):
	try:
		return ('number', int(word))
	except ValueError:
		return ('error', word)
