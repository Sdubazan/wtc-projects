
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

def convert_to_word_list(text):
    """ function that convert string to list"""
    word_list = split(', |.?',text)
    word_list = [word.lower() for word in word_list if len(word) != 0]
    return word_list

def words_longer_than(length, text):
    """ function that list word of specific length"""
    word_list = convert_to_word_list(text)
    word_list = [text for text in word_list if len(text) >= length]
    return word_list

def words_lengths_map(text):
    """ function to count word lenght"""
    text = convert_to_word_list(text)
    length = [len(num) for num in text]
    length = sorted(length)
    word_length = {i:length.count(i) for i in length}
    return word_length

def letters_count_map(text):
    """ count letters in a stirng function"""
    text = split('',text)
    alphabets = [chr(i) for i in range(97,123)]
    string_alphabets = [i.lower() for i in text if i.isalpha()]
    alphabets = {i:string_alphabets.count(i) for i in alphabets}
    return alphabets

def most_used_character(text):
    """ max occuring char fanction"""
    text = [char for char in text]
    char_list = [[text.count(char),char] for char in text]
    if not text:
        return None
    else:
        most_char = max(char_list)
    return max(most_char[1])
