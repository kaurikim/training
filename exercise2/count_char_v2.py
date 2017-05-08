#!/usr/bin/env python

# 아무것도 입력하지 않으면 입력하라는 메시지 출력 버전
# 공백은 입력받지 않은 것으로 간주하도록 strip() 처리

def main():
    in_str = ""

    while (len(in_str.strip()) == 0):
        in_str = raw_input("What is the input string? ")
        if len(in_str.strip()) == 0:
            print "Input anything!"

    print in_str.strip() + " has " + str(len(in_str.strip())) + " characters."

if __name__ == '__main__':
    main()
