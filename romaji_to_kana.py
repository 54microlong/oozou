#encoding:utf-8

import sys


class romaji_to_kana():
    'convert romaji to kana'
    
    _roma_to_kana = {}
    def __init__(self, dic_path="./dictionary/romaji_to_kana.dic"):
        for line in open(dic_path):
            (key,value) = line.strip().split(" ") 
            romaji_to_kana._roma_to_kana[key] = value 
       

    def _convert_roma_to_kana(self, roma_str):
        #Forward Maximum(4) Matching method
        suplited_words = []
        MAX_LENGTH = 4
        roma_len = roma_str.__len__()
        start_point = 0
        end_point = min(MAX_LENGTH, roma_len) 
        while(start_point < roma_len):
            while(end_point >= start_point):
                sub_roma = roma_str[start_point : end_point]
                if sub_roma in romaji_to_kana._roma_to_kana:
                    suplited_words.append(romaji_to_kana._roma_to_kana[sub_roma])
                    break
                else:
                    end_point -= 1
            else:
                #can not find matched item in the dictionary
                return "".join(suplited_words) + roma_str[start_point:]
            forward_len = sub_roma.__len__() 
            start_point += forward_len 
            end_point = start_point + MAX_LENGTH \
            if start_point + MAX_LENGTH < roma_len else roma_len  
            
        return "".join(suplited_words)

    def _test_dic(self, roma_str):
        return romaji_to_kana._roma_to_kana[roma_str]

    def _test_(self):
        a = romaji_to_kana()
        print a._test_dic("no")
        print a._test_dic("a")
        print a._test_dic("hi")
        print a._test_dic("to")
        print a._convert_roma_to_kana("anohhuto") 
    
    def _instant_test_(self):
        while 1:
            roma_str = raw_input()
            sys.stdout.write(self._convert_roma_to_kana(roma_str) + "\n")
            sys.stdout.flush()
if __name__ == "__main__":
    a = romaji_to_kana()
    a._test_()
    a._instant_test_()
