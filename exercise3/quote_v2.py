#-*- coding: utf-8 -*-
#!/usr/bin/env python
# 딕셔너리 자료구조를 만들고 items() 로 루프돌며 프린트한다.

def main():
    quote_dic = {'Obi-Wan Kenobi':"These aren't the droids you're looking for",\
                'Mahatma Gandhi':"The future depends on what we do in the present"}

    for key, value in quote_dic.items():
        print key + ' says, "' + value + '."'

if __name__ == '__main__':
    main()
