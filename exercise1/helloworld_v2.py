#!/usr/bin/env python
# 변수를 사용하지 않는 버전

def input_name():
    return raw_input("What is your name? ")

def main():
    print "Hello, " + input_name() + ", nice to meet you!"

if __name__ == '__main__':
    main()
