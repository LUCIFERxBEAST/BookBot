import sys

from stats import chars_dict_to_sorted_list, dict_char_count, word_count


def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
    return file_content


def print_report(
    book_path: str, word_count: int, sorted_list_count: list[tuple[str, int]]
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_list_count:
        char = pair[0]
        if char.isalpha():
            char_count = pair[1]
            print(f"{char}: {char_count}")
    print("============= END ===============")


def main():
    user_input = sys.argv
    if len(user_input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = user_input[1]
    file_content = get_book_text(file_path)
    num_words = word_count(file_content)
    # print(f"Found {num_words} total words")
    data_dict = dict_char_count(file_content)
    char_count = chars_dict_to_sorted_list(data_dict)
    # print(char_count)
    print_report(
        book_path=file_path, word_count=num_words, sorted_list_count=char_count
    )


main()
