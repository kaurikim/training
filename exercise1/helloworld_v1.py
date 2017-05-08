#!/usr/bin/env python

def input_name():
    return raw_input("What is your name? ")

def connect_str(name):
    return "Hello, " + name + ", nice to meet you!"

def print_str(ret_str):
    print ret_str

def main():
    name = input_name()
    ret_str = connect_str(name)
    print_str(ret_str)

if __name__ == '__main__':
    main()
