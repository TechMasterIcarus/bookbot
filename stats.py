def slist(characters):
	char_list = []
	for ch, count in characters.items():
		char_num_dict = {"char": ch, "num": count}
		char_list.append(char_num_dict)
	char_list.sort(reverse=True, key=sort_on)
	return char_list

def sort_on(char_num_dict):
	return char_num_dict["num"]
		
def word_count(book_text):
	return len(book_text.split())

def characters(book_text):
	characters = {}
	book_text = str.lower(book_text)
	for text in  book_text:
		if text in characters:
			characters[text] += 1
		else:
			characters[text] = 1

	return characters
