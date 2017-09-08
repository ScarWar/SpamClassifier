import re
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


def avg_word_length(word_list, M):
    return sum([len(w) for w in word_list]) / M


def vectorize(email):
    pass
