#!/usr/bin/env python
#-*- coding: utf-8 -*-
    
# global 변수
plus = 0.0
minus = 0.0
multi = 0.0
division = 0.0


def calc(first, second):
    global plus
    global minus
    global multi
    global division

    plus = first + second
    minus = first - second
    multi = first * second
    division = first / second

def main():
    first = ''
    second = ''
    # 입력 isdigit() 으로 숫자아닌값, 음수 체크
    while (len(first) == 0):
        first = raw_input("What is the first number? ")
        if first.isdigit() is True:
            break
        else:
            print "Please input digit only!"
            first = ''

    while (len(second) == 0):
        second = raw_input("What is the second number? ")
        if second.isdigit() is True:
            break
        else:
            print "Please input digit only!"
            second = ''

    # 연산부분 함수로 구현
    calc(float(first), float(second))

    # 출력
    out_str = "{first} + {second} = {plus}\n\
                \r{first} - {second} = {minus}\n\
                \r{first} * {second} = {multi}\n\
                \r{first} / {second} = {division}"
    print out_str.format(first = first,
                        second = second,
                        plus = plus,
                        minus = minus,
                        multi = multi,
                        division = division)
                        

if __name__ == '__main__':
    main()
