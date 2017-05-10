#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime

def input_func(question):
    in_str = ''
    # 입력 isdigit() 으로 숫자아닌값, 음수 체크
    while (len(in_str) == 0):
        in_str = raw_input(question)
        if in_str.isdigit() is True:
            return int(in_str)
        else:
            print "Please input digit only!"
            in_str = ''

def main():
    # Get current year: type(cur_year) is int
    cur_year = datetime.today().year
    cur_age = 0
    retire_age = 0
    remain = 0
    
    # 입력
    cur_age = input_func("What is your current age? ")

    # retire_age 가 cur_age 보다 작으면 다시 입력받음
    while True:
        retire_age = input_func("At what age would you like to retire? ")
        # 연산
        remain = retire_age - cur_age
        if remain >= 0:
            break
        else:
            print "Input retire age bigger than current age!"

    # 출력
    out_1 = "You have {0} years left until you can retire."
    print out_1.format(remain)

    out_2 = "It's {0}, so you can retire in {1}."
    print out_2.format(cur_year, cur_year + remain)

if __name__ == '__main__':
    main()
