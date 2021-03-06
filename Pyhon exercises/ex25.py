def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sorts the words"""  
	return sorted(words)

def print_first_word(words):
	"""prints the first word after pooping it off."""
	word = words.pop(0)#0 index references to first element
	print(word)

def print_last_word(words):
	"""prints the last word after popping it out"""
	word = words.pop(-1)#-1 index references to last element
	print(word)

def sort_sentence(sentence):
	"""Takes a whole statement and return the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints first and last word of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""sortd the words then prints the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)