#!/usr/bin/env python
# python 에서는 쌍따옴표 입력시 확장문자 불필요

def main():
    quote_str = raw_input("What is the quote? ")
    who_str = raw_input("Who said it? ")
    print who_str + ' says, "' + quote_str + '."'

if __name__ == '__main__':
    main()
