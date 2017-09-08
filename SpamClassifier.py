import re
import collections as coll
import math
# import numpy as np


def char_counter(email):
    return len(email)


def alpha_ratio(email, C):
    return len(list(re.finditer('[A-Za-z]', email))) / C


def digit_ratio(email, C):
    return len(list(re.finditer('[0-9]', email))) / C


def ws_ratio(email, C):
    return len(list(re.finditer('[0-9]', email))) / C


def regular_freq(email, C):
    tmp_lst = []
    tmp_lst += [(chr(v), 0) for v in range(ord('A'), ord('Z') + 1)]
    tmp_lst += [(chr(v), 0) for v in range(ord('a'), ord('z') + 1)]
    tmp_lst += [(chr(v), 0) for v in range(ord('0'), ord('9') + 1)]

    counter = dict(tmp_lst)
    reg_iter = re.finditer('[A-Za-z0-9]', email)
    for c in reg_iter:
        if c in counter:
            counter[c] += 1

    return [counter[c] / C for c in tmp_lst]


def special_freq(email, C):
    tmp_lst = [(c, 0) for c in '*_+=%$@\/']

    counter = dict(tmp_lst)
    s_iter = re.finditer('[*_+=%$@\/]', email)
    for c in s_iter:
        if c in counter:
            counter[c] += 1
    return [counter[c] / C for c in tmp_lst]


def word_counter(word_list):
    return len(word_list)


def shot_word_freq(word_list, M):
    return len([w for w in word_list if len(w) <= 2]) / M


def char_word_ratio(word_list, C):
    return sum([len(w) for w in word_list]) / C


def avg_word_len(word_list, M):
    return sum([len(w) for w in word_list]) / M


def avg_sentence_len_per_char(email):
    sntcs = email.split('\n')
    return sum([len(s) in sntcs]) / len(sntcs)


def avg_sentence_len_per_word(email):
    sntcs = email.split('\n')
    return sum([len(s.split('\s+') for s in sntcs)]) / len(sntcs)


def word_len_freq(word_list, M):
    len_counter = dict([(i, 0) for i in range(1, 16)])
    for w in word_list:
        if len(w) in len_counter:
            len_counter[len(w)] += 1

    return [len_counter[v] / M for v in range(1, 16)]


def uniqe_words_freq(email, word_list, M):
    return len(set(word_list)) / M


# Hapax Legomena Freq. of once-occurring words
def hapax_legomena_freq(word_list, M):
    token_counter = coll.Counter(w.upper() for w in word_list)
    return len(w for token_counter.keys()
               if token_counter[w] == 1) / M


# Hapax Dislegomena Freq. of twice-occurring words
def hapax_dislegonema_freq(email, word_list, M):
    token_counter = coll.Counter(w.upper() for w in word_list)
    return len(w for token_counter.keys()
               if token_counter[w] == 2) / M


def yules_k_measure(word_list):
    token_counter = coll.Counter(w.upper() for w in word_list)
    m1 = sum(token_counter.values())
    m2 = sum([freq ** 2 for freq in token_counter.values()])
    i = (m1 * m2) / (m2 - m1)
    k = 1/i * 10000
    return k


def simpson_d_measure(word_list, M):
    token_counter = coll.Counter(w.upper() for w in word_list)
    m1 = sum(token_counter.values())
    m2 = sum([n * (n - 1) for n in token_counter.values()])
    return 1 - m2 / (m1 * (m1 - 1))


def sichel_measure_s(word_list):
    token_counter = coll.Counter(w.upper() for w in word_list)
    v = len(set(w.upper() for w in word_list))
    v2 = len(set(w for w in token_counter.keys()
                 if token_counter[w] == 2))
    return v2 / v


def brunet_w_measure(word_list, alpha=0.17):
    v = len(set(w.upper() for w in word_list))
    n = len(word_list)
    return n ** (v - alpha)


def honore_r_measure(word_list):
    token_counter = coll.Counter(w.upper() for w in word_list)
    v = len(set(w.upper() for w in word_list))
    n = len(word_list)
    v1 = len(set(w for w in token_counter.keys()
                 if token_counter[w] == 1))
    return 100 * math.log(n) / (1 - (v1/v))


def punctuation_freq(email):
    punc = '.،;?!:()–"«»<>[]{}'
    token_counter = coll.Counter(c for c in email if c in punc)
    s = sum(token_counter.values())
    return [token_counter[c]/s for c in punc]


def vectorize(email):
    pass
