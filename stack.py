from node import Node

class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size -= 1
        else:
            print("Yıgında veri eklenecek bosluk kalmadı !")
    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Bu yıgın tamamiyle bos!!")
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Goruntulenecek deger yok!")
    
    def has_space(self):
        if self.limit > self.size:
            return True
    
    def is_empty(self):
        if self.size == 0:
            return True


# Bos bir pizza yığını tanımlayalım 
pizza_stack = Stack(6)
# Sahip olduğumuz pizzaları yığına ekleyelim 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Limit değişkenine değer olarak 6 atadık fazla pizza eklemeye çalışırsak ne olacak görmek için aşağıdaki satırı yorumdan çıkarın.
#pizza_stack.push("pizza #7")

# Yığının tepesinden aşağı doğru pizzaları teslim edelim
print("İlk Teslim Edilen Pizza :  " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Tüm pizzalar dağıtılmasına rağmen 'pop()' işlemi yaparsak ne olur görmek için aşağıdaki satırı yorumdan çıkarın.
pizza_stack.pop()
