def count_words(text: str, words: set) -> int:
    return len([w for w in words if w.lower() in text.lower() and w.isalpha()])
"""

def count_words(str1,sets1):
	counts =  0
	for item in sets1:
		#print (str1.count(item))
		if str1.lower().count(item)>=1:
			counts += 1
	print (counts)
	return counts
"""
if __name__ == '__main__':
	assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
	assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
	assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"}) == 1
	print("The local tests are done.")