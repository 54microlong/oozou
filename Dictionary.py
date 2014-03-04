#coding:utf-8

import sys
import Trie as my_trie

class Dictionary(object):
    'singleton implemente the basic dictionary function' 
    
    _instance = None
    
    def __init__(self):
        self._trie = my_trie.Trie()
        pass
     

    @staticmethod
    def get_instance():
        if not Dictionary._instance:
             Dictionary._instance = Dictionary() 
        
        return Dictionary._instance

    def load_dic(self,_file_path):
        #todo check the _file_path
        with open(_file_path) as _dic_file:
            for line in _dic_file:
                _word_list = (_word,_nota,_id,_cost,_tag) = line.rstrip().split("\t")
                self._trie.add_item(_nota, (_word_list))
        sys.stderr.write("==> load dic finished \n") 
    
    def search_exact(self, _key):
        return self._trie.search_item(_key)

    def search_prefix(self, _key):
        return self._trie.search_prefix(_key)

    def destory_dict(self):
        del self._trie

    

if __name__ == "__main__":
    tri = my_trie.Trie()
    diction = Dictionary.get_instance()
    diction.load_dic("./dictionary/basic.dic")
    print "\t".join(diction.search_exact("ひと"))
    for item in diction.search_prefix("わたし"):
        print "\t".join(item)
