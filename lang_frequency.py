import sys


def load_file(filepath):
    with open(filepath, 'r') as file_handler:              
        return file_handler.read()


def remove_extra_characters(text):
    replace_words = [('\n',''), ('"',''), (',',''),
        ('.', ''), ('?', '')]
    for find, replace in replace_words:
        text = text.replace(find, replace)
    return text


def get_most_frequent_words(text, max_values = 10):

    words_count = dict()
    for word in [remove_extra_characters(word).lower() 
                for word in text.split(' ')]:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 0
    
    return sorted(words_count.items(), 
                key=lambda x:x[1], reverse = True)[:max_values]


if __name__ == '__main__':
    try:
        file_content = load_file(sys.argv[1])
    except IndexError:
        print('warning: please add text file as argument: ' + 
            './python lang_frequency.py data.txt')
    except FileNotFoundError:
        print('file: {0} not found'.format(sys.argv[1]))        
    else:
        max_values = 10 if len(sys.argv) <= 2 else int(sys.argv[2])  
        for word, repeated in get_most_frequent_words(file_content,
                                                      max_values):
            print('word "{0}" repeated {1} times\n'.format(word, repeated))
