import nltk
import re
from collections import Counter
from functools import wraps

from utils import *

def fn_timer(function): 
    @wraps(function)
    def function_timer(*args, **kwargs):
        import time
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('%s costs %s (s)' %(function, t1 - t0))
        return result
    return function_timer

def mode_c(file_name , n=0):
    rule = re.compile(r"[^a-z]")
    counter = Counter()
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            line_result = rule.sub("" ,line.lower())
            counter.update(line_result)
    sum = 0 
    for charactor  in counter:
        frequency = counter[charactor]
        sum += frequency
    count = 0 
    if n == 0:
        n = 26
    for charactor , frequency in counter.most_common():
        if count == n:
            break
        print('%40s\t%f' % (charactor, frequency/sum))
        count += 1


@fn_timer
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
            print('%40s\t%d' % (str(key), val))
    else:
        count = 0
        for key, val in word_freq:
            if count == n: break
            print('%40s\t%d' % (str(key), val))
            count += 1

@fn_timer
def mode_d(directory, is_recursive, n=0, stop_words_file=None):
    if is_recursive:
        # here returns the final path
        file_list = list_all_files(directory)
    else:
        # here is only the relative path, need path.join
        fl = os.listdir(directory)
        file_list = []
        for i in range(len(fl)):
            t = os.path.join(directory, fl[i])
            if os.path.isfile(t):
                file_list.append(t)

    for file in file_list:
        print('File: %s' % file)
        mode_f(file, n, stop_words_file)

@fn_timer
def mode_p(file_pth , show_num , length):

    import time
    t0 = time.time()

    with open(file_pth, 'r' , encoding='utf-8') as f:
        sentences = get_sentences(f.read().lower())
    
    t1 = time.time()
    print('get_sentences costs %s (s)' %(t1 - t0))

    phrases = []
    for item in sentences:
        phrases.extend(get_phrases(item, length))

    t2 = time.time()
    print('get_phrases costs %s (s)' %(t2 - t1))

    phrases_freq = nltk.FreqDist(phrases)
    phrases_freq = sorted(phrases_freq.items(), \
        key=lambda item:item[1], reverse=True)
    if show_num == 0:
        for key, val in phrases_freq:
            print(str(key) + ':' + str(val))
    else:
        count = 0
        for key, val in phrases_freq:
            if count == show_num: break
            print(str(key) + ':' + str(val))
            count += 1



