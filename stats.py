def word_count(string: str) -> int:
    return len(string.split())


def chars_dict_to_sorted_list(data: dict[str, int]) -> list[tuple[str, int]]:
    sorted_data = sorted(data.items(), reverse=True, key=lambda item: item[1])
    return sorted_data


def dict_char_count(string: str) -> dict[str, int]:
    char_count: dict[str, int] = {}
    for ch in string:
        char = ch.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count
