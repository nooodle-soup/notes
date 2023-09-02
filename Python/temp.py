class LinkedList:
    length = 0
    _length = 0
    __length = 0


ll1 = LinkedList()
ll2 = LinkedList()
print(ll1.length)
print(ll2.length)

ll1.length = 10
ll2.length = 11
print(ll1.length)
print(ll2.length)

LinkedList.length = 1
print(ll1.length)
print(ll2.length)
ll3 = LinkedList()
print(ll3.length)
