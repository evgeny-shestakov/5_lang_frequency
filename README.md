# uses

- sys
- collections
- re

# Frequency Analysis of Words

Count the most repetitive words. First param is filepath (with data), and second (optional) param
it is max results (10 by default)

Module is consists of:

- get_most_frequent_words(text, max_values = 10)
return sorted list of typles: (word, frequency)

```#!bash

$ python bars.py filepath longitude latitude # possibly requires call of python3 executive instead of just python
python lang_frequency.py data.txt 10                                                                                                                                                  


word "в" repeated 11 times                                                                                                                                                                              
                                                                                                                                                                                                        
word "и" repeated 9 times                                                                                                                                                                               
                                                                                                                                                                                                        
word "скрипт" repeated 5 times                                                                                                                                                                          
                                                                                                                                                                                                        
word "на" repeated 5 times                                                                                                                                                                              
                                                                                                                                                                                                        
word "вход" repeated 3 times                                                                                                                                                                            
                                                                                                                                                                                                        
word "должен" repeated 3 times 

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
