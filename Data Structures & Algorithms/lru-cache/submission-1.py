class node:
    def __init__(self):
        self.val = 0
        self.key = -1
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = node()
        self.tail = node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.dic = {}
        
    def get(self, key: int) -> int:
        if(key in self.dic):
            nde = self.dic[key]

            nde.prev.next = nde.next
            nde.next.prev = nde.prev

            nde.prev = None
            nde.next = None

            self.tail.prev.next = nde
            nde.prev = self.tail.prev

            nde.next = self.tail
            self.tail.prev = nde

            return nde.val

        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if(key in self.dic):
            val = self.get(key)
            self.dic[key].val = value
        else:
            if(len(self.dic.keys())<self.cap):
                nde = node()
                nde.key = key
                nde.val = value

                self.tail.prev.next = nde
                nde.prev = self.tail.prev

                nde.next = self.tail
                self.tail.prev = nde

                self.dic[key] = nde

            else:
                nde = self.head.next
                del self.dic[nde.key]

                self.head.next = nde.next
                nde.next.prev = self.head

                nde.next = None
                nde.prev = None

                nde = node()
                nde.key = key
                nde.val = value

                self.tail.prev.next = nde
                nde.prev = self.tail.prev

                nde.next = self.tail
                self.tail.prev = nde

                self.dic[key] = nde





        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)