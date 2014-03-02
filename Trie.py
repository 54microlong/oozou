#encoding:utf-8

class trie():
    'trie data structure for dictionary of IME' 
    
    def __init__(self):
        self.all_trie = {}

    def search_item(self, key):
        _tem_trie = self.all_trie
        for _word in key:
            if _word in _tem_trie:
                _tem_trie = _tem_trie[_word]
            else:
                return None
        if "#" in _tem_trie:
            return _tem_trie["#"]
    
    
    def search_prefix(self, key):
        _tem_trie = self.all_trie
        for _word in key:
            if _word in _tem_trie:
                _tem_trie = _tem_trie[_word]
            else:
                return None
        
        #'递归深度优先遍历'
        #self.output_item(_tem_trie, key)
        
        result_list = []
        item_list = _tem_trie.values()
         
        
        if "#" in _tem_trie:
            result_list.append(_tem_trie["#"])

        while(item_list):
            next_level_items = []
             
            for _item in item_list:
                if not isinstance(_item, dict):
                    continue
                if "#" in _item:
                    result_list.append(_item["#"])
                
                next_level_items += _item.values()
            item_list = next_level_items
       
        
        return result_list             
            

    def add_item(self, key, value):
    #'utf-8的编码遍历会让索引结构按照字节码编码'
        _tem_trie = self.all_trie
        for _word in key:
            if _word not in _tem_trie:
                _tem_trie[_word] = {}
            _tem_trie = _tem_trie[_word] 
        _tem_trie["#"] = value

    def output_item(self, current_tree, current_string=""):
        if not current_tree:
            return None
        for _item in current_tree:
            if _item == "#":
                print current_string
            else:
                self.output_item(current_tree[_item], current_string + _item)
    
    def __del__ (self):
        del self.all_trie


    def _test_(self):
        
        self.add_item("あのひと", "あのひと")
        self.add_item("あの氷見", "あの氷見")
        self.add_item("あのみ", "あのみ")
        self.add_item("あの", "あの")
        self.add_item("いままで", "いままで")
        self.add_item("いまま", "いまま")

        self.output_item(self.all_trie)
        
        print self.search_item("いま")
        print self.search_item("あのみ")
        print self.search_item("あのち")
        #test
        print("output the search result")
        self.search_prefix("あの")
        print("output result")
        for item in self.search_prefix("あの"):
            print item

if __name__ == "__main__":
    dic = trie()
    dic._test_()
