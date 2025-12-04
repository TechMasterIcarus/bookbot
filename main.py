import sys

def get_book_text(book):
	with open (book) as f:
		file_contents = f.read()
	return file_contents

from stats import word_count, characters, slist

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_text = get_book_text(sys.argv[1])
#	print(book_text)
	char_dict = characters(book_text)
	num_words =  word_count(book_text)
	sorted_chars = slist(char_dict)
	print("============ BOOKBOT ============")
	print("Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	#print(char_dict)
	for item in sorted_chars:
		ch = item["char"]
		if not ch.isalpha():
			continue
		count = item["num"]
		print(f"{ch}: {count}")
main()

