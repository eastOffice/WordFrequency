import nltk
import re
from collections import Counter

from utils import get_words, get_stopwords

def mode_c(file_pth):
    rule = re.compile(r"[^a-z]")
    counter = Counter()
    with open(file_pth, encoding="utf-8") as f:
        for line in f:
            line_result = rule.sub("" ,line.lower())
            counter.update(line_result)
    sum = 0 
    for charactor  in counter:
        frequency = counter[charactor]
        sum += frequency
    for charactor , frequency in counter.most_common():
        print("Charactor: {0} Times: {1} Frequency: {2} "\
        .format(charactor , frequency , frequency/sum)) 
    pass

def mode_f(filename, n=0, stop_words_file=None):
    ''' - filename: .txt to read
        - n: return the first n words, 0 returns all
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        words = get_words(f.read())

    word_freq = nltk.FreqDist(words)
    
    if stop_words_file is not None:
        stop_words = get_stopwords(stop_words_file)
        for key in list(word_freq.keys()):
            if key in stop_words:
                word_freq.pop(key)

    word_freq = sorted(word_freq.items(), key=lambda item:item[1], reverse=True)
    if n == 0:
        for key, val in word_freq:
            print(str(key) + ':' + str(val))
    else:
        count = 0
        for key, val in word_freq:
            if count == n: break
            print(str(key) + ':' + str(val))
            count += 1

def mode_d(directory, is_recursive, n=0):
    pass
    


