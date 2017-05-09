#!/usr/bin/env python
#-*- coding: utf-8 -*-

def main():
    words = ['noun', 'verb', 'adjective', 'adverb']
    words_dic = {}
    # 부정관사: indefinite article
    article = 'a'
    # 모음: vowel
    vowel = ['a', 'e', 'i', 'o', 'u']

    # 입력
    for word in words:
        # a or an
        if word[0] in vowel:
            article = 'an'
        else:
            article = 'a'

        words_dic[word] = raw_input('Enter ' + article + ' ' + word + ': ')

    # 출력
    out_str = "Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
    print out_str.format(verb = words_dic['verb'],
                        adjective = words_dic['adjective'],
                        noun = words_dic['noun'],
                        adverb = words_dic['adverb'])

if __name__ == "__main__":
    main()
