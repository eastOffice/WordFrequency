import nltk

from utils import get_words, get_stopwords

def mode_c():
    pass

def mode_f(filename, n=0):
    ''' - filename: .txt to read
        - n: return the first n words, 0 returns all
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        words = get_words(f.read())
    word_freq = nltk.FreqDist(words)
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
    


