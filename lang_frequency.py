import sys
import collections
import re


def load_file(filepath):
    try:
        with open(filepath, 'r') as file_handler:              
            return file_handler.read()
    except FileNotFoundError:
        print('file {0} not found'.format(filepath))
        sys.exit(1)       


def get_most_frequent_words(text, max_values = 10):
    word_list = re.sub('[^\w]', ' ',  text).lower().split()
    return collections.Counter(word_list).most_common(max_values) 


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_content = load_file(sys.argv[1])
        try:
            max_values = 10 if len(sys.argv) <= 2 else int(sys.argv[2])
        except ValueError:
            print('wrong max values format, please use float')
            sys.exit(1)
        for word, repeated in get_most_frequent_words(file_content,
                                                      max_values):
            print('word "{0}" repeated {1} times\n'.format(word, repeated))
        sys.exit(0)
    else:
        print('error: please add text file as argument: ' + 
            './python lang_frequency.py data.txt [max_values]')
        sys.exit(1)          
        
